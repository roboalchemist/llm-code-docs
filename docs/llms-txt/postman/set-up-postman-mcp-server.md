# Set up the Postman MCP Server

The Postman MCP Server supports both [remote servers](#remote-server) through streamable HTTP and [local servers](#local-server) with STDIO. The remote server is available at `https://mcp.postman.com/` and `https://mcp.eu.postman.com` for the EU, and the local server is available in the [Postman MCP Server GitHub repository](https://github.com/postmanlabs/postman-mcp-server). You can also fork the Postman MCP collection from the Postman Public Workspace:

[![Fork the Postman MCP Server](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/681dc649440b35935978b8b7?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D681dc649440b35935978b8b7%26entityType%3DextensibleCollection%26workspaceId%3D405e0480-49cf-463b-8052-6c0d05a8e8f3)

Postman also offers servers as an [npm package](https://www.npmjs.com/package/@postman/postman-mcp-server) and as a [Docker image](#install-in-docker).

## Before getting started, ensure that you have a valid [Postman API key](https://postman.postman.co/settings/me/api-keys).

## Remote server

The remote Postman MCP server offers the following tool configurations through streamable HTTP:

* **Minimal** - (Default) This mode only includes essential tools for basic Postman operations, available at `https://mcp.postman.com/minimal` and `https://mcp.eu.postman.com/minimal` for EU users.
* **Code** - Includes tools for searching public and internal API definitions and generating client code, available at `https://mcp.postman.com/code` and `https://mcp.eu.postman.com/code` for EU users.
* **Full** - Includes all available Postman API tools (100+ tools), available at `https://mcp.postman.com/mcp` and `https://mcp.eu.postman.com/mcp` for EU users.

### Install in Cursor

Click the button to install the remote Postman MCP Server in Cursor:

[![Install the remote Postman MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=postman_mcp_server&config=eyJ1cmwiOiJodHRwczovL21jcC5wb3N0bWFuLmNvbS9taW5pbWFsIiwiaGVhZGVycyI6eyJBdXRob3JpemF0aW9uIjoiQmVhcmVyIFlPVVJfQVBJX0tFWSJ9fQ%3D%3D)

After installing, ensure that the Authorization header uses the `Bearer $POSTMAN-API-KEY` format.

To access **Full** mode, change the `url` value to `https://mcp.postman.com/mcp` in the `mcp.json` file. To access **Code** mode, change the value to `https://mcp.postman.com/code` in this file.

### Install in Visual Studio Code

To install the remote Postman MCP Server in VS Code, click the install button or use the [Postman VS Code Extension](/docs/developer/vs-code-extension/postman-mcp-server/):

[![Install the remote Postman MCP Server in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=postman_mcp_server&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fmcp.postman.com%2Fminimal%22%2C%22headers%22%3A%7B%22Authorization%22%3A%22Bearer%20YOUR_API_KEY%22%7D%7D)

To access **Full** mode, change the `url` value to `https://mcp.postman.com/mcp` in the `mcp.json` file. To access **Code** mode, change the value to `https://mcp.postman.com/code` in this file.

#### Manual installation

You can use the Postman MCP Server with MCP-compatible extensions in Cursor VS Code, such as GitHub Copilot, Claude for VS Code, or other AI assistants that support MCP. To do so, add the following JSON block to the `mcp.json` configuration file:

```json
{
    "servers": {
        "postman-api-http-server": {
            "type": "sse",
            "url": "https://mcp.postman.com/{minimal OR mcp}",
            // Use "https://mcp.postman.com/mcp" for full or "https://mcp.postman.com/minimal" for minimal mode.
            // For the EU server, use the "https://mcp.eu.postman.com" URL.
            "headers": {
                "Authorization": "Bearer ${input:postman-api-key}"
            }
        }
    },
    "inputs": [
        {
            "id": "postman-api-key",
            "type": "promptString",
            "description": "Enter your Postman API key"
        }
    ]
}
```

Start the server. When prompted, enter your Postman API key.

### Install in Claude Code

To install the MCP server in Claude Code, run the following command in your terminal:

For **Minimal** mode:

```bash
claude mcp add --transport http postman https://mcp.postman.com/minimal --header "Authorization: Bearer ${POSTMAN_API_KEY}"
```

For **Code** mode:

```bash
claude mcp add --transport http postman https://mcp.postman.com/mcp --header "Authorization: Bearer ${POSTMAN_API_KEY}"
```

For **Full** mode:

```bash
claude mcp add --transport http postman https://mcp.postman.com/mcp --header "Authorization: Bearer ${POSTMAN_API_KEY}"
```

### Use as a Gemini CLI extension

To install the MCP server as a Gemini CLI extension, run the following command in your terminal:

```bash
gemini extensions install https://github.com/postmanlabs/postman-mcp-server
```

### Install in Docker

To use the Postman MCP Server in Docker, you can use one of the following methods:

* To install the Postman MCP Server in Docker, see the [Postman MCP Server](https://hub.docker.com/mcp/server/postman/overview) at Docker MCP Hub. Click **+ Add to Docker Desktop** to automatically install it.
* To run the Postman MCP Server image in Docker, run the following command in your terminal. Docker automatically discovers, downloads, and runs the Postman MCP Server image:

    ```bash
    docker run -i -e POSTMAN_API_KEY="your-secret-key" mcp/postman
    ```

* To build and run the server in Docker manually, run the `docker build -t postman-api-mcp-stdio .` command. Then, run one of the following commands, replacing `$YOUR-POSTMAN-API-KEY` with your Postman API key:
    * **Minimal** - `docker run -i -e POSTMAN_API_KEY="your-secret-key" postman-api-mcp-stdio`
    * **Full** - `docker run -i -e POSTMAN_API_KEY="your-secret-key" postman-api-mcp-stdio --full`

### Install in Kiro

To use the Postman MCP Server in Kiro, you can use one of the following methods:

To set up the Postman MCP Server with one-click, see [API Testing with Postman](https://kiro.dev/powers/) on the Kiro Powers page. Click **Add to Kiro**.

To install the Postman MCP Server manually, do the following:

1. Launch Kiro and click the Kiro ghost icon in the left sidebar.
1. Add an MCP Server and select either **User Config** or **Workspace Config** to install the Postman MCP server.
1. Add the following JSON block to the `mcp.json` configuration file:

    ```json
    {
        "mcpServers": {
            "postman": {
                "command": "npx",
                "args": [
                    "@postman/postman-mcp-server"
                ],
                "env": {
                    "POSTMAN_API_KEY": "postman-api-key"
                },
                "disabled": false,
                "autoApprove": [
                    "getAuthenticatedUser"
                ]
            }
        }
    }
    ```

After you've completed your MCP configuration, you can return to the flow template or set up authorization for another integration in Postman.

## Local server

If remote MCP servers aren't supported by your MCP host, you can install the Postman MCP Server to your local machine.

STDIO is a lightweight solution that's ideal for integration with editors and tools like Visual Studio Code. Install an MCP-compatible VS Code extension, such as GitHub Copilot, Claude for VS Code, or other AI assistants that support MCP.

To run the server as a Node application, install [Node.js](https://nodejs.org/) before getting started.

The local server supports the following tool configurations:

* **Minimal** - (Default) Only includes essential tools for basic Postman operations.
* **Code** - Includes tools for searching public and internal API definitions and generating client code.
* **Full** - Includes all available Postman API tools (100+ tools). Use the `--full` flag to enable this configuration.

Use the `--region` flag to specify the Postman API region (`us` or `eu`), or set the `POSTMAN_API_BASE_URL` environment variable directly. By default, the server uses the `us` option.

### Install in Cursor

Click the button to install the local Postman MCP Server in Cursor:

[![Install the local Postman MCP Server in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=postman_api_mcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyJAcG9zdG1hbi9wb3N0bWFuLW1jcC1zZXJ2ZXIiLCItLWZ1bGwiXSwiZW52Ijp7IlBPU1RNQU5fQVBJX0tFWSI6IllPVVJfQVBJX0tFWSJ9fQ%3D%3D)

By default, the server uses **Full** mode. To access **Minimal** mode, remove the `--full` flag from the `mcp.json` configuration file. To access **Code** mode, replace the `--full` flag with the `--code` flag.

### Install in Visual Studio Code

Click the button to install the local Postman MCP Server in VS Code:

[![Install the local Postman MCP Server in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=postman_api_mcp&inputs=%5B%7B%22id%22%3A%22postman_api_key%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22Enter%20your%20Postman%20API%20key%22%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22%40postman%2Fpostman-mcp-server%22%2C%22--full%22%5D%2C%22env%22%3A%7B%22POSTMAN_API_KEY%22%3A%22%24%7Binput%3Apostman-api-key%7D%22%7D%7D)

By default, the server uses **Full** mode. To access **Minimal** mode, remove the `--full` flag from the `mcp.json` configuration file. To access **Code** mode, replace the `--full` flag with the `--code` flag.

#### Manual installation

You can manually integrate your MCP server with VS Code to use it with extensions that support MCP. To do so, create a `.vscode/mcp.json` file in your project and add the following JSON block to it:

```json
{
    "servers": {
        "postman-api-mcp": {
            "type": "stdio",
            "command": "npx",
            "args": [
                "@postman/postman-mcp-server",
                "--full" // (optional) Use this flag to enable full mode.
                "--code" // (optional) Use this flag to enable code mode.
                "--region us" // (optional) Use this flag to specify the Postman API region (us or eu). Defaults to us.
            ],
            "env": {
                "POSTMAN_API_KEY": "${input:postman-api-key}"
            }
        }
    },
    "inputs": [
        {
            "id": "postman-api-key",
            "type": "promptString",
            "description": "Enter your Postman API key"
        }
    ]
}
```

### Claude integration

To integrate the local Postman MCP Server with Claude, check the [latest Postman MCP server release](https://github.com/postmanlabs/postman-mcp-server/releases) and get the `.mcpb` file:

* **Minimal** - `postman-api-mcp-minimal.mcpb`
* **Code** - `postman-mcp-server-code.mcpb`
* **Full** - `postman-api-mcp-full.mcpb`

For more information, see the [Claude Desktop Extensions](https://www.anthropic.com/engineering/desktop-extensions) documentation.

### Install in Claude Code

To install the MCP server in Claude Code, run the following command in your terminal:

For **Minimal** mode:

```bash
claude mcp add postman --env POSTMAN_API_KEY=YOUR_KEY -- npx @postman/postman-mcp-server@latest
```

For **Code** mode:

```bash
claude mcp add postman --env POSTMAN_API_KEY=YOUR_KEY -- npx @postman/postman-mcp-server@latest  --code
```

For **Full** mode:

```bash
claude mcp add postman --env POSTMAN_API_KEY=YOUR_KEY -- npx @postman/postman-mcp-server@latest --full
```

### Use as a Gemini CLI extension

To install the MCP server as a Gemini CLI extension, run the following command in your terminal:

```bash
gemini extensions install https://github.com/postmanlabs/postman-mcp-server
```

### Install in Docker

To use the Postman MCP Server in Docker, you can use one of the following methods:

* To install the Postman MCP Server in Docker, see the [Postman MCP Server](https://hub.docker.com/mcp/server/postman/overview) at Docker MCP Hub. Click **+ Add to Docker Desktop** to automatically install it.
* To run the Postman MCP Server image in Docker, run the following command in your terminal. Docker automatically discovers, downloads, and runs the Postman MCP Server image:

    ```bash
    docker run -i -e POSTMAN_API_KEY="your-secret-key" mcp/postman
    ```

* To build and run the server in Docker manually, run the `docker build -t postman-api-mcp-stdio .` command. Then, run one of the following commands, replacing `$YOUR-POSTMAN-API-KEY` with your Postman API key:
    * **Minimal** - `docker run -i -e POSTMAN_API_KEY="your-secret-key" postman-api-mcp-stdio`
    * **Full** - `docker run -i -e POSTMAN_API_KEY="your-secret-key" postman-api-mcp-stdio --full`

### Install in Kiro

To use the Postman MCP Server in Kiro, you can use one of the following methods:

To set up the Postman MCP Server with one-click, see [API Testing with Postman](https://kiro.dev/powers/) on the Kiro Powers page. Click **Add to Kiro**.

To install the Postman MCP Server manually, do the following:

1. Launch Kiro and click the Kiro ghost icon in the left sidebar.
1. Add an MCP Server and select either **User Config** or **Workspace Config** to install the Postman MCP server.
1. Add the following JSON block to the `mcp.json` configuration file:

    ```json
    {
        "mcpServers": {
            "postman": {
                "command": "npx",
                "args": [
                    "@postman/postman-mcp-server"
                ],
                "env": {
                    "POSTMAN_API_KEY": "postman-api-key"
                },
                "disabled": false,
                "autoApprove": [
                    "getAuthenticatedUser"
                ]
            }
        }
    }
    ```

After you've completed your MCP configuration, you can return to the flow template or set up authorization for another integration in Postman.