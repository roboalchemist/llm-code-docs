# Source: https://docs.augmentcode.com/context-services/sdk/examples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Examples

> Example applications using the Auggie SDK

<Warning>
  **Experimental API** - Context Engine SDK is experimental and subject to breaking changes.
</Warning>

## Available Examples

<CardGroup cols={3}>
  <Card title="Direct Context" icon="code" href="#direct-context">
    API-based indexing and search
  </Card>

  <Card title="FileSystem Context" icon="folder" href="#filesystem-context">
    Local directory search
  </Card>

  <Card title="File Search Server" icon="server" href="#file-search-server">
    REST API for code search
  </Card>

  <Card title="Prompt Enhancer Server" icon="wand-magic-sparkles" href="#prompt-enhancer-server">
    Context-aware prompt enhancement
  </Card>

  <Card title="GitHub Action Indexer" icon="github" href="#github-action-indexer">
    CI/CD repository indexing
  </Card>
</CardGroup>

***

## Getting the Examples

All example code is available in the Auggie repository. To access the examples:

<CodeGroup>
  ```bash TypeScript theme={null}
  git clone https://github.com/augmentcode/auggie.git
  cd auggie/examples/typescript-sdk/context
  ```

  ```bash Python theme={null}
  git clone https://github.com/augmentcode/auggie.git
  cd auggie/examples/python-sdk/context
  ```
</CodeGroup>

Each example is a complete, runnable application demonstrating different use cases of the Auggie SDK.

## Prerequisites

Before running the examples:

1. **Runtime** - One of the following:
   * **TypeScript:** Node.js 18+
   * **Python:** Python 3.10+

2. **Auggie CLI** - Required for FileSystem Context examples
   ```bash  theme={null}
   npm install -g @augmentcode/auggie@latest
   ```

3. **Authentication** - Required for all examples

   ```bash  theme={null}
   auggie login
   ```

   This creates a session file at `~/.augment/session.json` with your API token.

   Alternatively, set environment variables:

   ```bash  theme={null}
   export AUGMENT_API_TOKEN="your-api-token"
   export AUGMENT_API_URL="https://your-tenant.api.augmentcode.com"
   ```

## Setup

Install dependencies:

<CodeGroup>
  ```bash TypeScript theme={null}
  cd examples/typescript-sdk/context
  npm install
  ```

  ```bash Python theme={null}
  cd examples/python-sdk/context
  pip install auggie-sdk
  ```
</CodeGroup>

***

## Simple Examples

Get started quickly with these basic examples that demonstrate core SDK functionality.

### Direct Context

Demonstrates indexing files from any source and performing semantic searches with AI-powered question answering.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run direct-context
  ```

  ```bash Python theme={null}
  python -m direct_context
  ```
</CodeGroup>

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx direct-context/index.ts
  ```

  ```bash Python theme={null}
  python direct_context/main.py
  ```
</CodeGroup>

***

### FileSystem Context

Shows how to search a local directory using automatic file discovery via the MCP protocol.

**Prerequisites:**

* Auggie CLI must be installed and in your PATH
* Authentication via `auggie login` or `AUGMENT_API_TOKEN` environment variable
* A `.gitignore` or `.augmentignore` file in the workspace directory to exclude `node_modules/` and other large directories

**Important:** The FileSystem Context indexes all files in the workspace directory. To avoid timeouts when indexing large directories (like `node_modules/`), make sure you have a `.gitignore` or `.augmentignore` file that excludes them.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run filesystem-context
  ```

  ```bash Python theme={null}
  python -m filesystem_context
  ```
</CodeGroup>

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx filesystem-context/index.ts
  ```

  ```bash Python theme={null}
  python filesystem_context/main.py
  ```
</CodeGroup>

***

## Developer Tools

Build production-ready applications with these server examples.

### File Search Server

A REST API server that provides semantic file search with AI-powered summarization.

**Prerequisites:** Auggie CLI must be installed and in your PATH.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run file-search-server [workspace-directory]
  ```

  ```bash Python theme={null}
  python -m file_search_server [workspace-directory]
  ```
</CodeGroup>

Then query the API:

```bash  theme={null}
curl "http://localhost:3000/search?q=typescript"
```

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx file-search-server/index.ts .
  ```

  ```bash Python theme={null}
  python file_search_server/main.py .
  ```
</CodeGroup>

***

### Prompt Enhancer Server

An HTTP server that automatically enriches user prompts with relevant codebase context.

**Prerequisites:** Auggie CLI must be installed and in your PATH.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run prompt-enhancer-server [workspace-directory]
  ```

  ```bash Python theme={null}
  python -m prompt_enhancer_server [workspace-directory]
  ```
</CodeGroup>

Then enhance prompts:

```bash  theme={null}
curl -X POST http://localhost:3001/enhance \
  -H "Content-Type: application/json" \
  -d '{"prompt": "fix the login bug"}'
```

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx prompt-enhancer-server/index.ts .
  ```

  ```bash Python theme={null}
  python prompt_enhancer_server/main.py .
  ```
</CodeGroup>

***

## CI/CD Integration

Integrate the SDK into your continuous integration workflows.

### GitHub Action Indexer

Automatically index your GitHub repositories with **zero-question setup** and incremental updates. Perfect for CI/CD workflows and keeping your codebase searchable.

**Key Features:**

* 🔄 **Incremental indexing** - Only processes changed files for efficiency
* 💾 **Smart caching** - Persists index state between runs
* 🚀 **30-second setup** - From zero to running GitHub Action

**Installation:**

<CodeGroup>
  ```bash TypeScript theme={null}
  # Install directly into your repository
  cd /path/to/your/repository
  npx @augment-samples/github-action-indexer install

  # Add your API secrets to GitHub repository settings
  # Push to trigger automatic indexing on every commit
  ```

  ```bash Python theme={null}
  # From the auggie repo, install into your target repository
  cd examples/python-sdk/context
  python -m github_action_indexer install /path/to/your/repository

  # Add your API secrets to GitHub repository settings
  # Push to trigger automatic indexing on every commit
  ```
</CodeGroup>

**What It Does:**

1. **Indexes** your codebase automatically on every push
2. **Updates** incrementally using GitHub's Compare API
3. **Caches** index state for fast subsequent runs
4. **Handles** large repositories with optimized performance settings

**Perfect For:**

* Keeping your codebase searchable and up-to-date
* CI/CD workflows that need codebase understanding
* Teams wanting automatic repository indexing
* Projects with frequent commits (incremental updates are fast)

**Try It Locally First:**

<CodeGroup>
  ```bash TypeScript theme={null}
  cd github-action-indexer
  npm install
  export AUGMENT_API_TOKEN="your-token"
  export AUGMENT_API_URL="https://your-tenant.api.augmentcode.com/"
  export GITHUB_TOKEN="your-github-token"
  export GITHUB_REPOSITORY="owner/repo"
  export GITHUB_SHA="$(git rev-parse HEAD)"
  npm run index
  npm run search "authentication functions"
  ```

  ```bash Python theme={null}
  cd examples/python-sdk/context
  pip install -r github_action_indexer/augment_indexer/requirements.txt
  export AUGMENT_API_TOKEN="your-token"
  export AUGMENT_API_URL="https://your-tenant.api.augmentcode.com/"
  export GITHUB_TOKEN="your-github-token"
  export GITHUB_REPOSITORY="owner/repo"
  export GITHUB_SHA="$(git rev-parse HEAD)"
  python -m github_action_indexer index
  python -m github_action_indexer search "authentication functions"
  ```
</CodeGroup>

📖 **Complete Setup Guides:**

* [TypeScript GitHub Action Indexer →](https://github.com/augmentcode/auggie/tree/main/examples/typescript-sdk/context/github-action-indexer)
* [Python GitHub Action Indexer →](https://github.com/augmentcode/auggie/tree/main/examples/python-sdk/context/github_action_indexer)

***

## Troubleshooting

### MCP Timeout in FileSystem Context

**Problem:** The FileSystem Context example times out during indexing.

**Cause:** The workspace directory contains too many files (e.g., `node_modules/` with 45,000+ files).

**Solution:** Create a `.gitignore` or `.augmentignore` file in the workspace directory to exclude large directories:

```bash  theme={null}
# .gitignore or .augmentignore
node_modules/
dist/
__pycache__/
.venv/
*.log
.DS_Store
```

The auggie CLI respects both `.gitignore` and `.augmentignore` patterns and will skip excluded files during indexing.

### Authentication Errors

**Problem:** `Error: API key is required for searchAndAsk()` or `ValueError: API credentials are required`

**Cause:** The SDK cannot find your authentication credentials.

**Solution:** Run `auggie login` to authenticate, or set the `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables.

***

## Next Steps

<CardGroup cols={2}>
  <Card title="API Reference" icon="code" href="/context-services/sdk/api-reference">
    Complete API documentation
  </Card>

  <Card title="Quick Start" icon="rocket" href="/context-services/sdk/overview">
    Back to quick start guide
  </Card>
</CardGroup>
