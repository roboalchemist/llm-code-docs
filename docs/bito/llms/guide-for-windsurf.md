# Source: https://docs.bito.ai/ai-architect/guide-for-windsurf.md

# Guide for Windsurf

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **Windsurf** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Windsurf can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

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

### Create Windsurf config directory

1. Press **Win + R**
2. Type: `%USERPROFILE%\.codeium\windsurf`
3. Press **Enter**

If the folders don't exist, create them:

1. Open File Explorer
2. Navigate to `%USERPROFILE%`
3. Create folders: `.codeium\windsurf`
   {% endstep %}

{% step %}

### Create or edit mcp\_config.json

1. Open `%USERPROFILE%\.codeium\windsurf\mcp_config.json` in a text editor.
2. If the file doesn't exist, create it with this content:

```json
{
  "mcpServers": {
    "BitoAIArchitect": {
      "serverUrl": "<Your-Bito-MCP-URL>",
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
      "serverUrl": "<Your-Bito-MCP-URL>",
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

4. Save
   {% endstep %}

{% step %}

### Add guidelines (optional but highly recommended)

The [**BitoAIArchitectGuidelines.md** file](#prerequisites) contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server.

The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

#### Option A: Global guidelines (applies to all projects):

Create directory:

```shellscript
mkdir %USERPROFILE%\.codeium\windsurf\memories
```

Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `global_rules.md` file:

```shellscript
copy BitoAIArchitectGuidelines.md %USERPROFILE%\.codeium\windsurf\memories\global_rules.md
```

#### Option B: Project-level guidelines (applies to specific project):

In your project directory, create `.windsurf\rules` directory:

```shellscript
mkdir .windsurf\rules
```

Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `bitoai-architect.md` file:

```shellscript
copy BitoAIArchitectGuidelines.md .windsurf\rules\bitoai-architect.md
```

{% hint style="info" %}
**Note:** Windsurf Wave 8+ uses `.windsurf\rules\*.md` format for project-level rules. Global guidelines in `~/.codeium/windsurf/memories/global_rules.md` are supported in all versions.
{% endhint %}
{% endstep %}

{% step %}

### Restart Windsurf

1. Close Windsurf completely
2. Reopen Windsurf
3. Open **Settings → Cascade → MCP Servers**
4. Click "Refresh"
5. Verify `BitoAIArchitect` appears with green status
   {% endstep %}
   {% endstepper %}

## macOS/Linux

{% stepper %}
{% step %}

### Create Windsurf config directory

```shellscript
mkdir -p ~/.codeium/windsurf
```

{% endstep %}

{% step %}

### Create or edit mcp\_config.json

```shellscript
nano ~/.codeium/windsurf/mcp_config.json
```

Add this content:

```json
{
  "mcpServers": {
    "BitoAIArchitect": {
      "serverUrl": "<Your-Bito-MCP-URL>",
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

#### Option A: Global guidelines (applies to all projects):

Create directory:

```shellscript
mkdir -p ~/.codeium/windsurf/memories
```

Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `global_rules.md` file:

```shellscript
cp BitoAIArchitectGuidelines.md ~/.codeium/windsurf/memories/global_rules.md
```

#### Option B: Project-level guidelines (applies to specific project):

In your project directory, create `.windsurf/rules` directory:

```shellscript
mkdir -p .windsurf/rules
```

Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `bitoai-architect.md` file:

```shellscript
cp BitoAIArchitectGuidelines.md .windsurf/rules/bitoai-architect.md
```

{% hint style="info" %}
**Note:** Windsurf Wave 8+ uses `.windsurf/rules/*.md` format for project-level rules. Global guidelines in `~/.codeium/windsurf/memories/global_rules.md` are supported in all versions.
{% endhint %}
{% endstep %}

{% step %}

### Restart Windsurf

1. Close Windsurf completely
2. Reopen Windsurf
3. Open **Settings → Cascade → MCP Servers**
4. Click "Refresh"
5. Verify `BitoAIArchitect` appears with green status
   {% endstep %}
   {% endstepper %}

## Troubleshooting Windsurf

#### Server not showing:

```shellscript
# Verify file location
ls -la ~/.codeium/windsurf/mcp_config.json

# Check permissions
chmod 755 ~/.codeium/windsurf
chmod 644 ~/.codeium/windsurf/mcp_config.json

# Verify JSON syntax
cat ~/.codeium/windsurf/mcp_config.json | python -m json.tool
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

* Check **Settings → Cascade → MCP Servers** for error messages.
