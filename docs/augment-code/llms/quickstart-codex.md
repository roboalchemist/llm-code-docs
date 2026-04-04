# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-codex.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart (Codex)

> Get started with Augment Context Engine MCP in OpenAI Codex CLI in minutes

## Quick Start with Codex

### 1. Install Auggie CLI

```bash  theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Codex

Add the MCP server using the Codex CLI:

```bash  theme={null}
codex mcp add codebase-retrieval -- auggie --mcp --mcp-auto-workspace
```

The `--mcp-auto-workspace` flag automatically detects your workspace when using Codex.

### 4. Test the integration

Run Codex and prompt it with:

```
"What is this project? Please use the codebase-retrieval tool to get the answer."
```

Codex should confirm it has access to the `codebase-retrieval` tool.

## Advanced: Non-Interactive Setup

For non-interactive environments like CI/CD pipelines, GitHub Actions, or automated scripts where you cannot run `auggie login` interactively, you can configure authentication using environment variables.

### 1. Get your authentication token

```bash  theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value.

### 2. Configure with environment variables

```bash  theme={null}
codex mcp add codebase-retrieval --env AUGMENT_API_TOKEN=your-access-token --env AUGMENT_API_URL=your-tenant-url -- auggie --mcp --mcp-auto-workspace
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.
