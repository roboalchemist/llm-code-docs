"""Dual search logic for querying documents and folders."""

from typing import List, Optional
import pandas as pd

from search import config
from search.db.connection import get_connection
from search.embeddings.generator import get_generator
from search.searcher.results import SearchResults


class QueryProcessor:
    """Processes search queries against documents and folders tables."""

    def __init__(self):
        """Initialize query processor with required components."""
        self.db = get_connection()
        self.generator = get_generator()

    def search(
        self,
        query: str,
        doc_limit: int = None,
        folder_limit: int = None,
        category: Optional[str] = None,
        framework: Optional[str] = None,
    ) -> SearchResults:
        """
        Search for documents and folders matching the query.

        Args:
            query: Search query string.
            doc_limit: Maximum number of documents to return.
            folder_limit: Maximum number of folders to return.
            category: Filter by category (llms-txt, github-scraped, web-scraped).
            framework: Filter by specific framework.

        Returns:
            SearchResults containing matching documents and folders.
        """
        doc_limit = doc_limit or config.DEFAULT_SEARCH_LIMIT
        folder_limit = folder_limit or config.DEFAULT_FOLDER_LIMIT

        # Generate query embedding
        query_embedding = self.generator.generate_single(query)

        # Search documents
        documents = self._search_documents(
            query_embedding,
            limit=doc_limit,
            category=category,
            framework=framework,
        )

        # Search folders
        folders = self._search_folders(
            query_embedding,
            limit=folder_limit,
            category=category,
        )

        return SearchResults(
            documents=documents,
            folders=folders,
            query=query,
            total_documents=len(documents),
            total_folders=len(folders),
        )

    def _search_documents(
        self,
        query_embedding: List[float],
        limit: int,
        category: Optional[str] = None,
        framework: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        Search documents table with vector similarity.

        Args:
            query_embedding: Query embedding vector.
            limit: Maximum results to return.
            category: Optional category filter.
            framework: Optional framework filter.

        Returns:
            DataFrame of matching documents with scores.
        """
        if not self.db.table_exists("documents"):
            return pd.DataFrame()

        try:
            # Build search query
            search = self.db.documents_table.search(query_embedding)

            # Apply filters
            filter_conditions = []
            if category:
                filter_conditions.append(f'category = "{category}"')
            if framework:
                filter_conditions.append(f'framework = "{framework}"')

            if filter_conditions:
                where_clause = " AND ".join(filter_conditions)
                search = search.where(where_clause)

            # Execute search with more results to allow for deduplication
            results = search.limit(limit * 3).to_pandas()

            if results.empty:
                return pd.DataFrame()

            # Deduplicate by path (keep highest scoring chunk per document)
            results = results.sort_values('_distance', ascending=True)
            results = results.drop_duplicates(subset=['path'], keep='first')

            # Convert distance to similarity score (cosine distance to similarity)
            results['similarity_score'] = 1 - results['_distance']

            # Limit results
            results = results.head(limit)

            return results

        except Exception as e:
            print(f"Error searching documents: {e}")
            return pd.DataFrame()

    def _search_folders(
        self,
        query_embedding: List[float],
        limit: int,
        category: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        Search folders table with vector similarity.

        Args:
            query_embedding: Query embedding vector.
            limit: Maximum results to return.
            category: Optional category filter.

        Returns:
            DataFrame of matching folders with scores.
        """
        if not self.db.table_exists("folders"):
            return pd.DataFrame()

        try:
            # Build search query
            search = self.db.folders_table.search(query_embedding)

            # Apply filters
            if category:
                search = search.where(f'category = "{category}"')

            # Execute search
            results = search.limit(limit).to_pandas()

            if results.empty:
                return pd.DataFrame()

            # Convert distance to similarity score
            results['similarity_score'] = 1 - results['_distance']

            return results

        except Exception as e:
            print(f"Error searching folders: {e}")
            return pd.DataFrame()

    def search_documents_only(
        self,
        query: str,
        limit: int = None,
        category: Optional[str] = None,
        framework: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        Search only the documents table.

        Args:
            query: Search query string.
            limit: Maximum results to return.
            category: Optional category filter.
            framework: Optional framework filter.

        Returns:
            DataFrame of matching documents.
        """
        limit = limit or config.DEFAULT_SEARCH_LIMIT
        query_embedding = self.generator.generate_single(query)

        return self._search_documents(
            query_embedding,
            limit=limit,
            category=category,
            framework=framework,
        )

    def search_folders_only(
        self,
        query: str,
        limit: int = None,
        category: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        Search only the folders table.

        Args:
            query: Search query string.
            limit: Maximum results to return.
            category: Optional category filter.

        Returns:
            DataFrame of matching folders.
        """
        limit = limit or config.DEFAULT_FOLDER_LIMIT
        query_embedding = self.generator.generate_single(query)

        return self._search_folders(
            query_embedding,
            limit=limit,
            category=category,
        )

    def get_document_by_path(self, path: str) -> Optional[pd.DataFrame]:
        """
        Get document(s) by file path.

        Args:
            path: File path to search for.

        Returns:
            DataFrame of matching document chunks or None.
        """
        if not self.db.table_exists("documents"):
            return None

        try:
            df = self.db.documents_table.to_pandas()
            results = df[df['path'] == path]
            return results if not results.empty else None
        except Exception as e:
            print(f"Error getting document by path: {e}")
            return None

    def get_folder_by_name(self, name: str) -> Optional[pd.DataFrame]:
        """
        Get folder by framework name.

        Args:
            name: Framework name to search for.

        Returns:
            DataFrame row for the folder or None.
        """
        if not self.db.table_exists("folders"):
            return None

        try:
            df = self.db.folders_table.to_pandas()
            results = df[df['framework_name'] == name]
            return results if not results.empty else None
        except Exception as e:
            print(f"Error getting folder by name: {e}")
            return None


# Global query processor instance
_processor = None


def get_processor() -> QueryProcessor:
    """Get global query processor instance."""
    global _processor
    if _processor is None:
        _processor = QueryProcessor()
    return _processor
