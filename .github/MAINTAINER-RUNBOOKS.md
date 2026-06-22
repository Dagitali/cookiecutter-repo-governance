# Maintainer Runbooks

Maintainer-facing runbooks for working with protected branches, GitHub pull requests, and tagged
releases.

- [Operating Model](#operating-model)
- [Feature Branch Runbook](#feature-branch-runbook)
- [Release Branch Runbook](#release-branch-runbook)
- [Hotfix Branch Runbook](#hotfix-branch-runbook)
- [Sync Main Back To Develop](#sync-main-back-to-develop)
- [Tagging](#tagging)
- [Solo-Maintainer Notes](#solo-maintainer-notes)
- [Keep Private Elsewhere](#keep-private-elsewhere)

## Operating Model

cookiecutter-repo-governance uses GitFlow-style branch names together with GitHub-protected
`develop` and `main` branches.

The important consequence is:

- Working happens on `feature/*`, `release/*`, and `hotfix/*`
- Authoritative integration happens through pull requests
- `feature/*` branches target `develop`
- `release/*` and `hotfix/*` branches target `main`
- `develop` and `main` are GitHub-managed integration branches

Local `git flow feature finish` and `git flow release finish` may still be useful for personal
experimentation in a local clone, but they should not be treated as the final source of truth for
protected branches.

## Feature Branch Runbook

Use for normal development work.

1. Create a local feature branch from `develop`.
   Example: `git flow feature start refine-template-docs`
2. Commit your changes locally on that feature branch.
3. Push the feature branch to the remote GitHub repository.
   Example: `git push -u origin feature/refine-template-docs`
4. Open a pull request from the remote `feature/*` branch into `develop`.
5. Let CI run on GitHub.
6. Merge the pull request in GitHub once required checks and review requirements pass.
7. Delete the remote feature branch after merge if it is no longer needed.

## Release Branch Runbook

Use for release stabilization and promotion.

1. Create a local `release/<version>` branch from `develop`.
   Example: `git flow release start 0.3.0`
2. Commit release-targeted stabilization changes locally on that release branch.
3. Push the release branch to the remote GitHub repository.
   Example: `git push -u origin release/0.3.0`
4. Open a pull request from the remote `release/*` branch into `main`.
5. Merge the pull request on GitHub after required checks and review requirements pass.
6. Fetch the newly merged remote `main` commit into your local repository.
   Example: `git fetch origin main`
7. Create an annotated release tag that points at the fetched `main` commit.
   Example: `git tag -a v0.3.0 origin/main -m "Release v0.3.0"`
8. Push the annotated release tag to GitHub.
   Example: `git push origin v0.3.0`
9. Sync the resulting remote `main` state back into `develop`.
   See [Sync Main Back To Develop](#sync-main-back-to-develop).

## Hotfix Branch Runbook

Use for urgent fixes that must land on `main` first.

1. Create a local `hotfix/<version>` branch from `main`.
   Example: `git flow hotfix start 0.3.1`
2. Apply and validate the fix locally on that hotfix branch.
3. Push the hotfix branch to the remote GitHub repository.
   Example: `git push -u origin hotfix/0.3.1`
4. Open a pull request from the remote `hotfix/*` branch into `main`.
5. Merge the pull request in GitHub after required checks and review requirements pass.
6. Create and push an annotated hotfix tag from the authoritative merged `main` commit.
7. Sync the resulting remote `main` state back into `develop`.

## Sync Main Back To Develop

After a release or hotfix lands on `main`, update `develop` deliberately rather than assuming both
protected branches are already aligned.

Preferred sequence:

1. Fetch the latest remote `main` and `develop` state.
   Example: `git fetch origin main develop`
2. Create a temporary sync branch from updated `develop`.
   Example: `git switch develop && git pull --ff-only origin develop && git switch -c sync/main-into-develop`
3. Merge the updated remote `main` state into the sync branch.
   Example: `git merge --no-ff origin/main`
4. Push the sync branch and open a pull request into `develop`.
   Example: `git push -u origin sync/main-into-develop`
5. Merge on GitHub once required checks pass.

## Tagging

- Use annotated tags for public releases.
- Tag the authoritative merged `main` commit.
- Use `vMAJOR.MINOR.PATCH` tag names.
- Keep the tag annotation concise, verb-oriented, and release-focused.

## Solo-Maintainer Notes

It is normal for a solo maintainer to use pull requests for both feature and release branches once
protected branches are enabled.

The pull request still provides value:

- Required checks run before the protected branch moves
- GitHub remains the authoritative merge surface for protected branches
- Release and branch history stay aligned with the repository protection model

## Keep Private Elsewhere

Sensitive operator documentation should live outside the public repository.

Examples that should live in a truly private location include:

- Secrets and credential recovery procedures
- Emergency branch-protection bypass procedures
- Security-incident response details
- Account recovery or succession notes
