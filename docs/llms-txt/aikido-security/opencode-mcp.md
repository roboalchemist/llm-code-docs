# Source: https://help.aikido.dev/mcp/opencode-mcp.md

# OpenCode MCP

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

### Add Aikido MCP server to your OpenCode config

Open or create `~/.config/opencode/opencode.json` and add the following to the file under `mcp`

```shellscript
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "aikido": {
      "type": "local",
      "command": ["npx", "-y", "@aikidosec/mcp"],
      "enabled": true,
      "environment": {
        "AIKIDO_API_KEY": "YOUR_TOKEN",
      },
    },
  },
}
```

Replace `YOUR_TOKEN` with the token from the previous step.
{% endstep %}

{% step %}

### Add the Aikido rule to Global AGENTS file

Create the vibe prompts directory if it doesn't exist yet.

```shellscript
mkdir -p ~/.config/opencode/skill/aikido/
```

Download the Aikido rule and add it to `~/.vibe/prompts/aikido-rule.txt`.

```shellscript
curl -fsSL "https://gist.githubusercontent.com/kidk/1d2c1e754d5a5ddd05c9966d2507ae42/raw/ea8183c0ae1af5ec9bcb8b93275145adbe936c20/aikido-skill.txt" \
  -o ~/.config/opencode/skill/aikido/SKILL.md
```

{% endstep %}

{% step %}

### Finished

Aikido MCP is now available in OpenCode.

{% hint style="info" %}
Restart OpenCode if it was open.
{% endhint %}
{% endstep %}
{% endstepper %}
