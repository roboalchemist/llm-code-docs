# Source: https://dev.writer.com/connectors/microsoft-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams connector

> Connect WRITER Agent to Microsoft Teams to access channels, messages, and team collaboration

This guide shows you how to configure the [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like accessing teams, channels, messages, and collaboration settings.

## Set up the Microsoft Teams connector

Configure the Microsoft Teams connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Microsoft Teams connector supports two authentication options:

* **WRITER-managed OAuth** (recommended): Writer provides the OAuth application. No setup required - just authorize access to your Microsoft Teams.
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

* `User.Read` - Read user profile information
* `Team.ReadBasic.All` - Read basic team information
* `Channel.ReadBasic.All` - Read basic channel information
* `ChannelMessage.ReadWrite` - Read and write channel messages
* `ChannelMessage.Read.All` - Read all channel messages
* `ChannelMessage.Send` - Send messages to channels
* `ChannelSettings.ReadWrite.All` - Read and write channel settings
* `Chat.Create` - Create chats
* `Chat.ReadBasic` - Read basic chat information
* `Chat.Read` - Read chat messages
* `Chat.ReadWrite` - Read and write chat messages
* `Chat.ReadWrite.All` - Read and write all chat messages
* `ChatMessage.Read` - Read chat messages
* `ChatMessage.Send` - Send chat messages
* `ChatMember.ReadWrite` - Manage chat members
* `Group.Read.All` - Read all groups
* `Group.ReadWrite.All` - Read and write all groups
* `TeamMember.ReadWrite.All` - Manage team members
* `offline_access` - Maintain access to data

<Note>
  OAuth scopes are fixed per connector and cannot be customized based on enabled tools. When users authorize the Microsoft Teams connector, they will grant all the scopes listed above, even if you disable certain tools in AI Studio.
</Note>

### Configure the connector in AI Studio

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the Microsoft Teams connector
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
