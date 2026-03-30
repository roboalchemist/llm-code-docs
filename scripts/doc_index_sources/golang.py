"""Go module index adapter — Go package documentation via index.golang.org."""

import re
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 60


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


def _module_to_name(module: str) -> str:
    """Convert a Go module path to a short name.

    e.g. github.com/gin-gonic/gin -> gin
         golang.org/x/net -> net
    """
    parts = module.rstrip("/").split("/")
    return parts[-1] if parts else module


class GolangSource(IndexSource):
    """Go module index — Go package documentation via pkg.go.dev."""

    platform = "golang"
    api_url = "https://index.golang.org/index"
    description = "Go module index (pkg.go.dev)"

    def fetch(self) -> Iterator[LibraryDoc]:
        # The index endpoint returns newline-delimited JSON
        # Each line is {"Path":"...", "Version":"...", "Timestamp":"..."}
        # Use ?limit=2000 for large batches
        seen: set[str] = set()

        resp = requests.get(
            self.api_url,
            params={"limit": 2000},
            timeout=_TIMEOUT,
            stream=True,
        )
        resp.raise_for_status()

        import json
        for line in resp.iter_lines(decode_unicode=True):
            if not line:
                continue
            try:
                entry = json.loads(line)
            except (json.JSONDecodeError, ValueError):
                continue

            module = entry.get("Path", "")
            if not module or module in seen:
                continue
            seen.add(module)

            short_name = _module_to_name(module)

            yield LibraryDoc(
                name=_normalize_name(short_name),
                display_name=short_name,
                doc_url=f"https://pkg.go.dev/{module}",
                language="go",
                doc_type="html",
                quality_signals={
                    "module": module,
                    "version": entry.get("Version", ""),
                },
            )
