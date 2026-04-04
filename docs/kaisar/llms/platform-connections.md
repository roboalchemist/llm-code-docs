# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/platform-connections.md

# Platform Connections

Connect your AI agents to external platforms and services.

![Platform Connections](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-4da44c7a420da8e6250b2ec33ec9f708b497131f%2Fplatform_connections_list_view.png?alt=media)

## Overview

Platform Connections allow you to integrate your AI agents with external platforms and services such as Discord, Telegram, Slack, webhooks, and more. Manage connections, credentials, and configurations in one centralized location.

## Platform Connections Dashboard

The dashboard displays key metrics at a glance:

**Summary Cards**:

* **Total Connections**: Total number of platform connections configured
* **Connected**: Number of connections currently active and working
* **Error**: Number of connections experiencing errors

## Connection List View

The connections table shows all platform connections with the following information:

**Columns**:

* **Connection**: Connection name and description
* **Platform**: Platform type with icon (Webhook, Telegram, Teams, Discord, Slack)
* **Status**: Current status (Active, Connected, Disconnected, Error)
* **Agents**: Number of agents using this connection
* **Last Connected**: Last connection time
* **Enabled**: Enable/disable toggle
* **Actions**: Quick actions menu

**Filtering and Search**:

* Search by connection name
* Filter by Platform (Webhook, Telegram, Slack, Discord, Teams, etc.)
* Filter by Status (Active, Connected, Disconnected, Error)

## Creating a Platform Connection

Navigate to **Agent Configuration** → **Platform Connections** → Click **Create**

![Create Platform Connection](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-583f735a87bb5b528100cbb9054fa54ea336dc79%2Fplatform_connection_create_form.png?alt=media)

### Basic Information

**Connection Name**\* (Required)

* A descriptive name for this connection
* Example: `Analytics Webhook`
* Helper text: "A descriptive name for this connection"

**Platform**\* (Required)

* Select platform from dropdown: Webhook, Discord, Telegram, Slack, Teams, etc.
* Helper text: "Platform to connect to"

**Description**

* Optional description
* Example: "Custom webhook for analytics and monitoring"
* Helper text: "Optional description"

**Enabled**

* Checkbox to enable/disable the connection
* Default: Unchecked

### Discord Configuration

Expandable section for Discord-specific settings.

**Bot Token**\* (Required)

* Discord bot token
* Helper text: "Discord bot token"

**Guild ID**

* Discord server (guild) ID
* Helper text: "Discord server (guild) ID"

**Client ID**

* Discord application client ID
* Helper text: "Discord application client ID"

### Telegram Configuration

Expandable section for Telegram-specific settings.

**Bot Token**\* (Required)

* Telegram bot token
* Helper text: "Telegram bot token"

**Chat ID**

* Telegram chat/channel ID
* Helper text: "Telegram chat/channel ID"

### Slack Configuration

Expandable section for Slack-specific settings.

**Bot Token**\* (Required)

* Slack bot token
* Helper text: "Slack bot token"

**App Token**

* Slack app-level token
* Helper text: "Slack app-level token"

**Signing Secret**

* Slack signing secret for request verification
* Helper text: "Slack signing secret for request verification"

**Channel ID**

* Slack channel ID
* Helper text: "Slack channel ID"

### Webhook Configuration

Expandable section for Webhook-specific settings.

**Webhook URL**\* (Required)

* Webhook endpoint URL
* Example: `https://analytics.company.com/webhook/dp`
* Helper text: "Webhook endpoint URL"

**Webhook Secret**

* Secret key for webhook authentication
* Example: `webhook_secret_key_encrypted`
* Helper text: "Secret key for webhook authentication"

### Advanced Settings

Expandable section for advanced configuration options.

### Rate Limits

Expandable section for rate limiting configuration.

### Actions

* **Cancel**: Discard and close
* **Create Platform Connection**: Save the connection

## Viewing Connection Details

To view detailed information about a connection:

1. Navigate to **Agent Configuration** → **Platform Connections**
2. Click on a connection from the list
3. View comprehensive details in the modal dialog

![View Platform Connection](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-82bf1a9634a1ed72da324ca8465bea6b48b67e0b%2Fplatform_connection_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Connection Name**: e.g., "Analytics Webhook"
* **Platform**: Webhook, Discord, Telegram, Slack, Teams, etc.
* **Description**: Full description
* **Enabled**: Checkbox status

**Platform-Specific Configuration** (Expandable): All configuration fields are displayed in read-only mode based on the selected platform:

* Discord: Bot Token, Guild ID, Client ID
* Telegram: Bot Token, Chat ID
* Slack: Bot Token, App Token, Signing Secret, Channel ID
* Webhook: Webhook URL, Webhook Secret

**Advanced Settings** (Expandable): Additional configuration options if set.

**Rate Limits** (Expandable): Rate limiting configuration if set.

## Editing a Connection

To update a connection:

1. Open connection details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Platform Connection modal

![Edit Platform Connection](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-ea4e032a3293f507d03020fc0f60470c0a0d6c9b%2Fplatform_connection_edit_form.png?alt=media)

4. Click **Update Platform Connection** to save changes

> \[!NOTE] The Edit form is identical to the Create/View form, but with an "Update Platform Connection" button.

**Editable Fields**:

* ✅ Connection Name
* ✅ Description
* ✅ Enabled (checkbox)
* ✅ All platform-specific configuration fields
* ✅ Advanced Settings
* ✅ Rate Limits
* ❌ Platform (cannot edit after creation)

## Supported Platforms

**Communication Platforms**:

* **Discord**: Bot integration for Discord servers
* **Telegram**: Bot integration for Telegram chats
* **Slack**: Bot integration for Slack workspaces
* **Microsoft Teams**: Integration for Teams channels

**Webhooks**:

* **Custom Webhooks**: HTTP endpoints for custom integrations
* **Outgoing Webhooks**: Send data to external services
* **Incoming Webhooks**: Receive data from external services

**Other Platforms**:

* Additional platforms may be available based on your configuration

## Connection Status

**Active** (Orange):

* Connection is configured but not yet connected
* Waiting for first connection

**Connected** (Green):

* Connection is active and working
* Successfully communicating with platform

**Disconnected** (Gray):

* Connection was previously active but is now disconnected
* May need reconfiguration or credential refresh

**Error** (Red):

* Connection has errors
* Check credentials and configuration
* Review error logs

## Managing Connections

### Enabling/Disabling Connections

To change connection status:

1. Toggle the **Enabled** switch in the list view, OR
2. Edit the connection and check/uncheck the **Enabled** checkbox

**Enabled**: Connection is active and available for agents **Disabled**: Connection is not available for use

### Testing Connections

To test a connection:

1. Open connection details
2. Click **Test Connection** button (if available)
3. Verify connection status

### Rotating Credentials

To update credentials:

1. Edit the connection
2. Update bot tokens, secrets, or API keys
3. Save changes
4. Test the connection

### Deleting a Connection

To remove a connection:

1. Navigate to connection details or list
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] Deleting a connection will affect any agents using it. Make sure to update agent configurations before deleting.

## Security Best Practices

**Credential Management**:

* Store credentials securely
* Rotate tokens regularly
* Use environment-specific credentials
* Never share credentials

**Access Control**:

* Grant minimum required permissions
* Use service accounts where possible
* Monitor access logs
* Audit connection usage

**Network Security**:

* Use HTTPS for webhooks
* Validate webhook signatures
* Implement rate limiting
* Monitor for suspicious activity

## Platform-Specific Guides

### Discord Setup

1. Create a Discord application at [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a bot and copy the bot token
3. Copy the application client ID
4. Copy the server (guild) ID
5. Invite the bot to your server
6. Configure the connection in Kaisar AI Ops

### Telegram Setup

1. Create a bot using [@BotFather](https://t.me/botfather)
2. Copy the bot token
3. Get the chat ID (use [@userinfobot](https://t.me/userinfobot))
4. Configure the connection in Kaisar AI Ops

### Slack Setup

1. Create a Slack app at [Slack API](https://api.slack.com/apps)
2. Enable Socket Mode and get app-level token
3. Add bot token scopes
4. Install app to workspace
5. Copy bot token, app token, and signing secret
6. Get channel ID
7. Configure the connection in Kaisar AI Ops

### Webhook Setup

1. Set up an HTTP endpoint to receive webhooks
2. Implement signature verification
3. Copy the webhook URL
4. Generate a secret key
5. Configure the connection in Kaisar AI Ops

## Troubleshooting

**Connection Errors**:

* Verify credentials are correct
* Check platform API status
* Review error logs
* Test connection manually

**Authentication Issues**:

* Rotate credentials
* Check token expiration
* Verify permissions
* Update scopes if needed

**Rate Limiting**:

* Configure rate limits
* Monitor usage
* Implement backoff strategies
* Contact platform support if needed

## Next Steps

* Configure [Instructions](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/instructions) for platform-specific behavior
* Enable [Tools](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/tools) for platform interactions
* Define [Routes](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/routes) that use these connections
* Assign connections to agents in [Organization → Agents](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents)
