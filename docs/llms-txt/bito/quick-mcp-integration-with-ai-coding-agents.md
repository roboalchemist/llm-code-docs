# Source: https://docs.bito.ai/ai-architect/quick-mcp-integration-with-ai-coding-agents.md

# Quick MCP integration with AI coding agents

## Prerequisites

Before running the installer, have these ready:

1. Your Bito Workspace ID (or full Bito MCP URL for self-hosted instances)
2. Your Bito MCP Access Token

{% hint style="info" %}
Note: For self-hosted instances, follow the [**AI Architect installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted). Upon successful setup, you will receive a **Bito MCP URL** and **Bito MCP Access Token** that you need to enter.
{% endhint %}

3. Your email ID (for tracking/identification)
4. At least one supported tool installed:
   * Claude Code
   * Cursor
   * Windsurf
   * VS Code (GitHub Copilot)
   * Junie
   * JetBrains AI Assistant

{% hint style="info" %}
**Note:** For [Claude.ai (Web)](https://docs.bito.ai/ai-architect/guide-for-claude.ai-web) and [ChatGPT (Web & Desktop)](https://docs.bito.ai/ai-architect/guide-for-chatgpt-web-and-desktop) you'll need to follow the manual setup process as they require OAuth authentication through your browser.
{% endhint %}

## Installation guide

Our automated installer will prompt you for credentials and automatically configure all supported AI tools available on your system.

#### macOS / Linux

Open your terminal and run:

```bash
curl -fsSL https://mcp-setup.bito.ai/install.sh | bash
```

#### Windows

Open **PowerShell** (not Command Prompt) and run:

```powershell
irm https://mcp-setup.bito.ai/install.ps1 | iex
```

{% hint style="info" %}
**Note:** When using a self-hosted AI Architect, ensure that the MCP server is up and running before proceeding with the setup. The setup will fail if MCP is not running.
{% endhint %}

#### What happens next

1. **The installer starts** and checks for compatible tools
2. **You'll be prompted** to enter your credentials.
3. **Automatic configuration** - All detected tools are configured
4. **Confirmation** - You'll see which tools were successfully set up

## After installation

{% stepper %}
{% step %}

### Restart your AI tool

After the installer completes, **completely close and reopen your AI tool** to ensure the configuration takes effect.
{% endstep %}

{% step %}

### Verify AI architect connection

Check that AI Architect appears in your tool's MCP server list:

* **Claude Desktop:** Click "+" → Connectors → look for BitoAIArchitect
* **Claude Code:** Run `claude mcp list` to see BitoAIArchitect
* **Cursor:** Settings → MCP → look for BitoAIArchitect
* **Windsurf:** Settings → Windsurf Settings → Cascade → MCP Servers → Open MCP Marketplace → look for BitoAIArchitect
* **VS Code:** Copilot Chat → gear icon → MCP Servers → look for BitoAIArchitect
  {% endstep %}

{% step %}

### Run a test query

Open a chat or conversation in your AI tool and try a test query to confirm AI Architect is working:

* "What repositories are available in my organization?"
* "Show me all Python repositories"
* "List the available tools"

If you receive accurate responses about your codebase, the setup is complete!
{% endstep %}
{% endstepper %}

## Uninstalling

To remove Bito AI Architect from all tools:

#### macOS / Linux

Open your terminal and run:

```bash
curl -fsSL https://mcp-setup.bito.ai/uninstall.sh | bash
```

#### Windows

Open **PowerShell** (not Command Prompt) and run:

```powershell
irm https://mcp-setup.bito.ai/uninstall.ps1 | iex
```

## Need manual setup?

If you prefer to configure tools individually or need to set up web-based tools (Claude.ai, ChatGPT), refer to our detailed integration guides:

* [Claude Code](https://docs.bito.ai/ai-architect/guide-for-claude-code)
* [Claude Desktop](https://docs.bito.ai/ai-architect/guide-for-claude-desktop)
* [Claude.ai (Web)](https://docs.bito.ai/ai-architect/guide-for-claude.ai-web)
* [Cursor](https://docs.bito.ai/ai-architect/guide-for-cursor)
* [Windsurf](https://docs.bito.ai/ai-architect/guide-for-windsurf)
* [GitHub Copilot (VS Code)](https://docs.bito.ai/ai-architect/guide-for-github-copilot-vs-code)
* [Junie](https://docs.bito.ai/ai-architect/guide-for-junie-jetbrains)
* [JetBrains AI Assistant](https://docs.bito.ai/ai-architect/guide-for-jetbrains-ai-assistant)
* [ChatGPT (Web & Desktop)](https://docs.bito.ai/ai-architect/guide-for-chatgpt-web-and-desktop)

## Troubleshooting

#### Installer issues

**"Command not found" or similar errors:**

* Verify you're using the correct shell (bash for macOS/Linux, PowerShell for Windows)
* Check your internet connection
* Try running the command again

**No tools detected:**

* Ensure your AI tools are installed before running the installer
* The installer only configures tools it can detect on your system
* You can run the installer again after installing new tools

#### Connection issues

* Verify **Bito MCP URL** and **Bito MCP Access Token** are correct.
* Test endpoint with MCP protocol:

```bash
curl -s -X POST \
  -H "Authorization: Bearer <Your-Bito-MCP-Access-Token>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}' \
  <Your-Bito-MCP-URL>

# Should return HTTP 200 with JSON response for valid credentials
# HTTP 401: Invalid Bito MCP Access Token
# HTTP 404: Invalid Bito MCP URL
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
  {% endhint %}

**Server not appearing after install:**

* Completely restart your AI tool (don't just reload)
* Verify your credentials were entered correctly
* Check that you have the minimum required versions (see below)

#### Minimum requirements

Some tools require specific versions:

* **Node.js 20.18.1+** for Claude Desktop, VS Code, and JetBrains
* **VS Code 1.99+** with Agent Mode enabled
* **JetBrains 2025.1+** with AI Assistant plugin 251.26094.80.5+

**Check Node.js version:**

```bash
node --version
```

If you need to install or update Node.js, visit [nodejs.org](https://nodejs.org/)
