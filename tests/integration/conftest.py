"""
:mod:`tests.integration.conftest` module.

Shared fixtures and helpers for pytest-based integration tests.
"""

from __future__ import annotations

import pytest

# SECTION: MARKERS ========================================================== #


# Directory-level marker for integration tests.
pytestmark = pytest.mark.integration
