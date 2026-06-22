"""
:mod:`post_gen_project` module.

Post-generation cleanup for rendered repository governance projects.
"""

import shutil
from collections.abc import Mapping
from pathlib import Path

# SECTION: CONSTANTS ======================================================== #


PROJECT_ROOT = Path.cwd()
HOST_DIRECTORIES = {
    'GitHub': Path('.github'),
    'GitLab': Path('.gitlab'),
    'Bitbucket': Path('.bitbucket'),
    'Azure DevOps': Path('.azuredevops'),
}

GITHUB_OPTIONAL_PATHS = {
    'include_issue_templates': (Path('.github') / 'ISSUE_TEMPLATE',),
    'include_pull_request_template': (Path('.github') / 'pull_request_template.md',),
    'include_branch_protection_docs': (Path('.github') / 'BRANCH-PROTECTION.md',),
    'include_maintainer_runbooks': (Path('.github') / 'MAINTAINER-RUNBOOKS.md',),
    'include_funding': (Path('.github') / 'FUNDING.yml',),
}
OPTIONAL_PATHS = {
    'include_references': (Path('REFERENCES.md'),),
    'include_agents_md': (Path('AGENTS.md'),),
}
RELEASE_DOC_PATHS = (
    Path('RELEASE-POLICY.md'),
    Path('RELEASE-CHECKLIST.md'),
)
GITHUB_RELEASE_DOC_PATHS = (Path('.github') / 'RELEASE-NOTES-TEMPLATE.md',)


# SECTION: INTERNAL FUNCTIONS =============================================== #


def _as_bool(
    value: str,
) -> bool:
    """Convert a string value to a boolean."""
    return value.strip().lower() in {'yes', 'y', 'true', '1'}


def _cleanup_generated_project(
    project_root: Path,
    git_service: str,
    options: Mapping[str, bool],
) -> None:
    """Remove generated files that do not match the selected template options."""
    is_github = git_service == 'GitHub'

    for service, relative_path in HOST_DIRECTORIES.items():
        if git_service != service:
            _remove_path(project_root / relative_path)

    if is_github:
        for option, relative_paths in GITHUB_OPTIONAL_PATHS.items():
            if not options[option]:
                for relative_path in relative_paths:
                    _remove_path(project_root / relative_path)

    if not options['include_release_docs']:
        for relative_path in RELEASE_DOC_PATHS:
            _remove_path(project_root / relative_path)
        if is_github:
            for relative_path in GITHUB_RELEASE_DOC_PATHS:
                _remove_path(project_root / relative_path)

    for option, relative_paths in OPTIONAL_PATHS.items():
        if not options[option]:
            for relative_path in relative_paths:
                _remove_path(project_root / relative_path)

    _remove_empty_directory(project_root / HOST_DIRECTORIES['GitHub'])


def _remove_path(
    path: Path,
) -> None:
    """Remove a file or directory at the given path."""
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def _remove_empty_directory(
    path: Path,
) -> None:
    """Remove the directory at the given path if it is empty."""
    if path.exists() and path.is_dir() and not any(path.iterdir()):
        path.rmdir()


# SECTION: FUNCTIONS ======================================================== #


def main() -> None:
    """Main entry point for post-generation cleanup."""
    git_service = '{{ cookiecutter.git_service }}'
    options = {
        'include_issue_templates': _as_bool(
            '{{ cookiecutter.include_issue_templates }}',
        ),
        'include_pull_request_template': _as_bool(
            '{{ cookiecutter.include_pull_request_template }}',
        ),
        'include_release_docs': _as_bool(
            '{{ cookiecutter.include_release_docs }}',
        ),
        'include_branch_protection_docs': _as_bool(
            '{{ cookiecutter.include_branch_protection_docs }}',
        ),
        'include_maintainer_runbooks': _as_bool(
            '{{ cookiecutter.include_maintainer_runbooks }}',
        ),
        'include_references': _as_bool('{{ cookiecutter.include_references }}'),
        'include_agents_md': _as_bool('{{ cookiecutter.include_agents_md }}'),
        'include_funding': _as_bool('{{ cookiecutter.include_funding }}'),
    }

    _cleanup_generated_project(PROJECT_ROOT, git_service, options)


# SECTION: MAIN ENTRY POINT ================================================= #


if __name__ == '__main__':
    main()
