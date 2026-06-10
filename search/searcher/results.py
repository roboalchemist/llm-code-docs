"""Search result dataclasses."""

from dataclasses import dataclass
import pandas as pd


@dataclass
class SearchResults:
    """Container for search results from both tables."""

    documents: pd.DataFrame
    folders: pd.DataFrame
    query: str
    total_documents: int
    total_folders: int
