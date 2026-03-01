"""cljdoc adapter — Clojure/ClojureScript library documentation (470+ libraries)."""

import re
from typing import Iterator
from xml.etree import ElementTree

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class CljdocSource(IndexSource):
    """cljdoc — Clojure/ClojureScript library documentation."""

    platform = "cljdoc"
    api_url = "https://cljdoc.org/sitemap.xml"
    description = "cljdoc Clojure/ClojureScript documentation"

    def fetch(self) -> Iterator[LibraryDoc]:
        resp = requests.get(self.api_url, timeout=_TIMEOUT)
        resp.raise_for_status()

        root = ElementTree.fromstring(resp.content)
        # Sitemap namespace
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

        seen: set[str] = set()

        for url_elem in root.findall("sm:url", ns):
            loc = url_elem.findtext("sm:loc", "", ns)
            if not loc:
                continue

            # URLs look like: https://cljdoc.org/d/group/artifact/version
            # We want unique group/artifact pairs
            parts = loc.replace("https://cljdoc.org/d/", "").split("/")
            if len(parts) < 2:
                continue

            group = parts[0]
            artifact = parts[1]
            key = f"{group}/{artifact}"
            if key in seen:
                continue
            seen.add(key)

            # Use artifact as the display name, group/artifact as full identifier
            display = artifact if group == artifact else f"{group}/{artifact}"

            yield LibraryDoc(
                name=_normalize_name(artifact),
                display_name=display,
                doc_url=f"https://cljdoc.org/d/{group}/{artifact}",
                language="clojure",
                doc_type="html",
                quality_signals={
                    "group": group,
                    "artifact": artifact,
                },
            )
