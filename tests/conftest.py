"""
:mod:`tests.conftest` module.

Shared fixtures for pytest-based tests.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from tests.pytest_helpers import PROJECT_ROOT
from tests.pytest_helpers import load_cookiecutter_config

# SECTION: CONSTANTS ======================================================== #


DIRECTORY_MARKERS = {
    'e2e': pytest.mark.e2e,
    'integration': pytest.mark.integration,
    'meta': pytest.mark.meta,
    'unit': pytest.mark.unit,
}


# SECTION: HOOKS ============================================================ #


def pytest_collection_modifyitems(
    items: list[pytest.Item],
) -> None:
    """Apply scope markers from each test module's directory."""
    for item in items:
        test_parts = item.path.relative_to(PROJECT_ROOT).parts
        if len(test_parts) < 2 or test_parts[0] != 'tests':
            continue

        marker = DIRECTORY_MARKERS.get(test_parts[1])
        if marker is not None:
            item.add_marker(marker)


# SECTION: FIXTURES ========================================================= #


@pytest.fixture(name='project_root')
def project_root_fixture() -> Path:
    """Return the repository root path."""
    return PROJECT_ROOT


@pytest.fixture(name='cookiecutter_config')
def cookiecutter_config_fixture() -> dict[str, Any]:
    """Load the template's Cookiecutter configuration."""
    return load_cookiecutter_config()
