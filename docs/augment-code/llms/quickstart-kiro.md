# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-kiro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart (Kiro)

> Get started with Augment Context Engine MCP in Kiro in minutes

## Quick Start with Kiro

### 1. Install Auggie CLI

```bash  theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Kiro

Open the command palette (`Cmd + Shift + P` on Mac, `Ctrl + Shift + P` on Windows/Linux) and select:

* **Kiro: Open workspace MCP config (JSON)** - For workspace-level configuration
* **Kiro: Open user MCP config (JSON)** - For user-level configuration

Paste this configuration:

```json  theme={null}
{
  "mcpServers": {
    "Augment-Context-Engine": {
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"],
      "disabled": false,
      "autoApprove": ["codebase-retrieval"]
    }
  }
}
```

### 4. Test the integration

```
Prompt: "Do you have access to the Augment codebase retrieval tool?"
```

Kiro should confirm it has access to the `codebase-retrieval` tool.
