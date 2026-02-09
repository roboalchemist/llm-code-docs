# Source: https://docs.bito.ai/ai-architect/guide-for-github-copilot-vs-code.md

# Guide for GitHub Copilot (VS Code)

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **GitHub Copilot in VS Code** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), GitHub Copilot can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

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
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "<Your-Bito-MCP-URL>",
        "--header",
        "Authorization: Bearer <Your-Bito-MCP-Access-Token>",
        "--header",
        "x-email-id: <Your-Email>"
      ]
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
* Replace `<Your-Email>` with your actual email address.
  {% endhint %}

**Important:**

* Include `"type": "stdio"` in the configuration
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

**Important:** VS Code requires manually starting MCP servers. Follow these steps:

1. Open **Copilot Chat** (Ctrl/Cmd + I)
2. Click the **gear icon** in the Copilot Chat panel
3. Select **"MCP Servers"**
4. Find **BitoAIArchitect** in the list
5. Click the **gear icon** next to BitoAIArchitect
6. Select **"Start Server"**

**Alternative method:**

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
5. Try asking: "What repositories are available?"
   {% endstep %}
   {% endstepper %}

### User configuration (global)

To make `BitoAIArchitect` available in ALL projects, create a user-level `mcp.json` file:

#### Windows

* **Create/edit:** `%APPDATA%\Code\User\mcp.json`

#### macOS

* **Create/edit:** `~/Library/Application Support/Code/User/mcp.json`

#### Linux

* **Create/edit:** `~/.config/Code/User/mcp.json`

#### Configuration

Add this to your `mcp.json`:

```json
{
  "servers": {
    "BitoAIArchitect": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "<Your-Bito-MCP-URL>",
        "--header",
        "Authorization: Bearer <Your-Bito-MCP-Access-Token>",
        "--header",
        "x-email-id: <Your-Email>"
      ]
    }
  }
}
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
* Replace `<Your-Email>` with your actual email address.
  {% endhint %}

#### Enable MCP discovery

Also ensure MCP discovery is enabled in your `settings.json`:

```
{
  "chat.mcp.discovery.enabled": true
}
```

**Important:**

* User-level config uses `mcp.json` (separate from `settings.json`)
* Include `"type": "stdio"` in the configuration
* After saving, manually start the server via Copilot Chat (see Step 4 above)

## Troubleshooting VS Code (GitHub Copilot)

#### Server not appearing in MCP Servers list:

1. Verify `mcp.json` is in the correct location (see paths above)
2. Ensure `"type": "stdio"` is included in the configuration
3. Check JSON syntax is valid
4. Restart VS Code completely (Cmd+Q / Alt+F4)

#### Server not starting:

1. Manually start the server:
   * Open Copilot Chat → gear icon → MCP Servers
   * Click gear icon next to BitoAIArchitect → Start Server
2. Check Node.js version: `node --version` (must be 20.18.1+)
3. View → Output → select "MCP" for error messages

#### Tools not showing in Copilot Chat:

1. Ensure server is started (see above)
2. Open Copilot Chat
3. Switch to Agent mode
4. Click Tools (wrench icon)
5. Verify BitoAIArchitect appears

#### Agent Mode not available:

1. Update VS Code to 1.99+
2. Settings → Search: `chat.agent.enabled`
3. Enable the checkbox

#### MCP discovery issues:

Ensure `settings.json` has:

```
"chat.mcp.discovery.enabled": true
```

**Note:** This must be a boolean `true`, NOT an object like `{"claude-desktop": true}`.

#### Node.js version too old:

Error: `ReferenceError: File is not defined` or similar

* Upgrade Node.js to 20.18.1 or later
* If using nvm: `nvm install 20 && nvm use 20 && nvm alias default 20`

#### Reset if needed:

* Ctrl/Cmd + Shift + P
* Run: `MCP: Reset Cached Tools`
* Restart VS Code

#### OAuth prompts appearing:

If VS Code is prompting for OAuth instead of using your Bearer token:

1. Ensure you're using the `mcp-remote` proxy configuration (not direct HTTP)
2. Verify `"type": "stdio"` is in your config
3. Cancel the OAuth prompt - the server should still work
4. Check that Node.js and npx are installed: `npx --version`
