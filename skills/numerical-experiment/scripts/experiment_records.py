#!/usr/bin/env python3
"""Inspect explicit configuration differences and fingerprint experiment inputs."""
import argparse
import hashlib
import json
from pathlib import Path

MISSING = object()


def changes(a, b, prefix=''):
    if isinstance(a, dict) and isinstance(b, dict):
        result = []
        for key in sorted(a.keys() | b.keys()):
            path = f'{prefix}.{key}' if prefix else key
            result.extend(changes(a.get(key, MISSING), b.get(key, MISSING), path))
        return result
    if a is MISSING or b is MISSING or a != b:
        return [{'path': prefix,
                 'before': {'missing': True} if a is MISSING else a,
                 'after': {'missing': True} if b is MISSING else b}]
    return []


def matches(path, fields):
    return any(path == p or path.startswith(p + '.') for p in fields)


def fingerprint(path):
    path = Path(path).expanduser().resolve(strict=True)
    if not path.is_file():
        raise ValueError(f'Expected file: {path}')
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': h.hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    compare = sub.add_parser('compare')
    compare.add_argument('before', type=Path)
    compare.add_argument('after', type=Path)
    compare.add_argument('--vary', action='append', required=True,
                         help='Explicit research factor path; repeat for a declared joint experiment')
    compare.add_argument('--ignore', action='append', default=[],
                         help='Explicit bookkeeping-only path; changes remain visible')
    fp = sub.add_parser('fingerprint')
    fp.add_argument('files', nargs='+')
    args = parser.parse_args()
    if args.command == 'fingerprint':
        result = [fingerprint(p) for p in args.files]
        code = 0
    else:
        if any(matches(p, args.ignore) for p in args.vary) or any(matches(p, args.vary) for p in args.ignore):
            parser.error('--vary and --ignore paths must not overlap')
        rows = changes(json.loads(args.before.read_text()), json.loads(args.after.read_text()))
        for row in rows:
            row['classification'] = ('research_factor' if matches(row['path'], args.vary)
                                     else 'bookkeeping' if matches(row['path'], args.ignore)
                                     else 'unexpected')
        unexpected = [r['path'] for r in rows if r['classification'] == 'unexpected']
        result = {'declared_factors': args.vary, 'bookkeeping_fields': args.ignore,
                  'changes': rows, 'unexpected_changes': unexpected,
                  'structural_check_passed': not unexpected,
                  'scope': 'Config structure only; inspect effective defaults, code, inputs and causal design separately.'}
        code = int(bool(unexpected))
    print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
