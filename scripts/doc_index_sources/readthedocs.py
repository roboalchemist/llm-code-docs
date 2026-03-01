"""ReadTheDocs adapter — discovers projects via subfinder subdomain enumeration.

ReadTheDocs API v3 requires authentication and v2 list endpoints are disabled.
Instead, we use subfinder to enumerate *.readthedocs.io subdomains passively,
which gives us 20K+ project slugs for free.

Requires: subfinder (go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest)
"""

import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Iterator

from ._base import IndexSource, LibraryDoc

_SUBFINDER_TIMEOUT = 300  # 5 minutes max


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


def _find_subfinder() -> str | None:
    """Find the subfinder binary."""
    # Check common locations
    for path in [
        os.path.expanduser("~/go/bin/subfinder"),
        "/usr/local/bin/subfinder",
        "/usr/bin/subfinder",
    ]:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    # Try PATH
    try:
        result = subprocess.run(
            ["which", "subfinder"], capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return None


# Subdomains to skip — infrastructure, not documentation projects
_SKIP_PREFIXES = {
    "www", "app", "api", "docs", "blog", "status", "help",
    "support", "community", "about", "readthedocs",
}


class ReadTheDocsSource(IndexSource):
    """ReadTheDocs — project documentation via subfinder subdomain enumeration."""

    platform = "readthedocs"
    api_url = "https://readthedocs.io"
    description = "ReadTheDocs project documentation (via subfinder)"

    def fetch(self) -> Iterator[LibraryDoc]:
        subfinder = _find_subfinder()
        if not subfinder:
            raise RuntimeError(
                "subfinder not found. Install: "
                "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
            )

        # Run subfinder to enumerate subdomains
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False
        ) as tmp:
            tmp_path = tmp.name

        try:
            subprocess.run(
                [subfinder, "-d", "readthedocs.io", "-silent", "-o", tmp_path],
                capture_output=True, text=True,
                timeout=_SUBFINDER_TIMEOUT,
            )

            subdomains = Path(tmp_path).read_text().strip().splitlines()
        finally:
            Path(tmp_path).unlink(missing_ok=True)

        seen: set[str] = set()

        for line in subdomains:
            line = line.strip().lower()
            if not line or not line.endswith(".readthedocs.io"):
                continue

            # Extract the project slug (subdomain part)
            slug = line.replace(".readthedocs.io", "")

            # Skip infrastructure subdomains and duplicates
            if not slug or slug in _SKIP_PREFIXES or slug in seen:
                continue
            # Skip subdomains with dots (nested like foo.bar.readthedocs.io)
            if "." in slug:
                continue
            seen.add(slug)

            yield LibraryDoc(
                name=_normalize_name(slug),
                display_name=slug,
                doc_url=f"https://{slug}.readthedocs.io/",
                doc_type="html",
                quality_signals={
                    "slug": slug,
                    "discovery": "subfinder",
                },
            )
