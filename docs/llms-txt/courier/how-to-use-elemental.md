# Source: https://www.courier.com/docs/tutorials/content/how-to-use-elemental.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Build Notifications with Elemental

> Create notification content programmatically using Courier Elemental, from simple title-and-body messages to multi-channel templates with conditionals and loops.

Courier Elemental lets you define notification content as JSON instead of using the visual template designer. This is useful when your content is generated dynamically, managed in code, or needs to differ per channel.

This tutorial walks through building a real notification end-to-end: starting with a simple message, then layering in channel-specific content, conditional rendering, and dynamic lists.

## Prerequisites

* A [Courier account](https://app.courier.com/) with at least one configured email provider (e.g. SendGrid)
* Your Courier API key (found in [Settings > API Keys](https://app.courier.com/settings/api-keys))

## Send a Simple Elemental Message

The fastest way to use Elemental is the sugar syntax: just `title` and `body`. Courier automatically converts this into the full Elemental format behind the scenes.

<Steps>
  <Step title="Send with title and body">
    <CodeGroup>
      ```bash cURL icon="terminal" wrap theme={null}
      curl -X POST https://api.courier.com/send \
        -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "message": {
            "to": { "email": "jane@example.com" },
            "content": {
              "title": "Your order has shipped",
              "body": "Hi {{name}}, your order #{{order_id}} is on its way. Expected delivery: {{delivery_date}}."
            },
            "data": {
              "name": "Jane",
              "order_id": "ORD-9042",
              "delivery_date": "Feb 12, 2026"
            }
          }
        }'
      ```

      ```javascript Node.js icon="node-js" theme={null}
      import Courier from "@trycourier/courier";

      const client = new Courier({ apiKey: "your_api_key" });

      const { requestId } = await client.send.message({
        message: {
          to: { email: "jane@example.com" },
          content: {
            title: "Your order has shipped",
            body: "Hi {{name}}, your order #{{order_id}} is on its way. Expected delivery: {{delivery_date}}.",
          },
          data: {
            name: "Jane",
            order_id: "ORD-9042",
            delivery_date: "Feb 12, 2026",
          },
        },
      });

      console.log("Request ID:", requestId);
      ```

      ```python Python icon="python" theme={null}
      from courier import Courier

      client = Courier(api_key="your_api_key")

      response = client.send.message(
          message={
              "to": {"email": "jane@example.com"},
              "content": {
                  "title": "Your order has shipped",
                  "body": "Hi {{name}}, your order #{{order_id}} is on its way. Expected delivery: {{delivery_date}}.",
              },
              "data": {
                  "name": "Jane",
                  "order_id": "ORD-9042",
                  "delivery_date": "Feb 12, 2026",
              },
          },
      )

      print("Request ID:", response.request_id)
      ```
    </CodeGroup>

    This sends an email with the subject "Your order has shipped" and the body text populated with your template variables. No stored template required.
  </Step>

  <Step title="Verify delivery">
    Check the [Message Logs](https://app.courier.com/logs/messages) in the Courier dashboard to confirm the message was delivered and see the rendered output.
  </Step>
</Steps>

<Note>
  The sugar syntax is ideal for simple messages. For multi-element layouts, channel-specific content, or dynamic logic, use the full Elemental format below.
</Note>

## Use Full Elemental Format

Full Elemental gives you complete control over the notification structure. Every template requires a `version` field (`"2022-01-01"`) and an `elements` array.

<Steps>
  <Step title="Build a structured notification">
    This example creates an order confirmation with a heading, body text, and a call-to-action button.

    <CodeGroup>
      ```bash cURL icon="terminal" wrap theme={null}
      curl -X POST https://api.courier.com/send \
        -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "message": {
            "to": { "email": "jane@example.com" },
            "content": {
              "version": "2022-01-01",
              "elements": [
                {
                  "type": "meta",
                  "title": "Order #{{order_id}} Confirmed"
                },
                {
                  "type": "text",
                  "content": "Hi {{name}}, your order has been confirmed and is being prepared."
                },
                {
                  "type": "action",
                  "content": "Track Your Order",
                  "href": "https://example.com/orders/{{order_id}}"
                },
                {
                  "type": "divider"
                },
                {
                  "type": "text",
                  "content": "Questions? Reply to this email or visit our help center.",
                  "text_style": "subtext"
                }
              ]
            },
            "data": {
              "name": "Jane",
              "order_id": "ORD-9042"
            }
          }
        }'
      ```

      ```javascript Node.js icon="node-js" theme={null}
      const { requestId } = await client.send.message({
        message: {
          to: { email: "jane@example.com" },
          content: {
            version: "2022-01-01",
            elements: [
              { type: "meta", title: "Order #{{order_id}} Confirmed" },
              {
                type: "text",
                content: "Hi {{name}}, your order has been confirmed and is being prepared.",
              },
              {
                type: "action",
                content: "Track Your Order",
                href: "https://example.com/orders/{{order_id}}",
              },
              { type: "divider" },
              {
                type: "text",
                content: "Questions? Reply to this email or visit our help center.",
                text_style: "subtext",
              },
            ],
          },
          data: { name: "Jane", order_id: "ORD-9042" },
        },
      });
      ```

      ```python Python icon="python" theme={null}
      response = client.send.message(
          message={
              "to": {"email": "jane@example.com"},
              "content": {
                  "version": "2022-01-01",
                  "elements": [
                      {"type": "meta", "title": "Order #{{order_id}} Confirmed"},
                      {
                          "type": "text",
                          "content": "Hi {{name}}, your order has been confirmed and is being prepared.",
                      },
                      {
                          "type": "action",
                          "content": "Track Your Order",
                          "href": "https://example.com/orders/{{order_id}}",
                      },
                      {"type": "divider"},
                      {
                          "type": "text",
                          "content": "Questions? Reply to this email or visit our help center.",
                          "text_style": "subtext",
                      },
                  ],
              },
              "data": {"name": "Jane", "order_id": "ORD-9042"},
          },
      )
      ```
    </CodeGroup>
  </Step>
</Steps>

## Element Types at a Glance

| Element   | Purpose                              | Key properties                                  |
| --------- | ------------------------------------ | ----------------------------------------------- |
| `meta`    | Sets the email subject / push title  | `title`                                         |
| `text`    | Body text with optional formatting   | `content`, `text_style`, `format`, `align`      |
| `action`  | Button or link                       | `content`, `href`, `style` (`button` or `link`) |
| `image`   | Inline image                         | `src`, `alt_text`, `width`, `href`              |
| `divider` | Horizontal rule                      | `color`                                         |
| `quote`   | Blockquote text                      | `content`, `border_color`                       |
| `html`    | Raw HTML (email only)                | `content`                                       |
| `group`   | Container for conditional/loop logic | `elements`, `if`, `loop`                        |
| `channel` | Channel-specific content branch      | `channel`, `elements`, `raw`                    |
| `columns` | Multi-column layout                  | `elements` (array of `column` nodes)            |

For full property details, see the [Elements Reference](/platform/content/elemental/elements/index).

## Customize Content Per Channel

Use `channel` elements to send different content to different channels from a single API call. This is one of Elemental's most powerful features.

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "channel",
      "channel": "email",
      "elements": [
        { "type": "meta", "title": "Order #{{order_id}} Confirmed" },
        { "type": "text", "content": "Hi {{name}}, here are your order details..." },
        { "type": "image", "src": "{{product_image}}", "alt_text": "{{product_name}}" },
        { "type": "action", "content": "Track Order", "href": "{{tracking_url}}" }
      ]
    },
    {
      "type": "channel",
      "channel": "sms",
      "elements": [
        { "type": "text", "content": "Order #{{order_id}} confirmed! Track: {{tracking_url}}" }
      ]
    },
    {
      "type": "channel",
      "channel": "push",
      "elements": [
        { "type": "meta", "title": "Order Confirmed" },
        { "type": "text", "content": "Your order #{{order_id}} is on its way." }
      ]
    }
  ]
}
```

You can also use the `channels` property on individual elements to show or hide them by channel without wrapping in a `channel` block:

```json  theme={null}
{
  "type": "text",
  "content": "This only appears in email and push",
  "channels": ["email", "push"]
}
```

## Add Conditional Logic

Use the `if` property on any element to conditionally render it based on your data.

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "text",
      "content": "Welcome back, {{name}}!"
    },
    {
      "type": "text",
      "content": "As a premium member, you have early access to new features.",
      "if": "data.tier === 'premium'"
    },
    {
      "type": "action",
      "content": "Upgrade to Premium",
      "href": "https://example.com/upgrade",
      "if": "data.tier !== 'premium'"
    }
  ]
}
```

The `if` expression is evaluated as JavaScript against the `data` object you pass in the send call.

## Render Dynamic Lists

The `loop` property iterates over an array in your data and renders the element once per item.

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "text",
      "content": "Your recent orders:",
      "text_style": "h2"
    },
    {
      "type": "group",
      "loop": "data.orders",
      "elements": [
        {
          "type": "text",
          "content": "**{{$.item.name}}** ; {{$.item.quantity}}x ; ${{$.item.price}}"
        }
      ]
    },
    {
      "type": "divider"
    },
    {
      "type": "text",
      "content": "Total: ${{total}}"
    }
  ]
}
```

Inside a loop, `{{$.item}}` refers to the current item and `{{$.index}}` gives the zero-based index.

<Note>
  The `format` property on text elements supports `"markdown"` for bold, italic, and link rendering. Use double asterisks (`**bold**`) or single asterisks (`*italic*`) in your content strings.
</Note>

## Send to a Stored User Profile

Instead of specifying an email address directly, you can send to a user by their profile ID. Courier looks up their contact details from the stored profile.

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": { "user_id": "user_123" },
        "content": {
          "version": "2022-01-01",
          "elements": [
            { "type": "meta", "title": "Weekly Summary" },
            { "type": "text", "content": "Here is your weekly activity summary, {{name}}." }
          ]
        },
        "data": { "name": "Jane" }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  await client.send.message({
    message: {
      to: { user_id: "user_123" },
      content: {
        version: "2022-01-01",
        elements: [
          { type: "meta", title: "Weekly Summary" },
          { type: "text", content: "Here is your weekly activity summary, {{name}}." },
        ],
      },
      data: { name: "Jane" },
    },
  });
  ```

  ```python Python icon="python" theme={null}
  client.send.message(
      message={
          "to": {"user_id": "user_123"},
          "content": {
              "version": "2022-01-01",
              "elements": [
                  {"type": "meta", "title": "Weekly Summary"},
                  {"type": "text", "content": "Here is your weekly activity summary, {{name}}."},
              ],
          },
          "data": {"name": "Jane"},
      },
  )
  ```
</CodeGroup>

## What's Next

<CardGroup cols={2}>
  <Card title="Elements Reference" icon="file-code" href="/platform/content/elemental/elements/index">
    Complete reference for all Elemental element types and properties
  </Card>

  <Card title="Control Flow" icon="code" href="/platform/content/elemental/control-flow">
    Deep dive into conditionals, loops, references, and channel filtering
  </Card>

  <Card title="Locales" icon="globe" href="/platform/content/elemental/locales">
    Localize Elemental templates for multiple languages
  </Card>

  <Card title="Send API Reference" icon="paper-plane" href="/api-reference/send/send-a-message">
    Full API documentation for sending messages
  </Card>
</CardGroup>
