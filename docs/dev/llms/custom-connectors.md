# Source: https://dev.writer.com/home/custom-connectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom connectors

> Create custom connectors from OpenAPI specifications to extend WRITER Agent with your own APIs

This guide shows you how to create custom connectors for WRITER Agent using OpenAPI specifications. After setting up a custom connector, WRITER Agent can perform operations defined in your API specification, enabling integration with internal tools and third-party services not available in the [prebuilt connector library](/home/mcp-gateway#available-connectors).

## Create a custom connector

### Prerequisites

Before creating a custom connector, make sure you have:

* An [OpenAPI definition](https://learn.openapis.org/specification/structure.html) that describes your API
* **Authentication details** for your API, based on the authentication method you choose:
  * **API key**: Key name and optional key prefix
  * **OAuth**: Authorization server URL, access token URL, refresh token URL, and token endpoint authentication method

### Set up the custom connector

Create a custom connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**.

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select **Create custom connector**
3. Upload your OpenAPI specification file (JSON or YAML format)
4. Enter a **Connector name** and **About this connector** description
5. Configure authentication:
   * **API key**: Enter the key name and optional key prefix
   * **OAuth**: Enter your OAuth credentials (authorization server URL, access token URL, refresh token URL, and token endpoint authentication method)
6. Select **Next** to proceed to [tool configuration](#configure-functions)

#### Configure tools

After uploading your [OpenAPI specification](#create-a-custom-connector), the tool configuration screen lets you review and edit the operations defined in your specification.

For each tool, you can:

* **Edit the tool description**: Double-click or select the pencil icon to modify the description. Clear descriptions help WRITER Agent understand when to use each tool.
* **Set the operation type**: Specify whether the tool performs a read, write, update, or delete operation.
* **Update the tool name**: Customize the name that appears in WRITER Agent.

The **Usage** column shows an estimated token count for each tool, including the tool name, description, and parameters. Use this to identify high-cost tools and reduce token usage.

After configuring your tools, select **Save** to create the connector.

## Configure the connector

After [creating a custom connector](#set-up-the-custom-connector), configure it for your organization:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Find your custom connector and select **Configure**
3. Set up access:
   * Choose who can access the connector (all users or specific teams)
   * Select which tools to enable
   * Enter your API key or OAuth credentials, depending on the authentication method configured for the connector

After configuration, the connector appears in your connected integrations and is available to authorized users in WRITER Agent.

## Edit a custom connector

Modify an existing custom connector to update its name, description, or function configurations.

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Find your custom connector and select **Edit connector**
3. Update the connector name or description as needed
4. Select **Next** to modify tool configurations:
   * Edit tool descriptions
   * Update operation types
   * Modify tool names
5. Select **Save** to apply your changes

<Note>
  When editing a custom connector, you cannot change the OpenAPI specification or authentication type. To use a different specification, create a new custom connector.
</Note>

## Delete a custom connector

Deleting a custom connector removes it from your organization's library and disconnects all users.

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Find your custom connector and select **Edit connector** (under the three vertical dots)
3. Select **Delete connector**
4. Confirm the deletion

<Warning>
  Deleting a custom connector removes it from your library and disconnects all users. This action cannot be undone.
</Warning>

## Next steps

* [Configure connectors](/home/mcp-gateway): Learn about connector authentication and access control
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [WRITER Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use WRITER Agent with connected tools
