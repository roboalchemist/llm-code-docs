# Source: https://docs.bito.ai/ai-architect/guide-for-claude-desktop.md

# Guide for Claude Desktop

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **Claude Desktop** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Claude Desktop can leverage AI Architect's deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Follow the [**AI Architect installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted). Upon successful setup, you will receive a **Bito MCP URL** and **Bito MCP Access Token** that you need to enter in your coding agent.
2. [Download **BitoAIArchitectGuidelines.md file**](https://github.com/gitbito/ai-architect/blob/main/BitoAIArchitectGuidelines.md). You will need to copy/paste the content from this file later when configuring AI Architect.
   * **Note:** This file contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server. The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.
3. **Claude Desktop installed** - Download and install Claude Desktop from [claude.ai/download](https://claude.ai/download) if you haven't already.
4. **Node.js 20.18.1 or higher** - Required for the `mcp-remote` proxy
   * **macOS:**

     ```shellscript
     brew install node@20
     # Or use nvm: nvm install 20 && nvm use 20
     ```
   * **Windows:** Download from <https://nodejs.org/> (download 20.x LTS)
   * **Linux (Ubuntu/Debian):**

     ```shellscript
     curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
     sudo apt-get install -y nodejs
     ```
   * **Verify installation:**

     ```shellscript
     node --version  # Should show v20.x.x or higher
     npx --version
     ```

{% hint style="info" %}
**Note:** Claude Desktop uses OAuth 2.1 authentication via the `mcp-remote` proxy, so you don't need to manually manage access tokens. Your email will be collected during the OAuth consent flow.
{% endhint %}

## Set up AI Architect

Claude Desktop uses `claude_desktop_config.json` with the `mcp-remote` proxy for OAuth-enabled remote servers.

Claude Desktop supports both local MCP servers and remote HTTP servers. For Bito AI Architect (a remote OAuth server), we use the `mcp-remote` proxy which handles the OAuth flow automatically.

{% stepper %}
{% step %}

### Open configuration file

#### **macOS:**

1. Open Claude Desktop
2. Click **Claude** menu → **Settings** → **Developer** tab
3. Click **Edit Config** to open `claude_desktop_config.json`

Or manually open: `~/Library/Application Support/Claude/claude_desktop_config.json`

#### **Windows:**

1. Open Claude Desktop
2. Click **File** → **Settings** → **Developer** tab
3. Click **Edit Config** to open `claude_desktop_config.json`

Or manually open: `%APPDATA%\Claude\claude_desktop_config.json`
{% endstep %}

{% step %}

### Add AI Architect configuration

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "BitoAIArchitect": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "<Your-Bito-MCP-URL>"
      ]
    }
  }
}
```

{% hint style="info" %}

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
    {% endhint %}

If you already have other MCP servers configured, add BitoAIArchitect to the existing `mcpServers` object:

```json
{
  "mcpServers": {
    "existing-server": {
      ...
    },
    "BitoAIArchitect": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "<Your-Bito-MCP-URL>"
      ]
    }
  }
}
```

{% hint style="info" %}

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
    {% endhint %}

**Windows-specific configuration:**

On Windows, you may need to use the `cmd` wrapper:

```json
{
  "mcpServers": {
    "BitoAIArchitect": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "mcp-remote",
        "<Your-Bito-MCP-URL>"
      ]
    }
  }
}
```

{% hint style="info" %}

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
    {% endhint %}
    {% endstep %}

{% step %}

### Restart Claude Desktop

1. **Completely quit** Claude Desktop (not just close the window)
   * macOS: Claude menu → Quit Claude
   * Windows: Right-click system tray icon → Exit
2. Reopen Claude Desktop
3. The MCP server will start automatically
   {% endstep %}

{% step %}

### Complete OAuth authorization

On first use, `mcp-remote` will open your browser to complete OAuth:

1. A browser window opens showing the **Bito Authorization** page
2. Review the requested permissions
3. **Enter your email address** (required for tracking)
4. Click **"Authorize"** or **"Allow"**
5. Return to Claude Desktop - the connection is now active
   {% endstep %}

{% step %}

### Verify connection

1. In Claude Desktop, click the **"+"** button at the bottom of the chat
2. Select **"Connectors"** or look for the hammer/wrench icon
3. BitoAIArchitect should appear in the list
4. Try asking: "What repositories are available?"
   {% endstep %}
   {% endstepper %}

## Troubleshooting Claude Desktop

#### **Server not appearing:**

1. Verify JSON syntax in config file
2. Ensure Node.js 20+ is installed: `node --version`
3. Check that `npx` is available: `npx --version`
4. Fully quit and restart Claude Desktop

#### **OAuth flow not starting:**

1. Ensure your browser is set as default
2. Allow pop-ups for the OAuth flow
3. Check firewall settings

#### **"mcp-remote not found" error:**

* Ensure Node.js is in your PATH
* Try running `npx -y mcp-remote --help` in terminal to verify it works

#### **Connection shows "Disconnected":**

* OAuth tokens may have expired - restart Claude Desktop to re-authorize
* Check your internet connection
* Verify the Workspace ID is correct
