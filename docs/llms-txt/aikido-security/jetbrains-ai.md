# Source: https://help.aikido.dev/mcp/jetbrains-ai.md

# Jetbrains AI

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

The Aikido JetBrains IDE plugin uses [Expansion Packs](https://help.aikido.dev/ide-plugins/features/aikido-expansion-packs) to provide additional features. The Aikido MCP for Jetbrains AI is one of these Expansion Packs, making installation simple and fast without a separate setup process. See the linked page below for instructions on how to enable it.

{% content-ref url="../ide-plugins/jetbrains-ide-plugins" %}
[jetbrains-ide-plugins](https://help.aikido.dev/ide-plugins/jetbrains-ide-plugins)
{% endcontent-ref %}
