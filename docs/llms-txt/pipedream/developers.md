# Source: https://pipedream.com/docs/connect/mcp/developers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Develop with Pipedream MCP

> Add Pipedream MCP to your app or agent to make tool calls on behalf of your users to 3,000+ APIs and 10,000+ tools.

export const PUBLIC_APPS = '3,000';

## Overview

Pipedream Connect includes [built-in user authentication](#user-account-connections) for [more than {PUBLIC_APPS} APIs](https://mcp.pipedream.com) via MCP, which means you don’t need to build any authorization flows or deal with token storage and refresh in order to make authenticated requests on behalf of your users.

## Examples

* **MCP Chat App**: Check out our [open source chat app](https://github.com/PipedreamHQ/mcp-chat) built with Vercel's AI SDK and Pipedream MCP
* **CLI Examples**: Load tools dynamically [using either OpenAI or Vercel's AI SDK](https://github.com/PipedreamHQ/pipedream-connect-examples/tree/master/mcp)
* **Gemini Agent**: Use Pipedream MCP with [Google Gemini](https://github.com/philschmid/gemini-samples/blob/main/scripts/gemini-mcp-pipedream.py) ([built by the Gemini team](https://x.com/_philschmid/status/1948025573403492621))

## AI Frameworks

Use Pipedream MCP with popular AI frameworks and LLMs:

<CardGroup cols={2}>
  <Card
    title="Vercel AI SDK"
    href="/connect/mcp/ai-frameworks/vercel-ai-sdk"
    icon={
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 256 222">
      <path d="m128 0l128 221.705H0z"/>
    </svg>
  }
  >
    Streamlined MCP integration with automatic tool execution
  </Card>

  <Card
    title="OpenAI"
    href="/connect/mcp/ai-frameworks/openai"
    icon={
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 256 260">
      <path d="M239.184 106.203a64.716 64.716 0 0 0-5.576-53.103C219.452 28.459 191 15.784 163.213 21.74A65.586 65.586 0 0 0 52.096 45.22a64.716 64.716 0 0 0-43.23 31.36c-14.31 24.602-11.061 55.634 8.033 76.74a64.665 64.665 0 0 0 5.525 53.102c14.174 24.65 42.644 37.324 70.446 31.36a64.72 64.72 0 0 0 48.754 21.744c28.481.025 53.714-18.361 62.414-45.481a64.767 64.767 0 0 0 43.229-31.36c14.137-24.558 10.875-55.423-8.083-76.483m-97.56 136.338a48.397 48.397 0 0 1-31.105-11.255l1.535-.87l51.67-29.825a8.595 8.595 0 0 0 4.247-7.367v-72.85l21.845 12.636c.218.111.37.32.409.563v60.367c-.056 26.818-21.783 48.545-48.601 48.601M37.158 197.93a48.345 48.345 0 0 1-5.781-32.589l1.534.921l51.722 29.826a8.339 8.339 0 0 0 8.441 0l63.181-36.425v25.221a.87.87 0 0 1-.358.665l-52.335 30.184c-23.257 13.398-52.97 5.431-66.404-17.803M23.549 85.38a48.499 48.499 0 0 1 25.58-21.333v61.39a8.288 8.288 0 0 0 4.195 7.316l62.874 36.272l-21.845 12.636a.819.819 0 0 1-.767 0L41.353 151.53c-23.211-13.454-31.171-43.144-17.804-66.405zm179.466 41.695l-63.08-36.63L161.73 77.86a.819.819 0 0 1 .768 0l52.233 30.184a48.6 48.6 0 0 1-7.316 87.635v-61.391a8.544 8.544 0 0 0-4.4-7.213m21.742-32.69l-1.535-.922l-51.619-30.081a8.39 8.39 0 0 0-8.492 0L99.98 99.808V74.587a.716.716 0 0 1 .307-.665l52.233-30.133a48.652 48.652 0 0 1 72.236 50.391zM88.061 139.097l-21.845-12.585a.87.87 0 0 1-.41-.614V65.685a48.652 48.652 0 0 1 79.757-37.346l-1.535.87l-51.67 29.825a8.595 8.595 0 0 0-4.246 7.367zm11.868-25.58L128.067 97.3l28.188 16.218v32.434l-28.086 16.218l-28.188-16.218z"/>
    </svg>
  }
  >
    Direct integration with OpenAI's API and playground
  </Card>

  <Card
    title="Anthropic Claude"
    href="/connect/mcp/ai-frameworks/anthropic"
    icon={
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 256 176">
      <path fill="currentColor" d="m147.487 0l70.081 175.78H256L185.919 0zM66.183 106.221l23.98-61.774l23.98 61.774zM70.07 0L0 175.78h39.18l14.33-36.914h73.308l14.328 36.914h39.179L110.255 0z"/>
    </svg>
  }
  >
    Native MCP connector through Claude's Messages API
  </Card>

  <Card
    title="Google Gemini"
    href="/connect/mcp/ai-frameworks/gemini"
    icon={
    <svg fill="none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 16 16">
      <path d="M16 8.016A8.522 8.522 0 008.016 16h-.032A8.521 8.521 0 000 8.016v-.032A8.521 8.521 0 007.984 0h.032A8.522 8.522 0 0016 7.984v.032z" fill="currentColor"/>
    </svg>
  }
  >
    Multimodal AI with text, image, and tool capabilities
  </Card>
</CardGroup>

### Key Pipedream concepts to understand

**`external_user_id`**

* This is your user's ID, in your system: whatever you use to uniquely identify them
* Requests made for that user ID are coupled to that end user and their connected accounts ([learn more](/connect/managed-auth/users))

**`app`**

* The app's "name slug" (the unique identifier for the app)
* Check out the [app discovery](/connect/app-discovery) docs to learn how to discover and use available apps

## Tool modes

Pipedream MCP supports different methods for interacting with tools. Learn about the available modes in the [Tool Modes section](/connect/mcp/tool-modes) of the docs.

## Prerequisites

To use either the remote or self-hosted MCP server, you’ll need:

1. A [Pipedream account](https://pipedream.com/auth/signup)
2. A [Pipedream project](/projects/#creating-projects). Accounts connected via MCP will be stored here.
3. [Pipedream OAuth credentials](/connect/api-reference/authentication)

### Set up your environment

Set the following environment variables:

```env  theme={null}
PIPEDREAM_CLIENT_ID=your_client_id
PIPEDREAM_CLIENT_SECRET=your_client_secret
PIPEDREAM_PROJECT_ID=your_project_id # proj_xxxxxxx
PIPEDREAM_ENVIRONMENT=development # development | production
```

Learn more about [environments in Pipedream Connect](/connect/managed-auth/environments/).

## Authentication

### Developer authentication

Your application authenticates with Pipedream using client credential OAuth. [See below](/connect/mcp/developers/#api-authentication) for details.

### User account connections

One of the core features of Pipedream Connect and the MCP server is the ability for your users to easily connect their accounts without having to build any of the authorization flow or handle token storage.

You can handle account connections in one of two ways in your app:

#### Add a button in your UI

* Use Pipedream’s [frontend SDK](/connect/managed-auth/quickstart/#use-the-pipedream-sdk-in-your-frontend) to let users connect their account directly in your UI
* You can see an example of this when you connect any account in [mcp.pipedream.com](https://mcp.pipedream.com)

#### Return a link

* Use [Connect Link](/connect/managed-auth/quickstart/#or-use-connect-link) to let your users connect their account in a new browser tab
* This is handled automatically by Pipedream's MCP server and **there’s no additional implementation required**
* If a user doesn’t have a connected account that’s required for a given tool call, the server will return a URL in the tool call response:

```sh  theme={null}
https://pipedream.com/_static/connect.html?token=ctok_xxxxxxx&connectLink=true&app={appSlug}
```

## Discover available integrations

Pipedream provides [{PUBLIC_APPS}+ APIs as MCP servers](https://mcp.pipedream.com). Each server corresponds to an app integration (like Notion, Gmail, or Slack) and has its own specific set of tools.

For detailed information on discovering apps and enabling automatic app discovery, check out [app discovery](/connect/app-discovery) section.

## Getting started

### Use Pipedream’s remote MCP server

### Supported transport types

The Pipedream MCP server supports both SSE and streamable HTTP transport types dynamically, with no configuration required by the developer or MCP client.

### Base URL

```sh  theme={null}
https://remote.mcp.pipedream.net
```

### API Authentication

To authenticate requests to Pipedream’s MCP server, you need to include an access token with every HTTP request. Here’s how to get it:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { PipedreamClient } from "@pipedream/sdk";

  // Initialize the Pipedream SDK client
  const client = new PipedreamClient({
    projectEnvironment: PIPEDREAM_ENVIRONMENT,
    clientId: PIPEDREAM_CLIENT_ID,
    clientSecret: PIPEDREAM_CLIENT_SECRET,
    projectId: PIPEDREAM_PROJECT_ID
  });

  // Get access token for MCP server auth
  const accessToken = await client.rawAccessToken;

  console.log(accessToken);

  ```

  ```python Python theme={null}
  from pipedream import Pipedream

  # Initialize the Pipedream SDK client
  pd = Pipedream(
      project_id=PIPEDREAM_PROJECT_ID,
      project_environment=PIPEDREAM_ENVIRONMENT,
      client_id=PIPEDREAM_CLIENT_ID,
      client_secret=PIPEDREAM_CLIENT_SECRET,
  )

  # Get access token for MCP server auth
  access_token = await pd.raw_access_token

  print(access_token)
  ```

  ```sh cURL theme={null}
  curl -s -X POST https://api.pipedream.com/v1/oauth/token \
    -H "Content-Type: application/json" \
    -d '{
      "grant_type": "client_credentials", 
      "client_id": "'$PIPEDREAM_CLIENT_ID'", 
      "client_secret": "'$PIPEDREAM_CLIENT_SECRET'"
    }'
  ```

</CodeGroup>

### Params

* Below are params that you should send with every HTTP request to Pipedream’s MCP server.
* You can pass them as HTTP headers or as query parameters on the URL.

| Header                  | Query Param      | Value                                    | Required?                  |
| ----------------------- | ---------------- | ---------------------------------------- | -------------------------- |
| `x-pd-project-id`       | `projectId`      | `proj_xxxxxxx`                           | Yes                        |
| `x-pd-environment`      | `environment`    | `development`, `production`              | Yes                        |
| `x-pd-external-user-id` | `externalUserId` | `<your-users-id>`                        | Yes                        |
| `x-pd-account-id`       | `accountId`      | `apn_xxxxxxx`                            | No                         |
| `x-pd-app-slug`         | `app`            | `linear`, `notion`, etc                  | Yes\*                      |
| `x-pd-tool-mode`        | `toolMode`       | `sub-agent`, `tools-only`, `full-config` | No Defaults to `sub-agent` |
| `x-pd-app-discovery`    | `appDiscovery`   | `true`                                   | No                         |

\*Required unless using `appDiscovery=true`

### Example request

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
  import { PipedreamClient } from "@pipedream/sdk";

  // Initialize the Pipedream SDK client
  const client = new PipedreamClient({
    projectEnvironment: PIPEDREAM_ENVIRONMENT,
    clientId: PIPEDREAM_CLIENT_ID,
    clientSecret: PIPEDREAM_CLIENT_SECRET,
    projectId: PIPEDREAM_PROJECT_ID
  });

  // Retrieve your developer access token via the Pipedream SDK
  const accessToken = await client.rawAccessToken;
  const serverUrl = MCP_SERVER_URL || `https://remote.mcp.pipedream.net`;

  const transport = new StreamableHTTPClientTransport(new URL(serverUrl), {
    requestInit: {
      headers: {
        "Authorization": `Bearer ${accessToken}`,
        "x-pd-project-id": PIPEDREAM_PROJECT_ID, // proj_xxxxxxx
        "x-pd-environment": PIPEDREAM_ENVIRONMENT, // development | production
        "x-pd-external-user-id": EXTERNAL_USER_ID, // the user's ID from your system
        "x-pd-app-slug": APP_SLUG, // notion, linear, gmail, etc
      }
    }
  });

  ```

  ```python Python theme={null}
  from mcp import ClientSession
  from mcp.client.streamable_http import streamablehttp_client
  from pipedream import Pipedream

  # Initialize the Pipedream SDK client
  pd = Pipedream(
      project_id=PIPEDREAM_PROJECT_ID,
      project_environment=PIPEDREAM_ENVIRONMENT,
      client_id=PIPEDREAM_CLIENT_ID,
      client_secret=PIPEDREAM_CLIENT_SECRET,
  )

  # Retrieve your developer access token via the Pipedream SDK
  access_token = await pd.raw_access_token
  server_url = MCP_SERVER_URL or "https://remote.mcp.pipedream.net"

  # Configure MCP client with authentication headers
  headers = {
      "Authorization": f"Bearer {access_token}",
      "x-pd-project-id": PIPEDREAM_PROJECT_ID,  # proj_xxxxxxx
      "x-pd-environment": PIPEDREAM_ENVIRONMENT,  # development | production
      "x-pd-external-user-id": EXTERNAL_USER_ID,  # the user's ID from your system
      "x-pd-app-slug": APP_SLUG,  # notion, linear, gmail, etc
  }

  # Create MCP client connection
  async with streamablehttp_client(server_url, headers=headers) as (read, write, _):
      async with ClientSession(read, write) as session:
          await session.initialize()
          
          # Now you can use the session to call tools
          tools = await session.list_tools()
  ```

</CodeGroup>

### Using the MCP inspector

The [MCP inspector](https://modelcontextprotocol.io/tools/inspector) can be helpful when debugging tool calls.

```sh  theme={null}
npx @modelcontextprotocol/inspector
```

Enter the server URL:

```
https://remote.mcp.pipedream.net?externalUserId={external_user_id}&app={app_slug}
```

## Using custom tools

Publish [custom tools](/connect/components/custom-tools/) to your workspace to use them with Pipedream's MCP server. This lets you add custom and unique functionality that may not be available in the public registry.

Built with [Mintlify](https://mintlify.com).
