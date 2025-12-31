# Source: https://docs.bito.ai/ai-architect/guide-for-github-copilot-vs-code.md

# Guide for GitHub Copilot (VS Code)

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **GitHub Copilot in VS Code** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), GitHub Copilot can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Follow the [**AI Architect installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted). Upon successful setup, you will receive a **Bito MCP URL** and **Bito MCP Access Token** that you need to enter in your coding agent.
2. [Download **BitoAIArchitectGuidelines.md** file](https://github.com/gitbito/ai-architect/blob/main/BitoAIArchitectGuidelines.md). You will need to copy/paste the content from this file later when configuring AI Architect.
   * **Note:** This file contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server. The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.
3. **Requires Visual Studio Code version 1.99 or later**
   1. **Check VS Code version:** `code --version`
   2. **Update VS Code if needed:** Help → Check for Updates
4. **Enable Agent Mode**
   1. Open VS Code Settings (Ctrl/Cmd + ,)
   2. Search: `chat.agent.enabled`
   3. Check the box to enable Agent Mode
5. **Ensure Node.js 20.18.1+ is Installed:**

   VS Code's MCP implementation automatically tries to use OAuth for HTTP servers. For static Bearer token authentication (which Bito AI Architect uses), you need to use the `mcp-remote` proxy tool.

   The `mcp-remote` proxy requires **Node.js 20.18.1 or higher**.

   **Why Node.js 20+?** The mcp-remote proxy depends on undici v7, which requires Node.js 20+ (needs the `File` global API added in Node 20.0.0). Node.js 18 and earlier will fail with `ReferenceError: File is not defined`.

   **Windows:** Download from <https://nodejs.org/> (download 20.x LTS)

   **macOS:**

   ```shellscript
   brew install node@20
   # Or use nvm: nvm install 20 && nvm use 20
   ```

   **Linux (Ubuntu/Debian):**

   ```shellscript
   curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

   **Verify:**

   ```shellscript
   node --version  # Should show v20.x.x or higher
   npx --version
   ```
6. GitHub Copilot extension installed and enabled
7. GitHub account with Copilot access

## Set up AI Architect

VS Code has the same setup process across all platforms (Windows, macOS, Linux, WSL).

### Workspace configuration (recommended)

{% stepper %}
{% step %}

### Create .vscode directory

In your project root:

```shellscript
mkdir .vscode
```

{% endstep %}

{% step %}

### Create mcp.json

Create `.vscode/mcp.json`:

```json
{
  "servers": {
    "BitoAIArchitect": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "<Your-Bito-MCP-URL>",
        "--header",
        "Authorization: Bearer <Your-Bito-MCP-Access-Token>"
      ]
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
  {% endhint %}

**Important:**

* VS Code requires `mcp-remote` proxy for static Bearer token authentication
* The `"servers"` object is at the root level in workspace configs
* Direct HTTP transport with static Bearer tokens triggers OAuth flows in VS Code

**Why mcp-remote?** VS Code's MCP implementation automatically initiates OAuth discovery when connecting to HTTP MCP servers. Since `BitoAIArchitect` uses static Bearer token authentication (not OAuth), we use the `mcp-remote` proxy to handle the authentication properly.
{% endstep %}

{% step %}

### Add guidelines (optional but highly recommended)

The [**BitoAIArchitectGuidelines.md** file](#prerequisites) contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server.

The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

Create `.github` directory:

```shellscript
mkdir -p .github
```

Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `.github/copilot-instructions.md` file:

```shellscript
cp BitoAIArchitectGuidelines.md .github/copilot-instructions.md
```

{% endstep %}

{% step %}

### Start the MCP server

1. Open `.vscode/mcp.json` in VS Code
2. Look for a **Start** button above the configuration
3. Click **Start** to initialize the server
   {% endstep %}

{% step %}

### Verify in Copilot Chat

1. Open Copilot Chat (Ctrl/Cmd + I)
2. Switch to Agent mode (toggle in chat interface)
3. Click the Tools icon (wrench)
4. Verify `BitoAIArchitect` appears in the tools list
   {% endstep %}
   {% endstepper %}

### User configuration (global)

To make `BitoAIArchitect` available in ALL projects:

#### Windows

* **Open:** `%APPDATA%\Code\User\settings.json`

#### macOS

* **Open:** `~/Library/Application Support/Code/User/settings.json`

#### Linux

* **Open:** `~/.config/Code/User/settings.json`

#### Configuration

Add this to your `settings.json`:

```json
{
  "mcp": {
    "servers": {
      "BitoAIArchitect": {
        "command": "npx",
        "args": [
          "-y",
          "mcp-remote",
          "<Your-Bito-MCP-URL>",
          "--header",
          "Authorization: Bearer <Your-Bito-MCP-Access-Token>"
        ]
      }
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
  {% endhint %}

**Important:**

* In User settings, use `"mcp"` → `"servers"` nested structure
* In Workspace config, use `"servers"` at root level
* VS Code uses `mcp-remote` proxy for Bearer token authentication

## Troubleshooting VS Code (GitHub Copilot)

#### Agent Mode not available:

1. Update VS Code to 1.99+
2. Settings → Search: `chat.agent.enabled`
3. Enable the checkbox

#### Server not starting:

1. View → Output
2. Select **GitHub Copilot Chat** from dropdown
3. Look for error messages
4. Click **Start** button in `.vscode/mcp.json`

#### Tools not showing:

1. Open Copilot Chat
2. Switch to Agent mode
3. Click Tools (wrench icon)
4. Verify `BitoAIArchitect` appears

#### Reset if needed:

* Ctrl/Cmd + Shift + P
* Run: `MCP: Reset Cached Tools`
* Restart VS Code

#### OAuth prompts appearing:

If VS Code is prompting for OAuth instead of using your Bearer token:

1. Ensure you're using the `mcp-remote` proxy configuration (not direct HTTP)
2. Verify the `--header` argument is correctly formatted
3. Check that Node.js and `npx` are installed: `npx --version`
4. Try removing any cached OAuth credentials:
   * Command Palette → `Authentication: Remove Dynamic Authentication Providers`
