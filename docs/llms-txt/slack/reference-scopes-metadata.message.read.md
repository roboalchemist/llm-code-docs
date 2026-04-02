Source: https://docs.slack.dev/reference/scopes/metadata.message.read

# metadata.message:read scope

Allows your Slack app to read message metadata in channels that your Slack app has been added to

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

[`Legacy Bot`](/authentication/tokens#legacy-bot)

## Compatible events

[`message_metadata_deleted`](/reference/events/message_metadata_deleted)

[`message_metadata_posted`](/reference/events/message_metadata_posted)

[`message_metadata_updated`](/reference/events/message_metadata_updated)

## Usage info {#usage-info}

Event triggers that listen for message metadata require the `metadata.message:read` scope to be added to the `botScopes` property of your app's manifest. Refer to [Register a custom event type](/tools/deno-slack-sdk/guides/integrating-message-metadata-events#register) for more information.
