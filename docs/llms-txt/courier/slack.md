# Source: https://www.courier.com/docs/external-integrations/direct-message/slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack

> Send Slack messages with Courier by creating a Slack app, configuring it in Courier, designing a notification template, and delivering messages via the Send API. This guide covers setup, message targeting, advanced features, and troubleshooting.

## Prerequisites

**To get started, you'll need:**

* A Courier account ([Sign up](https://app.courier.com/signup))
* A Slack account ([Sign up](https://slack.com/get-started))

**What you'll do:**

1. Add the Slack integration in Courier
2. Create and configure a Slack app
3. Design a notification template
4. Send a test message

<Note>
  * [Courier API Reference](/reference/get-started)
  * [Slack API Documentation](https://api.slack.com/)
  * [Slack Block Kit Builder](https://app.slack.com/block-kit-builder/)
</Note>

***

## Step-by-Step: Send Your First Slack Message

<Steps>
  <Step title="Add Slack Integration in Courier">
    Once logged in to Courier, go to the [Integrations page](https://app.courier.com/integrations) and select Slack. Click "Install" to add the integration.

    <Frame caption="Courier Slack Integration">
            <img src="https://mintcdn.com/courier-4f1f25dc/ZduYe6WElFIzD_rq/assets/external-integrations/direct-message/slack-integration.png?fit=max&auto=format&n=ZduYe6WElFIzD_rq&q=85&s=28c317f213d358dfcc053d8bec866d08" alt="" width="1488" height="1622" data-path="assets/external-integrations/direct-message/slack-integration.png" />
    </Frame>
  </Step>

  <Step title="Create and Configure a Slack App">
    1. Go to the [Slack Apps page](https://api.slack.com/apps) and click "Create an App".
    2. Choose "From scratch", give your app a name, and select your development workspace.
    3. Under "OAuth & Permissions", add these Bot Token Scopes: `chat:write`, `im:write`, `users:read`, `users:read.email`.
    4. Click "Install App to Workspace" and authorize.
    5. Copy the **Bot User OAuth Access Token** (starts with `xoxb-`).

    <Frame caption="Slack OAuth Scopes">
            <img src="https://mintcdn.com/courier-4f1f25dc/ZduYe6WElFIzD_rq/assets/external-integrations/direct-message/slack-oauth-scopes.png?fit=max&auto=format&n=ZduYe6WElFIzD_rq&q=85&s=57825ddd579f280fddab69ea39bd5111" alt="Slack OAuth Scopes" width="1279" height="920" data-path="assets/external-integrations/direct-message/slack-oauth-scopes.png" />
    </Frame>
  </Step>

  <Step title="Design a Slack Notification Template">
    Go to the Courier [Assets page](https://app.courier.com/assets/templates) and click <b>+ New > Message Template</b>.
    Select Slack from your list of integrations.
    In the sidebar, click the newly added Slack block to open the Slack template editor.
    Add your desired message content to the template.
  </Step>

  <Step title="Send a Test Message">
    Click <b>Preview</b>, then select <b>Create Test Event</b>.
    Enter your bot token in the <b>Access Token</b> field.
    Click <b>Send</b>—your message should appear in Slack!
  </Step>
</Steps>

***

## Message Targeting Reference

Courier supports sending Slack messages to users and channels in several ways. Here are the most common targeting methods:

<CodeGroup>
  ```json Direct Message by Email theme={null}
  {
    "message": {
      "to": {
        "slack": {
          "access_token": "xoxb-xxxxx",
          "email": "user@example.com"
        }
      }
    }
  }
  ```

  ```json Direct Message by User ID theme={null}
  {
    "message": {
      "to": {
        "slack": {
          "access_token": "xoxb-xxxxx",
          "user_id": "UEFNTF6QL"
        }
      }
    }
  }
  ```

  ```json Message a Channel theme={null}
  {
    "message": {
      "to": {
        "slack": {
          "access_token": "xoxb-xxxxx",
          "channel": "CL2MR6HEX"
        }
      }
    }
  }
  ```
</CodeGroup>

<Tip>
  <b>Order of Precedence:</b> If you provide more than one of <code>channel</code>, <code>user\_id</code>, or <code>email</code>, Courier will use them in this order: <b>channel</b> > <b>user\_id</b> > <b>email</b>.
</Tip>

***

## Overrides

You can override the payload sent to Slack's [chat.postMessage](https://api.slack.com/methods/chat.postMessage) using `providers.slack.override.body`. This is useful for advanced formatting, interactivity, and threading.

#### Unfurl Links

```json  theme={null}
{
  "providers": {
    "slack": {
      "override": {
        "body": {
          "unfurl_links": true
        }
      }
    }
  }
}
```

#### Slack Blocks (Block Kit)

Send rich, interactive layouts using [Slack blocks](https://api.slack.com/block-kit):

```json  theme={null}
{
  "providers": {
    "slack": {
      "override": {
        "body": {
          "blocks": [
            { "type": "header", "text": { "type": "plain_text", "text": "Welcome!" } },
            { "type": "section", "text": { "type": "mrkdwn", "text": "This is a *section* block." } }
          ],
          "text": "Fallback plain text."
        }
      }
    }
  }
}
```

Design and preview your blocks visually with the [Slack Block Kit Builder](https://app.slack.com/block-kit-builder/).

#### Replying in a Thread

To reply to a thread, set the `thread_ts` value:

```json  theme={null}
{
  "providers": {
    "slack": {
      "override": {
        "body": {
          "thread_ts": "1234567890.123456"
        }
      }
    }
  }
}
```

### Mentioning Users

Mention a user in your message using `<@USER_ID>` syntax in your template:

```
Hello <@UEFNTF6QL>, you have a new notification!
```

You can also use variables for dynamic mentions.

### Slash Command Responses

If responding to a [Slash Command](https://api.slack.com/interactivity/slash-commands), use the `response_url` as an incoming webhook:

```json  theme={null}
{
  "to": {
    "slack": {
      "incoming_webhook": {
        "url": "https://hooks.slack.com/commands/1234/5678"
      }
    }
  }
}
```

Set `override.slack.body.response_type` to `in_channel` or `ephemeral` as needed.

### Incoming Webhooks

You can send messages to a channel using a Slack [Incoming Webhook](https://api.slack.com/messaging/webhooks):

```json  theme={null}
{
  "to": {
    "slack": {
      "incoming_webhook": {
        "url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
      }
    }
  }
}
```

### Updating Notifications

To update a previously sent Slack message, set a "replacement key" (usually `ts`) in your notification template's Slack channel settings. Courier will use this key to update the message instead of posting a new one.

***

## Troubleshooting

* **Missing or incorrect Slack scopes:**
  * Double-check your app has all required scopes (`chat:write`, `im:write`, `users:read`, `users:read.email`, and `chat:write.public` for channels).
  * Reinstall your Slack app after updating scopes.

* **Bot not invited to channel:**
  * Make sure your Slack app/bot is a member of the channel you want to message.

* **Invalid or missing tokens:**
  * Ensure you are using the correct Bot User OAuth Access Token (starts with `xoxb-`).
  * Never use a user token or an expired token.

* **Permission errors or message not delivered:**
  * Check the [Courier Message Logs](https://app.courier.com/logs/messages) for error details and troubleshooting tips.

* **User or channel not found:**
  * Double-check the email, user\_id, or channel ID. For channels, copy the ID from the Slack URL.

* **Message Truncated:**
  * Slack blocks [limit the characters](https://api.slack.com/reference/block-kit/blocks#section) in a single section to 3k characters. Courier automatically truncates Slack messages over 3k characters by removing escape and formating characters that are added by Slack after submitting the block.

If you're still stuck, reach out to Courier support at [support@courier.com](mailto:support@courier.com).
