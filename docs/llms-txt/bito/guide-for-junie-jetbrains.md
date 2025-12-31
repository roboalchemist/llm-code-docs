# Source: https://docs.bito.ai/ai-architect/guide-for-junie-jetbrains.md

# Guide for Junie (JetBrains)

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **Junie (JetBrains)** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Junie can leverage AI Architect’s deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Follow the [**AI Architect installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted). Upon successful setup, you will receive a **Bito MCP URL** and **Bito MCP Access Token** that you need to enter in your coding agent.
2. [Download **BitoAIArchitectGuidelines.md** file](https://github.com/gitbito/ai-architect/blob/main/BitoAIArchitectGuidelines.md). You will need to copy/paste the content from this file later when configuring AI Architect.
   * **Note:** This file contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server. The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.
3. **Junie installed in a JetBrains IDE** (IntelliJ IDEA, PyCharm, WebStorm, etc.)
4. **Node.js 20.18.1+** installed (for `mcp-remote` proxy)
   1. **Why Node.js 20+?** The mcp-remote proxy depends on undici v7, which requires Node.js 20+ (needs the `File` global API added in Node 20.0.0). Node.js 18 and earlier will fail with `ReferenceError: File is not defined`.
   2. **Verify:**

      ```shellscript
      node --version  # Should show v20.x.x or higher
      npx --version
      ```
   3. If Node.js is not installed or the version < 20 then [download Node.js 20.x LTS](https://nodejs.org/)

## Set up AI Architect <a href="#set-up-ai-architect" id="set-up-ai-architect"></a>

Junie has the same setup process across all platforms (Windows, macOS, Linux, WSL).

{% stepper %}
{% step %}

### Access Junie MCP settings

1. Open your JetBrains IDE (IntelliJ, PyCharm, etc.)
2. Go to: **Settings** (Ctrl/Cmd + Alt + S)
3. Navigate to: **Tools** → **Junie** → **MCP Settings**
4. Click the **+** (Add) button to open the global `mcp.json` configuration file in the editor, or manually edit the file as shown below
   {% endstep %}

{% step %}

### Configure `BitoAIArchitect`

The global configuration file is located at:

* **macOS/Linux**: `~/.junie/mcp/mcp.json`
* **Windows**: `%USERPROFILE%\.junie\mcp\mcp.json`

**macOS/Linux configuration:**

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
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <Your-Bito-MCP-Access-Token>"
      }
    }
  }
}
```

**Windows configuration (IMPORTANT - uses cmd /c):**

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
        "Authorization:${AUTH_HEADER}"
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
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
  {% endhint %}
  {% endstep %}

{% step %}

### Save and restart

1. Save the `mcp.json` file
2. Close all JetBrains IDE windows
3. Reopen your IDE
   {% endstep %}

{% step %}

### Verify connection

1. Go to: **Settings** → **Tools** → **Junie** → **MCP Settings**
2. Check that `BitoAIArchitect` appears in the server list
3. Status should show as **Connected** or **Running**
   {% endstep %}

{% step %}

### Add guidelines (optional but highly recommended)

The [**BitoAIArchitectGuidelines.md** file](#prerequisites) contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server.

The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.

To add Bito AI Architect usage guidelines to a specific project:

1. Navigate to your project root
2. Create `.junie` directory:

   ```shellscript
   mkdir -p .junie
   ```

   Copy the contents of your [**BitoAIArchitectGuidelines.md** file](#prerequisites) into `.junie/guidelines.md` file:

   ```shellscript
   cp /path/to/BitoAIArchitectGuidelines.md .junie/guidelines.md
   ```
3. Junie will automatically use these guidelines for the project

**What Junie guidelines should contain:**

* `BitoAIArchitect` MCP usage best practices
* When to query repository information
* How to search for dependencies and tech stacks
  {% endstep %}
  {% endstepper %}

## Troubleshooting

#### Junie not showing `BitoAIArchitect`:

1. Verify Node.js is installed: `node --version`
2. Check `mcp.json` syntax (must be valid JSON)
3. On Windows, ensure you're using `cmd` with `/c` argument
4. Restart the IDE completely

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
* Replace `<Your-Bito-MCP-Access-Token>` with the **Bito MCP Access Token** you received after completing the AI Architect setup.
  {% endhint %}

2. Verify your **Bito MCP URL** and **Bito MCP Access Token** are correct
3. Check firewall settings
