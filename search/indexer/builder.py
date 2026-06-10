"""Main indexing orchestrator for building and updating the search index."""

import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
from tqdm import tqdm

from search import config
from search.db.connection import get_connection
from search.db.schema import create_document_record, create_folder_record
from search.embeddings.generator import get_generator
from search.indexer.scanner import DocumentScanner, DocumentInfo, get_scanner
from search.indexer.extractor import MetadataExtractor
from search.indexer.chunker import get_chunker
from search.utils.yaml_parser import get_parser
from search.utils.hashing import hash_file, hash_string
from search.utils.checkpoint import IndexCheckpoint
from search.utils.server_manager import get_server_manager
import logging

logger = logging.getLogger(__name__)


class IndexBuilder:
    """Orchestrates the indexing process for documents and folders."""

    def __init__(self):
        """Initialize index builder with required components."""
        self.db = get_connection()
        self.scanner = get_scanner()
        self.extractor = MetadataExtractor()
        self.chunker = get_chunker()
        self.generator = get_generator()
        self.yaml_parser = get_parser()
        self.checkpoint = IndexCheckpoint(config.LANCEDB_DIR)
        self.server_manager = get_server_manager()

    def full_rebuild(self):
        """
        Perform a full rebuild of the search index.

        Drops existing tables and reindexes all documents and folders.
        Supports resume from checkpoint if interrupted.
        """
        # Ensure server is running
        print("Ensuring embedding server is running...")
        if not self.server_manager.ensure_server_running():
            raise RuntimeError("Failed to start embedding server")

        # Check for existing checkpoint
        if self.checkpoint.exists():
            self.checkpoint.print_status()
            response = input("Resume from checkpoint? [Y/n]: ").strip().lower()
            if response in ['n', 'no']:
                print("Clearing checkpoint and starting fresh...")
                self.checkpoint.clear()
                self.db.drop_tables()
        else:
            print("Starting full index rebuild...")
            # Drop existing tables only if no checkpoint
            print("Dropping existing tables...")
            self.db.drop_tables()

        # Index all documents with checkpoint support
        self._index_all_documents_with_checkpoint()

        # Index all folders
        self._index_all_folders()

        # Create search indices
        self._create_indices()

        # Clear checkpoint on success
        self.checkpoint.clear()

        print("\nFull rebuild complete!")
        stats = self.db.get_stats()
        print(f"Documents indexed: {stats.get('documents_count', 0)}")
        print(f"Folders indexed: {stats.get('folders_count', 0)}")

    def incremental_update(self):
        """
        Perform incremental update of the search index.

        Only processes new, modified, or deleted files since last index.
        """
        print("Starting incremental update...")

        # Get current files and their hashes
        print("Scanning files...")
        documents = self.scanner.scan()
        current_files = {}

        for doc in tqdm(documents, desc="Computing hashes"):
            try:
                file_hash = hash_file(doc.path)
                current_files[str(doc.path)] = {
                    'hash': file_hash,
                    'doc': doc
                }
            except Exception as e:
                print(f"Warning: Could not hash {doc.path}: {e}")

        # Get existing hashes from database
        existing_hashes = self._get_existing_hashes()

        # Detect changes
        current_paths = set(current_files.keys())
        existing_paths = set(existing_hashes.keys())

        new_files = current_paths - existing_paths
        deleted_files = existing_paths - current_paths
        modified_files = {
            p for p in current_paths & existing_paths
            if current_files[p]['hash'] != existing_hashes[p]
        }

        print(f"\nChanges detected:")
        print(f"  New files: {len(new_files)}")
        print(f"  Modified files: {len(modified_files)}")
        print(f"  Deleted files: {len(deleted_files)}")

        # Process changes
        if deleted_files:
            self._delete_documents(deleted_files)

        if new_files or modified_files:
            files_to_index = new_files | modified_files
            docs_to_index = [current_files[p]['doc'] for p in files_to_index]
            self._index_documents(docs_to_index, is_update=True)

        # Rebuild folder index if any changes
        if new_files or modified_files or deleted_files:
            print("\nUpdating folder index...")
            self._rebuild_folders()

        print("\nIncremental update complete!")
        stats = self.db.get_stats()
        print(f"Documents indexed: {stats.get('documents_count', 0)}")
        print(f"Folders indexed: {stats.get('folders_count', 0)}")

    def index_framework(self, framework_name: str):
        """
        Index a single framework.

        Args:
            framework_name: Name of the framework to index.
        """
        print(f"Indexing framework: {framework_name}")

        documents = self.scanner.scan_framework(framework_name)
        if not documents:
            print(f"No documents found for framework: {framework_name}")
            return

        self._index_documents(documents, is_update=False)
        print(f"Indexed {len(documents)} documents for {framework_name}")

    def _index_all_documents(self):
        """Index all documents in the docs directory."""
        print("\nScanning documents...")
        documents = self.scanner.scan()
        print(f"Found {len(documents)} documents")

        self._index_documents(documents, is_update=False)

    def _index_all_documents_with_checkpoint(self):
        """Index all documents with checkpoint support for resume."""
        print("\nScanning documents...")
        documents = self.scanner.scan()
        total_docs = len(documents)
        print(f"Found {total_docs} documents")

        # Load checkpoint
        processed_paths = self.checkpoint.get_processed_paths()

        # Filter to unprocessed documents
        remaining_docs = [d for d in documents if str(d.path) not in processed_paths]

        if processed_paths:
            print(f"Resuming: {len(processed_paths)} already processed, {len(remaining_docs)} remaining")

        if not remaining_docs:
            print("All documents already processed!")
            return

        # Process in batches for incremental checkpointing
        batch_size = 500  # Checkpoint every 500 documents
        total_chunks = 0

        for batch_start in range(0, len(remaining_docs), batch_size):
            batch_end = min(batch_start + batch_size, len(remaining_docs))
            batch_docs = remaining_docs[batch_start:batch_end]

            print(f"\nProcessing batch {batch_start//batch_size + 1} ({len(batch_docs)} documents)...")

            # Index this batch
            batch_chunks = self._index_documents_batch(batch_docs)
            total_chunks += batch_chunks

            # Update checkpoint
            for doc in batch_docs:
                processed_paths.add(str(doc.path))

            self.checkpoint.save(
                processed_paths=processed_paths,
                total_documents=len(processed_paths),
                total_chunks=total_chunks,
            )

            print(f"Checkpoint saved: {len(processed_paths)}/{total_docs} documents, {total_chunks} chunks")

    def _index_documents(self, documents: List[DocumentInfo], is_update: bool = False):
        """
        Index a list of documents.

        Args:
            documents: List of DocumentInfo objects to index.
            is_update: Whether this is an incremental update.
        """
        if not documents:
            return

        # Prepare records
        records = []
        texts_to_embed = []
        record_indices = []

        print("\nExtracting metadata and chunking...")
        for doc in tqdm(documents, desc="Processing documents"):
            try:
                doc_records, doc_texts = self._prepare_document_records(doc)
                for i, (record, text) in enumerate(zip(doc_records, doc_texts)):
                    records.append(record)
                    texts_to_embed.append(text)
                    record_indices.append(len(records) - 1)
            except Exception as e:
                print(f"Error processing {doc.path}: {e}")
                continue

        if not records:
            print("No records to index")
            return

        # Generate embeddings
        print(f"\nGenerating embeddings for {len(texts_to_embed)} chunks...")
        embeddings = self.generator.generate(texts_to_embed)

        # Add embeddings to records
        for idx, embedding in enumerate(embeddings):
            records[idx]['embedding'] = embedding

        # Insert into database
        print("\nInserting into database...")
        if is_update:
            # For updates, delete existing records first by path
            paths_to_update = {r['path'] for r in records}
            self._delete_documents(paths_to_update)

        # Insert in batches
        batch_size = 1000
        for i in tqdm(range(0, len(records), batch_size), desc="Inserting batches"):
            batch = records[i:i + batch_size]
            self.db.documents_table.add(batch)

    def _index_documents_batch(self, documents: List[DocumentInfo]) -> int:
        """
        Index a batch of documents and return chunk count.

        Returns:
            Number of chunks indexed.
        """
        if not documents:
            return 0

        # Prepare records
        records = []
        texts_to_embed = []

        for doc in tqdm(documents, desc="Processing documents", leave=False):
            try:
                doc_records, doc_texts = self._prepare_document_records(doc)
                for record, text in zip(doc_records, doc_texts):
                    records.append(record)
                    texts_to_embed.append(text)
            except Exception as e:
                logger.error(f"Error processing {doc.path}: {e}")
                continue

        if not records:
            return 0

        # Generate embeddings
        embeddings = self.generator.generate(texts_to_embed, show_progress=False)

        # Add embeddings to records
        for idx, embedding in enumerate(embeddings):
            records[idx]['embedding'] = embedding

        # Insert into database immediately (incremental save)
        batch_size = 1000
        for i in range(0, len(records), batch_size):
            batch = records[i:i + batch_size]
            self.db.documents_table.add(batch)

        return len(records)

    def _prepare_document_records(
        self, doc_info: DocumentInfo
    ) -> tuple[List[Dict[str, Any]], List[str]]:
        """
        Prepare document records from a DocumentInfo.

        Args:
            doc_info: DocumentInfo object.

        Returns:
            Tuple of (records list, texts for embedding list).
        """
        # Extract metadata
        metadata = self.extractor.extract_metadata(doc_info.path)
        content = metadata['content']
        content_hash = hash_string(content)

        # Get source URL from index.yaml
        source_info = self.yaml_parser.get_source_by_name(doc_info.framework)
        source_url = source_info.get('url', '') if source_info else ''

        # Chunk content
        chunks = self.chunker.chunk(content)
        chunk_count = len(chunks)

        records = []
        texts = []

        now = datetime.utcnow()
        last_modified = datetime.fromtimestamp(doc_info.path.stat().st_mtime)

        for chunk_id, chunk_content in enumerate(chunks):
            doc_id = str(uuid.uuid4())

            record = create_document_record(
                doc_id=doc_id,
                path=str(doc_info.path),
                relative_path=doc_info.relative_path,
                filename=doc_info.filename,
                content=chunk_content,
                content_hash=content_hash,
                embedding=[],  # Placeholder, will be filled later
                chunk_id=chunk_id,
                chunk_count=chunk_count,
                category=doc_info.category,
                framework=doc_info.framework,
                source_url=source_url,
                file_size=metadata['file_size'],
                line_count=metadata['line_count'],
                last_modified=last_modified,
                indexed_at=now,
                title=metadata['title'],
                headings=metadata['headings'],
                keywords=metadata['keywords'],
            )

            records.append(record)

            # Text for embedding: title + headings + content
            embed_text = f"{metadata['title']}\n{' '.join(metadata['headings'])}\n{chunk_content}"
            texts.append(embed_text[:8000])  # Limit text length

        return records, texts

    def _index_all_folders(self):
        """Index all folders from index.yaml."""
        print("\nIndexing folders...")

        sources = self.yaml_parser.get_all_sources()
        if not sources:
            print("No sources found in index.yaml")
            return

        records = []
        texts_to_embed = []

        for source in tqdm(sources, desc="Processing folders"):
            try:
                record, text = self._prepare_folder_record(source)
                if record:
                    records.append(record)
                    texts_to_embed.append(text)
            except Exception as e:
                print(f"Error processing folder {source.get('name', 'unknown')}: {e}")

        if not records:
            print("No folder records to index")
            return

        # Generate embeddings
        print(f"\nGenerating folder embeddings for {len(texts_to_embed)} folders...")
        embeddings = self.generator.generate(texts_to_embed)

        # Add embeddings to records
        for idx, embedding in enumerate(embeddings):
            records[idx]['embedding'] = embedding

        # Insert into database
        print("\nInserting folders into database...")
        self.db.folders_table.add(records)

    def _prepare_folder_record(
        self, source: Dict[str, Any]
    ) -> tuple[Optional[Dict[str, Any]], str]:
        """
        Prepare a folder record from index.yaml source entry.

        Args:
            source: Source dictionary from index.yaml.

        Returns:
            Tuple of (record dict, text for embedding) or (None, '') if invalid.
        """
        name = source.get('name', '')
        if not name:
            return None, ''

        category = source.get('_category', '')
        folder_path = config.DOCS_ROOT / category / name

        if not folder_path.exists():
            return None, ''

        # Collect metadata from all documents in folder
        all_titles = []
        all_headings = []
        readme_content = ''

        for md_file in folder_path.rglob("*.md"):
            try:
                metadata = self.extractor.extract_metadata(md_file)
                if metadata['title']:
                    all_titles.append(metadata['title'])
                all_headings.extend(metadata['headings'])

                # Check for README
                if md_file.name.lower() in ['readme.md', 'index.md']:
                    readme_content = metadata['content'][:5000]  # Limit size
            except Exception:
                continue

        # Parse dates
        last_updated = self.yaml_parser.parse_last_updated(
            source.get('last_updated', '')
        )
        if not last_updated:
            last_updated = datetime.utcnow()

        folder_id = str(uuid.uuid4())

        record = create_folder_record(
            folder_id=folder_id,
            framework_name=name,
            description=source.get('description', ''),
            path=str(folder_path),
            relative_path=f"{category}/{name}",
            category=category,
            embedding=[],  # Placeholder
            source_url=source.get('url', ''),
            file_count=source.get('file_count', 0),
            size=source.get('size', ''),
            last_updated=last_updated,
            status=source.get('status', 'fetched'),
            all_titles='\n'.join(all_titles[:100]),  # Limit
            all_headings='\n'.join(all_headings[:200]),  # Limit
            readme_content=readme_content,
            topics=source.get('topics', []) if isinstance(source.get('topics'), list) else [],
        )

        # Text for embedding
        embed_text = f"{name}\n{source.get('description', '')}\n{' '.join(all_titles)}\n{' '.join(all_headings[:50])}\n{readme_content[:2000]}"

        return record, embed_text

    def _rebuild_folders(self):
        """Rebuild the folders table."""
        # Drop and recreate folders table
        if self.db.table_exists("folders"):
            self.db.db.drop_table("folders")
            self.db._folders_table = None

        self._index_all_folders()

    def _get_existing_hashes(self) -> Dict[str, str]:
        """
        Get content hashes for all indexed documents.

        Returns:
            Dictionary mapping file paths to their content hashes.
        """
        if not self.db.table_exists("documents"):
            return {}

        try:
            # Query unique path and content_hash pairs
            df = self.db.documents_table.to_pandas()
            # Group by path and take first hash (all chunks have same hash)
            path_hashes = df.groupby('path')['content_hash'].first().to_dict()
            return path_hashes
        except Exception as e:
            print(f"Warning: Could not get existing hashes: {e}")
            return {}

    def _delete_documents(self, paths: Set[str]):
        """
        Delete documents by path.

        Args:
            paths: Set of file paths to delete.
        """
        if not paths:
            return

        try:
            for path in tqdm(paths, desc="Deleting old records"):
                self.db.documents_table.delete(f'path = "{path}"')
        except Exception as e:
            print(f"Warning: Error deleting documents: {e}")

    def _create_indices(self):
        """Create vector search indices on tables."""
        print("\nCreating search indices...")

        try:
            # Index documents table with IVF_PQ
            doc_count = self.db.documents_table.count_rows()
            if doc_count > 1000:
                print("Creating IVF_PQ index for documents table...")
                self.db.documents_table.create_index(
                    metric=config.DOCUMENTS_INDEX_CONFIG["metric"],
                    num_partitions=min(
                        config.DOCUMENTS_INDEX_CONFIG["num_partitions"],
                        doc_count // 10  # Ensure enough data per partition
                    ),
                    num_sub_vectors=config.DOCUMENTS_INDEX_CONFIG["num_sub_vectors"],
                )
            else:
                print("Documents table too small for IVF_PQ, using FLAT index")

            # Folders table uses FLAT by default (small table)
            print("Folders table using FLAT index (small dataset)")

        except Exception as e:
            print(f"Warning: Could not create indices: {e}")


# Global builder instance
_builder = None


def get_builder() -> IndexBuilder:
    """Get global index builder instance."""
    global _builder
    if _builder is None:
        _builder = IndexBuilder()
    return _builder
