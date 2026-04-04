# Source: https://pipedream.com/docs/connect/app-discovery.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# App Discovery

> Discover and configure available apps programmatically, with automatic app identification from prompts.

export const PUBLIC_APPS = '3,000';

Pipedream provides access to {PUBLIC_APPS}+ APIs. Every integration is also available as an MCP server and the vast majority of integrations (like Notion, Gmail, or Slack) have their own specific set of tools.

## Discovering apps

### Search for available apps

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

  // Search for Google Sheets apps, sorted by featured weight
  const apps = await client.apps.list({
    q: "google sheets",
    sortKey: "featured_weight",
    sortDirection: "desc"
  });

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

  # Search for Google Sheets apps, sorted by featured weight
  apps = pd.apps.list(
      q="google sheets",
      sort_key="featured_weight",
      sort_direction="desc"
  )
  ```

</CodeGroup>

<Note>
  Check out the full API reference for [listing apps](/connect/api-reference/list-apps)
</Note>

## Automatic app discovery

If using [Pipedream MCP](/connect/mcp/developers), you can enable Pipedream to automatically identify relevant apps from a given prompt.

<Note>
  Check out how this works at [chat.pipedream.com](https://chat.pipedream.com)
</Note>

### Enabling app discovery

Add the `appDiscovery=true` parameter to your MCP server requests:

| Header               | Query Param    | Value  | Required? |
| -------------------- | -------------- | ------ | --------- |
| `x-pd-app-discovery` | `appDiscovery` | `true` | No        |

<Info>
  App discovery currently requires [full-config mode](/connect/mcp/developers#full-config) to be enabled
</Info>

### How it works

When app discovery is enabled:

1. Pipedream analyzes the incoming prompt to identify which apps are most relevant
2. The initial tool call responses with an array of relevant apps
3. When the client reload its available tools, it will now have tools for the relevant apps

### Examples

#### Basic setup with app discovery

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
  import { PipedreamClient } from "@pipedream/sdk";

  // Get access token
  const client = new PipedreamClient({
    projectEnvironment: PIPEDREAM_ENVIRONMENT,
    clientId: PIPEDREAM_CLIENT_ID,
    clientSecret: PIPEDREAM_CLIENT_SECRET,
    projectId: PIPEDREAM_PROJECT_ID
  });

  const accessToken = await client.rawAccessToken;

  // Configure MCP transport with app discovery enabled
  const transport = new StreamableHTTPClientTransport(new URL(serverUrl), {
    requestInit: {
      headers: {
        "Authorization": `Bearer ${accessToken}`,
        "x-pd-project-id": PIPEDREAM_PROJECT_ID,
        "x-pd-environment": PIPEDREAM_ENVIRONMENT,
        "x-pd-external-user-id": EXTERNAL_USER_ID,
        "x-pd-app-discovery": "true",
        "x-pd-tool-mode": "full-config"
      }
    }
  });

  ```

  ```python Python theme={null}
  from mcp import ClientSession
  from mcp.client.streamable_http import streamablehttp_client
  from pipedream import Pipedream

  # Get access token
  pd = Pipedream(
      project_id=PIPEDREAM_PROJECT_ID,
      project_environment=PIPEDREAM_ENVIRONMENT,
      client_id=PIPEDREAM_CLIENT_ID,
      client_secret=PIPEDREAM_CLIENT_SECRET,
  )

  const accessToken = await client.rawAccessToken;

  # Configure MCP client with app discovery enabled
  headers = {
      "Authorization": f"Bearer {access_token}",
      "x-pd-project-id": PIPEDREAM_PROJECT_ID,
      "x-pd-environment": PIPEDREAM_ENVIRONMENT,
      "x-pd-external-user-id": EXTERNAL_USER_ID,
      "x-pd-app-discovery": "true",
      "x-pd-tool-mode": "full-config"
  }

  # Create MCP client connection with app discovery
  async with streamablehttp_client(server_url, headers=headers) as (read, write, _):
      async with ClientSession(read, write) as session:
          await session.initialize()
  ```

</CodeGroup>

#### How app discovery works with different prompts

App discovery automatically detects which apps are referenced in user prompts:

| User Input                                                 | Apps Detected                                                              |
| ---------------------------------------------------------- | -------------------------------------------------------------------------- |
| "Send a message to the #general channel in Slack"          | slack                                                                      |
| "Create a task in Notion and send a notification to Slack" | notion, slack                                                              |
| "Add this email to my spreadsheet"                         | google\_sheets, microsoft\_excel, airtable\_oauth, zoho\_sheet, smartsheet |
| "Schedule a meeting and update my CRM"                     | google\_calendar, zoho\_crm, hubspot                                       |

### Limitations

* App discovery currently requires `full-config` mode to be enabled
* Detection accuracy depends heavily on the clarity of the prompt

Built with [Mintlify](https://mintlify.com).
