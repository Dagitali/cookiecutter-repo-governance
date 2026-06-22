# Contributing Guidelines

Version-controllable contributions toward improving [this project][README.md] (its source code,
documentation, etc.) are welcome via GitHub's pull request process. By submitting a pull request,
you acknowledge and agree to licensing your contribution to [Dagitali LLC][owner].

Before making substantial changes, please open an issue or discussion so maintainers can confirm the
scope, expected behavior, and review path.

- [Ways to Contribute](#ways-to-contribute)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Protected-Branch Workflow](#protected-branch-workflow)
  - [Preferred Flow](#preferred-flow)
  - [Recommended Branch Mapping](#recommended-branch-mapping)
- [Maintainer Runbooks](#maintainer-runbooks)
- [Code of Conduct](#code-of-conduct)
- [Local Quality Gates](#local-quality-gates)

## Ways to Contribute

Not every valuable contribution needs to be code. cookiecutter-repo-governance also benefits from
codeless contributions, such as:

- Documentation corrections and clarity improvements
- Reproducible bug reports with environment details and sample inputs
- Validation of rendered template output across supported Git hosting services
- Examples, tutorials, and workflow suggestions
- Issue triage and feedback on feature proposals
- Answers to usage questions in community channels
- Sponsorship through [GitHub Sponsors] or [Buy Me a Coffee][Buy Me a Coffee]

If you are looking for the lowest-friction way to help, strong documentation, feedback, and
reproducible bug reports are often as valuable as small code changes.

## How to Contribute

1. Open an issue to discuss substantial changes.
2. Fork the repository and create a feature branch.
3. Add or update tests and documentation when appropriate.
4. Open a pull request describing your changes.

## Pull Request Process

1. Do not commit or push directly to the protected `main` or `develop` branches. Work from a topic
   branch and open a pull request instead.
2. Update the [README] when user-facing behavior, support expectations, repository workflows, or
   examples change.
3. For release-affecting changes (CI, release automation, usage snippets, or stable public surface
   decisions), consult [.github/MAINTAINER-RUNBOOKS.md].
4. Keep protected-branch settings and required checks aligned with the repository's documented
   contribution and review process in [.github/BRANCH-PROTECTION.md].
5. Merge only after the protected-branch requirements have been satisfied. The recommended baseline
   is one approval for `develop` and two approvals, or one approval for small teams, for `main`.
6. For release expectations and versioning rules, consult the release policy and checklist used by
   this repository.

## Protected-Branch Workflow

cookiecutter-repo-governance uses GitFlow-style branch roles with protected integration branches.

- Treat `feature/*`, `release/*`, and `hotfix/*` as working branches.
- Treat `develop` and `main` as GitHub-managed integration branches.
- Do not rely on `git flow feature finish` or `git flow release finish` as the authoritative way to
  update protected branches. Those commands create local merges, but protected branches and required
  checks are enforced in GitHub.

### Preferred Flow

1. Create a topic branch from the correct base branch.
2. Push the topic branch.
3. Open a pull request into the protected target branch. Feature branches should target `develop`;
   only `release/*` and `hotfix/*` should target `main`.
4. Let the required checks run against the proposed branch change.
5. Merge the pull request in GitHub after the branch protection requirements pass.

### Recommended Branch Mapping

- `feature/*` -> pull request into `develop`
- `release/*` -> pull request into `main`
- `hotfix/*` -> pull request into `main`

Use [.github/pull_request_template.md] when opening pull requests so validation, risks, and
follow-up work are visible during review.

After a release or hotfix lands on `main`, sync that change back into `develop` deliberately rather
than assuming a local GitFlow finish command already made both protected branches authoritative.

For small/solo maintainer teams, using pull requests for both feature and release branches is
still normal once protected branches are enabled. The repository owner can keep the review workflow
while choosing lower-friction settings, such as fewer required approvals on `develop`, or an admin
bypass policy that is intentionally narrow and documented.

## Maintainer Runbooks

Maintainer runbooks should stay focused on project-local operating procedures, such as:

- Feature branch integration under protected branches
- Release and hotfix branch finishing
- Syncing `main` back into `develop`
- Tagging and tag-triggered release behavior

Private operator procedures, credentials, incident-response steps, and recovery playbooks should
live outside the repository.

## Code of Conduct

All contributors are expected to read and follow [CODE_OF_CONDUCT.md].

## Local Quality Gates

Run the repository's documented local checks before opening a pull request:

```bash
python -m pip install -e ".[dev]"
pre-commit run --all-files
ruff check hooks tests
pytest
```

[Buy Me a Coffee]: https://buymeacoffee.com/djrlj694
[CODE_OF_CONDUCT.md]: CODE_OF_CONDUCT.md
[GitHub Sponsors]: https://github.com/sponsors/Dagitali
[.github/BRANCH-PROTECTION.md]: .github/BRANCH-PROTECTION.md
[.github/MAINTAINER-RUNBOOKS.md]: .github/MAINTAINER-RUNBOOKS.md
[.github/pull_request_template.md]: .github/pull_request_template.md
[owner]: https://dagitali.com
[README.md]: README.md
