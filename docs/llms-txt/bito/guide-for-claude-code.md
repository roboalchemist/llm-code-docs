# Source: https://docs.bito.ai/ai-architect/guide-for-claude-code.md

# Guide for Claude Code

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **Claude Code** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Claude Code can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Quick setup (recommended)

**Want to get started faster?** We offer an automated installer that can configure AI Architect for all your AI coding tools in just a few seconds.

The automated setup will:

* Detect all compatible AI tools installed on your system
* Configure them automatically with your credentials
* Save you time by eliminating manual configuration steps

👉 [**Try our Quick MCP Integration Guide**](https://docs.bito.ai/ai-architect/quick-mcp-integration-with-ai-coding-agents) for automated setup.

## Manual setup

If you prefer manual configuration, follow the step-by-step instructions below.

## Prerequisites

1. Follow the [**AI Architect installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted). Upon successful setup, you will receive a **Bito MCP URL** and **Bito MCP Access Token** that you need to enter in your coding agent.
2. [Download **BitoAIArchitectGuidelines.md** file](https://github.com/gitbito/ai-architect/blob/main/BitoAIArchitectGuidelines.md). You will need to copy/paste the content from this file later when configuring AI Architect.
   * **Note:** This file contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server. The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

## Set up AI Architect

Claude Code has the same setup process across all platforms (Windows, macOS, Linux, WSL) using the command line.

Claude Code uses CLI-based configuration, NOT manual JSON editing.

{% stepper %}
{% step %}

### Install Claude Code

If you haven't already:

```shellscript
npm install -g @anthropic-ai/claude-code
```

Verify installation:

```shellscript
claude --version
```

{% endstep %}

{% step %}

### Add Bito AI Architect MCP server

Use the `claude mcp add` command with the correct parameter order:

```shellscript
claude mcp add \
  --transport http \
  --scope user \
  BitoAIArchitect \
  <Your-Bito-MCP-URL> \
  --header "Authorization: Bearer <Your-Bito-MCP-Access-Token>" \
  --header "x-email-id: <Your-Email>"
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
* Replace `<Your-Email>` with your actual email address.
  {% endhint %}

{% hint style="info" %}
**Important:** The server name and URL must come BEFORE the `--header` option.
{% endhint %}

{% hint style="info" %}
**Scope options:**

* `--scope user`: Available in all your projects (recommended)
* `--scope project`: Only in current project (stored in `.mcp.json`)
* `--scope local`: Only in current directory (default)
  {% endhint %}
  {% endstep %}

{% step %}

### Verify installation

List your MCP servers:

```shellscript
claude mcp list
```

You should see "BitoAIArchitect" in the list.

Test the server:

```shellscript
claude mcp get BitoAIArchitect
```

{% endstep %}

{% step %}

### Add guidelines (optional but highly recommended)

The [**BitoAIArchitectGuidelines.md** file](#prerequisites) contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server.

The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

**You can either create:**

1. **Global guidelines** - Apply across all your projects. Best for teams or developers who want consistent standards everywhere.
2. **Project-specific guidelines** - Apply to a single project only.

Choose one of the following based on your preference:

### Option A: Global guidelines

Create `.claude` directory if it doesn't exist:

```shellscript
mkdir -p ~/.claude
```

Create or edit `CLAUDE.md`:

```shellscript
nano ~/.claude/CLAUDE.md
```

Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into this file, then save.

### Option B: Project-specific guidelines

Run this command in your project directory:

```shellscript
nano CLAUDE.md
```

Or run these commands:

```shellscript
mkdir -p .claude
```

```shellscript
nano .claude/CLAUDE.md
```

Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into this file, then save.
{% endstep %}

{% step %}

### Start using Claude Code

In your project directory, run:

```shellscript
claude
```

Now, in the chat you can ask questions about your indexed repositories. The AI Architect will help Claude Code provide accurate answers based on your codebase.

**Try asking something like:**

```
What repositories are available in my organization?
```

{% endstep %}
{% endstepper %}

## Windows-specific notes

#### Windows (Native - Command Prompt/PowerShell):

* MCP servers using `npx` require the `cmd /c` wrapper:

```shellscript
# For stdio servers on Windows
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

#### Windows (WSL):

* Configuration is stored in Linux file system
* No need for `cmd /c` wrapper
* Use standard Linux paths (`~/.claude/`)

## Configuration file locations

<table><thead><tr><th width="104.60003662109375">Platform</th><th>Main config</th><th>Settings</th><th>Global guidelines</th></tr></thead><tbody><tr><td><strong>Windows</strong></td><td><code>%USERPROFILE%\.claude\claude.json</code></td><td><code>%USERPROFILE%\.claude\settings.json</code></td><td><code>%USERPROFILE%\.claude\CLAUDE.md</code></td></tr><tr><td><strong>macOS</strong></td><td><code>~/.claude/claude.json</code></td><td><code>~/.claude/settings.json</code></td><td><code>~/.claude/CLAUDE.md</code></td></tr><tr><td><strong>Linux</strong></td><td><code>~/.claude/claude.json</code></td><td><code>~/.claude/settings.json</code></td><td><code>~/.claude/CLAUDE.md</code></td></tr><tr><td><strong>WSL</strong></td><td><code>~/.claude/claude.json</code></td><td><code>~/.claude/settings.json</code></td><td><code>~/.claude/CLAUDE.md</code></td></tr></tbody></table>

{% hint style="info" %}
**IMPORTANT:**

* ✅ These files are managed automatically by `claude mcp` commands
* ❌ Do NOT manually create `~/.claude/mcp.json` (this file doesn't exist)
* ❌ Do NOT manually edit `~/.claude/claude.json` (use CLI commands instead)
  {% endhint %}

## Common Claude Code MCP commands

```shellscript
# Add HTTP server with Bearer token (correct parameter order)
claude mcp add --transport http --scope user \
  <name> <url> \
  --header "Authorization: Bearer <token>" \
  --header "x-email-id: <your-email>"

# Add server with environment variables
claude mcp add <name> -e API_KEY="value" -- npx @server/package

# Add server with JSON config (for complex setups)
claude mcp add-json <name> '{"type":"http","url":"...","headers":{...}}'

# List all MCP servers
claude mcp list

# Get server details
claude mcp get <name>

# Remove MCP server
claude mcp remove <name>

# View server status (inside Claude Code session)
/mcp

# Reset project-scoped server approval choices
claude mcp reset-project-choices

```

## Troubleshooting Claude Code

#### Server not appearing:

```shellscript
# Verify it was added
claude mcp list

# Check for errors
claude --verbose

# Try removing and re-adding
claude mcp remove BitoAIArchitect
claude mcp add --transport http --scope user \
  BitoAIArchitect <Your-Bito-MCP-URL> \
  --header "Authorization: Bearer <Your-Bito-MCP-Access-Token>" \
  --header "x-email-id: <Your-Email>"
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
* Replace `<Your-Email>` with your actual email address.
  {% endhint %}

#### Connection issues:

```shellscript
# Test the endpoint with proper MCP protocol
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

#### Permission issues (macOS/Linux):

```shellscript
chmod 755 ~/.claude
chmod 644 ~/.claude/claude.json
chmod 644 ~/.claude/settings.json
```
