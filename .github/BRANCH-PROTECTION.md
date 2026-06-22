# Branch Protection

This document defines the recommended GitHub branch protection configuration for the protected
`main` and `develop` branches used by cookiecutter-repo-governance.

- [Purpose](#purpose)
- [Recommended Required Checks](#recommended-required-checks)
  - [Current Required Check Names](#current-required-check-names)
- [Shared Protection Baseline](#shared-protection-baseline)
- [Branch Protection Checklist For `main`](#branch-protection-checklist-for-main)
- [Branch Protection Checklist For `develop`](#branch-protection-checklist-for-develop)
- [How To Disallow Direct Pushes](#how-to-disallow-direct-pushes)
- [How To Update Required Checks In GitHub](#how-to-update-required-checks-in-github)
- [Maintenance Notes](#maintenance-notes)

## Purpose

These protections enforce three repository policies:

- No direct pushes to `main`
- No direct pushes to `develop`
- No merge into either protected branch unless the required CI checks pass

Local hooks in `.pre-commit-config.yaml` complement this policy, but GitHub branch protection is the
authoritative enforcement layer.

## Recommended Required Checks

Require the CI checks that validate repository hygiene, Python linting, and template rendering.
GitHub exposes matrix jobs by their resolved names in branch protection settings.

### Current Required Check Names

Select these status checks for both protected branches:

- `Guard PR target branch`
- `Repository hygiene checks`
- `Template validation on Python 3.13`
- `Template validation on Python 3.14`

These checks cover:

- GitFlow target-branch enforcement for pull requests
- Pre-commit repository hygiene checks
- Ruff linting for hooks and tests
- Unit tests for post-generation hook helpers
- Integration tests for rendered Cookiecutter output

## Shared Protection Baseline

Apply this baseline to both protected branches:

- Require a pull request before merging
- Dismiss stale approvals when new commits are pushed
- Require conversation resolution before merging
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Add the required checks listed above
- Block force pushes
- Block branch deletion
- Keep bypass actors empty if possible

## Branch Protection Checklist For `main`

Target:

- Branch name pattern: `main`
- Enforcement: `Active`

Branch-specific additions:

- Require `2` approvals, or `1` approval for small maintainer teams
- Require Code Owners review
- Consider requiring signed commits

## Branch Protection Checklist For `develop`

Target:

- Branch name pattern: `develop`
- Enforcement: `Active`

Branch-specific additions:

- Require `1` approval
- Require Code Owners review for sensitive paths when practical

## How To Disallow Direct Pushes

The reliable way to disallow direct pushes is to protect the branch and require pull requests. CI
alone cannot block a normal direct push after the fact, because GitHub Actions runs only after the
push exists.

In GitHub:

1. Open repository `Settings`.
2. Open `Branches`.
3. Open the branch protection rule for `main` or `develop`.
4. Enable `Require a pull request before merging`.
5. Enable `Require status checks to pass before merging`.
6. Enable `Require branches to be up to date before merging`.
7. Enable `Block force pushes`.
8. Enable `Block deletions`.
9. Remove bypass actors unless there is a strict operational need.

## How To Update Required Checks In GitHub

After workflow job names change, update protected-branch rules so required checks match the current
CI job names.

In GitHub:

1. Open repository `Settings`.
2. Open `Branches`.
3. Open the branch protection rule for `main`.
4. Under `Require status checks to pass`, remove stale check names.
5. Add the current required checks listed above.
6. Save the `main` branch protection rule.
7. Repeat the same status-check set for `develop` unless the branch intentionally uses a different
   policy.

## Maintenance Notes

- Keep this file aligned with `.github/workflows/ci.yml`.
- Keep branch-target guidance aligned with `CONTRIBUTING.md`.
- Update required check names whenever CI job names change.
