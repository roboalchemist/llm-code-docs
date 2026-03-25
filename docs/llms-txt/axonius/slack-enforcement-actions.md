# Source: https://docs.axonius.com/docs/slack-enforcement-actions.md

# Slack Enforcement Actions

The Slack-related Enforcement Actions and the permissions required for each action are as follows:

### [Slack - Send Message via Webhook](/docs/send-slack-message)

Required permissions:

* **Bot tokens** *(Not for Slack Enterprise accounts)* - chat:write

* **User tokens** - chat:write, chat: write:user, chat:write:bot

### [Slack - Send Direct Message to a User](https://docs.axonius.com/axonius-help-docs/docs/slack-send-dm-to-user)

Required permissions:

* **Bot tokens** *(Not for Slack Enterprise accounts)* - chat:write

* **User tokens** - chat:write, chat: write:user, chat:write:bot

### [Slack - Send Direct Message to Assets](/docs/slack-send-dm-to-assets)

Required permissions:

* **Bot tokens** *(Not for Slack Enterprise accounts)* - chat:write

* **User tokens** - chat:write, chat: write:user, chat:write:bot

### [Slack - Create Group](/docs/slack-create-group)

Required Permissions:

* write

* edit

* admin

### [Slack - Create User](/docs/create-slack-user)

Required Permissions:

* write

* edit

* admin

### [Slack - Delete Group](/docs/delete-slack-group)

Required Permissions:

* write

* edit

* admin

### [Slack - Update Group](/docs/slack-update-group)

Required Permissions:

* write

* edit

* admin

### [Slack - Update User](/docs/update-slack-user)

Required Permissions:

* write

* edit

* admin

### [Slack - Suspend User](/docs/suspend-slack-user)

* Requires an OAuth token with admin scope
* The Slack user must be either *Workspace Owner* or *Org Owner* and have access to the following URLs:
  * `https://{sub_domain}.slack.com/admin/billing`
  * `https://{sub_domain}.slack.com/admin/settings`
  * `https://{sub_domain}.slack.com/admin/auth`
  * `https://{sub_domain}.slack.com/apps/manage/settings`

### [Slack - Assign Group to Users](/docs/assign-slack-group-to-user)

Required Permissions:

* write

* edit

* admin

### [Slack - Assign Role to Users](/docs/assign-slack-role-to-user)

Required Permissions:

* write

* edit

* admin

### [Slack - Assign Workspace to Channels](/docs/assign-slack-workspace-to-channel)

Required Permission:

* admin.conversations:write

### [Slack - Assign Resource to Users](/docs/assign-slack-resource-to-user)

Required Permission:

* admin.teams:write

### [Slack - Set Permissions to Users in Channel](/docs/slack-channel-user-permissions)

Required Permission:

* admin.conversations:write

<br />