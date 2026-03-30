# Source: https://www.courier.com/docs/platform/content/elemental/elements/channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Channel

> Customize notification content based on the delivery channel. Use channel elements to provide different content for email, push, SMS, and other channels.

## Overview

The channel element allows you to customize notification content based on which channel the notification is sent through. For example, you can display a detailed message in email and a more concise message in push notifications.

**When to use:**

* Provide channel-specific content (different content for email vs push vs SMS)
* Use raw channel data for provider-specific formats (MJML for email, Slack blocks, etc.)
* Create channel-specific layouts and structures

<Warning>
  Channel elements are only valid as top-level elements. You cannot nest channel elements. If a channel element is specified at the top level, all sibling elements must be channel elements.
</Warning>

<Tip>
  **Alternative**: Most elements support a `channels` property that allows you to selectively display individual elements on a per-channel basis. See the [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</Tip>

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "channel",
    "channel": "email",
    "elements": [
      {
        "type": "meta",
        "title": "My Subject"
      },
      {
        "type": "text",
        "content": "My email body"
      }
    ]
  }
  ```

  ```javascript Node.js icon="node-js" lines theme={null}
  const { CourierClient } = require("@trycourier/courier");

  const courier = new CourierClient({
    authorizationToken: process.env.COURIER_AUTH_TOKEN,
  });

  await courier.send({
    message: {
      to: { email: "user@example.com" },
      content: {
        version: "2022-01-01",
        elements: [
          {
            type: "channel",
            channel: "email",
            elements: [
              {
                type: "meta",
                title: "Welcome Email",
              },
              {
                type: "text",
                content: "Thanks for signing up! Check your email for details.",
              },
            ],
          },
          {
            type: "channel",
            channel: "default",
            elements: [
              {
                type: "meta",
                title: "Welcome",
              },
              {
                type: "text",
                content: "Thanks for signing up!",
              },
            ],
          },
        ],
      },
    },
  });
  ```

  ```python Python icon="python" lines theme={null}
  import os
  from trycourier import Courier

  client = Courier(auth_token=os.environ["COURIER_AUTH_TOKEN"])

  client.send_message(
      message={
          "to": {"email": "user@example.com"},
          "content": {
              "version": "2022-01-01",
              "elements": [
                  {
                      "type": "channel",
                      "channel": "email",
                      "elements": [
                          {"type": "meta", "title": "Welcome Email"},
                          {
                              "type": "text",
                              "content": "Thanks for signing up! Check your email for details.",
                          },
                      ],
                  },
                  {
                      "type": "channel",
                      "channel": "default",
                      "elements": [
                          {"type": "meta", "title": "Welcome"},
                          {"type": "text", "content": "Thanks for signing up!"},
                      ],
                  },
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For channel elements, this value must be `"channel"`.
</ParamField>

<ParamField path="channel" type="string" required>
  The channel the contents of this element should be applied to. Can be:

  * Standard channels: `"email"`, `"push"`, `"direct_message"`, `"sms"`
  * Provider names: `"slack"`, `"discord"`, `"teams"`, etc.
  * `"default"` - applies to all channels not explicitly specified
</ParamField>

<ParamField path="elements" type="CourierElement[]">
  An array of Elemental elements to apply to the channel. If `raw` has not been specified, `elements` is required.
</ParamField>

<ParamField path="raw" type="object">
  Raw data to apply to the channel. This allows you to provide channel-specific formats like MJML for email, Slack blocks, or webhook payloads. If `elements` has not been specified, `raw` is required.
</ParamField>

## Examples & Variants

### Using Elements

Provide different Elemental content per channel:

```json  theme={null}
{
  "type": "channel",
  "channel": "email",
  "elements": [
    {
      "type": "meta",
      "title": "Order Confirmation"
    },
    {
      "type": "text",
      "content": "Your order #{{order_id}} has been confirmed. We'll send you tracking information once your order ships."
    },
    {
      "type": "action",
      "content": "View Order",
      "href": "https://app.example.com/orders/{{order_id}}"
    }
  ]
},
{
  "type": "channel",
  "channel": "push",
  "elements": [
    {
      "type": "meta",
      "title": "Order Confirmed"
    },
    {
      "type": "text",
      "content": "Order #{{order_id}} confirmed"
    }
  ]
}
```

### Using Raw Data

Use raw channel data for provider-specific formats:

#### Email with MJML

```json  theme={null}
{
  "type": "channel",
  "channel": "email",
  "raw": {
    "subject": "Order Confirmation",
    "html": "<mjml><mj-body><mj-section><mj-column><mj-text>Your order has been confirmed!</mj-text></mj-column></mj-section></mj-body></mjml>",
    "text": "Your order has been confirmed!",
    "transformers": ["handlebars", "mjml"]
  }
}
```

#### Slack

```json  theme={null}
{
  "type": "channel",
  "channel": "slack",
  "raw": {
    "text": "Hello World!",
    "blocks": [
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "Your order has been confirmed!"
        }
      }
    ]
  }
}
```

#### Webhook

```json  theme={null}
{
  "type": "channel",
  "channel": "webhook",
  "raw": {
    "payload": {
      "body": {
        "event": "order.confirmed",
        "order_id": "{{order_id}}",
        "timestamp": "{{timestamp}}"
      }
    }
  }
}
```

### Default Channel

Use `"default"` to provide content for all channels not explicitly specified:

```json  theme={null}
{
  "type": "channel",
  "channel": "email",
  "elements": [
    {
      "type": "text",
      "content": "Detailed email content here"
    }
  ]
},
{
  "type": "channel",
  "channel": "default",
  "elements": [
    {
      "type": "text",
      "content": "Content for push, SMS, and other channels"
    }
  ]
}
```

## Channel-Specific Considerations

### Email

* Supports full Elemental elements or raw HTML/MJML
* Can use `raw.subject` for email subject line
* Supports `transformers` array for templating engines

### Push

* Typically uses `meta.title` for notification title
* Content should be concise due to character limits
* Supports action buttons via action elements

### SMS

* Very limited character count
* Best for short, essential messages
* No rich formatting support

### Direct Message (Slack, Discord, Teams, etc.)

* Provider-specific formats via `raw` property
* Can use provider-specific block structures
* Supports rich interactive elements per provider

## Related Elements

* [Meta Element](/platform/content/elemental/elements/meta) - For channel-specific titles and subjects
* [Text Element](/platform/content/elemental/elements/text) - For channel-specific body content
* [Action Element](/platform/content/elemental/elements/action) - For channel-specific call-to-action buttons
* [Control Flow](/platform/content/elemental/control-flow#channel-specific-content) - For using `channels` property on individual elements
