# Source: https://docs-containers.back4app.com/docs/mcp.md

---
title: Model Context Protocol (MCP)
slug: docs/mcp
description: Unlock the potential of Large Language Models (LLMs) with the Model Context Protocol (MCP) in this comprehensive guide. Learn how to seamlessly integrate AI tools like Cursor, Windsurf, and Visual Studio Code with Back4App. Discover step-by-step instructi
createdAt: 2025-04-29T20:19:47.638Z
updatedAt: 2025-06-24T14:36:39.025Z
---

The Model Context Protocol (MCP) is a standard for connecting Large Language Models (LLMs) to platforms like Back4App. This guide covers how to connect Back4App to the following AI tools using MCP:

- Cursor
- Windsurf (Codium)
- Visual Studio Code (Copilot)
- Cline (VS Code extension)
- Claude desktop
- Claude code

Once connected, your AI assistants can interact with and query your Back4App projects on your behalf.

:::hint{type="warning"}
AI agents with MCP are configured to have full access to your Back4App apps, which includes the ability to create, modify, and delete resources. We strongly recommend first trying on a test account and app to understand its capabilities and potential impact before using it with production environments.
:::

## **Prerequisites**

1. An account created at back4app.com. (each new account has a deafult limit of apps if you need more please contact us);
2. A recent NodeJs version installed (16^);
3. For better results we recommend to use the most advanced LLM Models and coding Agents;
4. [**Activate Web-Hosting**](https://www.back4app.com/docs/platform/activating-web-hosting) for visualizing deployments on your subdomain;



## 1 - Create a Account Key

First, go to your Back4App dashboard and create a personal access token:

1. Log into your Back4App account
2. Hover over the "Hello, \[username]" menu
3. Go to **Account Keys** and create a new key
4. Give it a name that describes its purpose, like "AI Assistant MCP"
5. Copy the token securely - you won't be able to see it again

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Vtf9h_neBfwWz0MOTYGb8_screenshot-2024-11-28-at-164118.png" signedSrc size="56" width="622" height="488" position="center" caption alt}

Then give your account key token a name and click on +.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8PVJ3_IeA8HBRTy-uIO3y_image.png" signedSrc size="66" width="626" height="251" position="center" caption}

This token will be used to authenticate the MCP server with your Back4app account.

## 2 - Install MCP - Auto

Follow these steps to install Back4app MCP on your prefered IDE/LLM:

### 2.1- Run Installation Command

Run this command on your terminal substituting `<ide>` for your prefered enviroment and YOUR\_ACCOUNT\_KEY for your account key copied on **Step 1**.

```bash
npx @back4app/mcp-installer install <ide> --account-key YOUR_ACCOUNT_KEY
```

The specific commands for each IDE are listed below:

**Cursor&#x20;**

```bash
npx @back4app/mcp-installer install cursor --account-key YOUR_ACCOUNT_KEY
```

**Windsurf&#x20;**

```bash
npx @back4app/mcp-installer install windsurf --account-key YOUR_ACCOUNT_KEY
```

**Visual Studio &#x20;**

```bash
npx @back4app/mcp-installer install vscode --account-key YOUR_ACCOUNT_KEY
```

****

**Cline**

```bash
npx @back4app/mcp-installer install cline --account-key YOUR_ACCOUNT_KEY
```

### 2.2- Verify Connection

**Cursor** : Go to Settings -> Cursor Settings -> MCP

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/T0J8l4WXPTFY5NvECNNyE_image.png" signedSrc size="66" width="1108" height="530" position="center" caption}

**Windsurf:** Find the toolbar above the Cascade input and click on refresh

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZDSDM3KpJvUjHSUOXWZNS_image.png" signedSrc size="84" width="746" height="144" position="center" caption}

**Visual Studio:** Click on configure tools on the Agent Mode (Copilot) and find the back4app MCP tools.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/K1JQ7h0Akw9R4vkwDLgxT_image.png" signedSrc size="68" width="998" height="268" position="center" caption}

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/XBOptYUJCZrJHYWp51Aij_image.png" signedSrc size="80" width="1224" height="622" position="center" caption}

## 3 - Configure in your AI tool - Manual

MCP compatible tools can connect to Back4App using the Back4App MCP server. Below are instructions for connecting to this server using popular AI tools:

:::ExpandableHeading
### Cursor

1. Open Cursor and go to Cursor menu.
2. Navitage to Cursor->Settings->Cursor Settings->MCP
3. Click on +Add a new global MCP&#x20;

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/YzKx3lkm0svvSRTOv6A5W_image.png)

Then add the following configuration:

**macOS / Linux**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

**Windows**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx.cmd",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

1. Replace `<account-key>` with your account key copied from back4app.
2. Save the configuration file

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/yjyGhtyrINZlB9OY9o5rx_image.png)
:::

**Alternative Setup**

If you prefer a project setup you can create a local project config file:

1. Create a `.cursor` directory in your project root if it doesn't exist
2. Create a `.cursor/mcp.json` file if it doesn't exist and open it
3. Add the connfiguration mentioned before

:::ExpandableHeading
### Windsurf

1. Open Windsurf and navigate to the Cascade assistant
2. Tap on the hammer (MCP) icon, then Configure to open the configuration file
3. Add the following configuration:

**macOS / Linux**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

**Windows**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx.cmd",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

1. Replace `<account-key>` with your account key copied from back4app.
2. Save the configuration file and reload by tapping Refresh in the Cascade assistant
3. You should see a green active status after the server is successfully connected


:::

:::ExpandableHeading
### Visual Studio(Copilot)

1. Open VS Code and create a `.vscode` directory in your project root if it doesn't exist
2. Create a `.vscode/mcp.json` file if it doesn't exist and open it
3. Add the following configuration:

**macOS / Linux**

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "back4app-account-key",
      "description": "Back4App personal access token",
      "password": true
    }
  ],
  "servers": {
    "back4app": {
      "command": "npx",
      "args": ["-y", "@back4app/mcp-server-back4app@latest"],
      "env": {
        "BACK4APP_ACCOUNT_KEY": "${input:back4app-account-key}"
      }
    }
  }
}
```

**Windows**

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "back4app-account-key",
      "description": "Back4App personal access token",
      "password": true
    }
  ],
  "servers": {
    "back4app": {
      "command": "npx.cmd",
      "args": ["-y", "@back4app/mcp-server-back4app@latest"],
      "env": {
        "BACK4APP_ACCOUNT_KEY": "${input:back4app-account-key}"
      }
    }
  }
}
```

1. Save the configuration file
2. Open Copilot chat and switch to "Agent" mode. You should see a tool icon that you can tap to confirm the MCP tools are available
3. Once you begin using the server, you will be prompted to enter your personal access token. Enter the token that you created earlier

For more info on using MCP in VS Code, see the Copilot documentation.


:::

:::ExpandableHeading
### Cline

1. Open the Cline extension in VS Code and tap the MCP Servers icon
2. Tap Configure MCP Servers to open the configuration file
3. Add the following configuration:

**macOS / Linux**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

**Windows**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx.cmd",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

1. Replace `<account-key>` with your account key copied from back4app.
2. Save the configuration file. Cline should automatically reload the configuration
3. You should see a green active status after the server is successfully connected


:::

::::ExpandableHeading
### Claude desktop

1. Open Claude desktop and navigate to Settings
2. Under the Developer tab, tap Edit Config to open the configuration file
3. Add the following configuration:

**macOS / Linux**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

**Windows**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx.cmd",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

1. Replace `<account-key>` with your account key copied from back4app.
2. Save the configuration file and restart Claude desktop
3. From the new chat screen, you should see a hammer (MCP) icon appear with the new MCP server available

:::hint{type="warning"}
Outdated Node.js installations can cause the npx command to fail in Claude Desktop. We recommend uninstalling any versions older than 16 and using Node.js v16 or higher.
:::


::::

::::ExpandableHeading
### Claude Code

1. Create a `.mcp.json` file in your project root if it doesn't exist
2. Add the following configuration:

**macOS / Linux**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

**Windows**

```json
{
  "mcpServers": {
    "back4app": {
      "command": "npx.cmd",
      "args": [
        "-y",
        "@back4app/mcp-server-back4app@latest",
        "--account-key",
        "<account-key>"
      ]
    }
  }
}
```

1. Replace `<account-key>` with your account key copied from back4app.
2. Save the configuration file
3. Restart Claude code to apply the new configuration

:::hint{type="warning"}
Outdated Node.js installations can cause the npx command to fail in Claude Code. We recommend uninstalling any versions older than 16 and using Node.js v16 or higher.
:::


::::

## 3 - Available Tools

Once connected, your AI assistant can perform a wide range of tasks on your Back4App account. Here are some of the available tools:

### App Management

- **create\_parse\_app** - Create a new Parse app
- **get\_parse\_apps** - Get a list of all your Parse apps
- **get\_parse\_app** - Get details for a specific Parse app
- **set\_current\_app** - Set a default app for subsequent operations
- **get\_current\_app** - Get the currently set default app

### Direct API Access (Parse REST API)

- **call\_parse\_api** - Calls the Parse Server REST API endpoints to fully manage your app.&#x20;

**Database Operations**
&#x20;– Create, read, update, delete objects in any class
&#x20;– Rich querying (filters, sorting, pagination, count, aggregate, distinct)

**User Management & Security**
&#x20;– Sign up / log in / log out / password reset
&#x20;– Roles, ACLs & CLPs to lock down data at object- and class-level

**Real-Time & Push**
&#x20;– LiveQuery over WebSockets (subscribe to creates/updates/deletes)
&#x20;– Push notifications & installation records

**Call Cloud Code functions**
&#x20;– Cloud Functions and Scheduled Jobs
&#x20;– Before/after triggers, custom webhooks

**Files, Analytics & Extensions**
&#x20;– File upload/download


### Cloud Code and Web Hosting on Parse App

- **list\_cloud\_code\_and\_web\_hosting\_files** - List all cloud code and web hosting files
- **get\_file\_content** - View the content of specific files
- **deploy\_cloud\_code\_files** - Deploy cloud code files to your app
- **deploy\_web\_hosting\_files** - Deploy web hosting files to your app

## 4 - Security Considerations

:::hint{type="danger"}
The MCP server has full access to your Back4App account with the permissions of your personal access token. This means AI tools can create, modify, and overwrite your apps and data. Always take the following precautions:
:::

1. **Use a dedicated test account** for initial experimentation
2. **Create a separate access token** specifically for MCP use
3. **Never share your configuration files** containing access tokens
4. **Review all code and API Calls** generated or modified by AI before deploying to production
5. **Revoke access tokens** immediately if you suspect any unauthorized use

## 5 - Troubleshooting

### Common Issues

- **Connection failures**: Ensure your personal access token is valid and correctly entered
- **Server not responding**: Check that you have Node.js installed and that npx is working correctly
- **Permission errors**: Verify that your access token has the necessary permissions
- **Updates not appearing**: Some MCP clients require a restart after configuration changes



## 6 - Next Steps

Your AI tool is now connected to Back4App using MCP. Try asking your AI assistant to create a new app, deploy some cloud code, or manage your data using natural language.

If you experience any issues or have feedback, please send us a message at: [**community@back4app.com**](mailto\:community@back4app.com)

## Conclusion

With Back4App's MCP integration, you can leverage the power of AI Agents to accelerate your development workflow. From creating and configuring apps to deploying code and managing data, your AI assistant can now seamlessly interact with the Back4App platform on your behalf.
