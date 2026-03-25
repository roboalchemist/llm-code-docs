# Source: https://www.courier.com/docs/tutorials/sending/how-to-configure-multi-channel-routing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Configure Multi-Channel Routing

> Configure multi-channel routing in Courier using the routing object in the Send API or the visual designer to prioritize, fallback, or deliver messages across email, SMS, push, and chat channels.

Courier makes it easy to set custom routing rules and ensure your users get exactly the product notification experience you intend.

## Routing in the Send API

The `routing` object allows you to select various channels and decide which ones you want to send messages to.

When the `method` property is defined as `single`, Courier will attempt to the send messages to only one channel. In the example below, it will first attempt SMS and fail since `phone_number` is not included in the user profile. Next, it will attempt to send via email *instead*. If the email is sent successfully, it will not attempt to send a push or chat notification.

```json  theme={null}
"message": {
      "to": {
        "email": "example@email.com",
      },
      "routing": {
        "method": "single",
        "channels": ["email", "sms", "push", "chat"],
      },
    },
```

When the `method` property is defined as `all`, Courier will attempt to send messages to all listed channels. In the example below, Courier will send the message via email and SMS. Since the push and chat profile requirements are not completed, it will not be able to send via those channels.

```json  theme={null}
"to": {
    "phone_number": "123456789",
    "email": "example@email.com",
    "slack": {
        "access_token": "xoxb-xxxxx",
        "email": "user@example.com"
      },
    "apn": {
                "token": "YOUR_APNS_TOKEN"
            }
},
"routing": {
    "method": "all",
    "channels": ["sms", "email", "push", "chat"],
}
```

Ensure that for all channels listed, the profile requirements are met. You can find information about profile requirements for a provider in the respective integration documentation.

### Combining Routing with Channel Conditions

When using custom routing in the Send API, you can combine it with channel conditions using the `message.channels` object.

<Warning>
  **Important**: When you specify a `routing` object, channel conditions configured in the template's default routing strategy are not automatically included. You must explicitly provide channel conditions in `message.channels` if you want them evaluated.
</Warning>

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user_123" },
    "template": "order-confirmation",
    "data": {
      "order_id": "ORD-12345",
      "urgency": "high"
    },
    "routing": {
      "method": "single",
      "channels": ["email", "sms", "push"]
    },
    "channels": {
      "sms": {
        "if": "data.urgency === 'high'"
      },
      "push": {
        "if": "profile.custom.push_enabled === true"
      }
    }
  }
}
```

For more details on channel conditions, see [Channel Settings](/platform/sending/channel-settings#channel-conditions-in-json).

## Routing in the Designer

The priority of the channels you select for your notification are arranged in a top-to-bottom hierarchy. To change priority, simply drag and drop your notification channels.

<Frame caption="Channel Priority">
  <img src="https://mintcdn.com/courier-4f1f25dc/QbP8b2qHqZl-zVnL/assets/tutorials/reorder-channel-priority.png?fit=max&auto=format&n=QbP8b2qHqZl-zVnL&q=85&s=6e7c92548befff1f147d9b576045ebe4" width="906" height="852" data-path="assets/tutorials/reorder-channel-priority.png" />
</Frame>

Courier will attempt to send the notification to the best channel possible, starting from the top and going to the bottom, based on the provided user contact information. You must provide Courier with user's contact information within their [Courier recipient profile](/api-reference/user-profiles/get-a-profile) or via the [Send API](/api-reference/send/send-a-message) call itself.

Take, for example, a notification that is designed to send via `email`, `SMS` or `push`, in that order of priority:

<Frame caption="Overview of the Designer Routing">
  <img src="https://mintcdn.com/courier-4f1f25dc/2GNhpTa50HDyTjlu/assets/tutorials/channel-priority-sample.png?fit=max&auto=format&n=2GNhpTa50HDyTjlu&q=85&s=d225e035a3f42c180bc154d579cd9cbd" width="2854" height="1424" data-path="assets/tutorials/channel-priority-sample.png" />
</Frame>

Courier will first attempt to send the notification via email. If the recipient has an email address in their profile, the notification will send via email only. If they don't have an email address, Courier will look for a phone number. Finally, if they don't have an email or phone number, Courier will look for a push configuration.

You can also choose to 'always send' to a specific channel. In order to do this, select the channel settings and turn on `Always`.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/2GNhpTa50HDyTjlu/assets/tutorials/channel-settings-always-send-to.png?fit=max&auto=format&n=2GNhpTa50HDyTjlu&q=85&s=534c034d822c723260b50c515d05cc52" width="1696" height="988" data-path="assets/tutorials/channel-settings-always-send-to.png" />
</Frame>

Now Courier will always send this notification via email as well as to the best of the other channels.

<Frame caption="Always send to email and best of to sms and push">
  <img src="https://mintcdn.com/courier-4f1f25dc/X4imlV9f_sunHT-I/assets/tutorials/notification-always-send-to.png?fit=max&auto=format&n=X4imlV9f_sunHT-I&q=85&s=f503ed0cab3a9120368ab48d98e50413" width="2156" height="1324" data-path="assets/tutorials/notification-always-send-to.png" />
</Frame>

The routing settings created in the designer can always be overridden using the [preferences API](/api-reference/user-preferences/get-users-preferences). This will override the hierarchy of the channel rules and send the message only via the Integration specified in the recipient's [profile](/api-reference/user-profiles/get-a-profile).

## What's Next

<CardGroup cols={2}>
  <Card title="Send Your First Message" icon="mailbox-flag-up" href="/tutorials/sending/how-to-send-your-first-message">
    End-to-end guide for creating and sending notifications
  </Card>

  <Card title="Configure User Preferences" icon="sliders" href="/tutorials/preferences/how-to-configure-user-preferences">
    Let users control which channels they receive notifications on
  </Card>

  <Card title="Channel Priority Reference" icon="arrow-down-1-9" href="/platform/sending/channel-priority">
    Deep dive into routing strategies and priority rules
  </Card>

  <Card title="Channel Settings Reference" icon="gear" href="/platform/sending/channel-settings">
    Configure conditions, timeouts, and overrides per channel
  </Card>
</CardGroup>
