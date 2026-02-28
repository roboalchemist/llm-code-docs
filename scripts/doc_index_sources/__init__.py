"""Doc-index source adapters registry."""

from .devdocs import DevDocsSource
from .dash import DashSource
from .devhints import DevhintsSource
from .apisguru import APIsGuruSource

# Registry of all available source adapters, keyed by platform name.
# Order reflects recommended build sequence (Tier A first = quick wins).
SOURCES: dict[str, type] = {
    "devdocs": DevDocsSource,
    "dash": DashSource,
    "devhints": DevhintsSource,
    "apisguru": APIsGuruSource,
}
