# Source: https://dev.writer.com/connectors/gmail.md

# Gmail connector

> Connect WRITER Agent to Gmail to manage emails, search messages, and automate email workflows

This guide shows you how to configure the [Gmail](https://mail.google.com/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like listing email threads, retrieving messages, searching by filters and labels, drafting emails, and sending messages.

## Set up the Gmail connector

Configure the Gmail connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Gmail connector supports two authentication options:

* **WRITER-managed OAuth** (recommended): Writer provides the OAuth application. No setup required, just authorize access to your Gmail account when you first use the connector.
* **Organization-managed OAuth**: Create your own Google OAuth application for custom branding and control.

<Note>
  Most users should choose WRITER-managed OAuth for faster setup. Only use organization-managed OAuth if you need custom branding or have specific security requirements.
</Note>

<Note>
  Google OAuth credentials expire after 6 months of inactivity. If the Gmail connector is not used for 6 months, users will need to re-authenticate.
</Note>

### Create a Google OAuth application (organization-managed only)

If you choose to create a self-managed OAuth application to connect, first create a new Google OAuth application in the Google Cloud Console:

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing project
3. Enable the Gmail API for your project
4. Configure the OAuth consent screen with your application details
5. Create OAuth 2.0 credentials (Web application type)
6. Add the Writer redirect URI to authorized redirect URIs:
   ```
   https://app.writer.com/mcp/oauth/callback
   ```
7. Configure the [required OAuth scopes](#required-oauth-scopes) for your application
8. Copy the client ID and client secret for use in AI Studio

For detailed instructions, see [Google's OAuth 2.0 documentation](https://support.google.com/cloud/answer/15549257).

#### Required OAuth scopes

* `https://www.googleapis.com/auth/gmail.labels` - View and manage labels
* `https://www.googleapis.com/auth/gmail.send` - Send email on the user's behalf
* `https://www.googleapis.com/auth/gmail.readonly` - View email messages and settings
* `https://www.googleapis.com/auth/gmail.compose` - Manage drafts and compose emails
* `https://www.googleapis.com/auth/gmail.insert` - Add emails to the mailbox
* `https://www.googleapis.com/auth/gmail.modify` - Modify email metadata
* `https://mail.google.com/` - Full Gmail access

<Note>
  OAuth scopes are fixed per connector and cannot be customized based on enabled tools. When users authorize the Gmail connector, they will grant all the scopes listed above, even if you disable certain tools in AI Studio.
</Note>

### Configure the connector in AI Studio

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the Gmail connector
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
