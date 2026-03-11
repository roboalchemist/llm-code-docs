# Source: https://www.courier.com/docs/external-integrations/direct-message/intro-to-direct-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat & Direct Message Providers

> Overview of Courier's chat and direct message integrations, including provider directory, profile targeting, and provider-level overrides.

Courier integrates with chat and direct message platforms to deliver notifications to users in the apps they already use. Each provider requires specific profile fields to identify the recipient, such as a Slack user ID, Discord channel ID, or phone number.

## Available Providers

| Provider                                                                       | Description                                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [Slack](/external-integrations/direct-message/slack)                           | Workspace messaging with Block Kit, threading, webhooks, and slash command support |
| [Microsoft Teams](/external-integrations/direct-message/microsoft-teams)       | Enterprise messaging via Teams apps and bots with Adaptive Card support            |
| [Discord](/external-integrations/direct-message/discord)                       | Send direct messages or channel messages via a Discord bot                         |
| [WhatsApp](/external-integrations/direct-message/whatsapp)                     | WhatsApp messaging via Twilio with template verification                           |
| [Facebook Messenger](/external-integrations/direct-message/facebook-messenger) | Messenger delivery using Page-Scoped IDs                                           |
| [Viber](/external-integrations/direct-message/viber)                           | Direct messages via a Viber bot account                                            |
| [Stream Chat](/external-integrations/direct-message/stream-chat)               | In-app messaging via the Stream Chat API                                           |
| [Chat API](/external-integrations/direct-message/chat)                         | WhatsApp and other chat delivery via the Chat API service                          |

<Tip>
  Can't find a provider? Send us a chat or email [support@courier.com](mailto:support@courier.com)
</Tip>

## Provider Overrides

Overrides let you modify parts of a message at send time without changing your notification template. They are passed in the `message` payload of a [Send request](/api-reference/send/send-a-message) and applied just before Courier hands the message off to the provider.

Provider overrides (`message.providers.<key>.override`) target a single provider and can pass through fields specific to that provider's API. Most chat providers support:

* **`body`** overrides to change the message content, add embeds, blocks, or other provider-specific payload fields.
* **`config`** overrides to swap credentials or endpoint URLs at send time.

Each provider page documents its supported override schema.
