# Source: https://docs.datadoghq.com/feature_flags/feature_flag_mcp_server.md

---
title: Feature Flags MCP Server
description: Learn how to use the Feature Flags toolset in the Datadog MCP Server
breadcrumbs: Docs > Feature Flags > Feature Flags MCP Server
---

# Feature Flags MCP Server

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Feature Flags are in Preview. Complete the form to request access.

[Request Access](http://datadoghq.com/product-preview/feature-flags/)
{% /callout %}

## Overview{% #overview %}

The Datadog MCP Server uses the Model Context Protocol (MCP) to provide AI agents with access to [Feature Flags](https://docs.datadoghq.com/feature_flags/) management capabilities, including flag creation, configuration, and React/JavaScript integration guidance.

## Setup{% #setup %}

The following configurations give your AI agent access to the Feature Flags toolset in the Datadog MCP Server. You must restart your agent after performing this setup.

For all clients, install the MCP Server binary:

```bash
curl -sSL https://coterm.datadoghq.com/mcp-cli/install.sh | bash
```

Then follow the instructions below to add the MCP Server to your specific client.

### Claude Code{% #claude-code %}

```bash
claude mcp add datadog -- ~/.local/bin/datadog_mcp_cli --endpoint-path /api/unstable/mcp-server/mcp?toolsets=feature-flags
```

### Cursor{% #cursor %}

Add this to `~/.cursor/mcp.json` (remember to save the file):

```json
{
  "mcpServers": {
    "datadog-ff": {
      "type": "stdio",
      "command": "~/.local/bin/datadog_mcp_cli --endpoint-path /api/unstable/mcp-server/mcp?toolsets=feature-flags",
      "args": [],
      "env": {}
    }
  }
}
```

## Use cases{% #use-cases %}

The MCP Server includes tools to help you manage feature flags in your codebase. The following use cases provide sample prompts for using the tools.

{% alert level="info" %}
The MCP Server only supports React applications.
{% /alert %}

### Create feature flags{% #create-feature-flags %}

Use the `create-feature-flag` tool to create feature flags. You do not need to specify the tool name in the prompt, but it can provide more consistent results. The MCP Server has access to Datadog's documentation and uses it to implement the flag in your codebase.

If you do not yet have feature flags implemented, mention in the prompt that you want to implement Datadog feature flags.

Example prompts:

- Use the `create-feature-flag` tool to create a flag to control the title on the main page.
- I want to show a confirmation modal when `<SOME_EVENT>` happens. Use a Datadog feature flag to control whether the confirmation modal is shown.

### Check feature flag implementation{% #check-feature-flag-implementation %}

Use the `check-flag-implementation` tool to check if a feature flag is implemented correctly.

The tool checks that the flag is being referenced as the correct value type, is passing the correct subject attributes, and is providing the correct default value that agrees with the default in production environments.

Example prompts:

- Check if the `show-confirmation-modal` flag is implemented correctly.
- Check if all feature flags in `/some/directory` are implemented correctly.

**Note**: This may not find all issues. Checking flags individually is more reliable.

This tool can also be used to add feature flags created in the UI to your codebase. For example:

- Use the `show-confirmation-modal` flag to control whether the confirmation modal is shown when `<SOME_EVENT>` happens.

### List feature flags{% #list-feature-flags %}

Use the `list-feature-flags` tool to list all feature flags. For example:

- List all feature flags.

### List environments{% #list-environments %}

Use the `list-environments` tool to list all environments. For example:

- List my flagging environments.

### Update feature flag environments{% #update-feature-flag-environments %}

Use the `update-feature-flag-environment` tool to update a feature flag environment. This tool can control the default variants, and enable or disable the flag. It cannot modify flags in production environments.

Example prompts:

- I want `show-confirmation-modal` to serve true in development.
- Disable `show-confirmation-modal` in staging.

## Further reading{% #further-reading %}

- [Getting Started with Feature Flags](https://docs.datadoghq.com/getting_started/feature_flags)
- [Datadog MCP Server](https://docs.datadoghq.com/bits_ai/mcp_server)
