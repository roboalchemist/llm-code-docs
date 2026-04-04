# Source: https://docs.bito.ai/ai-architect/guide-for-jetbrains-ai-assistant.md

# Guide for JetBrains AI Assistant

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **JetBrains AI Assistant** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), JetBrains AI Assistant can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

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
3. **JetBrains IDE**: IntelliJ IDEA 2025.1+ (or PyCharm, WebStorm, PhpStorm, etc. 2025.1+)
4. **AI Assistant Plugin (version 251.26094.80.5 or higher)**
   1. Open your JetBrains IDE
   2. Go to: **Settings** (Ctrl/Cmd + Alt + S)
   3. Navigate to: **Plugins**
   4. Search for "AI Assistant"
   5. Verify version is 251.26094.80.5 or higher
5. **Node.js**: **20.18.1+** installed (for mcp-remote proxy)
   1. **Why Node.js 20+?** The mcp-remote proxy depends on undici v7, which requires Node.js 20+ (needs the `File` global API added in Node 20.0.0). Node.js 18 and earlier will fail with `ReferenceError: File is not defined`.
   2. Verify:

      ```shellscript
      node --version  # Should show v20.x.x or higher
      npx --version
      ```
   3. If Node.js is not installed or the version < 20 then [download Node.js 20.x LTS](https://nodejs.org/)

## Set up AI Architect <a href="#set-up-ai-architect" id="set-up-ai-architect"></a>

JetBrains AI Assistant has the same setup process across all platforms (Windows, macOS, Linux, WSL).

{% stepper %}
{% step %}

### Access MCP settings

1. Open your JetBrains IDE (IntelliJ IDEA, PyCharm, WebStorm, etc.)
2. Go to: **Settings** (Ctrl/Cmd + Alt + S)
3. Navigate to: **Tools** → **AI Assistant** → **Model Context Protocol (MCP)**
4. Click **Add** to add a new MCP server
   {% endstep %}

{% step %}

### Configure `BitoAIArchitect`

The configuration dialog accepts JSON input. Paste the appropriate JSON configuration for your platform:

#### **macOS/Linux configuration:**

```json
{
  "mcpServers": {
    "BitoAIArchitect": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "<Your-Bito-MCP-URL>",
        "--header",
        "Authorization:${AUTH_HEADER}",
        "--header",
        "x-email-id: <Your-Email>"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <Your-Bito-MCP-Access-Token>"
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

#### **Windows configuration (IMPORTANT - uses cmd):**

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
        "<Your-Bito-MCP-URL>",
        "--header",
        "Authorization:${AUTH_HEADER}",
        "--header",
        "x-email-id: <Your-Email>"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <Your-Bito-MCP-Access-Token>"
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

### Save and restart

1. Click **OK** to save the MCP server configuration
2. Click **OK** to close Settings
3. Restart your IDE completely
   {% endstep %}

{% step %}

### Verify connection

1. Go to: **Settings** → **Tools** → **AI Assistant** → **Model Context Protocol (MCP)**
2. Find `BitoAIArchitect` in the list
3. Check the **Status** column - should show **Running** or **Connected**
   {% endstep %}

{% step %}

### Enable Codebase Mode

**IMPORTANT**: MCP tools only work in "Codebase" mode or Edit mode.

To use `BitoAIArchitect`:

1. Open JetBrains AI Assistant chat
2. Toggle on the **"Codebase"** mode switch at the top of the chat window
3. OR use Edit mode (Ctrl/Cmd + Shift + Enter), which implicitly enables codebase context
   {% endstep %}

{% step %}

### Add guidelines (optional but highly recommended)

The [**BitoAIArchitectGuidelines.md** file](#prerequisites) contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server.

The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

To add Bito AI Architect usage rules to a specific project:

1. Navigate to your project root
2. Create `.aiassistant/rules/` directory:

   ```shellscript
   mkdir -p .aiassistant/rules
   ```
3. Create a rule file (e.g., `bitoai-architect.md`):

   Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `.aiassistant/rules/bitoai-architect.md` file:

   ```shellscript
   cp /path/to/BitoAIArchitectGuidelines.md .aiassistant/rules/bitoai-architect.md
   ```
4. In your IDE: **Settings** → **Tools** → **AI Assistant** → **Rules**
5. The rule file should appear automatically
6. Configure how it should be applied:
   * **Always**: Applied to all chats automatically
   * **Manually**: Invoked using `@rule:bitoai-architect`
   * **By Model Decision**: AI decides when to apply
   * **By File Patterns**: Applied when specific files are open

**What AI Assistant rules should contain:**

* `BitoAIArchitect` MCP usage instructions
* When to query organizational repositories
* How to search for dependencies and tech stacks
  {% endstep %}
  {% endstepper %}

## Troubleshooting

#### JetBrains AI Assistant not showing MCP settings:

1. Verify IDE version is 2025.1 or later
2. Verify AI Assistant plugin is version 251.26094.80.5+
3. Update both if needed

#### `BitoAIArchitect` not appearing or showing "Not started":

1. Verify Node.js is installed: `node --version`
2. Check that you've toggled "Codebase" mode ON in the chat
3. On Windows, ensure you're using `cmd` command (not `npx` directly)
4. Restart the IDE completely
5. Check IDE logs for errors: **Help** → **Show Log in Explorer/Finder**
   * Look for files in the `mcp` folder

#### Connection errors:

1. **Test the endpoint manually:**

```shellscript
# Use proper MCP protocol to test authentication
curl -s -X POST \
  -H "Authorization: Bearer <Your-Bito-MCP-Access-Token>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}' \
  <Your-Bito-MCP-URL>
```

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
  {% endhint %}

2. Verify your **Bito MCP URL** and **Bito MCP Access Token** are correct
3. Check firewall settings
4. Verify the `--header` argument format: `Authorization:${AUTH_HEADER}` (colon, no space)

#### Windows-specific issues:

1. Verify the JSON uses `"command": "cmd"` (not `npx`)
2. Ensure `"/c"` is the first element in the `args` array
3. Node.js must be in system PATH
