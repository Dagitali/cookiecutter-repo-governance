"""
:mod:`tests.pytest_helpers` module.

Shared test helper functions and constants.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

# SECTION: CONSTANTS (PRIMARY) ============================================== #


PROJECT_ROOT = Path(__file__).resolve().parents[1]
UNRESOLVED_TEMPLATE_PATTERNS = ('{{', '{%', '{#')


# SECTION: FUNCTIONS ======================================================== #


def load_cookiecutter_config() -> dict[str, Any]:
    """Load the template's Cookiecutter configuration."""
    return json.loads(
        (PROJECT_ROOT / 'cookiecutter.json').read_text(encoding='utf-8'),
    )


def local_markdown_links(
    markdown: str,
) -> list[str]:
    """Return local Markdown link targets from a Markdown document."""
    links = []

    inline_targets = re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', markdown)
    reference_targets = re.findall(r'(?m)^\[[^\]]+\]:\s+(\S+)', markdown)

    for target in inline_targets + reference_targets:
        if target.startswith(
            ('http://', 'https://', 'mailto:', '#'),
        ) or target.startswith('<http'):
            continue
        links.append(target.strip('<>'))

    return links


def markdown_files(
    root: Path,
) -> list[Path]:
    """Return Markdown files below a root path."""
    return sorted(root.rglob('*.md'))


# SECTION: CONSTANTS (SECONDARY) ============================================ #


SUPPORTED_GIT_SERVICES = tuple(load_cookiecutter_config()['git_service'])
