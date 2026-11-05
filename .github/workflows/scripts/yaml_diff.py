#!/usr/bin/env python3

"""
Stub of yaml_diff.py for ci_test.

It only lists the repositories imported by `vcs import` and writes yaml_diff_report.md,
so that the token handling of yaml_check.yaml (private clone and PR comment) can be checked.
"""

from pathlib import Path


def find_imported_repos(src_dir: str) -> list[str]:
    return sorted(str(git_dir.parent) for git_dir in Path(src_dir).rglob(".git"))


def main() -> None:
    repos = find_imported_repos("src")
    lines = ["## yaml_check (ci_test)", "", f"Imported {len(repos)} repositories:", ""]
    lines += [f"- `{repo}`" for repo in repos]
    Path("yaml_diff_report.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
