"""Hybrid ranking for search results combining semantic, keyword, and recency scores."""

import re
from datetime import datetime
from typing import List, Set
import pandas as pd

from search import config


class HybridRanker:
    """Reranks search results using hybrid scoring."""

    def __init__(
        self,
        semantic_weight: float = None,
        keyword_weight: float = None,
        recency_weight: float = None,
    ):
        """
        Initialize ranker with scoring weights.

        Args:
            semantic_weight: Weight for semantic similarity score.
            keyword_weight: Weight for keyword match score.
            recency_weight: Weight for recency score.
        """
        self.semantic_weight = semantic_weight or config.RANKING_WEIGHTS["semantic"]
        self.keyword_weight = keyword_weight or config.RANKING_WEIGHTS["keyword"]
        self.recency_weight = recency_weight or config.RANKING_WEIGHTS["recency"]

    def rerank_documents(
        self,
        results: pd.DataFrame,
        query: str,
    ) -> pd.DataFrame:
        """
        Rerank document search results with hybrid scoring.

        Args:
            results: DataFrame of search results with similarity_score column.
            query: Original search query.

        Returns:
            Reranked DataFrame with final_score column.
        """
        if results.empty:
            return results

        results = results.copy()

        # Extract query terms
        query_terms = self._extract_terms(query)

        # Calculate hybrid scores
        scores = []
        for _, row in results.iterrows():
            semantic = row.get('similarity_score', 0)
            keyword = self._keyword_score_document(row, query_terms)
            recency = self._recency_score(row.get('last_modified'))

            final_score = (
                self.semantic_weight * semantic +
                self.keyword_weight * keyword +
                self.recency_weight * recency
            )
            scores.append(final_score)

        results['keyword_score'] = [
            self._keyword_score_document(row, query_terms)
            for _, row in results.iterrows()
        ]
        results['recency_score'] = [
            self._recency_score(row.get('last_modified'))
            for _, row in results.iterrows()
        ]
        results['final_score'] = scores

        # Sort by final score
        results = results.sort_values('final_score', ascending=False)

        return results

    def rerank_folders(
        self,
        results: pd.DataFrame,
        query: str,
    ) -> pd.DataFrame:
        """
        Rerank folder search results with hybrid scoring.

        Args:
            results: DataFrame of search results with similarity_score column.
            query: Original search query.

        Returns:
            Reranked DataFrame with final_score column.
        """
        if results.empty:
            return results

        results = results.copy()

        # Extract query terms
        query_terms = self._extract_terms(query)

        # Calculate hybrid scores
        scores = []
        for _, row in results.iterrows():
            semantic = row.get('similarity_score', 0)
            keyword = self._keyword_score_folder(row, query_terms)
            recency = self._recency_score(row.get('last_updated'))

            final_score = (
                self.semantic_weight * semantic +
                self.keyword_weight * keyword +
                self.recency_weight * recency
            )
            scores.append(final_score)

        results['keyword_score'] = [
            self._keyword_score_folder(row, query_terms)
            for _, row in results.iterrows()
        ]
        results['recency_score'] = [
            self._recency_score(row.get('last_updated'))
            for _, row in results.iterrows()
        ]
        results['final_score'] = scores

        # Sort by final score
        results = results.sort_values('final_score', ascending=False)

        return results

    def _extract_terms(self, query: str) -> Set[str]:
        """
        Extract search terms from query.

        Args:
            query: Search query string.

        Returns:
            Set of normalized search terms.
        """
        # Split on whitespace and punctuation
        terms = re.split(r'[\s\-_/\\.,;:!?()[\]{}]+', query.lower())
        # Filter out empty and very short terms
        terms = {t for t in terms if len(t) >= 2}
        return terms

    def _keyword_score_document(
        self,
        row: pd.Series,
        query_terms: Set[str],
    ) -> float:
        """
        Calculate keyword match score for a document.

        Args:
            row: Document row from DataFrame.
            query_terms: Set of query terms.

        Returns:
            Score between 0 and 1.
        """
        if not query_terms:
            return 0.0

        matches = 0
        total_weight = 0

        # Check title (weight 3)
        title = str(row.get('title', '')).lower()
        for term in query_terms:
            if term in title:
                matches += 3
            total_weight += 3

        # Check filename (weight 2)
        filename = str(row.get('filename', '')).lower()
        for term in query_terms:
            if term in filename:
                matches += 2
            total_weight += 2

        # Check framework name (weight 2)
        framework = str(row.get('framework', '')).lower()
        for term in query_terms:
            if term in framework:
                matches += 2
            total_weight += 2

        # Check headings (weight 1)
        headings = row.get('headings', [])
        if isinstance(headings, list):
            headings_text = ' '.join(str(h).lower() for h in headings)
        else:
            headings_text = str(headings).lower()

        for term in query_terms:
            if term in headings_text:
                matches += 1
            total_weight += 1

        # Check content (weight 0.5, limit to first 2000 chars)
        content = str(row.get('content', ''))[:2000].lower()
        for term in query_terms:
            if term in content:
                matches += 0.5
            total_weight += 0.5

        return matches / total_weight if total_weight > 0 else 0.0

    def _keyword_score_folder(
        self,
        row: pd.Series,
        query_terms: Set[str],
    ) -> float:
        """
        Calculate keyword match score for a folder.

        Args:
            row: Folder row from DataFrame.
            query_terms: Set of query terms.

        Returns:
            Score between 0 and 1.
        """
        if not query_terms:
            return 0.0

        matches = 0
        total_weight = 0

        # Check framework name (weight 4)
        name = str(row.get('framework_name', '')).lower()
        for term in query_terms:
            if term in name:
                matches += 4
            total_weight += 4

        # Check description (weight 2)
        description = str(row.get('description', '')).lower()
        for term in query_terms:
            if term in description:
                matches += 2
            total_weight += 2

        # Check all titles (weight 1)
        all_titles = str(row.get('all_titles', '')).lower()
        for term in query_terms:
            if term in all_titles:
                matches += 1
            total_weight += 1

        # Check all headings (weight 0.5)
        all_headings = str(row.get('all_headings', '')).lower()
        for term in query_terms:
            if term in all_headings:
                matches += 0.5
            total_weight += 0.5

        return matches / total_weight if total_weight > 0 else 0.0

    def _recency_score(self, timestamp) -> float:
        """
        Calculate recency score based on last modified time.

        Args:
            timestamp: Last modified timestamp.

        Returns:
            Score between 0 and 1 (1 = very recent).
        """
        if timestamp is None:
            return 0.5  # Neutral score for unknown dates

        try:
            if isinstance(timestamp, str):
                timestamp = datetime.fromisoformat(timestamp)
            elif not isinstance(timestamp, datetime):
                # Handle pandas Timestamp
                timestamp = timestamp.to_pydatetime()

            # Calculate age in days
            now = datetime.utcnow()
            age_days = (now - timestamp).days

            # Score decay: 1.0 for today, 0.5 for ~180 days old, approaches 0 for old docs
            # Using exponential decay with half-life of ~180 days
            score = 0.5 ** (age_days / 180)

            return min(1.0, max(0.0, score))

        except Exception:
            return 0.5  # Neutral score on error


# Global ranker instance
_ranker = None


def get_ranker() -> HybridRanker:
    """Get global ranker instance."""
    global _ranker
    if _ranker is None:
        _ranker = HybridRanker()
    return _ranker
