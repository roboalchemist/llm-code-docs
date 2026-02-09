# Source: https://docs.bito.ai/ai-architect/guide-for-cursor.md

# Guide for Cursor

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **Cursor** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Cursor can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

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

Follow the setup instructions for your operating system:

* [**Windows**](#windows)
* [**macOS/Linux**](#macos-linux)

## Windows

{% stepper %}
{% step %}

### Create Cursor config directory

1. Press `Win + R`
2. Type: `%USERPROFILE%\.cursor`
3. Press Enter

If the folder doesn't exist, create it:

1. Open File Explorer
2. Navigate to `%USERPROFILE%`
3. Create new folder: `.cursor`
   {% endstep %}

{% step %}

### Create or edit mcp.json

1. Open `%USERPROFILE%\.cursor\mcp.json` in a text editor.
2. If the file doesn't exist, create it with this content:

```json
{
  "mcpServers": {
    "BitoAIArchitect": {
      "url": "<Your-Bito-MCP-URL>",
      "headers": {
        "Authorization": "Bearer <Your-Bito-MCP-Access-Token>",
        "x-email-id": "<Your-Email>"
      }
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

3. If the file exists with other servers, add `BitoAIArchitect` to the `mcpServers` object:

```json
{
  "mcpServers": {
    "existing-server": {
      ...
    },
    "BitoAIArchitect": {
      "url": "<Your-Bito-MCP-URL>",
      "headers": {
        "Authorization": "Bearer <Your-Bito-MCP-Access-Token>",
        "x-email-id": "<Your-Email>"
      }
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
  {% endstep %}

{% step %}

### Add guidelines (optional but highly recommended)

The [**BitoAIArchitectGuidelines.md** file](#prerequisites) contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server.

The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

1. In your project root, create `.cursorrules` file.
2. Open this file with a text editor.
3. Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `.cursorules` file.
4. Save.
   {% endstep %}

{% step %}

### Restart Cursor

1. Close Cursor completely
2. Reopen Cursor
3. Open **Settings → Tools & MCP**
4. Verify `BitoAIArchitect` appears in the MCP servers list
   {% endstep %}
   {% endstepper %}

## macOS/Linux

{% stepper %}
{% step %}

### Create Cursor config directory

```shellscript
mkdir -p ~/.cursor
```

{% endstep %}

{% step %}

### Create or edit mcp.json

```
nano ~/.cursor/mcp.json
```

Add this content:

```json
{
  "mcpServers": {
    "BitoAIArchitect": {
      "url": "<Your-Bito-MCP-URL>",
      "headers": {
        "Authorization": "Bearer <Your-Bito-MCP-Access-Token>",
        "x-email-id": "<Your-Email>"
      }
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

Save and exit (Ctrl+O, Enter, Ctrl+X)
{% endstep %}

{% step %}

### Add guidelines (optional but highly recommended)

The [**BitoAIArchitectGuidelines.md** file](#prerequisites) contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server.

The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

1. In your project root, create `.cursorrules` file.
2. Open this file with a text editor.
3. Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `.cursorules` file.
4. Save.
   {% endstep %}

{% step %}

### Restart Cursor

1. Close Cursor completely
2. Reopen Cursor
3. Open **Settings → Tools & MCP**
4. Verify `BitoAIArchitect` appears in the MCP servers list
   {% endstep %}
   {% endstepper %}

## Troubleshooting Cursor

#### Server not showing:

```shellscript
# Verify file location
ls -la ~/.cursor/mcp.json

# Check file permissions
chmod 644 ~/.cursor/mcp.json

# Verify JSON syntax
cat ~/.cursor/mcp.json | python -m json.tool
```

#### Connection errors:

* Verify **Bito MCP URL** and **Bito MCP Access Token** are correct.
* Test endpoint with MCP protocol:

```shellscript
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

* Check **Settings → Tools & MCP** for error messages
