# Source: https://docs.rootly.com/integrating-with-slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack Integration

> Configuring the Slack integration only takes a few minutes and provides incident management features you can use right from the Slack interface.

<Note>
  For comprehensive installation instructions, screenshots, and video guides, see the detailed [Slack Installation Guide](/integrations/slack/installation).
</Note>

### Before you get started

You should know which Slack plan you're subscribed to. If you're unsure which plan you're on, click the organization name in the top left corner of Slack. The plan will be under the organization's name.

**Supported Slack Plans:**

* Slack Free, Business, or Pro plan - Integrate at the workspace level
* Slack Enterprise Grid - Install at the organizational level across multiple workspaces using [Multi Workspace Channels](https://slack.com/help/articles/115001399587-Add-a-channel-to-multiple-workspaces-in-your-Enterprise-Grid-organization)

<Accordion title="Data Permissions" defaultOpen="false">
  ### Bot Scopes (Standard Integration)

  **Core Permissions:**\
  **bookmarks:write:** Add bookmarks to incident channels for quick access to important resources.\
  **channels:manage:** Create public dedicated Slack channels for incidents.\
  **channels:read:** View basic information about public channels in a workspace.\
  **chat:write + chat:write.public:** Write messages in your dedicated incident Slack channels and respond to different actions.\
  **commands:** Add /rootly and /incident slash commands.\
  **files:read:** Save files associated with pinned or reacted messages to the Rootly timeline.\
  **files:write:** Upload files (like console output) directly to Slack through workflows. We will never delete files in your Slack workspace.\
  **groups:read:** View basic information about private channels that Rootly has been added to.\
  **groups:write:** Create private Slack channels for sensitive incidents (e.g., security).\
  **pins:read:** Add pinned Slack messages to your incident timeline.\
  **pins:write:** Pin important messages in incident channels.\
  **reactions:read:** Add Slack messages to your incident timeline through reactions of your choice.\
  **reactions:write:** React to your messages when successfully added to your incident timeline.\
  **usergroups:read:** View user groups in a workspace (e.g., aliases to invite @security people directly).\
  **usergroups:write:** Manage on-call user groups for scheduling and rotation.\
  **users:read + users:read.email:** View email addresses of people in a workspace for one-click invitations. We will never invite them on your behalf.\
  **users.profile:read:** Display user's full names (Firstname + Lastname) instead of Slack usernames.

  **AI & Assistant Features:**\
  **app\_mentions:read:** View messages that directly mention @rootly in conversations.\
  **channels:history:** Read message history in public channels for AI-powered features.\
  **groups:history:** Read message history in private channels for AI-powered features.\
  **assistant:write:** Enable Rootly AI Assistant capabilities.\
  **im:history:** Read direct message history for AI Assistant interactions.

  ### User Scopes

  **usergroups:write:** Required for on-call user group management (user permission).

  ### Additional Scopes for Slack Enterprise Grid

  **conversations.connect:write:** Connect channels across multiple workspaces in Enterprise Grid organizations.\
  **admin.conversations:write:** Manage conversations at the organization admin level for Enterprise Grid.

  ### Additional User Scopes (When Bot Cannot Create Channels)

  In some Slack workspace configurations, only workspace admins/owners can create channels. When this restriction is in place, Rootly will request these additional user scopes from admin/owner users to create channels on their behalf:

  **channels:write (user scope):** Create and manage public channels on behalf of admin/owner users.\
  **groups:write (user scope):** Create and manage private channels on behalf of admin/owner users.
</Accordion>

### Quick Installation Steps

<Info>
  **Requirements:**

  * **Rootly Account:** Must be an Admin or Owner
  * **Slack Account:** Must be a workspace Admin or Owner (or Organization Admin/Owner for Enterprise Grid)
</Info>

**For Slack Free, Pro, or Business:**

1. Go to **Configuration** > **Integrations** and select **Setup** under the Slack logo
2. Select **Other Slack Plans**
3. Choose your Slack workspace and review permissions
4. Click **Allow** to authorize

**For Slack Enterprise Grid:**

1. Go to **Configuration** > **Integrations** and select **Setup** under the Slack logo
2. Select **Slack Enterprise Grid**
3. Authorize at the organization level
4. Add Rootly to specific workspaces via **Organization settings** > **Integrations** > **Installed apps**

<Note>
  For detailed step-by-step instructions with screenshots and video guides, see the [Slack Installation Guide](/integrations/slack/installation).
</Note>

### Workspace Setup

After connecting Slack, go to **Configuration** > **Slack** to set smart defaults and manage alerts.

* **Set a channel** for incident creation
* **Team notifications**: Set the default announcement channel and alert specific groups for high-severity incidents
* **Smart Reminders**: Have the Rootly app remind users to add roles, update the status page, and keep on task.
* **Updates**: Keep your team updated throughout the incident.
* **Incident Slack Channels**: Set channel naming conventions, add bookmarks to the webapp, and auto-update incident TPOCs
* **Interactions**: Use Emojis to pin messages, add follow actions, and add tasks.
* **Archive channels**: Incident channels can be archived up to a month after resolution.
* **Members**: Require members to connect to Slack or track incident access.


Built with [Mintlify](https://mintlify.com).