# Source: https://help.aikido.dev/mcp/github-copilot.md

# Github Copilot

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

### IDE

The Aikido VSCode IDE plugin uses [Expansion Packs](https://help.aikido.dev/ide-plugins/features/aikido-expansion-packs) to provide additional features. The Aikido MCP for Github Copilot is one of these Expansion Packs, making installation simple and fast without a separate setup process. See the linked page below for instructions on how to enable it.

{% content-ref url="../ide-plugins/vs-code-plugin" %}
[vs-code-plugin](https://help.aikido.dev/ide-plugins/vs-code-plugin)
{% endcontent-ref %}

### Integration with Copilot Agents

GitHub Copilot coding agent can call tools from MCP servers while it runs. Follow the steps below to set up Aikido MCP for your repository. Configuration is done per repository.&#x20;

If you already use Aikido MCP in VS Code, [you can reuse that configuration](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp#reusing-your-mcp-configuration-from-visual-studio-code) and only add the token in your repository settings.

#### Set-up Instructions

{% hint style="info" %}
For the full GitHub flow (where to paste JSON, how validation works, and how Copilot environments expose secrets), [check out GitHub’s guide](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp).
{% endhint %}

{% stepper %}
{% step %}

#### Create an Aikido MCP token

In Aikido, go to [MCP Integration page](https://app.aikido.dev/settings/integrations/ide/mcp) and create a Personal Access Token.&#x20;
{% endstep %}

{% step %}

#### Add the token to your Copilot environment

Github Copilot only exposes secrets/variables to MCP config if their names start with `COPILOT_MCP_`

Create a secret like:

`COPILOT_MCP_AIKIDO_API_KEY` = your Aikido token
{% endstep %}

{% step %}

#### Add the MCP configuration in your repo settings

In your GitHub repository, go to Settings → Copilot → Coding agent and paste an MCP JSON config.&#x20;

Example configuration for Aikido MCP (local/stdio via npx):

```json
{
  "mcpServers": {
    "aikido": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@aikidosec/mcp"],
      "tools": ["aikido_full_scan", "aikido_sast_scan", "aikido_secrets_scan"],
      "env": {
        "AIKIDO_API_KEY": "COPILOT_MCP_AIKIDO_API_KEY"
      }
    }
  }
}
```

{% endstep %}

{% step %}

#### Add custom prompt instructions

To ensure GitHub Copilot uses the MCP server, configure repository instructions as [described in the GitHub guide](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions).

Add an instruction such as:

```
Scan any new or modified code with `aikido_full_scan` before finalizing changes. This security check is required.
```

{% endstep %}

{% step %}

#### Validate

You can now [verify your configuration](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp#validating-your-mcp-configuration) by asking Copilot to security scan one of your files.
{% endstep %}
{% endstepper %}
