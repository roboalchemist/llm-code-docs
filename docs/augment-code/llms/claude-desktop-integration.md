# Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/claude-desktop-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Local MCP Server

> Add codebase search to Claude Desktop, Claude Code, Cursor, or another agent in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* Claude Desktop installed
* An indexed project (see [Index and Search Code](/context-services/context-connectors/quickstart/index-git-repos))
* Augment API credentials

## Steps

### 1. Open Claude Desktop config

<Tabs>
  <Tab title="macOS">
    ```bash  theme={null}
    open ~/Library/Application\ Support/Claude/claude_desktop_config.json
    ```
  </Tab>

  <Tab title="Windows">
    ```
    %APPDATA%\Claude\claude_desktop_config.json
    ```
  </Tab>
</Tabs>

### 2. Add MCP server config

<Tabs>
  <Tab title="Local Filesystem">
    ```json  theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="GitHub">
    ```json  theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/",
            "GITHUB_TOKEN": "ghp_..."
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="GitLab">
    ```json  theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/",
            "GITLAB_TOKEN": "glpat-..."
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="BitBucket">
    ```json  theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/",
            "BITBUCKET_TOKEN": "..."
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

### 3. Restart Claude Desktop

Quit and reopen Claude Desktop.

### 4. Test it

Ask Claude:

> Search for authentication logic in my-project

You should see Claude use the search tool and return code snippets.

## Done!

Your agent can now search your codebase via the local MCP server.

## Works With Other Agents

This same configuration works with any MCP-compatible agent:

* **Claude Desktop** - Follow the steps above
* **Claude Code** (VS Code extension) - Add to Claude Code's MCP settings
* **Cursor** - Configure in Cursor's MCP settings
* **GitHub Copilot** - Add to Copilot's MCP configuration
* **Custom agents** - Any tool that supports MCP stdio protocol

Each agent has its own config file location, but the MCP server configuration is the same.

## Also Works With

| Instead of... | Try...                                                         |
| ------------- | -------------------------------------------------------------- |
| One repo      | Add multiple entries to `mcpServers` for different projects    |
| Local index   | S3-stored indexes with `--store s3` and `CC_S3_BUCKET` env var |
| Search only   | Add `--search-only` to disable file reading                    |
