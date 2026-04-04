Source: https://docs.slack.dev/legacy/legacy-custom-integrations/legacy-custom-integrations-slash-commands

# legacy custom integrations: slash commands

Slash Commands let users trigger an interaction with your app directly from the message box in Slack.

Because we strongly recommend you do not use legacy custom integrations anymore, you should instead use the similar feature in Slack apps. Our [guide to Getting Started with Slash Commands](/interactivity/implementing-slash-commands) will walk you through the process of enabling this functionality in a Slack app.

* * *

## Migrating from legacy Slash Commands {#migrating-from-legacy}

If you previously created any commands using legacy integrations, you should switch to using the same functionality with a Slack app instead. To do this you need to follow the [Getting Started with Slash Commands guide](/interactivity/implementing-slash-commands) and create new commands to replicate your existing ones.

The majority of your legacy code for handling and responding to Slash Commands should continue to work within a Slack app without much modification.

* * *

## Legacy information {#legacy-info}

Though we recommend that all legacy custom integrations should [migrate to Slack apps](/legacy/legacy-custom-integrations/legacy-custom-integrations-migration), we also understand that some will still need to maintain older integrations. This section contains any information about using Slash Commands that is specific to the legacy implementation.

#### Legacy management {#legacy-bot-manage}

If you need to configure your legacy integrations, you can access the [Integrations management pages here](https://www.slack.com/apps/manage/custom-integrations).

#### Additional limitations {#additional-limitations}

While you can respond to legacy Slash Commands to post messages in the same way as Slack Apps can, legacy integrations do not have access to [interactive messages features](/legacy/legacy-messaging/legacy-making-messages-interactive). To make your messages interactive, you'll need to [create a Slash Command with a Slack app](/interactivity/implementing-slash-commands) instead.
