# Source: https://www.courier.com/docs/external-integrations/direct-message/discord.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Discord

> Send notifications to Discord users and channels via a Discord bot, with support for embeds, attachments, and provider overrides.

## Setup

To send notifications via Discord, you need a Discord bot. You can use an existing bot or [create a new one](https://discord.com/developers/docs/intro). In Courier, navigate to the [Discord Integration](https://app.courier.com/integrations/catalog/discord) page, enter your bot token, then click "Save."

### Scopes

Update the `bot` scope with the following permissions:

* `View Channels`
* `Send Messages`
* Optional: `Read Message History` to send a message as a reply to another message

[Learn more about Adding Scopes and Permissions.](https://discord.com/developers/docs/getting-started#adding-scopes-and-permissions)

Once the permissions are finalized, go to the generated URL below. This URL will invite the bot to the server and authorize it with the permissions chosen.

## Profile Requirements

The information required in the recipient profile is different based on the type of message you are sending.

### Sending a Direct Message

To send a message to a user, you'll need to supply the Discord profile object with a `user_id`:

1. Go to User Settings on Discord (next to profile on the bottom left),
2. Access the Advanced settings page and enable Developer Mode <Icon icon="square-check" iconType="solid" />,
3. Right click on the user and copy the user ID.

This is not the user tag. The user you are trying to message must be a member of a server the bot is installed in.

```json  theme={null}
{
  "message": {
    // Recipient Profile
    "to": {
      "discord": {
        "user_id": "617099137532932107"
      }
    }
  }
}
```

### Sending a Message to a Channel

To send a message to a channel, you'll need to supply the discord profile object with a `channel_id`:

1. Go to User Settings on Discord (next to profile on the bottom left),
2. Access the Advanced settings page and enable Developer Mode  <Icon icon="square-check" iconType="solid" />,
3. Right click on the channel and copy the channel ID.

The bot must be installed in the server to send to the channel.

```json  theme={null}
{
  "message": {
    // Recipient Profile
    "to": {
      "discord": {
        "channel_id": "768866348853383208"
      }
    }
  }
}
```

## Overrides

You can use a provider override to replace what Courier sends to Discord's [Create Message](https://discord.com/developers/docs/resources/channel#create-message) endpoint. For example, you can add an embed.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "discord": {
        "channel_id": "768866348853383208"
      }
    },
    "providers": {
      "discord": {
        "override": {
          "body": {
            "embed": {
              "title": "Hello, Embed!",
              "description": "This is an embedded message."
            }
          }
        }
      }
    }
  }
}
```
