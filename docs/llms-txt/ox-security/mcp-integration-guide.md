# Source: https://docs.ox.security/vibesec/model-context-protocol/mcp-integration-guide.md

# MCP Integration Guide

This guide explains how to integrate OX Security with your IDE using an [MCP server](https://docs.ox.security/vibesec/model-context-protocol). It includes setup for the following:

* [MCP Integration key](#creating-a-new-mpc-integration-key)
* [Cursor integration with OX MCP](#integrating-cursor-with-ox-mcp)
* [Claude Desktop integration with OX MCP](#integrating-claude-desktop-with-ox-mpc)
* [VS Code integration with OX MCP](#integrating-visual-studio-code-with-ox-mpc)

## Creating a new MCP integration key

To integrate with the MCP server, you need to create an integration key.

**To create a new MCP integration key:**

1. From the left pane of the **OX dashboard**, select **Settings > API Key Settings**.
2. In the **API Key Settings** window, select **CREATE API KEY**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ed087c212916d7e7389e378bbd03ea6c662ddbac%2FMPC%20integration%20key.png?alt=media" alt="" width="360"><figcaption></figcaption></figure>

1. In the **Create API Key** box set the following:

| Parameter           | Description                                                                                                                                                                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **API Key Name**    | A descriptive name for the API key to identify its purpose MCP key 1                                                                                                                                                                                                       |
| **API Key Type**    | Select **MCP Integration**                                                                                                                                                                                                                                                 |
| **Assign role**     | Assign a role according to your permissions needs. Example: **Admin** for full access. **Operator** for limited access to specific actions.                                                                                                                                |
| **Assign scopes**   | <p>Defines which applications and issues the API key can access:</p><ul><li><strong>Entire organization:</strong> Access to all applications and issues in the organization.</li><li><strong>Custom:</strong> Access restricted to specific applications/issues.</li></ul> |
| **Expiration Date** | The date and time when the API key will expire and no longer be valid.                                                                                                                                                                                                     |

1. Copy the **API Key Secret** to be used when connecting to APIs. Save the key in a safe location. This is the only time when you can see and copy the actual key.
2. Select **CLOSE**. The new key appears in the **API Key Settings** page.

## Integrating Cursor with OX MCP

By integrating with OX’s MCP, Cursor becomes a security-aware development assistant, able to query live security data, suggest actions, and triage issues directly from your IDE

**To integrate Cursor with OX MCP:**

1\. Click [here](cursor://anysphere.cursor-deeplink/mcp/install?name=ox-security\&config=eyJ1cmwiOiJodHRwczovL2FwaS5jbG91ZC5veC5zZWN1cml0eS9hcGkvbWNwIiwiaGVhZGVycyI6eyJBdXRob3JpemF0aW9uIjoiUEFTVEVfWU9VUl9BUElfVE9LRU5fSEVSRSJ9fQ%3D%3D), to open Cursor in the relevant location where you can start working.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3291943584292074739b143b39f69bd0e6fa3997%2FCursor1.png?alt=media" alt=""><figcaption></figcaption></figure>

1. In the authorization header, replace the placeholder value with the [MCP Integration key that you saved](#creating-a-new-mpc-integration-key).
2. Click **Install**.

In the Cursor tools menu, OX Security logo appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5067db4e36ccb61a04570fd7d7c92234d0ea7ece%2FCursor2.png?alt=media" alt=""><figcaption></figcaption></figure>

More info: [Cursor Documentation](https://docs.cursor.com/en/tools/developers).

## Integrating Claude Desktop with OX MCP

Claude Desktop offers an intuitive interface for integrating with OX Security's MCP, providing teams with robust security capabilities directly from their desktop environment.

> **Note:** Ensure Node.js v18+ is installed. If using `nvm`, make sure no versions lower than 18.x are active.

**To integrate Claude Desktop with OX MCP:**

1. In Claude Desktop, go to **Settings** > **Developer**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2c38ac78f90dc26e530b97e6add13c2ef6220abf%2FClaude%20Desktop1.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **Edit Config**.

Claude automatically opens the configuration file `claude_desktop_config.json`

1. Add the JSON MCP server configuration for OX Security as provided by your administrator or documentation.

```
{
  "mcpServers": {
    "ox-security": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://api.cloud.ox.security/api/mcp",
        "--header",
        "Authorization:PASTE_YOUR_API_TOKEN_HERE"
      ]
    }
  }
```

1. Replace `PASTE_YOUR_API_TOKEN_HERE` with the [MCP Integration key that you saved](#creating-a-new-mpc-integration-key).
2. Save the file and restart Claude Desktop.

After restart, OX Security appears as an available MCP server in Claude Desktop.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a6d21a824fb18ab5b953d1a223ca1ae240f6d370%2FClaude%20Desktop2.png?alt=media" alt="" width="532"><figcaption></figcaption></figure>

#### Troubleshooting (Windows)

In case you have issues setting up MCP servers in Windows, consider using alternative commands, such as `npx.cmd` or direct Node.js execution.

**Use `npx.cmd`:**

```json
{
  "mcpServers": {
    "ox-security": {
      "command": "npx.cmd",
      "args": [
        "-y",
        "mcp-remote@0.1.18",
        "https://api.cloud.ox.security/api/mcp",
        "--header",
        "Authorization:${AUTH_TOKEN}"
      ],
      "env": {
        "AUTH_TOKEN": "PASTE_YOUR_API_TOKEN_HERE"
      }
    }
  }
}
```

**Run Node.js directly:**

1. Install MCP Remote globally:

   ```bash
   npm install -g mcp-remote@0.1.2
   ```

2. Update your config with your local Node.js path:

```json
{
  "mcpServers": {
    "ox-security": {
      "command": "C:\YOUR_NODE_INSTALL_FOLDER\node.exe",
      "args": [
        "YOUR_MCP_REMOTE_FOLDER\node_modules\mcp-remote\dist\client.js",
        "https://api.cloud.ox.security/api/mcp",
        "--header",
        "Authorization:${AUTH_TOKEN}"
      ],
      "env": {
        "AUTH_TOKEN": "PASTE_YOUR_API_TOKEN_HERE"
      }
    }
  }
}
```

## Integrating Visual Code with OX MCP

Visual Studio Code provides versatile options to connect with OX Security's MCP, enabling developers to streamline their security workflows within the versatile VS Code ecosystem.

**To integrate VS Code with OX MCP:**

1. Open **VS Code Settings**.
2. Open **MCP User Configuration**, see [VS Code MCP Docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for details.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-10b8d3a1a223661db9412972b251935c45228a87%2FVS1.png?alt=media" alt="" width="449"><figcaption></figcaption></figure>

1. Add the JSON MCP server configuration for OX Security in `mcp.json`:

```json
{
  "servers": {
    "ox-security": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://api.cloud.ox.security/api/mcp",
        "--header",
        "Authorization:PASTE_YOUR_API_TOKEN_HERE"
      ]
    }
  }
```

1. Replace `PASTE_YOUR_API_TOKEN_HERE` with the [MCP Integration key that you saved](#creating-a-new-mpc-integration-key).
2. Save the configuration.
3. In the **VS Code chat**, click **Add Context**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8aed8e4e136f0e8339e2098e1136b3d4b593ba12%2FVS2.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select the desired tools.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ece98043cb07eae67b96e5f6197a6b85af10edea%2FVS3.png?alt=media" alt=""><figcaption></figcaption></figure>

OX Security appears as an available MCP server.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2c45ac35e40e84d52186fd51704a6a7edaee814e%2FVS4.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6f310dacb1b01293df9204be14b53191a1260b7d%2FVS5.png?alt=media" alt=""><figcaption></figcaption></figure>
