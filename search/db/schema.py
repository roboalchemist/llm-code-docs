"""LanceDB table schemas for documents and folders."""

import pyarrow as pa
from datetime import datetime
from typing import List, Dict, Any
from search import config


def get_documents_schema() -> pa.Schema:
    """
    Schema for the documents table.

    Stores individual markdown documents with embeddings and metadata.
    Each document may be chunked into multiple rows if it's large.
    """
    return pa.schema([
        # Primary identifiers
        pa.field("doc_id", pa.string()),
        pa.field("path", pa.string()),
        pa.field("relative_path", pa.string()),
        pa.field("filename", pa.string()),

        # Content
        pa.field("content", pa.string()),
        pa.field("content_hash", pa.string()),
        pa.field("embedding", pa.list_(pa.float32(), config.EMBEDDING_DIMENSION)),

        # Chunking metadata
        pa.field("chunk_id", pa.int32()),
        pa.field("chunk_count", pa.int32()),

        # Categorization
        pa.field("category", pa.string()),       # llms-txt | github-scraped | web-scraped
        pa.field("framework", pa.string()),      # e.g., "gitea", "fastapi"
        pa.field("source_url", pa.string()),     # From index.yaml

        # File metadata
        pa.field("file_size", pa.int64()),
        pa.field("line_count", pa.int32()),
        pa.field("last_modified", pa.timestamp('us')),
        pa.field("indexed_at", pa.timestamp('us')),

        # Search optimization
        pa.field("title", pa.string()),
        pa.field("headings", pa.list_(pa.string())),
        pa.field("keywords", pa.list_(pa.string())),
    ])


def get_folders_schema() -> pa.Schema:
    """
    Schema for the folders table.

    Stores framework/tool-level metadata with aggregated embeddings.
    Each folder represents a complete documentation set (e.g., gitea, fastapi).
    """
    return pa.schema([
        # Primary identifiers
        pa.field("folder_id", pa.string()),
        pa.field("framework_name", pa.string()),
        pa.field("description", pa.string()),
        pa.field("path", pa.string()),
        pa.field("relative_path", pa.string()),
        pa.field("category", pa.string()),

        # Embedding
        pa.field("embedding", pa.list_(pa.float32(), config.EMBEDDING_DIMENSION)),

        # Metadata from index.yaml
        pa.field("source_url", pa.string()),
        pa.field("file_count", pa.int32()),
        pa.field("size", pa.string()),
        pa.field("last_updated", pa.timestamp('us')),
        pa.field("status", pa.string()),  # fetched | pending

        # Aggregated content for search
        pa.field("all_titles", pa.string()),
        pa.field("all_headings", pa.string()),
        pa.field("readme_content", pa.string()),
        pa.field("topics", pa.list_(pa.string())),
    ])


def create_document_record(
    doc_id: str,
    path: str,
    relative_path: str,
    filename: str,
    content: str,
    content_hash: str,
    embedding: List[float],
    chunk_id: int,
    chunk_count: int,
    category: str,
    framework: str,
    source_url: str,
    file_size: int,
    line_count: int,
    last_modified: datetime,
    indexed_at: datetime,
    title: str,
    headings: List[str],
    keywords: List[str],
) -> Dict[str, Any]:
    """
    Create a document record dictionary matching the schema.

    Args:
        All parameters match the documents schema fields.

    Returns:
        Dictionary ready for insertion into documents table.
    """
    return {
        "doc_id": doc_id,
        "path": path,
        "relative_path": relative_path,
        "filename": filename,
        "content": content,
        "content_hash": content_hash,
        "embedding": embedding,
        "chunk_id": chunk_id,
        "chunk_count": chunk_count,
        "category": category,
        "framework": framework,
        "source_url": source_url,
        "file_size": file_size,
        "line_count": line_count,
        "last_modified": last_modified,
        "indexed_at": indexed_at,
        "title": title,
        "headings": headings,
        "keywords": keywords,
    }


def create_folder_record(
    folder_id: str,
    framework_name: str,
    description: str,
    path: str,
    relative_path: str,
    category: str,
    embedding: List[float],
    source_url: str,
    file_count: int,
    size: str,
    last_updated: datetime,
    status: str,
    all_titles: str,
    all_headings: str,
    readme_content: str,
    topics: List[str],
) -> Dict[str, Any]:
    """
    Create a folder record dictionary matching the schema.

    Args:
        All parameters match the folders schema fields.

    Returns:
        Dictionary ready for insertion into folders table.
    """
    return {
        "folder_id": folder_id,
        "framework_name": framework_name,
        "description": description,
        "path": path,
        "relative_path": relative_path,
        "category": category,
        "embedding": embedding,
        "source_url": source_url,
        "file_count": file_count,
        "size": size,
        "last_updated": last_updated,
        "status": status,
        "all_titles": all_titles,
        "all_headings": all_headings,
        "readme_content": readme_content,
        "topics": topics,
    }
