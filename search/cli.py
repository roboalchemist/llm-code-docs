"""Click CLI interface for LLM Code Docs Search Engine."""

import click
import json

from search import config


@click.group()
@click.version_option(version="0.2.0", prog_name="llm-code-docs-search")
def cli():
    """LLM Code Docs Search Engine - Semantic search over documentation."""
    pass


@cli.command()
@click.argument('query')
@click.option(
    '--limit', '-l',
    default=config.DEFAULT_SEARCH_LIMIT,
    help='Maximum number of documents to return.'
)
@click.option(
    '--folder-limit', '-f',
    default=config.DEFAULT_FOLDER_LIMIT,
    help='Maximum number of frameworks to return.'
)
@click.option(
    '--category', '-c',
    type=click.Choice(['llms-txt', 'github-scraped', 'web-scraped']),
    help='Filter by category.'
)
@click.option(
    '--framework', '-w',
    help='Filter by specific framework.'
)
@click.option(
    '--docs-only', '-d',
    is_flag=True,
    help='Search documents only (skip frameworks).'
)
@click.option(
    '--folders-only', '-F',
    is_flag=True,
    help='Search frameworks only (skip documents).'
)
@click.option(
    '--no-rerank', '-n',
    is_flag=True,
    help='Disable hybrid reranking.'
)
@click.option(
    '--no-preview', '-P',
    is_flag=True,
    help='Hide content preview.'
)
@click.option(
    '--no-scores', '-S',
    is_flag=True,
    help='Hide relevance scores.'
)
@click.option(
    '--backend', '-b',
    type=click.Choice(['opensearch', 'lancedb']),
    default='opensearch',
    help='Search backend to use (default: opensearch).'
)
@click.option(
    '--explain', '-e',
    is_flag=True,
    help='Show scoring breakdown for each result.'
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Show verbose output including SPLADE term expansion.'
)
def search(
    query: str,
    limit: int,
    folder_limit: int,
    category: str,
    framework: str,
    docs_only: bool,
    folders_only: bool,
    no_rerank: bool,
    no_preview: bool,
    no_scores: bool,
    backend: str,
    explain: bool,
    verbose: bool,
):
    """Search documentation for QUERY."""
    if backend == 'opensearch':
        _search_opensearch(
            query=query,
            limit=limit,
            folder_limit=folder_limit,
            category=category,
            framework=framework,
            docs_only=docs_only,
            folders_only=folders_only,
            no_rerank=no_rerank,
            no_preview=no_preview,
            no_scores=no_scores,
            explain=explain,
            verbose=verbose,
        )
    else:
        _search_lancedb(
            query=query,
            limit=limit,
            folder_limit=folder_limit,
            category=category,
            framework=framework,
            docs_only=docs_only,
            folders_only=folders_only,
            no_rerank=no_rerank,
            no_preview=no_preview,
            no_scores=no_scores,
        )


def _search_opensearch(
    query: str,
    limit: int,
    folder_limit: int,
    category: str,
    framework: str,
    docs_only: bool,
    folders_only: bool,
    no_rerank: bool,
    no_preview: bool,
    no_scores: bool,
    explain: bool,
    verbose: bool,
):
    """Execute search using the OpenSearch backend with hybrid BM25+SPLADE+dense retrieval."""
    import pandas as pd
    from search.opensearch.searcher import get_searcher, HybridSearchConfig, SearchMetrics
    from search.searcher.results import SearchResults
    from search.searcher.formatter import get_formatter

    searcher = get_searcher()
    formatter = get_formatter()

    # Update formatter settings
    formatter.show_content_preview = not no_preview
    formatter.show_scores = not no_scores

    doc_results = pd.DataFrame()
    folder_results = pd.DataFrame()
    doc_metrics = None
    folder_metrics = None

    # Search documents
    if not folders_only:
        doc_results, doc_metrics = searcher.search(
            query=query,
            size=limit,
            category=category,
            framework=framework,
        )

    # Search folders/frameworks
    if not docs_only:
        folder_results, folder_metrics = searcher.search_folders(
            query=query,
            size=folder_limit,
            category=category,
        )

    # Wrap in SearchResults for formatter compatibility
    results = SearchResults(
        documents=doc_results,
        folders=folder_results,
        query=query,
        total_documents=len(doc_results),
        total_folders=len(folder_results),
    )

    # Format and display results
    output = formatter.format_results(results)
    click.echo(output)

    # Show verbose SPLADE information
    if verbose and doc_metrics:
        click.echo("")
        click.echo("=== Search Metrics ===")
        click.echo(f"  Backend: OpenSearch (hybrid)")
        click.echo(f"  BM25: {'enabled' if doc_metrics.bm25_enabled else 'disabled'}")
        click.echo(f"  SPLADE: {'enabled' if doc_metrics.splade_enabled else 'disabled'}")
        click.echo(f"  Dense vectors: {'enabled' if doc_metrics.dense_enabled else 'disabled'}")
        click.echo(f"  OpenSearch took: {doc_metrics.took_ms}ms")
        click.echo(f"  Total latency: {doc_metrics.total_latency_ms:.1f}ms")
        click.echo(f"  Total hits: {doc_metrics.total_hits}")
        click.echo(f"  Returned: {doc_metrics.returned_hits}")

        # Show SPLADE term info from the searcher config
        config_obj = searcher.config
        click.echo(f"  Weights: BM25={config_obj.bm25_weight:.1f}, "
                    f"SPLADE={config_obj.splade_weight:.1f}, "
                    f"Dense={config_obj.dense_weight:.1f}")

    # Show explain scoring breakdown
    if explain:
        _show_explain_output(doc_results, folder_results, doc_metrics, folder_metrics, searcher)


def _show_explain_output(doc_results, folder_results, doc_metrics, folder_metrics, searcher):
    """Display scoring breakdown for search results."""
    click.echo("")
    click.echo("=== Scoring Breakdown ===")

    config_obj = searcher.config
    click.echo(f"  Search pipeline: hybrid_search_pipeline")
    click.echo(f"  Normalization: min_max + arithmetic_mean")
    click.echo(f"  Component weights: BM25={config_obj.bm25_weight:.2f}, "
               f"SPLADE={config_obj.splade_weight:.2f}, "
               f"Dense={config_obj.dense_weight:.2f}")
    click.echo("")

    if not doc_results.empty:
        click.echo("  --- Document Scores ---")
        for idx, (_, row) in enumerate(doc_results.iterrows(), 1):
            title = row.get('title', 'Untitled')
            fw = row.get('framework', 'unknown')
            raw_score = row.get('_raw_score', 0.0)
            norm_score = row.get('similarity_score', 0.0)
            final_score = row.get('final_score', norm_score)

            click.echo(f"  {idx}. [{fw}] {title}")
            click.echo(f"     Raw score: {raw_score:.4f}")
            click.echo(f"     Normalized: {norm_score:.4f}")
            click.echo(f"     Final: {final_score:.4f}")

            # Show highlight if available
            highlight = row.get('highlighted_content', '')
            if highlight:
                click.echo(f"     Highlight: {highlight[:120]}...")
            click.echo("")

    if not folder_results.empty:
        click.echo("  --- Framework Scores ---")
        for idx, (_, row) in enumerate(folder_results.iterrows(), 1):
            name = row.get('framework_name', 'unknown')
            raw_score = row.get('_raw_score', 0.0)
            norm_score = row.get('similarity_score', 0.0)

            click.echo(f"  {idx}. {name}")
            click.echo(f"     Raw score: {raw_score:.4f}")
            click.echo(f"     Normalized: {norm_score:.4f}")
            click.echo("")


def _search_lancedb(
    query: str,
    limit: int,
    folder_limit: int,
    category: str,
    framework: str,
    docs_only: bool,
    folders_only: bool,
    no_rerank: bool,
    no_preview: bool,
    no_scores: bool,
):
    """Execute search using the LanceDB backend (original implementation)."""
    from search.searcher.query import get_processor
    from search.searcher.ranker import get_ranker
    from search.searcher.formatter import get_formatter

    processor = get_processor()
    ranker = get_ranker()
    formatter = get_formatter()

    # Update formatter settings
    formatter.show_content_preview = not no_preview
    formatter.show_scores = not no_scores

    # Perform search
    results = processor.search(
        query=query,
        doc_limit=limit if not folders_only else 0,
        folder_limit=folder_limit if not docs_only else 0,
        category=category,
        framework=framework,
    )

    # Apply hybrid reranking if enabled
    if not no_rerank:
        if not results.documents.empty:
            results.documents = ranker.rerank_documents(results.documents, query)
        if not results.folders.empty:
            results.folders = ranker.rerank_folders(results.folders, query)

    # Format and display results
    output = formatter.format_results(results)
    click.echo(output)


@cli.command()
@click.option(
    '--rebuild', '-r',
    is_flag=True,
    help='Full rebuild of the index (drops existing data).'
)
@click.option(
    '--update', '-u',
    is_flag=True,
    help='Incremental update (only process changes).'
)
@click.option(
    '--framework', '-f',
    help='Index only a specific framework.'
)
@click.option(
    '--folders',
    is_flag=True,
    help='Build the folders index from index.yaml (for suggestions).'
)
def index(rebuild: bool, update: bool, framework: str, folders: bool):
    """Build or update the search index (OpenSearch backend)."""
    if not rebuild and not update and not framework and not folders:
        click.echo("Please specify --rebuild, --update, --framework, or --folders")
        click.echo("Use 'search.py index --help' for more information.")
        return

    # Use OpenSearch builder
    from search.opensearch.builder import get_builder
    builder = get_builder()

    if folders:
        click.echo("Building folders index...")
        stats = builder.build_folders_index()
        click.echo(f"✓ Folders indexed: {stats.get('folders', 0)}")
        if stats.get('errors'):
            click.echo(f"⚠ Errors: {len(stats['errors'])}")
    elif framework:
        click.echo(f"Indexing framework: {framework}")
        stats = builder.index_framework(framework)
        click.echo(f"✓ Indexed {stats.get('documents', 0)} documents, {stats.get('chunks', 0)} chunks")
    elif rebuild:
        if not click.confirm(
            "This will drop all existing data. Continue?",
            default=False
        ):
            click.echo("Aborted.")
            return
        stats = builder.full_rebuild()
        click.echo(f"✓ Full rebuild complete!")
    elif update:
        stats = builder.incremental_update()
        click.echo(f"✓ Incremental update complete!")


@cli.command()
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Show detailed statistics.'
)
def stats(verbose: bool):
    """Show index statistics."""
    # Lazy imports
    from search.db.connection import get_connection
    from search.searcher.formatter import get_formatter

    db = get_connection()
    formatter = get_formatter()

    stats_data = db.get_stats()
    output = formatter.format_stats(stats_data)
    click.echo(output)

    if verbose and stats_data.get('documents_count', 0) > 0:
        click.echo("")
        click.echo("=== Category Breakdown ===")

        try:
            df = db.documents_table.to_pandas()

            # Documents by category
            cat_counts = df.groupby('category')['path'].nunique()
            for cat, count in cat_counts.items():
                click.echo(f"  {cat}: {count:,} documents")

            click.echo("")
            click.echo("=== Top Frameworks ===")

            # Top frameworks by document count
            fw_counts = df.groupby('framework')['path'].nunique().sort_values(ascending=False)
            for fw, count in fw_counts.head(10).items():
                click.echo(f"  {fw}: {count:,} documents")

        except Exception as e:
            click.echo(f"Error getting detailed stats: {e}")


@cli.command()
@click.argument('path')
def show(path: str):
    """Show details for a document by path."""
    # Lazy imports
    from search.searcher.query import get_processor
    from search.searcher.formatter import get_formatter

    processor = get_processor()
    formatter = get_formatter()

    document = processor.get_document_by_path(path)
    if document is None:
        click.echo(f"Document not found: {path}")
        return

    output = formatter.format_document_detail(document)
    click.echo(output)


@cli.command()
@click.argument('name')
def framework(name: str):
    """Show details for a framework by name."""
    # Lazy imports
    from search.searcher.query import get_processor
    from search.searcher.formatter import get_formatter

    processor = get_processor()
    formatter = get_formatter()

    folder = processor.get_folder_by_name(name)
    if folder is None:
        click.echo(f"Framework not found: {name}")
        return

    output = formatter.format_folder_detail(folder)
    click.echo(output)


@cli.command()
def list_frameworks():
    """List all indexed frameworks."""
    # Lazy import
    from search.db.connection import get_connection

    db = get_connection()

    if not db.table_exists("folders"):
        click.echo("No frameworks indexed yet. Run 'search.py index --rebuild' first.")
        return

    try:
        df = db.folders_table.to_pandas()
        df = df.sort_values('framework_name')

        click.echo(f"=== Indexed Frameworks ({len(df)}) ===")
        click.echo("")

        for _, row in df.iterrows():
            name = row.get('framework_name', 'unknown')
            category = row.get('category', 'unknown')
            file_count = row.get('file_count', 0)
            click.echo(f"  {name:<30} [{category}] ({file_count} files)")

    except Exception as e:
        click.echo(f"Error listing frameworks: {e}")


def main():
    """Entry point for CLI."""
    cli()


if __name__ == "__main__":
    main()
