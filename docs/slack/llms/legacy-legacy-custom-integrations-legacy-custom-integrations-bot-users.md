Source: https://docs.slack.dev/legacy/legacy-custom-integrations/legacy-custom-integrations-bot-users

# Legacy custom integration: bot users

Building a bot enables conversations between users and your app in Slack.

Discontinuing legacy custom bot creation

You won't be able to create new legacy custom integration bot users or classic apps anymore after June 4, 2024. [Learn how](/changelog/2024-04-discontinuing-new-creation-of-classic-slack-apps-and-custom-bots) this may impact you and your team.

Because we strongly recommend you do not use legacy custom integrations anymore, we recommend reading our [Handling user interaction in your Slack apps guide](/interactivity/handling-user-interaction) instead. It will help you recreate any existing legacy bot functionality.

Though we recommend that all legacy custom integrations should [migrate to Slack apps](/legacy/legacy-custom-integrations/legacy-custom-integrations-migration), we also understand that some will still need to maintain older integrations. This section contains any information about building bots that is specific to the legacy implementation.

#### Legacy management {#legacy-bot-manage}

If you need to configure your legacy integrations, you can access the [Integrations management pages here](https://www.slack.com/apps/manage/custom-integrations).

#### Additional limitations {#additional-limitations}

While you can use legacy bots to post messages, they do not have access to [interactive messages features](/legacy/legacy-messaging/legacy-making-messages-interactive). To make your messages interactive, you'll need to build a [Slack app](/app-management/quickstart-app-settings) instead.

#### API methods for legacy bots {#legacy-methods}

Legacy custom integration bot users, and legacy bot tokens, can be used with a restricted set of Web API methods. These methods are shown below.

Web API method

Description

[`api.test`](/reference/methods/api.test)

Checks API calling code.

[`auth.revoke`](/reference/methods/auth.revoke)

Revokes a token.

[`auth.test`](/reference/methods/auth.test)

Checks authentication & identity.

[`bots.info`](/reference/methods/bots.info)

Gets information about a bot user.

[`calls.add`](/reference/methods/calls.add)

Registers a new Call.

[`calls.end`](/reference/methods/calls.end)

Ends a Call.

[`calls.info`](/reference/methods/calls.info)

Returns information about a Call.

[`calls.participants.add`](/reference/methods/calls.participants.add)

Registers new participants added to a Call.

[`calls.participants.remove`](/reference/methods/calls.participants.remove)

Registers participants removed from a Call.

[`calls.update`](/reference/methods/calls.update)

Updates information about a Call.
