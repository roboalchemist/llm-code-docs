"""ReadTheDocs adapter — Python/multi-language documentation (12K+ projects)."""

import re
import time
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30
_PAGE_DELAY = 1.0  # 60 req/min auth, 5 req/min unauth


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class ReadTheDocsSource(IndexSource):
    """ReadTheDocs — multi-language project documentation."""

    platform = "readthedocs"
    api_url = "https://readthedocs.org/api/v3/projects/"
    description = "ReadTheDocs project documentation"

    def fetch(self) -> Iterator[LibraryDoc]:
        import os
        headers = {}
        token = os.environ.get("RTD_TOKEN")
        if token:
            headers["Authorization"] = f"Token {token}"

        url = self.api_url
        params = {"limit": 100, "ordering": "slug"}

        while url:
            resp = requests.get(
                url, params=params, headers=headers, timeout=_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()

            for project in data.get("results", []):
                slug = project.get("slug", "")
                name = project.get("name", slug)
                if not slug:
                    continue

                language = project.get("programming_language", {})
                if isinstance(language, dict):
                    language = language.get("code", None)

                urls = project.get("urls", {})
                doc_url = urls.get("documentation", f"https://{slug}.readthedocs.io/")

                yield LibraryDoc(
                    name=_normalize_name(slug),
                    display_name=name,
                    doc_url=doc_url,
                    language=language,
                    doc_type="html",
                    quality_signals={
                        "slug": slug,
                    },
                )

            url = data.get("next")
            params = {}  # next URL includes all params
            time.sleep(_PAGE_DELAY)
