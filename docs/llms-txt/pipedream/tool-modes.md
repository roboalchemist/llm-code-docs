# Source: https://pipedream.com/docs/connect/mcp/tool-modes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tool Modes

> Configure how the Pipedream MCP server exposes and handles tools

## Tool modes

Pipedream MCP supports a few different methods for interacting with tools:

1. [Sub-agent](/connect/mcp/tool-modes#sub-agent) (default)
2. [Full config](/connect/mcp/tool-modes#full-config)
3. [Tools only](/connect/mcp/tool-modes#tools-only)

### **Sub-agent**

When using Pipedream MCP in sub-agent mode, all tools you expose to your LLM take a single input: **`instruction`**.

The Pipedream MCP server passes the **`instruction`** to an LLM to handle the configuration of the main tool using a set of agents with narrowly scoped sets of instructions and additional tools to aid in the configuration and execution of the top-level user prompt.

* The benefit with this approach is that sub-agent mode abstracts some of the complexity with handling things like [remote options](/connect/components/actions#configuring-action-props) and [dynamic props](/connect/components/actions#configuring-dynamic-props), especially for MCP clients that don't automatically [reload tools](https://modelcontextprotocol.io/concepts/tools#tool-discovery-and-updates).
* However, one downside is that as a developer, you lose some of the control and observability in this model.

<Warning>
  While in Beta, Pipedream eats the costs of the LLM tokens in sub-agent mode. We'll likely pass these costs to developers in the future.
</Warning>

<Accordion title="View the schema for the google_sheets-add-single-row tool in sub-agent mode">
  ```javascripton  theme={null}
  {
    "name": "GOOGLE_SHEETS-ADD-SINGLE-ROW",
    "description": "Add a single row of data to Google Sheets. [See the documentation](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append)",
    "inputSchema": {
      "type": "object",
      "properties": {
        "instruction": {
          "type": "string"
        }
      },
      "required": [
        "instruction"
      ],
      "additionalProperties": false,
      "$schema": "http://json-schema.org/draft-07/schema#"
    }
  }
  ```
</Accordion>

### **Full-config**

Full-config mode enables support for loading and configuring dynamic props. This mode provides the most flexibility for tool configuration and is required for certain features like [automatic app discovery](/connect/app-discovery#automatic-app-discovery).

Use `full-config` mode when you need:

* Greater control over tool configuration
* Support for [dynamic props](/connect/api-reference/reload-component-props)
* [Automatic app discovery](/connect/app-discovery#automatic-app-discovery) functionality

<Warning>
  Your MCP client must be able to reload the list of available tools on each turn. See [here](https://github.com/PipedreamHQ/mcp-chat) for example implementations.
</Warning>

#### Configuring dynamic props

* Tools that use [dynamic props](/connect/api-reference/reload-component-props) can't be configured in one shot, as the full prop definition isn't known until certain inputs are defined.
* For example, the full set of props for `google_sheets-add-single-row` aren't known until you configure the `hasHeaders` prop. Once you know if there's a header row, you can retrieve the column names from the header row and make them available as props that can be configured.
* As you call each tool, you should reload the available tools for the server to expose meta tools for configuration, such as `begin_configuration_google_sheets-add-single-row`, which causes the rest of the tools to be removed and only expose tools relevant to the configuration.

#### Enabling full-config mode

To use full-config mode, you need to set 2 parameters:

* Set the `toolMode` to `full-config`
* Pass a `conversationId` in order to maintain state for your end user's conversation

<CodeGroup>
  ```typescript TypeScript focus={9,10} theme={null}
  const transport = new StreamableHTTPClientTransport(new URL(serverUrl), {
    requestInit: {
      headers: {
        "Authorization": `Bearer ${accessToken}`,
        "x-pd-project-id": PIPEDREAM_PROJECT_ID,
        "x-pd-environment": PIPEDREAM_ENVIRONMENT,
        "x-pd-external-user-id": EXTERNAL_USER_ID,
        "x-pd-app-slug": APP_SLUG,
        "x-pd-tool-mode": "full-config", // Enable full-config mode
        "x-pd-conversation-id": CONVERSATION_ID // Maintain conversation state
      }
    }
  });
  ```

  ```python Python focus={11,12} theme={null}
  from mcp import ClientSession
  from mcp.client.streamable_http import streamablehttp_client

  # Configure headers for full-config mode
  headers = {
      "Authorization": f"Bearer {access_token}",
      "x-pd-project-id": PIPEDREAM_PROJECT_ID,
      "x-pd-environment": PIPEDREAM_ENVIRONMENT,
      "x-pd-external-user-id": EXTERNAL_USER_ID,
      "x-pd-app-slug": APP_SLUG,
      "x-pd-tool-mode": "full-config",  # Enable full-config mode
      "x-pd-conversation-id": CONVERSATION_ID  # Maintain conversation state
  }

  # Create MCP client connection with full-config mode
  async with streamablehttp_client(server_url, headers=headers) as (read, write, _):
      async with ClientSession(read, write) as session:
          await session.initialize()
  ```

</CodeGroup>

<Accordion title="View the schema for the google_sheets-add-single-row tool in full-config mode">
  ```javascripton  theme={null}
  {
    "name": "google_sheets-add-single-row",
    "description": "Add a single row of data to Google Sheets. [See the documentation](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append)",
    "inputSchema": {
      "type": "object",
      "properties": {
        "drive": {
          "anyOf": [
            {
              "anyOf": [
                {
                  "not": {}
                },
                {
                  "type": "string"
                }
              ]
            },
            {
              "type": "null"
            }
          ],
          "description": "Defaults to `My Drive`. To select a [Shared Drive](https://support.google.com/a/users/answer/9310351) instead, select it from this list.\n\nYou can use the \"CONFIGURE_COMPONENT\" tool using these parameters to get the values. key: google_sheets-add-single-row, propName: drive"
        },
        "sheetId": {
          "type": "string",
          "description": "Select a spreadsheet or provide a spreadsheet ID\n\nYou can use the \"CONFIGURE_COMPONENT\" tool using these parameters to get the values. key: google_sheets-add-single-row, propName: sheetId"
        },
        "worksheetId": {
          "type": "string",
          "description": "Select a worksheet or enter a custom expression. When referencing a spreadsheet dynamically, you must provide a custom expression for the worksheet.\n\nYou can use the \"CONFIGURE_COMPONENT\" tool using these parameters to get the values. key: google_sheets-add-single-row, propName: worksheetId"
        },
        "hasHeaders": {
          "type": "boolean",
          "description": "If the first row of your document has headers, we'll retrieve them to make it easy to enter the value for each column. Note: When using a dynamic reference for the worksheet ID (e.g. `{{steps.foo.$return_value}}`), this setting is ignored."
        }
      },
      "required": [
        "sheetId",
        "worksheetId",
        "hasHeaders"
      ],
      "additionalProperties": false,
      "$schema": "http://json-schema.org/draft-07/schema#"
    }
  }
  ```
</Accordion>

### **Tools-only**

To handle all tool configuration and calling directly, you should use `tools-only` mode.

<Warning>
  While some tools will be able to be fully configured and executed in a single shot, not all tools will work in tools-only mode.
</Warning>

<Accordion title="View the schema for the google_sheets-add-single-row tool in tools-only mode">
  ```javascripton  theme={null}
  {
    "name": "google_sheets-add-single-row",
    "description": "Add a single row of data to Google Sheets. [See the documentation](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append)",
    "inputSchema": {
      "type": "object",
      "properties": {
        "drive": {
          "anyOf": [
            {
              "anyOf": [
                {
                  "not": {}
                },
                {
                  "type": "string"
                }
              ]
            },
            {
              "type": "null"
            }
          ],
          "description": "Defaults to `My Drive`. To select a [Shared Drive](https://support.google.com/a/users/answer/9310351) instead, select it from this list.\n\nYou can use the \"CONFIGURE_COMPONENT\" tool using these parameters to get the values. key: google_sheets-add-single-row, propName: drive"
        },
        "sheetId": {
          "type": "string",
          "description": "Select a spreadsheet or provide a spreadsheet ID\n\nYou can use the \"CONFIGURE_COMPONENT\" tool using these parameters to get the values. key: google_sheets-add-single-row, propName: sheetId"
        },
        "worksheetId": {
          "type": "string",
          "description": "Select a worksheet or enter a custom expression. When referencing a spreadsheet dynamically, you must provide a custom expression for the worksheet.\n\nYou can use the \"CONFIGURE_COMPONENT\" tool using these parameters to get the values. key: google_sheets-add-single-row, propName: worksheetId"
        },
        "hasHeaders": {
          "type": "boolean",
          "description": "If the first row of your document has headers, we'll retrieve them to make it easy to enter the value for each column. Note: When using a dynamic reference for the worksheet ID (e.g. `{{steps.foo.$return_value}}`), this setting is ignored."
        }
      },
      "required": [
        "sheetId",
        "worksheetId",
        "hasHeaders"
      ],
      "additionalProperties": false,
      "$schema": "http://json-schema.org/draft-07/schema#"
    }
  }
  ```
</Accordion>

Built with [Mintlify](https://mintlify.com).
