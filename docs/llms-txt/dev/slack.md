# Source: https://dev.writer.com/connectors/slack.md

# Slack connector

> Connect WRITER Agent to Slack to search messages, manage channels, and automate team communication

This guide shows you how to configure the [Slack](https://slack.com/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like searching messages and files, reading conversations, managing channels, viewing user profiles, and sending messages to Slack workspaces.

## Set up the Slack connector

Configure the Slack connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Slack connector requires organization-managed OAuth authentication.

<Note>
  The Slack connector only supports organization-managed OAuth. You must create your own Slack OAuth application. WRITER-managed OAuth is not available for Slack.
</Note>

### Create a Slack OAuth application

Create an OAuth 2.0 application in Slack:

1. Navigate to the [Slack API Apps page](https://api.slack.com/apps)
2. Create a new app (select "From scratch")
3. Configure OAuth & Permissions with the [required scopes](#required-oauth-scopes)
4. Add the Writer redirect URI to Redirect URLs:
   ```
   https://app.writer.com/mcp/oauth/callback
   ```
5. Install the app to your workspace
6. Copy the client ID and client secret from Basic Information

For detailed instructions, see [Slack's OAuth documentation](https://api.slack.com/authentication/oauth-v2).

#### Required OAuth scopes

* `search:read.public` - Search public channel content
* `search:read.private` - Search private channel content
* `search:read.mpim` - Search multi-party direct messages
* `search:read.im` - Search direct messages
* `search:read.files` - Search files
* `search:read.users` - Search user information
* `chat:write` - Send messages as the user
* `channels:history` - View messages in public channels
* `mpim:history` - View messages in multi-party direct messages
* `im:history` - View messages in direct messages
* `canvases:read` - View Canvas documents
* `canvases:write` - Create and edit Canvas documents
* `users:read` - View users in the workspace
* `users:read.email` - View email addresses of users

<Note>
  OAuth scopes are fixed per connector and cannot be customized based on enabled tools. When users authorize the Slack connector, they will grant all the scopes listed above, even if you disable certain tools in AI Studio.
</Note>

### Configure the connector in AI Studio

After creating your Slack OAuth application:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the Slack connector
3. Select who has access by default (all users or specific teams)
4. Select which tools to enable for your agents
5. Enter your OAuth client ID and client secret
6. Complete the OAuth authorization flow

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [Action Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use Action Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
