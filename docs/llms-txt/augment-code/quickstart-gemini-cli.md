# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-gemini-cli.md

# Quickstart (Gemini CLI)

> Get started with Augment Context Engine MCP in Gemini CLI in minutes

## Quick Start with Gemini CLI

### 1. Install Auggie CLI (Pre-release version)

```bash  theme={null}
npm install -g @augmentcode/auggie@prerelease
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Gemini CLI

Gemini CLI reads the MCP server configuration from a settings file. You can configure MCP servers at either the user level (applies to all projects) or project level (applies only to that specific project):

**Configuration file locations:**

* **User settings** (global):
  * macOS/Linux: `~/.gemini/settings.json`
  * Windows: `%USERPROFILE%\.gemini\settings.json`
* **Project settings** (optional): `.gemini/settings.json` in your project's root directory

Add the following configuration to your Gemini CLI settings file:

```json  theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": [
        "--mcp"
      ]
    }
  }
}
```

### 4. Test the integration

Prompt the Gemini CLI with:

```
"What is this project? Please use codebase retrieval tool to get the answer."
```

Gemini CLI should confirm it has access to the `codebase-retrieval` tool.

## Configuration

### Workspace Root

Specify the workspace to index by adding the `-w` argument. Update the **/path/to/project**.

```json  theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": ["-w", "/path/to/project", "--mcp"]
    }
  }
}
```

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

Add the `env` section to your configuration:

```json  theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": ["--mcp"],
      "env": {
        "AUGMENT_API_TOKEN": "your-access-token",
        "AUGMENT_API_URL": "your-tenant-url"
      }
    }
  }
}
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.

For a specific workspace:

```json  theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": ["-w", "/path/to/project", "--mcp"],
      "env": {
        "AUGMENT_API_TOKEN": "your-access-token",
        "AUGMENT_API_URL": "your-tenant-url"
      }
    }
  }
}
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt