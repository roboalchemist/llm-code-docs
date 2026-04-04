# Source: https://docs.augmentcode.com/context-services/context-connectors/cli-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI Reference

> Complete command-line reference for Context Connectors

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Global Requirements

All commands require these environment variables:

```bash  theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

## Data Storage

By default, indexes are stored at `~/.augment/context-connectors`.

Override with `--store-path` or the `CONTEXT_CONNECTORS_STORE_PATH` environment variable.

## Commands

### `index` - Index a data source

Index code from various sources using source-specific subcommands.

```bash  theme={null}
npx ctxc index <source> [options]
```

#### Subcommands

| Source      | Description                  |
| ----------- | ---------------------------- |
| `github`    | Index a GitHub repository    |
| `gitlab`    | Index a GitLab project       |
| `bitbucket` | Index a Bitbucket repository |
| `website`   | Crawl and index a website    |

***

#### `index github`

```bash  theme={null}
npx ctxc index github [options]
```

| Option               | Description                 | Default |
| -------------------- | --------------------------- | ------- |
| `-i, --index <name>` | Index name (required)       | -       |
| `--owner <owner>`    | Repository owner (required) | -       |
| `--repo <repo>`      | Repository name (required)  | -       |
| `--ref <ref>`        | Branch, tag, or commit      | `HEAD`  |

**Environment:** Requires `GITHUB_TOKEN` with repo read access.

***

#### `index gitlab`

```bash  theme={null}
npx ctxc index gitlab [options]
```

| Option               | Description                   | Default              |
| -------------------- | ----------------------------- | -------------------- |
| `-i, --index <name>` | Index name (required)         | -                    |
| `--project <id>`     | Project ID or path (required) | -                    |
| `--ref <ref>`        | Branch, tag, or commit        | `HEAD`               |
| `--gitlab-url <url>` | GitLab base URL (self-hosted) | `https://gitlab.com` |

**Environment:** Requires `GITLAB_TOKEN` with repo read access.

***

#### `index bitbucket`

```bash  theme={null}
npx ctxc index bitbucket [options]
```

| Option                  | Description                             | Default                         |
| ----------------------- | --------------------------------------- | ------------------------------- |
| `-i, --index <name>`    | Index name (required)                   | -                               |
| `--workspace <slug>`    | Workspace slug (required)               | -                               |
| `--repo <repo>`         | Repository name (required)              | -                               |
| `--ref <ref>`           | Branch, tag, or commit                  | `HEAD`                          |
| `--bitbucket-url <url>` | Bitbucket base URL (Server/Data Center) | `https://api.bitbucket.org/2.0` |

**Environment:** Requires `BITBUCKET_TOKEN` with repo read access.

***

#### `index website`

```bash  theme={null}
npx ctxc index website [options]
```

| Option                    | Description                     | Default |
| ------------------------- | ------------------------------- | ------- |
| `-i, --index <name>`      | Index name (required)           | -       |
| `--url <url>`             | Website URL to crawl (required) | -       |
| `--max-depth <n>`         | Maximum crawl depth             | `3`     |
| `--max-pages <n>`         | Maximum pages to crawl          | `100`   |
| `--include <patterns...>` | URL patterns to include (glob)  | -       |
| `--exclude <patterns...>` | URL patterns to exclude (glob)  | -       |

***

#### Store Options (all index subcommands)

| Option                | Description                    | Default           |
| --------------------- | ------------------------------ | ----------------- |
| `--store <type>`      | Store type: `filesystem`, `s3` | `filesystem`      |
| `--store-path <path>` | Store base path                | Platform-specific |

**S3 Configuration (environment variables):**

| Variable                 | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `AWS_ACCESS_KEY_ID`      | AWS access key (required for S3)                 |
| `AWS_SECRET_ACCESS_KEY`  | AWS secret key (required for S3)                 |
| `CC_S3_BUCKET`           | S3 bucket name                                   |
| `CC_S3_ENDPOINT`         | Custom endpoint URL (for S3-compatible services) |
| `CC_S3_FORCE_PATH_STYLE` | Use path-style URLs (`true`/`false`)             |

#### Examples

```bash  theme={null}
# Index GitHub repo
export GITHUB_TOKEN='ghp_...'
npx ctxc index github --owner facebook --repo react -i react

# Index GitLab project
export GITLAB_TOKEN='glpat-...'
npx ctxc index gitlab --project mygroup/myrepo -i myrepo

# Index Bitbucket repo
export BITBUCKET_TOKEN='...'
npx ctxc index bitbucket --workspace myws --repo myrepo -i myrepo

# Index website
npx ctxc index website --url https://docs.example.com -i docs

# Index to S3
export CC_S3_BUCKET='my-team-indexes'
npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3
```

***

### `list` - List local indexes

List all indexes in the local store.

```bash  theme={null}
npx ctxc list [options]
```

#### Optional Options

| Option                | Description             | Default                         |
| --------------------- | ----------------------- | ------------------------------- |
| `--store-path <path>` | Store path to list from | `~/.augment/context-connectors` |

#### Examples

```bash  theme={null}
# List all local indexes
npx ctxc list

# List from custom store path
npx ctxc list --store-path /data/indexes
```

***

### `delete` - Delete a local index

Delete an index from the local store.

```bash  theme={null}
npx ctxc delete <name> [options]
```

#### Arguments

| Argument | Description                            |
| -------- | -------------------------------------- |
| `<name>` | Name of the index to delete (required) |

#### Optional Options

| Option                | Description                     | Default                         |
| --------------------- | ------------------------------- | ------------------------------- |
| `--store-path <path>` | Store path containing the index | `~/.augment/context-connectors` |

#### Examples

```bash  theme={null}
# Delete an index
npx ctxc delete my-project

# Delete from custom store path
npx ctxc delete my-project --store-path /data/indexes
```

***

### `search` - Search indexed content

Search indexed content and answer questions using an LLM.

```bash  theme={null}
npx ctxc search <query> [options]
```

#### Arguments

| Argument  | Description                        |
| --------- | ---------------------------------- |
| `<query>` | Search query / question (required) |

#### Required Options

| Option               | Description                                            |
| -------------------- | ------------------------------------------------------ |
| `-i, --index <spec>` | Index spec: `name`, `path:/path`, or `s3://bucket/key` |

#### Optional Options

| Option                 | Description                                     | Default |
| ---------------------- | ----------------------------------------------- | ------- |
| `--raw`                | Return raw search results instead of LLM answer | `false` |
| `--max-chars <number>` | Maximum output characters (only with `--raw`)   | -       |

#### Index Spec Formats

| Format | Example                   | Description                   |
| ------ | ------------------------- | ----------------------------- |
| Name   | `my-project`              | Index from default store path |
| Path   | `path:/data/indexes/proj` | Direct filesystem path        |
| S3     | `s3://bucket/prefix/proj` | S3 location                   |

#### Examples

```bash  theme={null}
# Ask a question (uses LLM to answer)
npx ctxc search "How does authentication work?" -i my-project

# Raw search results (no LLM)
npx ctxc search "authentication logic" -i my-project --raw

# Search S3-stored index
npx ctxc search "API routes" -i s3://my-bucket/indexes/my-project

# Search from a specific path
npx ctxc search "database queries" -i path:/data/indexes/my-project
```

***

### `agent` - Interactive AI agent

Run an interactive AI agent that can search and read your codebase.

```bash  theme={null}
npx ctxc agent [query] [options]
```

#### Arguments

| Argument  | Description            |
| --------- | ---------------------- |
| `[query]` | Optional initial query |

#### Required Options

| Option                   | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| `-i, --index <specs...>` | Index spec(s): `name`, `path:/path`, or `s3://bucket/key` |
| `--provider <name>`      | LLM provider: `openai`, `anthropic`, `google`             |

#### Optional Options

| Option            | Description                                   | Default                   |
| ----------------- | --------------------------------------------- | ------------------------- |
| `--print`         | Non-interactive mode: print response and exit | `false`                   |
| `--model <name>`  | Model to use                                  | Provider-specific default |
| `--max-steps <n>` | Maximum agent steps                           | `10`                      |
| `-v, --verbose`   | Show tool calls                               | `false`                   |
| `--search-only`   | Disable file operations                       | `false`                   |

**Environment:** Requires provider-specific API key:

* OpenAI: `OPENAI_API_KEY`
* Anthropic: `ANTHROPIC_API_KEY`
* Google: `GOOGLE_API_KEY`

**Default Models:**

* OpenAI: `gpt-5-mini`
* Anthropic: `claude-haiku-4-5`
* Google: `gemini-3-flash-preview`

#### Examples

```bash  theme={null}
# Interactive mode (default)
export OPENAI_API_KEY='sk-...'
npx ctxc agent -i my-project --provider openai

# Interactive mode with initial query (continues interactively after response)
export ANTHROPIC_API_KEY='sk-ant-...'
npx ctxc agent -i my-project --provider anthropic "How does auth work?"

# Non-interactive mode (prints response and exits)
npx ctxc agent -i my-project --provider anthropic "How does auth work?" --print

# Multiple indexes
npx ctxc agent -i my-project -i s3://bucket/other-project --provider openai

# Verbose mode
npx ctxc agent -i my-project --provider openai --verbose
```

***

### `mcp stdio` - Run as MCP server (stdio)

Run as an MCP server using stdio transport for integration with MCP-compatible agents like Claude Desktop.

```bash  theme={null}
npx ctxc mcp stdio [options]
```

#### Optional Options

| Option                   | Description                                               | Default     |
| ------------------------ | --------------------------------------------------------- | ----------- |
| `-i, --index <specs...>` | Index spec(s): `name`, `path:/path`, or `s3://bucket/key` | All indexes |
| `--search-only`          | Disable file operations                                   | `false`     |

When no `--index` is specified, all indexes in the default store are exposed.

#### Examples

```bash  theme={null}
# Expose a specific index
npx ctxc mcp stdio -i my-project

# Multiple indexes
npx ctxc mcp stdio -i my-project -i other-project

# From S3
npx ctxc mcp stdio -i s3://my-bucket/indexes/my-project

# All indexes in default store
npx ctxc mcp stdio
```

***

### `mcp http` - Start MCP HTTP server

Start an MCP server accessible over HTTP for remote clients.

```bash  theme={null}
npx ctxc mcp http [options]
```

#### Optional Options

| Option                   | Description                                               | Default     |
| ------------------------ | --------------------------------------------------------- | ----------- |
| `-i, --index <specs...>` | Index spec(s): `name`, `path:/path`, or `s3://bucket/key` | All indexes |
| `--port <number>`        | Port to listen on                                         | `3000`      |
| `--host <host>`          | Host to bind to                                           | `localhost` |
| `--cors <origins>`       | CORS origins (comma-separated, or `*`)                    | -           |
| `--base-path <path>`     | Base path for MCP endpoint                                | `/mcp`      |
| `--api-key <key>`        | API key for authentication                                | -           |
| `--search-only`          | Disable file operations                                   | `false`     |

**Environment:** Can use `MCP_API_KEY` instead of `--api-key` flag.

#### Examples

```bash  theme={null}
# Basic HTTP server
npx ctxc mcp http -i my-project --port 8080

# With authentication and CORS
npx ctxc mcp http -i my-project --port 8080 \
  --api-key "secret" --cors "*"

# Accept external connections
npx ctxc mcp http -i my-project --host 0.0.0.0 --port 8080

# Search-only mode
npx ctxc mcp http -i my-project --search-only

# From S3
npx ctxc mcp http -i s3://my-bucket/indexes/my-project --port 8080
```

***

## Common Patterns

### Using S3 Storage

All commands support S3 storage for team sharing:

```bash  theme={null}
# Set AWS credentials and S3 bucket
export AWS_ACCESS_KEY_ID='your-key'
export AWS_SECRET_ACCESS_KEY='your-secret'
export CC_S3_BUCKET='my-team-indexes'

# Index to S3
npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3

# Search from S3
npx ctxc search "query" -i s3://my-team-indexes/my-project
```

### Using S3-Compatible Services

For MinIO, DigitalOcean Spaces, Cloudflare R2, etc.:

```bash  theme={null}
export CC_S3_BUCKET='my-bucket'
export CC_S3_ENDPOINT='http://localhost:9000'
export CC_S3_FORCE_PATH_STYLE='true'

npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3
```

### File Operations

The `--search-only` flag controls whether file operations are available:

* **Without `--search-only`**: Enables `search`, `listFiles`, and `readFile` tools
* **With `--search-only`**: Only `search` tool is available

***

## Troubleshooting

### "Index not found"

Make sure the index spec points to the correct location (name, path, or S3 URL).

### "AUGMENT\_API\_TOKEN is not set"

Set the required environment variables:

```bash  theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

### S3 Access Denied

Verify your AWS credentials and bucket permissions:

```bash  theme={null}
export AWS_ACCESS_KEY_ID='your-key'
export AWS_SECRET_ACCESS_KEY='your-secret'
```

### GitHub/GitLab/BitBucket Authentication

Make sure the appropriate token is set:

```bash  theme={null}
export GITHUB_TOKEN='ghp_...'
export GITLAB_TOKEN='glpat-...'
export BITBUCKET_TOKEN='...'
```
