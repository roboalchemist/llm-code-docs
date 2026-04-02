Source: https://docs.slack.dev/reference/scopes/conversations.connect.write

# conversations.connect:write scope

Create Slack Connect invitations for channels that your Slack app has been added to, and accept invitations sent to your Slack app

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

[`Legacy Bot`](/authentication/tokens#legacy-bot)

## Compatible API methods

[`conversations.acceptSharedInvite`](/reference/methods/conversations.acceptsharedinvite)

[`conversations.inviteShared`](/reference/methods/conversations.inviteshared)

## Usage info {#usage-info}

This scope allows your app to use [Slack Connect APIs](/apis/slack-connect/using-slack-connect-api-methods) to initiate or accept invites to conversations with Slack Connect. Once an invite is initiated and accepted, it will still need to be [approved](https://slack.com/help/articles/360050528953-Manage-settings-and-permissions-for-Slack-Connect-channels#choose-who-can-approve-and-manage-channels).
