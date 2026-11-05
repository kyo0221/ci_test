# ci_test

Test bed for a GitHub Actions workflow that imports repositories with `vcs import` and comments the result on the pull request.

- `.github/workflows/yaml_check.yaml`: workflow under test
- `.github/workflows/load-env.yaml`: reusable workflow that loads `amd64.env`
- `.github/workflows/scripts/yaml_diff.py`: stub that lists the imported repositories
- `rsf.repos`: repositories to import

The workflow runs on a pull request that changes `rsf.repos` when the label `tag:run-parameter-check` is added.
