"""APIs.guru adapter — 4000+ OpenAPI specifications."""

import re
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 60


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class APIsGuruSource(IndexSource):
    """APIs.guru — 4000+ OpenAPI specifications."""

    platform = "apisguru"
    api_url = "https://api.apis.guru/v2/list.json"
    description = "APIs.guru OpenAPI specification directory"

    def fetch(self) -> Iterator[LibraryDoc]:
        resp = requests.get(
            self.api_url, timeout=_TIMEOUT,
            headers={"Accept-Encoding": "gzip, deflate"},
        )
        resp.raise_for_status()
        providers = resp.json()

        for provider_name, apis in providers.items():
            # Each provider can have multiple API versions
            for api_key, api_info in apis.get("versions", {}).items():
                info = api_info.get("info", {})
                title = info.get("title", provider_name)

                # Use the swagger/openapi spec URL as the doc URL
                spec_url = api_info.get("swaggerUrl") or api_info.get(
                    "openapiVer", ""
                )
                if not spec_url:
                    # Fall back to the explorer URL
                    spec_url = f"https://apis.guru/browse-apis/?provider={provider_name}"

                # Use the externalDocs URL if available (usually better for humans)
                external_docs = info.get("externalDocs", {}).get("url", "")
                doc_url = external_docs or spec_url

                yield LibraryDoc(
                    name=_normalize_name(provider_name),
                    display_name=title,
                    doc_url=doc_url,
                    doc_type="api-spec",
                    quality_signals={
                        "provider": provider_name,
                        "version": api_key,
                        "has_external_docs": bool(external_docs),
                        "categories": info.get("x-apisguru-categories", []),
                    },
                )
                # Only yield one entry per provider (the latest version)
                break
