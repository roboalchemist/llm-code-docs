# Source: https://mintlify.com/docs/ai/model-context-protocol.md

# Model Context Protocol

> Connect your documentation and API endpoints to AI tools with a hosted MCP server.

export const PreviewButton = ({children, href}) => {
  return <a href={href} className="text-sm font-medium text-white dark:!text-zinc-950 bg-zinc-900 hover:bg-zinc-700 dark:bg-zinc-100 hover:dark:bg-zinc-300 rounded-full px-3.5 py-1.5 not-prose">
        {children}
      </a>;
};

## About MCP servers

The Model Context Protocol (MCP) is an open protocol that creates standardized connections between AI applications and external services, like documentation. Mintlify generates an MCP server from your documentation and OpenAPI specifications, preparing your content for the broader AI ecosystem where any MCP client (like Claude, Cursor, Goose, and others) can connect to your documentation and APIs.

Your MCP server exposes tools for AI applications to search your documentation and interact with your APIs.

## Accessing your MCP server

<Note>
  MCP servers can only be generated for public documentation. Documentation behind end-user authentication cannot be accessed for server generation.
</Note>

Mintlify automatically generates an MCP server for your documentation and hosts it at your documentation URL with the `/mcp` path. For example, Mintlify's MCP server is available at `https://mintlify.com/docs/mcp`.

You can see and copy your MCP server URL in your [dashboard](https://dashboard.mintlify.com/products/mcp).

The `/mcp` path is reserved for hosted MCP servers and cannot be used for other navigation elements.

## Configuring your MCP server

All MCP servers include the `search` tool by default, which allows users to query information from your docs in other tools.

If you have a [Pro or Custom plan](https://mintlify.com/pricing?ref=mcp), you can expose endpoints from your OpenAPI specification as MCP tools.

To expose endpoints as MCP tools, use the `mcp` object within the `x-mint` extension at either the file or endpoint level. For example, the Mintlify MCP server includes tools to create assistant chats, get status updates, and trigger updates.

MCP servers follow a security-first approach where API endpoints are not exposed by default. You must explicitly enable endpoints to make them available as MCP tools. Only expose endpoints that are safe for public access through AI tools.

<ResponseField name="mcp" type="object">
  The MCP configuration for the endpoint.

  <Expandable title="MCP">
    <ResponseField name="enabled" type="boolean">
      Whether to expose the endpoint as an MCP tool. Takes precedence over the file-level configuration.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the MCP tool.
    </ResponseField>

    <ResponseField name="description" type="string">
      The description of the MCP tool.
    </ResponseField>
  </Expandable>
</ResponseField>

### File-level configuration

Enable MCP for all endpoints by default in an OpenAPI specification file and selectively exclude endpoints:

```json  theme={null}
{
  "openapi": "3.1.0",
  "x-mint": {
    "mcp": {
      "enabled": true
    }
  },
  // ...
  "paths": {
    "/api/v1/users": {
      "get": {
        "x-mint": {
          "mcp": {
            "enabled": false // Disables MCP for this endpoint
          }
        },
        // ...
      }
    }
  }
}
```

### Endpoint-level configuration

Enable MCP for specific endpoints:

```json  theme={null}
{
  "paths": {
    "/api/v1/users": {
      "get": {
        "x-mint": {
          "mcp": {
            "enabled": true,
            "name": "get-users",
            "description": "Get a list of users"
          },
          // ...
        }
      }
    },
    "/api/v1/delete": {
      "delete": {
        // No `x-mint: mcp` so this endpoint is not exposed as an MCP tool
        // ...
      }
    }
  }
}
```

## Using your MCP server

Your users must connect your MCP server to their preferred AI tools.

1. Make your MCP server URL publicly available.
2. Users copy your MCP server URL and add it to their tools.
3. Users access your documentation and API endpoints through their tools.

These are some of the ways you can help your users connect to your MCP server:

<Tabs>
  <Tab title="Contextual menu">
    Add options in the [contextual menu](/ai/contextual-menu) for your users to connect to your MCP server from any page of your documentation.

    | Option                  | Identifier | Description                                         |
    | :---------------------- | :--------- | :-------------------------------------------------- |
    | **Copy MCP server URL** | `mcp`      | Copies your MCP server URL to the user's clipboard. |
    | **Connect to Cursor**   | `cursor`   | Installs your MCP server in Cursor.                 |
    | **Connect to VS Code**  | `vscode`   | Installs your MCP server in VS Code.                |
  </Tab>

  <Tab title="Claude">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the steps to connect it to Claude.

        1. Navigate to the [Connectors](https://claude.ai/settings/connectors) page in the Claude settings.
        2. Select **Add custom connector**.
        3. Add your MCP server name and URL.
        4. Select **Add**.
        5. When using Claude, select the attachments button (the plus icon).
        6. Select your MCP server.
      </Step>
    </Steps>

    See the [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/tutorials/use-remote-mcp-server#connecting-to-a-remote-mcp-server) for more details.
  </Tab>

  <Tab title="Claude Code">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the command to connect it to Claude Code.

        ```bash  theme={null}
        claude mcp add --transport http <name> <url>
        ```
      </Step>
    </Steps>

    See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/mcp#installing-mcp-servers) for more details.
  </Tab>

  <Tab title="Cursor">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the steps to connect it to Cursor.

        1. Use <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on Windows) to open the command palette.
        2. Search for "Open MCP settings".
        3. Select **Add custom MCP**. This will open the `mcp.json` file.
        4. In `mcp.json`, configure your server:

        ```json  theme={null}
        {
          "mcpServers": {
            "<your-mcp-server-name>": {
              "url": "<your-mcp-server-url>"
            }
          }
        }
        ```
      </Step>
    </Steps>

    See the [Cursor documentation](https://docs.cursor.com/en/context/mcp#installing-mcp-servers) for more details.
  </Tab>

  <Tab title="VS Code">
    <Steps>
      <Step title="Get your MCP server URL.">
        Navigate to your [dashboard](https://dashboard.mintlify.com/products/mcp) and find your MCP server URL.
      </Step>

      <Step title="Publish your MCP server URL for your users.">
        Create a guide for your users that includes your MCP server URL and the steps to connect it to VS Code.

        1. Create a `.vscode/mcp.json` file.
        2. In `mcp.json`, configure your server:

        ```json  theme={null}
        {
          "servers": {
            "<your-mcp-server-name>": {
              "type": "http",
              "url": "<your-mcp-server-url>"
            }
          }
        }
        ```
      </Step>
    </Steps>

    See the [VS Code documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more details.
  </Tab>
</Tabs>

### Example: Connecting to the Mintlify MCP server

Connect to the Mintlify MCP server to interact with the Mintlify API and search our documentation. This will give you more accurate answers about how to use Mintlify in your local environment and demonstrates how you can help your users connect to your MCP server.

<Tabs>
  <Tab title="Contextual menu">
    At the top of this page, select the contextual menu and choose **Connect to Cursor** or **Connect to VS Code** to connect the Mintlify MCP server to the IDE of your choice.
  </Tab>

  <Tab title="Claude">
    To use the Mintlify MCP server with Claude:

    <Steps>
      <Step title="Add the Mintlify MCP server to Claude">
        1. Navigate to the [Connectors](https://claude.ai/settings/connectors) page in the Claude settings.
        2. Select **Add custom connector**.
        3. Add the Mintlify MCP server:

        * Name: `Mintlify`
        * URL: `https://mintlify.com/docs/mcp`

        4. Select **Add**.
      </Step>

      <Step title="Access the MCP server in your chat">
        1. When using Claude, select the attachments button (the plus icon).
        2. Select the Mintlify MCP server.
        3. Ask Claude a question about Mintlify.
      </Step>
    </Steps>

    See the [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/tutorials/use-remote-mcp-server#connecting-to-a-remote-mcp-server) for more details.
  </Tab>

  <Tab title="Claude Code">
    To use the Mintlify MCP server with Claude Code, run the following command:

    ```bash  theme={null}
    claude mcp add --transport http Mintlify https://mintlify.com/docs/mcp
    ```

    Test the connection by running:

    ```bash  theme={null}
    claude mcp list
    ```

    See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/mcp#installing-mcp-servers) for more details.
  </Tab>

  <Tab title="Cursor">
    <PreviewButton href="cursor://anysphere.cursor-deeplink/mcp/install?name=mintlify&config=eyJ1cmwiOiJodHRwczovL21pbnRsaWZ5LmNvbS9kb2NzL21jcCJ9">Install in Cursor</PreviewButton>

    To connect the Mintlify MCP server to Cursor, click the **Install in Cursor** button. Or to manually connect the MCP server, follow these steps:

    <Steps>
      <Step title="Open MCP settings">
        1. Use <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on Windows) to open the command palette.
        2. Search for "Open MCP settings".
        3. Select **Add custom MCP**. This will open the `mcp.json` file.
      </Step>

      <Step title="Configure the Mintlify MCP server">
        In `mcp.json`, add:

        ```json  theme={null}
        {
          "mcpServers": {
            "Mintlify": {
              "url": "https://mintlify.com/docs/mcp"
            }
          }
        }
        ```
      </Step>

      <Step title="Test the connection">
        In Cursor's chat, ask "What tools do you have available?" Cursor should show the Mintlify MCP server as an available tool.
      </Step>
    </Steps>

    See [Installing MCP servers](https://docs.cursor.com/en/context/mcp#installing-mcp-servers) in the Cursor documentation for more details.
  </Tab>

  <Tab title="VS Code">
    <PreviewButton href="https://vscode.dev/redirect/mcp/install?name=mintlify&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmintlify.com%2Fdocs%2Fmcp%22%7D">Install in VS Code</PreviewButton>

    To connect the Mintlify MCP server to VS Code, click the **Install in VS Code** button. Or to manually connect the MCP server, create a `.vscode/mcp.json` file and add:

    ```json  theme={null}
    {
      "servers": {
        "Mintlify": {
          "type": "http",
          "url": "https://mintlify.com/docs/mcp"
        }
      }
    }
    ```

    See the [VS Code documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more details.
  </Tab>
</Tabs>

## Authentication

When you enable an API endpoint for MCP, the server includes the authentication requirements defined in your OpenAPI `securitySchemes` and `securityRequirement`. Any keys are handled directly by the tool and not stored or processed by Mintlify.

If a user asks their AI tool to call a protected endpoint, the tool will request the necessary authentication credentials from the user at that moment.

## Monitoring your MCP server

You can view all available MCP tools in the **Available tools** section of the [MCP Server page](https://dashboard.mintlify.com/products/mcp) in your dashboard.

<Frame>
  <img src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c369f390aa3f129b29193bb4d3434cef" alt="MCP dashboard with Available tools section emphasized" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1548" height="1548" data-path="images/mcp/mcp-server-page-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c578d322fd05f23a72742fcf6064dba6 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a4ac282920f79d787429c0660fa1e53c 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b4bc9185afd76ede33c644fb8b76da86 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e009c48bfcb603154c8c65ee5f85af57 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=bb94ccfc738c7ab831bdbef0a0d6004d 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4c10450981a41f94529b144529d8d9b5 2500w" />

  <img src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=77c2901b45017b6e2c978f92f335b813" alt="MCP dashboard with Available tools section emphasized" className="hidden dark:block" data-og-width="3018" width="3018" data-og-height="1540" height="1540" data-path="images/mcp/mcp-server-page-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=878922df800c3f6af0a2252751875841 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=12f14f7dc63efed79e6b236b741537cc 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a9b4c02a878876c97cdfd1c678a5f55a 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a5254919bde1cc9276ca77cbfdd729b5 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a351abe9adc0599d36d946ca17872a8f 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/mcp/mcp-server-page-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=db77e179fe76df93f369434e1399d223 2500w" />
</Frame>

## Troubleshooting

<AccordionGroup>
  <Accordion title="MCP server only shows search tool">
    If your MCP server only exposes the search tool despite having an OpenAPI specification:

    1. Verify your OpenAPI specification is valid and accessible.
    2. Ensure you've explicitly enabled MCP for specific endpoints using `x-mint.mcp.enabled: true`.
    3. Check your deployment logs for OpenAPI processing errors.

    If OpenAPI processing fails, the server continues with just the search tool to maintain functionality.
  </Accordion>

  <Accordion title="Authentication issues">
    If users report authentication problems:

    1. Check that your OpenAPI specification includes proper `securitySchemes` definitions.
    2. Confirm that enabled endpoints work with the specified authentication methods.
  </Accordion>

  <Accordion title="Tool descriptions missing or unclear">
    If AI tools aren't using your API endpoints effectively:

    1. Add detailed `summary` and `description` fields to your endpoints.
    2. Ensure parameter names and descriptions are self-explanatory.
    3. Use the MCP dashboard to verify how your endpoints appear as tools.
  </Accordion>
</AccordionGroup>
