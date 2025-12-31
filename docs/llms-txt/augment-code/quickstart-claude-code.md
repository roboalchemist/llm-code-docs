# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-claude-code.md

# Quickstart (Claude Code)

> Get started with Augment Context Engine MCP in Claude Code in minutes

## Quick Start with Claude Code

### 1. Install Auggie CLI (Pre-release version)

```bash  theme={null}
npm install -g @augmentcode/auggie@prerelease
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Claude Code

Add the MCP server to user scope (available in all projects):

```bash  theme={null}
claude mcp add-json auggie-mcp --scope user '{"type":"stdio","command":"auggie","args":["--mcp"]}'
```

Or add to project scope (only available in the current project):

```bash  theme={null}
claude mcp add-json auggie-mcp --scope project '{"type":"stdio","command":"auggie","args":["--mcp"]}'
```

### 4. Test the integration

```bash  theme={null}
claude --print "Do you have access to the Augment codebase retrieval tool? Answer in one sentence."
```

Claude should confirm it has access to the `codebase-retrieval` tool.

## Configuration

### Workspace Root

Specify the workspace to index by adding the `-w` argument:

```bash  theme={null}
claude mcp add-json auggie-mcp --scope user '{"type":"stdio","command":"auggie","args":["-w","/path/to/project","--mcp"]}'
```

Update `/path/to/project` with your actual project path.

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
claude mcp add-json auggie-mcp --scope user '{"type":"stdio","command":"auggie","args":["--mcp"],"env":{"AUGMENT_API_TOKEN":"your-access-token","AUGMENT_API_URL":"your-tenant-url"}}'
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.

For a specific workspace:

```bash  theme={null}
claude mcp add-json auggie-mcp --scope user '{"type":"stdio","command":"auggie","args":["-w","/path/to/project","--mcp"],"env":{"AUGMENT_API_TOKEN":"your-access-token","AUGMENT_API_URL":"your-tenant-url"}}'
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt