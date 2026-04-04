# Source: https://help.aikido.dev/mcp/aikido-mcp.md

# Aikido MCP

The Aikido MCP Server connects Aikido’s security engine to AI coding tools that support [MCP](https://modelcontextprotocol.io/). It automatically scans AI generated code for vulnerabilities and hardcoded secrets as soon as it is created.

AI assistants can review their own output, but that review is not perfect. Aikido adds a reliable and consistent security layer that checks every generated snippet with proven scanning rules.<br>

**Why connect Aikido via MCP**

* Deterministic, independent security checks on every AI generated snippet before it is committed
* Immediate detection and remediation of vulnerabilities and hardcoded secrets in AI assisted workflows
* Real time feedback inside your IDE or agent environment, making AI driven development safer by default

## Available Tools

* **`aikido_full_scan`**: Runs a combined SAST + Secrets scan on provided files.&#x20;
* **`aikido_sast_scan`**: Runs a local SAST (static application security testing) scan on provided files
* **`aikido_secrets_scan`**: Runs a secrets-only scan on provided files&#x20;

## Installation

### Aikido IDE plugins

When the [Aikido IDE plugin](https://help.aikido.dev/ide-plugins) is installed you can use the Aikido Expansion Packs to install the Aikido MCP server with one click. [Learn more in the Expansion Packs docs.](https://help.aikido.dev/ide-plugins/features/aikido-expansion-packs)

{% hint style="warning" %}
Currently only available for VS Code and variants like Windsurf, Cursor, Kiro, ..
{% endhint %}

{% content-ref url="../ide-plugins/cursor-ide" %}
[cursor-ide](https://help.aikido.dev/ide-plugins/cursor-ide)
{% endcontent-ref %}

{% content-ref url="../ide-plugins/google-antigravity" %}
[google-antigravity](https://help.aikido.dev/ide-plugins/google-antigravity)
{% endcontent-ref %}

{% content-ref url="../ide-plugins/kiro-ide" %}
[kiro-ide](https://help.aikido.dev/ide-plugins/kiro-ide)
{% endcontent-ref %}

{% content-ref url="../ide-plugins/vs-code-plugin" %}
[vs-code-plugin](https://help.aikido.dev/ide-plugins/vs-code-plugin)
{% endcontent-ref %}

{% content-ref url="../ide-plugins/windsurf-ide" %}
[windsurf-ide](https://help.aikido.dev/ide-plugins/windsurf-ide)
{% endcontent-ref %}

### AI Platforms

{% content-ref url="anthropic-claude-code-mcp" %}
[anthropic-claude-code-mcp](https://help.aikido.dev/mcp/anthropic-claude-code-mcp)
{% endcontent-ref %}

{% content-ref url="openai-codex-cli-mcp" %}
[openai-codex-cli-mcp](https://help.aikido.dev/mcp/openai-codex-cli-mcp)
{% endcontent-ref %}

{% content-ref url="gemini-cli-mcp" %}
[gemini-cli-mcp](https://help.aikido.dev/mcp/gemini-cli-mcp)
{% endcontent-ref %}

{% content-ref url="jetbrains-ai" %}
[jetbrains-ai](https://help.aikido.dev/mcp/jetbrains-ai)
{% endcontent-ref %}

{% content-ref url="github-copilot" %}
[github-copilot](https://help.aikido.dev/mcp/github-copilot)
{% endcontent-ref %}

{% content-ref url="mistral-vibe-mcp" %}
[mistral-vibe-mcp](https://help.aikido.dev/mcp/mistral-vibe-mcp)
{% endcontent-ref %}

{% content-ref url="opencode-mcp" %}
[opencode-mcp](https://help.aikido.dev/mcp/opencode-mcp)
{% endcontent-ref %}

### Manual installation for other platforms

For any other AI platform or custom MCP setup, refer to the [npm package page for detailed manual installation instructions](https://www.npmjs.com/package/@aikidosec/mcp).

## Rules

Aikido IDE plugins will automatically add rules to every repository you open so the LLM's are aware of the MCP and use it during generation. For more information check out the docs below.&#x20;

{% content-ref url="../ide-plugins/features/automatically-handle-mcp-rules-in-ide" %}
[automatically-handle-mcp-rules-in-ide](https://help.aikido.dev/ide-plugins/features/automatically-handle-mcp-rules-in-ide)
{% endcontent-ref %}

## Demo

Demo of the Aikio MCP server working with an agent rule to scan and fix vulnerabilities in AI generated code:

{% embed url="<https://www.youtube.com/watch?v=D0ltRTSuKmk>" %}
