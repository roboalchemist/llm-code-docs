# Source: https://help.aikido.dev/mcp/gemini-cli-mcp.md

# Gemini CLI MCP

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

{% stepper %}
{% step %}

### Create a personal access token

In Aikido, go to [Settings → Integrations → IDE → MCP](https://app.aikido.dev/settings/integrations/ide/mcp)

Create a Personal Access Token.
{% endstep %}

{% step %}

### Install the Aikido MCP server

```shellscript
gemini mcp add aikido \
  --env AIKIDO_API_KEY=YOUR_TOKEN \
  npx -y @aikidosec/mcp
```

Replace `YOUR_TOKEN` with the token from the previous step.
{% endstep %}

{% step %}

### Add the Aikido rule to Global AGENTS file

Create the gemini directory if it doesn't exist yet.

```shellscript
mkdir -p ~/.gemini/skills/
```

Download the Aikido rule and add it to `~/.gemini/skills/aikido-rule.txt`.

```shellscript
curl -fsSL "https://gist.githubusercontent.com/kidk/aa48cad6db80ba4a38493016aae67712/raw/3644397b7df43423e3da06434491b40bbb79dd47/aikido-rule.txt" \
  -o ~/.gemini/skills/aikido-rule.txt
```

{% endstep %}

{% step %}

### Finished

Aikido MCP is now available in Gemini CLI.

{% hint style="info" %}
Restart Gemini CLI if it was open.
{% endhint %}
{% endstep %}
{% endstepper %}
