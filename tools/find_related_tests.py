#!/usr/bin/env python3
"""Report changed files and filename-based test candidates for a PR update."""

import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(os.fsdecode(result.stderr).strip() or "git command failed")
    return result.stdout


def paths(data):
    return {os.fsdecode(item) for item in data.split(b"\0") if item}


def commit(repo, ref):
    return os.fsdecode(
        git(repo, "rev-parse", "--verify", "--end-of-options", ref + "^{commit}")
    ).strip()


def test_key(path):
    name = PurePosixPath(path).name
    stem = name.rsplit(".", 1)[0] if "." in name else name
    if re.search(r"\.(?:test|spec)$", stem, re.IGNORECASE):
        return re.sub(r"\.(?:test|spec)$", "", stem, flags=re.IGNORECASE).lower()
    if re.match(r"^(?:test|spec)_", stem, re.IGNORECASE):
        return re.sub(r"^(?:test|spec)_", "", stem, flags=re.IGNORECASE).lower()
    if re.search(r"_(?:test|tests|spec)$", stem, re.IGNORECASE):
        return re.sub(r"_(?:test|tests|spec)$", "", stem, flags=re.IGNORECASE).lower()
    if re.search(r"(?:Test|Tests|Spec)$", stem):
        return re.sub(r"(?:Test|Tests|Spec)$", "", stem).lower()
    return None


def report(repo, base_ref, before_ref):
    repo = Path(os.fsdecode(git(repo, "rev-parse", "--show-toplevel")).strip())
    base = commit(repo, base_ref)
    before = commit(repo, before_ref)
    common = os.fsdecode(git(repo, "merge-base", base, before)).strip()
    if git(repo, "diff", "--name-only", "--diff-filter=U", "-z", "--"):
        raise RuntimeError("resolve and stage merge conflicts before finding tests")

    changed = paths(git(repo, "diff", "--name-only", "-z", "--no-renames", common, "--"))
    changed |= paths(git(repo, "diff", "--name-only", "-z", "--no-renames", before, "--"))
    untracked = paths(git(repo, "ls-files", "--others", "--exclude-standard", "-z"))
    changed |= untracked
    available = paths(git(repo, "ls-files", "--cached", "-z")) | untracked
    available = {path for path in available if (repo / path).is_file()}

    tests = {path: test_key(path) for path in available}
    tests = {path: key for path, key in tests.items() if key}
    changed_tests = sorted(changed & tests.keys())
    candidates = {}
    unmatched = []
    for path in sorted(changed - tests.keys()):
        filename = PurePosixPath(path).name
        key = (filename.rsplit(".", 1)[0] if "." in filename else filename).lower()
        matches = sorted(test for test, test_name in tests.items() if test_name == key)
        if matches:
            candidates[path] = matches
        else:
            unmatched.append(path)

    return {
        "base_commit": base,
        "before_merge_commit": before,
        "changed_files": sorted(changed),
        "changed_tests": changed_tests,
        "related_test_candidates": candidates,
        "unmatched_changed_files": unmatched,
        "limitations": (
            "Candidates are filename matches only, not a dependency or coverage analysis. "
            "Deleted files, indirect dependencies, shared configuration, and other test naming "
            "conventions may require additional tests. Use project test selection or coverage "
            "data when available; otherwise run an appropriately broader suite."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="repository or directory within it")
    parser.add_argument("--base", required=True, help="fetched PR base branch or commit")
    parser.add_argument("--before-merge", required=True, help="PR head commit captured before merging")
    args = parser.parse_args()
    try:
        result = report(args.repo, args.base, args.before_merge)
    except (OSError, RuntimeError) as error:
        print(f"find_related_tests: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
