"""FastAPI application for librarian search and suggestions.

Provides REST API endpoints for:
- Full hybrid search over indexed documentation
- Fast framework/library suggestions
- Service health checks including OpenSearch status

Usage:
    uvicorn api.main:app --host 0.0.0.0 --port 8080
"""

import logging
import math
import time
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from search.opensearch.client import OpenSearchClient, get_client, reset_client
from search.opensearch.searcher import (
    HybridSearcher,
    HybridSearchConfig,
    SearchMetrics,
    get_searcher,
    reset_searcher,
)
from search.opensearch import config as os_config

logger = logging.getLogger(__name__)

# =============================================================================
# Pydantic Models
# =============================================================================


class HealthDependency(BaseModel):
    """Health status of a single dependency."""
    status: str = Field(..., description="Dependency status: ok or error")
    latency_ms: float = Field(..., description="Latency of health check in milliseconds")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional details")


class HealthResponse(BaseModel):
    """Response model for /health endpoint."""
    status: str = Field(..., description="Overall service status: ok, degraded, or error")
    version: str = Field(..., description="API version")
    dependencies: Dict[str, HealthDependency] = Field(
        ..., description="Status of each dependency"
    )


class SearchResultItem(BaseModel):
    """A single search result."""
    doc_id: str = Field(..., description="Document identifier")
    title: str = Field("", description="Document title")
    content: str = Field("", description="Document content or snippet")
    framework: str = Field("", description="Framework/library name")
    category: str = Field("", description="Source category")
    file_path: str = Field("", description="File path within the framework")
    score: float = Field(0.0, description="Relevance score (0-1)")
    highlight: Optional[str] = Field(None, description="Highlighted content snippet")
    chunk_index: int = Field(0, description="Chunk index within the document")
    total_chunks: int = Field(1, description="Total chunks in the document")


class SearchResponse(BaseModel):
    """Response model for /search endpoint."""
    query: str = Field(..., description="Original search query")
    results: List[SearchResultItem] = Field(..., description="Search results")
    total_hits: int = Field(0, description="Total number of matching documents")
    returned: int = Field(0, description="Number of results returned")
    took_ms: float = Field(0.0, description="OpenSearch query time in milliseconds")
    total_latency_ms: float = Field(0.0, description="Total end-to-end latency in milliseconds")


class SuggestResultItem(BaseModel):
    """A single suggestion result."""
    framework_name: str = Field(..., description="Framework/library name")
    description: str = Field("", description="Brief description")
    category: str = Field("", description="Source category")
    path: str = Field("", description="Path to documentation")
    file_count: int = Field(0, description="Number of documentation files")
    source_url: str = Field("", description="Original source URL")
    score: float = Field(0.0, description="Relevance score (0-1)")


class SuggestResponse(BaseModel):
    """Response model for /suggest endpoint."""
    query: str = Field(..., description="Original suggestion query")
    suggestions: List[SuggestResultItem] = Field(..., description="Framework suggestions")
    total_hits: int = Field(0, description="Total number of matching frameworks")
    returned: int = Field(0, description="Number of suggestions returned")
    took_ms: float = Field(0.0, description="Query time in milliseconds")
    total_latency_ms: float = Field(0.0, description="Total end-to-end latency in milliseconds")


# =============================================================================
# Application Factory
# =============================================================================


def create_app(
    opensearch_client: Optional[OpenSearchClient] = None,
    searcher: Optional[HybridSearcher] = None,
) -> FastAPI:
    """Create and configure the FastAPI application.

    Args:
        opensearch_client: Optional pre-configured OpenSearch client (for testing).
        searcher: Optional pre-configured HybridSearcher (for testing).

    Returns:
        Configured FastAPI application.
    """
    application = FastAPI(
        title="Librarian Search API",
        description="Search and suggestion API for llm-code-docs documentation.",
        version="0.1.0",
    )

    # Store injected dependencies on the app state for use in endpoints
    application.state.opensearch_client = opensearch_client
    application.state.searcher = searcher

    def _get_client() -> OpenSearchClient:
        """Get OpenSearch client, preferring injected instance."""
        if application.state.opensearch_client is not None:
            return application.state.opensearch_client
        return get_client()

    def _get_searcher() -> HybridSearcher:
        """Get HybridSearcher, preferring injected instance."""
        if application.state.searcher is not None:
            return application.state.searcher
        return get_searcher()

    # =========================================================================
    # GET /health
    # =========================================================================

    @application.get(
        "/health",
        response_model=HealthResponse,
        summary="Service health check",
        description="Returns service health including OpenSearch connectivity.",
    )
    async def health() -> HealthResponse:
        """Check service health and dependency status."""
        dependencies: Dict[str, HealthDependency] = {}
        overall_status = "ok"

        # Check OpenSearch
        os_start = time.time()
        try:
            client = _get_client()
            is_alive = client.ping()
            os_latency = (time.time() - os_start) * 1000

            if is_alive:
                try:
                    cluster_health = client.health_check()
                    cluster_status = cluster_health.get("status", "unknown")
                    doc_count = client.get_document_count()
                    dependencies["opensearch"] = HealthDependency(
                        status="ok",
                        latency_ms=round(os_latency, 2),
                        details={
                            "cluster_status": cluster_status,
                            "cluster_name": cluster_health.get("cluster_name", "unknown"),
                            "number_of_nodes": cluster_health.get("number_of_nodes", 0),
                            "document_count": doc_count,
                        },
                    )
                    if cluster_status == "red":
                        overall_status = "degraded"
                except Exception as e:
                    dependencies["opensearch"] = HealthDependency(
                        status="ok",
                        latency_ms=round(os_latency, 2),
                        details={"note": f"Ping OK but health check failed: {e}"},
                    )
            else:
                os_latency = (time.time() - os_start) * 1000
                dependencies["opensearch"] = HealthDependency(
                    status="error",
                    latency_ms=round(os_latency, 2),
                    details={"error": "Ping returned False"},
                )
                overall_status = "error"
        except Exception as e:
            os_latency = (time.time() - os_start) * 1000
            dependencies["opensearch"] = HealthDependency(
                status="error",
                latency_ms=round(os_latency, 2),
                details={"error": str(e)},
            )
            overall_status = "error"

        return HealthResponse(
            status=overall_status,
            version="0.1.0",
            dependencies=dependencies,
        )

    # =========================================================================
    # GET /search
    # =========================================================================

    @application.get(
        "/search",
        response_model=SearchResponse,
        summary="Full hybrid search",
        description="Search indexed documentation using BM25 + optional SPLADE + dense vector retrieval.",
    )
    async def search(
        q: str = Query(..., min_length=1, description="Search query string"),
        limit: int = Query(10, ge=1, le=100, description="Maximum number of results"),
        category: Optional[str] = Query(None, description="Filter by category (llms-txt, github-scraped, web-scraped)"),
        framework: Optional[str] = Query(None, description="Filter by framework name"),
        min_score: Optional[float] = Query(None, ge=0.0, le=1.0, description="Minimum relevance score"),
    ) -> SearchResponse:
        """Execute a hybrid search across indexed documentation."""
        start_time = time.time()

        try:
            searcher = _get_searcher()
            results_df, metrics = searcher.search(
                query=q,
                size=limit,
                category=category,
                framework=framework,
                min_score=min_score,
            )
        except Exception as e:
            logger.error(f"Search failed: {e}")
            raise HTTPException(status_code=503, detail=f"Search service unavailable: {e}")

        total_latency = (time.time() - start_time) * 1000

        # Convert DataFrame to response items
        items: List[SearchResultItem] = []
        if not results_df.empty:
            for _, row in results_df.iterrows():
                # Sanitize score: NaN/Inf -> 0.0
                raw_score = row.get("final_score", 0.0)
                score = float(raw_score) if isinstance(raw_score, (int, float)) and math.isfinite(raw_score) else 0.0

                # Sanitize highlight: None/NaN/empty -> None
                raw_highlight = row.get("highlighted_content")
                highlight = None
                if raw_highlight is not None and isinstance(raw_highlight, str) and raw_highlight.strip():
                    highlight = raw_highlight

                items.append(SearchResultItem(
                    doc_id=str(row.get("doc_id", "")),
                    title=str(row.get("title", "")),
                    content=str(row.get("content", ""))[:500],  # Truncate content
                    framework=str(row.get("framework", "")),
                    category=str(row.get("category", "")),
                    file_path=str(row.get("file_path", "")),
                    score=score,
                    highlight=highlight,
                    chunk_index=int(row.get("chunk_index", 0)),
                    total_chunks=int(row.get("total_chunks", 1)),
                ))

        return SearchResponse(
            query=q,
            results=items,
            total_hits=metrics.total_hits,
            returned=len(items),
            took_ms=metrics.took_ms,
            total_latency_ms=round(total_latency, 2),
        )

    # =========================================================================
    # GET /suggest
    # =========================================================================

    @application.get(
        "/suggest",
        response_model=SuggestResponse,
        summary="Fast framework suggestions",
        description=(
            "Get fast framework/library suggestions matching a query. "
            "Optimized for speed (<50ms) using the folders index."
        ),
    )
    async def suggest(
        q: str = Query(..., min_length=1, description="Suggestion query string"),
        limit: int = Query(5, ge=1, le=50, description="Maximum number of suggestions"),
        category: Optional[str] = Query(None, description="Filter by category"),
    ) -> SuggestResponse:
        """Get fast framework suggestions from the folders index."""
        start_time = time.time()

        try:
            searcher = _get_searcher()
            results_df, metrics = searcher.search_folders(
                query=q,
                size=limit,
                category=category,
            )
        except Exception as e:
            logger.error(f"Suggest failed: {e}")
            raise HTTPException(status_code=503, detail=f"Suggestion service unavailable: {e}")

        total_latency = (time.time() - start_time) * 1000

        # Convert DataFrame to response items
        suggestions: List[SuggestResultItem] = []
        if not results_df.empty:
            for _, row in results_df.iterrows():
                suggestions.append(SuggestResultItem(
                    framework_name=str(row.get("framework_name", "")),
                    description=str(row.get("description", "")),
                    category=str(row.get("category", "")),
                    path=str(row.get("path", "")),
                    file_count=int(row.get("file_count", 0)),
                    source_url=str(row.get("source_url", "")),
                    score=float(row.get("final_score", 0.0)),
                ))

        return SuggestResponse(
            query=q,
            suggestions=suggestions,
            total_hits=metrics.total_hits,
            returned=len(suggestions),
            took_ms=metrics.took_ms,
            total_latency_ms=round(total_latency, 2),
        )

    return application


# =============================================================================
# Default Application Instance
# =============================================================================

app = create_app()
