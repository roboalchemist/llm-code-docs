# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-droid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart (Droid)

> Get started with Augment Context Engine MCP in Droid in minutes

## Quick Start with Droid

### 1. Install Auggie CLI

```bash  theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Droid

Add the Augment Context Engine MCP server:

```bash  theme={null}
droid mcp add augment-code "auggie" --mcp --mcp-auto-workspace
```

### 4. Test the integration

```
Prompt: "Do you have access to the Augment codebase retrieval tool?"
```

Droid should confirm it has access to the `codebase-retrieval` tool.

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
droid mcp add augment-code "auggie" --mcp --mcp-auto-workspace --env AUGMENT_API_TOKEN=your-access-token --env AUGMENT_API_URL=your-tenant-url
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.
