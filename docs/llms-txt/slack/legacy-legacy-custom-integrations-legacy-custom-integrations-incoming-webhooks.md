Source: https://docs.slack.dev/legacy/legacy-custom-integrations/legacy-custom-integrations-incoming-webhooks

# Legacy custom integrations: incoming webhooks

Incoming webhooks are an efficient way to post messages from apps into Slack.

* * *

## Migrating to app-based webhooks {#migrating-from-legacy}

If you previously created any incoming webhooks using legacy custom integrations, you should switch to using the same functionality with a Slack app instead. To create new app-based webhooks or replicate your existing ones, follow our [Quickstart guide](/app-management/quickstart-app-settings) or the more advanced [Getting started with incoming webhooks guide](/messaging/sending-messages-using-incoming-webhooks).

The majority of your legacy code for sending messages using incoming webhooks should continue to work within a Slack app without much modification; the only thing you can no longer do is customize the destination channel and author identity at runtime.

* * *

## Legacy information {#legacy-info}

Though we recommend that all legacy custom integrations should [migrate to Slack apps](/legacy/legacy-custom-integrations/legacy-custom-integrations-migration), we also understand that some will still need to maintain older integrations. This section contains any information about using incoming webhooks that is specific to the legacy implementation.

#### Legacy management {#legacy-bot-manage}

If you need to configure your legacy integrations, you can access the [Integrations management pages here](https://www.slack.com/apps/manage/custom-integrations).

#### Additional limitations {#additional-limitations}

While you can use legacy incoming webhooks to post messages, they do not have access to [interactive messages features](/legacy/legacy-messaging/legacy-making-messages-interactive). To make your messages interactive, you'll need to [create an incoming webhook with a Slack app](/messaging/sending-messages-using-incoming-webhooks) instead.

**Please note:** it's not possible to send files via webhook. The [`files.upload`](/messaging/working-with-files#uploading_files) API method is the method of choice for this task.

#### Runtime customizations {#legacy-customizations}

Here is a reference list of fields that are used with legacy incoming webhooks to provide runtime customization:

* `username` - override the legacy integration's default name.
* `icon_emoji` - an [emoji code](https://www.webpagefx.com/tools/emoji-cheat-sheet/) string to use in place of the default icon.
* `icon_url` - an icon image URL string to use in place of the default icon. This field has a 255 character limit.
* `channel` - override the legacy integration's default channel. This should be an ID, such as `C8UJ12P4P`.
