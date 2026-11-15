#!/usr/bin/env python3
"""Run short Python commands through the verified Windows Tailscale/SSH profile."""
import argparse
import base64
import json
from pathlib import Path
import subprocess
import zlib

PROBE = '''import sys, platform, pathlib, shutil, importlib.util, json
print(json.dumps({"system":platform.system(),"python":sys.version.split()[0],"executable":sys.executable,"desktop":str(pathlib.Path.home()/"Desktop"),"git_on_path":shutil.which("git"),"modules":{n:importlib.util.find_spec(n) is not None for n in ["numpy","scipy","matplotlib","mpmath","psutil","numba"]}},ensure_ascii=True))
'''


def command(profile, source):
    compile(source, '<remote-python>', 'exec')
    python_command = profile['python_command']
    # Known launcher tokens only; project-specific code belongs in the encoded source.
    if not isinstance(python_command, list) or not python_command:
        raise ValueError('python_command must be a nonempty token list')
    if any(not token or any(c in token for c in ' \t\r\n"\'&|<>^%') for token in python_command):
        raise ValueError('Unsupported launcher token; use a simple executable/launcher or adapt quoting explicitly')
    encoded = base64.b64encode(zlib.compress(source.encode('utf-8'))).decode('ascii')
    remote = ' '.join(python_command) + ' -c "import base64,zlib;exec(zlib.decompress(base64.b64decode(\'' + encoded + '\')))"'
    if len(remote) > 7800:
        raise ValueError('Remote command exceeds Windows command budget; transfer a file instead')
    ssh = ['/usr/bin/ssh', '-o', 'ConnectTimeout=15', '-o', 'BatchMode=yes',
           '-o', 'StrictHostKeyChecking=yes', '-o', 'IdentitiesOnly=yes']
    if profile.get('host_key_alias'):
        ssh += ['-o', 'HostKeyAlias=' + profile['host_key_alias']]
    for option in profile.get('ssh_options', []):
        ssh += ['-o', option]
    ssh += ['-i', str(Path(profile['identity_file']).expanduser()),
            profile['user'] + '@' + profile['host'], remote]
    return ssh


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', type=Path,
                        default=Path(__file__).resolve().parents[1] / 'references/hosts.json')
    parser.add_argument('--profile')
    parser.add_argument('--timeout', type=float, default=60)
    parser.add_argument('--dry-run', action='store_true')
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('probe')
    run = sub.add_parser('run')
    run.add_argument('source', type=Path)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error('timeout must be positive')
    profiles = json.loads(args.profiles.read_text())
    name = args.profile or profiles['default']
    profile = profiles['profiles'][name]
    source = PROBE if args.action == 'probe' else args.source.read_text(encoding='utf-8')
    argv = command(profile, source)
    if args.dry_run:
        # Do not expose user source or encoded source in logs.
        print(json.dumps({'profile': name, 'target': profile['user'] + '@' + profile['host'],
                          'source_bytes': len(source.encode('utf-8')),
                          'remote_command_chars': len(argv[-1]),
                          'strict_host_key_checking': True, 'executed': False}))
        return 0
    try:
        result = subprocess.run(argv, capture_output=True, timeout=args.timeout)
    except subprocess.TimeoutExpired:
        print(json.dumps({'status': 'timeout', 'profile': name, 'seconds': args.timeout}))
        return 124
    print(result.stdout.decode('utf-8', errors='replace'), end='')
    if result.stderr:
        import sys
        print(result.stderr.decode('utf-8', errors='replace'), end='', file=sys.stderr)
    return result.returncode


if __name__ == '__main__':
    raise SystemExit(main())
