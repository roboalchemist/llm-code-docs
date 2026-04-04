# Source: https://docs.augmentcode.com/context-services/context-connectors/how-it-works.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How It Works

> Architecture and data flow of Context Connectors

Context Connectors is a pipeline that indexes your code and content for semantic search. Here's how the pieces fit together.

## Architecture

Content flows through five components:

<Steps>
  <Step title="Source" icon="folder">
    Connect to your content: GitHub, GitLab, BitBucket, or website
  </Step>

  <Step title="Indexer" icon="gear">
    Discover files, filter, chunk, and send to Context Engine for embedding
  </Step>

  <Step title="Store" icon="database">
    Persist index state (local filesystem or S3) for incremental updates
  </Step>

  <Step title="Context Engine" icon="magnifying-glass">
    Augment's semantic search backend stores embeddings and handles queries
  </Step>

  <Step title="Client" icon="terminal">
    Query via CLI, MCP server, or your own application
  </Step>
</Steps>

## Data Flow

### Indexing

When you run `ctxc index`, here's what happens:

1. **Discover** - Source connector lists all files (respects `.gitignore`)
2. **Filter** - Skip binary files, large files, excluded patterns
3. **Hash** - Compute file hashes to detect changes
4. **Diff** - Compare with stored state to find new/modified/deleted files
5. **Index** - Send changed files to Context Engine for embedding
6. **Save** - Store new state for next incremental run

### Searching

When you run `ctxc search` or query via MCP:

1. **Query** - User submits natural language query
2. **Embed** - Context Engine converts query to vector
3. **Match** - Find semantically similar code chunks
4. **Return** - Results with file paths, line numbers, and snippets

### File Reading (MCP/Agent)

When an agent needs full file content (not just search snippets):

1. **Request** - Agent requests file by path
2. **Fetch** - MCP server reads from original source (filesystem or Git API)
3. **Return** - Full file content returned to agent

This is why MCP servers need source credentials (e.g., `GITHUB_TOKEN`) - they read files on demand from the original source, not from the index.

## Incremental Updates

Context Connectors tracks file state to avoid re-indexing unchanged files:

| Scenario       | What Happens           |
| -------------- | ---------------------- |
| File unchanged | Skipped (hash matches) |
| File modified  | Re-indexed             |
| File deleted   | Removed from index     |
| New file       | Added to index         |

State is stored in your chosen store:

* **Local filesystem** - Platform-specific directory (e.g., `~/.local/share/context-connectors` on Linux)
* **S3** - `s3://bucket/index-name/` prefix

This makes subsequent runs fast - only changed files are processed.
