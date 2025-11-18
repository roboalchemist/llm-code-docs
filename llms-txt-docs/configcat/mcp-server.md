# Source: https://configcat.com/docs/advanced/mcp-server.md

# MCP Server

## Overview[​](#overview "Direct link to Overview")

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) is an open protocol that standardizes how applications provide context to large language models (LLMs). The ConfigCat MCP server lets you manage feature flags and configurations via the Public Management API seamlessly from AI tools. It also enables your code editor to understand your feature flags, integrate the appropriate ConfigCat SDK into your project or even create new feature flags directly in your codebase.

Your browser does not support the video tag. You can download the video here: [mcp-demo.mp4](https://configcat.com/docs/docs/assets/mcp/mcp-demo.mp4).

## Features[​](#features "Direct link to Features")

* Manage organizations, members and permissions
* Create and update products, configs, and environments
* Manage feature flags and settings
* Manage tags and user segments
* Connect with integrations and webhooks
* Track activity with audit logs and zombie flag (stale flag) reports
* Find code references linked to your features
* Integrate ConfigCat SDK and implement feature flags in your project

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Node.js](https://nodejs.org) version 16 or higher installed
* [Public Management API basic auth credentials](https://app.configcat.com/my-account/public-api-credentials) for ConfigCat MCP server created

## Setup[​](#setup "Direct link to Setup")

Supply your [Public Management API basic auth credentials](https://app.configcat.com/my-account/public-api-credentials).

The MCP server's configuration includes the following environment variables:

| Variable             | Required | Default                     | Description                         |
| -------------------- | -------- | --------------------------- | ----------------------------------- |
| `CONFIGCAT_API_USER` | ☑        | –                           | Management API basic auth username. |
| `CONFIGCAT_API_PASS` | ☑        | –                           | Management API basic auth password. |
| `CONFIGCAT_BASE_URL` |          | `https://api.configcat.com` | Override API host (rarely needed).  |

### Client Configuration[​](#client-configuration "Direct link to Client Configuration")

* Cursor
* Visual Studio Code
* Claude Desktop

1. Install [Cursor](https://cursor.com/)
2. Open **Preferences** → **Cursor Settings** → **MCP & Integrations**
3. Click **Add Custom MCP**
4. Add (or merge) the snippet below into your JSON settings:

```
{
  "mcpServers": {
    "ConfigCat": {
      "command": "npx",
      "args": ["-y", "@configcat/mcp-server"],
      "env": {
        "CONFIGCAT_API_USER": "YOUR_API_USER",
        "CONFIGCAT_API_PASS": "YOUR_API_PASSWORD"
      }
    }
  }
}
```

5. **Save** – the server will start on demand.
6. You can start writing prompts into Cursor's AI panel.

1) Install [VS Code](https://code.visualstudio.com/) and [GitHub Copilot](https://code.visualstudio.com/docs/copilot/setup)
2) Create a `.vscode/mcp.json` file in your project root with the following content:

```
{
  "servers": {
    "ConfigCat": {
      "command": "npx",
      "args": ["-y", "@configcat/mcp-server"],
      "env": {
        "CONFIGCAT_API_USER": "YOUR_API_USER",
        "CONFIGCAT_API_PASS": "YOUR_API_PASSWORD"
      }
    }
  }
}
```

3. Save the settings file. The MCP server should now be available in VS Code.
4. You can start writing prompts into VS Code's AI panel.

1) Install [Claude Desktop](https://claude.ai/download)
2) Open **Settings** → **Developer**
3) Click **Edit Config**
4) In `claude_desktop_config.json` add:

```
{
  "mcpServers": {
    "ConfigCat": {
      "command": "npx",
      "args": ["-y", "@configcat/mcp-server"],
      "env": {
        "CONFIGCAT_API_USER": "YOUR_API_USER",
        "CONFIGCAT_API_PASS": "YOUR_API_PASSWORD"
      }
    }
  }
}
```

5. **Save** & restart Claude Desktop.

info

Replace `YOUR_API_USER` and `YOUR_API_PASSWORD` environment variables with your [Public Management API basic auth credentials](https://app.configcat.com/my-account/public-api-credentials).

## Interaction[​](#interaction "Direct link to Interaction")

After you install the ConfigCat MCP server in your AI client, you can prompt your agent to create or manage your feature flags and configurations. Typically you need to click Run tool (or the equivalent option in your AI client) to execute the result.

For example, you could try asking

> Create a boolean feature flag called "my\_awesome\_feature" in the "Backend" config

or

> Turn the "my\_awesome\_feature" flag ON in all environments

or

> Update the "my\_awesome\_feature” flag in dev environment so it’s only enabled for users in Canada

or

> Create a new feature flag by cloning the configuration of the "my\_awesome\_feature" flag, and name it "my\_another\_awesome\_feature".

or

> Update the "my\_awesome\_feature" flag description: "When enabled, show my awesome feature.”

or

> List the stale feature flags that haven’t been modified in the past 6 days.

or

> Show who last modified the "myNewAwesomeFeature" flag, and to what.

or

> Invite sarah\@example.com to the "Main" product with "Administrators" permissions.

## See Also[​](#see-also "Direct link to See Also")

* [ConfigCat MCP server GitHub repository](https://github.com/configcat/mcp-server)
* [ConfigCat MCP server available tools](https://github.com/configcat/mcp-server?tab=readme-ov-file#available-tools)
* [Management API Reference](https://configcat.com/docs/docs/api/reference/configcat-public-management-api/.md)
* [How to Manage Feature Flags with ConfigCat's MCP Server - Blog post](https://configcat.com/blog/mcp-server-feature-flags/)
