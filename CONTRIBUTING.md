# Contributing to shoplite

- Python 3.10+, standard library only at runtime. Tests use pytest.
- Keep changes minimal: fix the root cause, do not refactor unrelated code.
- Every bug fix must add a regression test in `tests/test_<module>.py` that fails before the fix.
- Public functions keep their signatures; behaviour changes need a note in the PR body.
- Never edit `.github/`, `pyproject.toml` dependencies or version numbers in a fix PR.
- Branch name: `patchpilot/issue-<number>`. PR title: `Fix #<number>: <short summary>`.
