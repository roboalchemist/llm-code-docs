# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/capabilities/context.md

# /context

This tool performs **semantic search** across codebase(s) to find relevant code snippets.

**Key Features:**

* **Semantic Search**: Uses vector embeddings to find conceptually similar code, not just keyword matches.
* **Multi-Repository Support**: Search across multiple repositories simultaneously.
* **Language Filtering**: Filter results by programming language (Python, JavaScript, TypeScript, etc.).
* **Intelligent Ranking**: Returns results ranked by relevance with configurable result limits.

***

**Example Usage:**

```json
{
  "tool": "get_context",
  "parameters": {
    "query": "authentication middleware implementation",
    "repositories": ["backend/api", "frontend/app"],  // Target specific repos
    "language": ["python", "typescript"],              // Filter by language
    "max_results": 10                                  // Limit number of results
  }
}
```
