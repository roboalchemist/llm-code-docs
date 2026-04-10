# Source: https://dev.writer.com/connectors/microsoft-onedrive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft OneDrive connector

> Connect WRITER Agent to OneDrive to access and manage files and folders

This guide shows you how to configure the [Microsoft OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like accessing files and folders stored in OneDrive, reading file content, managing documents, and searching across cloud storage.

## Set up the Microsoft OneDrive connector

Configure the Microsoft OneDrive connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Microsoft OneDrive connector supports two authentication options:

* **WRITER-managed OAuth** (recommended): Writer provides the OAuth application. No setup required - just authorize access to your OneDrive.
* **Organization-managed OAuth**: Create your own Microsoft OAuth application for custom branding and control.

<Note>
  Most users should choose WRITER-managed OAuth for faster setup. Only use organization-managed OAuth if you need custom branding or have specific security requirements.
</Note>

### Create a Microsoft OAuth application (organization-managed only)

If you choose to create a self-managed OAuth application to connect, first create a new Microsoft OAuth application in Microsoft Entra ID (Azure AD):

1. Navigate to the [Microsoft Entra admin center](https://entra.microsoft.com/)
2. Go to Applications > App registrations
3. Create a new registration
4. Configure authentication with Web platform
5. Add the Writer redirect URI to Redirect URIs:
   ```
   https://app.writer.com/mcp/oauth/callback
   ```
6. Add API permissions for the [required Microsoft Graph scopes](#required-oauth-scopes)
7. Create a client secret in Certificates & secrets
8. Copy the application (client) ID and client secret

For detailed instructions, see [Microsoft's OAuth 2.0 documentation](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow).

#### Required OAuth scopes

* `Files.ReadWrite` - Read and write user files
* `User.Read` - Read user profile information
* `offline_access` - Maintain access to data

<Note>
  OAuth scopes are fixed per connector and cannot be customized based on enabled tools. When users authorize the Microsoft OneDrive connector, they will grant all the scopes listed above, even if you disable certain tools in AI Studio.
</Note>

### Configure the connector in AI Studio

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the Microsoft OneDrive connector
3. Select who has access by default (all users or specific teams)
4. Select the connection type:
   * **Level**: User level (each user authenticates their own account) or org level (shared connection to a single account)
   * **Managed by**: WRITER-managed or self-managed (your own OAuth app)
5. Select which tools to enable for your agents
6. Enter your OAuth client ID and client secret (if using self-managed OAuth)
7. Complete the OAuth authorization flow

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [Action Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use Action Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
