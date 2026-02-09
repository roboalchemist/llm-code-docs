# Source: https://dev.writer.com/connectors/databricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Databricks connector

> Connect WRITER Agent to Databricks using MCP to access SQL, Unity Catalog functions, and Genie spaces

This guide shows you how to configure the [Databricks](https://www.databricks.com/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like querying Databricks SQL, accessing Unity Catalog functions, and interacting with Genie spaces through Databricks' managed MCP servers.

<Note>
  Databricks managed MCP servers are currently in Beta. Workspace administrators control access to this feature through the Databricks **Previews** page. If you don’t see MCP servers available in your workspace, ask a workspace admin to enable the [Managed MCP Servers preview](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
</Note>

## Set up the Databricks connector

Configure the Databricks connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Databricks connector requires a personal access token to authenticate with a Databricks-managed MCP server.

<Note>
  The Databricks connector only supports organization-managed authentication. WRITER-managed authentication is not available for Databricks.
</Note>

### Obtain your Databricks MCP server URL

Before configuring the connector in AI Studio, locate your MCP server endpoint in your Databricks workspace:

1. Log in to your [Databricks workspace](https://accounts.cloud.databricks.com/)
2. Navigate to **Workspace → Agents → MCP Servers**
3. Select the managed MCP server you want to connect (for example, SQL or Genie)
4. Copy the MCP server endpoint URL for use in [AI Studio](#configure-the-connector-in-ai-studio)

   The URL format depends on the type of MCP server:

   | Server type             | Example URL format                                                          |
   | ----------------------- | --------------------------------------------------------------------------- |
   | Vector search           | `https://<workspace-hostname>/api/2.0/mcp/vector-search/{catalog}/{schema}` |
   | DBSQL                   | `https://<workspace-hostname>/api/2.0/mcp/sql`                              |
   | Genie space             | `https://<workspace-hostname>/api/2.0/mcp/genie/{genie_space_id}`           |
   | Unity Catalog functions | `https://<workspace-hostname>/api/2.0/mcp/functions/{catalog}/{schema}`     |

For more details about Databricks managed MCP servers, see [Databricks MCP documentation](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp).

### Create a Databricks personal access token

Generate a personal access token to authenticate the connector:

1. In your Databricks workspace, select your username in the top-right corner
2. Select **Settings** from the dropdown menu
3. Navigate to **Developer** → **Access tokens**
4. Select **Generate new token**
5. Enter a description (for example, "WRITER MCP connector")
6. Set the token lifetime or leave blank for no expiration
7. Select **Generate** and copy the personal access token for use in [AI Studio](#configure-the-connector-in-ai-studio)

For detailed instructions, see [Databricks personal access tokens documentation](https://docs.databricks.com/en/dev-tools/auth/pat.html).

### Configure the connector in AI Studio

After obtaining your [MCP server URL](#obtain-your-databricks-mcp-server-url) and [personal access token](#create-a-databricks-personal-access-token):

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the Databricks connector
3. Select who has access by default (all users or specific teams)
4. Enter your Databricks MCP server endpoint URL as the **tenant URL**
5. Enter your personal access token as the **API Key**

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [WRITER Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use WRITER Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
