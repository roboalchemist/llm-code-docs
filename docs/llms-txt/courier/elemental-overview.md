# Source: https://www.courier.com/docs/platform/content/elemental/elemental-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Elemental Markup Overview

> Courier Elemental is a JSON-based templating format for defining notification content across channels. It supports localization, channel-specific customization, and dynamic logic using structured elements.

## Why Courier Elemental?

Courier Elemental provides a modern, programmatic approach to building notification templates that works seamlessly across all channels. Unlike standard templates that require separate content definitions for each channel, Elemental lets you define your notification structure once and customize it per channel, locale, or user context.

### Elemental vs Standard Templates

|                       | Standard Templates           | Courier Elemental                  |
| --------------------- | ---------------------------- | ---------------------------------- |
| **Format**            | Block-based                  | JSON-based                         |
| **Cross-Channel**     | Separate content per channel | Single structure, channel-adaptive |
| **Localization**      | Manual per channel           | Built-in locale system             |
| **Conditional Logic** | Limited                      | Full support (`if`, `loop`, `ref`) |
| **Programmatic**      | Dashboard/API only           | JSON structure, easy to generate   |
| **Version Control**   | Template-level               | Element-level structure            |
| **Complex Layouts**   | Limited                      | Columns, groups, nested structures |
| **Best For**          | Simple, static notifications | Dynamic, multi-channel, localized  |

<Info>
  Most existing templates use the standard template format. New templates created with Courier Create or Courier Design Studio 2.0 use Elemental format. You can use both formats in the same workspace.
</Info>

## Elemental Capabilities

Courier Elemental provides powerful features for building sophisticated, adaptive notifications. Here's a quick overview of the main capabilities:

### Localization

Automatically serve content in your users' preferred language using Elemental's built-in locale system. Define translations once and Courier handles the rest based on the recipient's locale.

```json  theme={null}
{
  "type": "text",
  "content": "Welcome, {{user_name}}!",
  "locales": {
    "es": {
      "content": "¡Bienvenido, {{user_name}}!"
    },
    "fr": {
      "content": "Bienvenue, {{user_name}} !"
    }
  }
}
```

<Info>
  Learn more about localization in the [Locales documentation](/platform/content/elemental/locales).
</Info>

### Channel-Specific Customization

Customize your notification content for different channels using channel elements or the `channels` property. Send detailed emails and concise SMS from the same template structure.

**Using channel elements:**

```json  theme={null}
{
  "type": "channel",
  "channel": "email",
  "elements": [
    { "type": "text", "content": "Detailed email content..." }
  ]
},
{
  "type": "channel",
  "channel": "sms",
  "elements": [
    { "type": "text", "content": "Short SMS message" }
  ]
}
```

**Using the `channels` property:**

```json  theme={null}
{
  "type": "text",
  "content": "This only appears in email and push",
  "channels": ["email", "push"]
}
```

<Info>
  Learn more about channel customization in the [Control Flow documentation](/platform/content/elemental/control-flow#channels).
</Info>

### Dynamic Logic

Use conditional rendering, loops, and element references to create notifications that adapt to your data and user context.

**Conditional rendering with `if`:**

```json  theme={null}
{
  "type": "text",
  "content": "Premium feature available!",
  "if": "data.user_tier === 'premium'"
}
```

**Iteration with `loop`:**

```json  theme={null}
{
  "type": "group",
  "loop": "data.products",
  "elements": [
    {
      "type": "text",
      "content": "{{$.item.name}} - {{$.item.price}}"
    }
  ]
}
```

**Element references with `ref`:**

```json  theme={null}
{
  "type": "text",
  "content": "Hello",
  "ref": "greeting"
},
{
  "type": "text",
  "content": "This shows if greeting is visible",
  "if": "refs.greeting.visible"
}
```

<Info>
  Learn more about dynamic logic in the [Control Flow documentation](/platform/content/elemental/control-flow).
</Info>

## Where Elemental is Used

Courier Elemental is the modern template format used across Courier's platform:

* **Courier Create**: The embeddable designer component uses Elemental format for all templates
* **Courier Design Studio 2.0**: The new template designer in Courier Studio creates templates in Elemental format
* **Send API**: You can send notifications using Elemental format directly via the Send API
* **Template API**: Elemental templates can be created, updated, and managed via the Templates API

## Construct an Elemental Template

All Courier Elemental templates have the following top level structure. When used in API calls, this structure is passed as the `content` property of the message object:

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    // CourierElement[]
  ]
}
```

**In API calls**, the Elemental template is nested under `message.content`:

```json  theme={null}
{
  "message": {
    "to": { "email": "user@example.com" },
    "content": {
      "version": "2022-01-01",
      "elements": [
        // CourierElement[]
      ]
    }
  }
}
```

### Required Fields

<ParamField path="version" type="string" required>
  Specifies the Elemental format version. The only supported value at this time is `"2022-01-01"`
</ParamField>

<ParamField path="elements" type="CourierElement[]" required>
  Array of Courier Elements. See the [Elements Index](/platform/content/elemental/elements/index) for a complete reference of all available element types.
</ParamField>

<Note>
  The `version` field specifies the Elemental format version. This version identifier ensures compatibility and allows for future format evolution while maintaining backward compatibility.
</Note>

## Understanding Elemental Structure

Elemental templates use a tree-like structure where elements can contain other elements. The `elements` array is the root container, and many element types support nested `elements` arrays of their own.

### Element Nesting

Elements can be nested within other elements to create complex, hierarchical structures:

**Container elements** that support nesting:

* **`group`** - Groups elements together for conditional logic or loops
* **`channel`** - Contains channel-specific element collections
* **`columns`** - Contains `column` elements, which in turn contain their own elements
* **`list`** - Contains `list-item` elements, which can contain text content or nested lists

**Example of nested structure:**

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "channel",
      "channel": "email",
      "elements": [
        {
          "type": "meta",
          "title": "Order Confirmation"
        },
        {
          "type": "group",
          "if": "data.items.length > 0",
          "elements": [
            {
              "type": "columns",
              "elements": [
                {
                  "type": "column",
                  "width": "50%",
                  "elements": [
                    {
                      "type": "image",
                      "src": "{{item.image}}"
                    }
                  ]
                },
                {
                  "type": "column",
                  "width": "50%",
                  "elements": [
                    {
                      "type": "text",
                      "content": "{{item.name}}"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

In this example:

1. The root `elements` array contains a `channel` element
2. The `channel` element contains its own `elements` array with `meta` and `group` elements
3. The `group` element contains a `columns` element
4. The `columns` element contains `column` elements
5. Each `column` contains its own `elements` array with `image` and `text` elements

### Tree Structure Benefits

This hierarchical structure enables:

* **Logical grouping**: Related elements can be grouped together
* **Conditional rendering**: Entire groups can be shown or hidden based on conditions
* **Reusable patterns**: Common element combinations can be encapsulated in groups
* **Channel customization**: Different branches of the tree can target different channels
* **Complex layouts**: Nested structures enable sophisticated multi-column and grid layouts

<Info>
  For a complete reference of all available element types and their properties, see the [Elements Index](/platform/content/elemental/elements/index).
</Info>

## Two Ways to Use Elemental

Courier Elemental offers two formats to suit different needs: **ElementalContentSugar** for simple notifications and **full Elemental** for advanced use cases.

### ElementalContentSugar (Simplified Format)

ElementalContentSugar provides a fast shorthand for basic notifications. Instead of defining a full element structure with the required `version` and `elements` fields outlined above, you can simply use `title` and `body` fields—those required fields aren't needed in the sugar format.

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": { "email": "user@example.com" },
        "content": {
          "title": "Welcome!",
          "body": "Thanks for signing up, {{name}}"
        },
        "data": { "name": "John Doe" }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  const { requestId } = await courier.send({
    message: {
      to: { email: "user@example.com" },
      content: {
        title: "Welcome!",
        body: "Thanks for signing up, {{name}}"
      },
      data: { name: "John Doe" }
    }
  });
  ```

  ```python Python icon="python" theme={null}
  response = client.send(
    message=courier.ContentMessage(
      to=courier.UserRecipient(email="user@example.com"),
      content=courier.ElementalContentSugar(
        title="Welcome!",
        body="Thanks for signing up, {{name}}"
      ),
      data={"name": "John Doe"}
    )
  )
  ```
</CodeGroup>

**When to use ElementalContentSugar:**

* Simple notifications with just a title and body
* Quick inline prototyping and testing
* Basic welcome emails, confirmations, or alerts
* When you don't need advanced features like conditionals, loops, or complex layouts

<Note>
  ElementalContentSugar is automatically converted to full Elemental format by Courier's backend. The `title` becomes a `meta` element, and `body` becomes a `text` element.
</Note>

### Full Elemental Format

Full Elemental format gives you complete control over your notification structure with support for all element types, conditional logic, loops, and complex layouts.

**When to use full Elemental:**

* Multi-channel notifications with channel-specific customization
* Complex layouts with columns, groups, or nested structures
* Dynamic content with conditionals (`if`), loops (`loop`), or references (`ref`)
* Localized content with locale-specific translations
* Advanced styling and customization needs

**Example using full Elemental format:**

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": { "email": "user@example.com" },
        "content": {
          "version": "2022-01-01",
          "elements": [
            {
              "type": "meta",
              "title": "Welcome to {{company_name}}, {{user_name}}!"
            },
            {
              "type": "image",
              "src": "https://example.com/welcome-banner.jpg",
              "alt_text": "Welcome Banner"
            },
            {
              "type": "text",
              "content": "Hi {{user_name}}, we're excited to have you join us! Your account is now active and ready to use."
            },
            {
              "type": "action",
              "content": "Get Started",
              "href": "https://app.example.com/dashboard"
            }
          ]
        },
        "data": {
          "user_name": "Alex",
          "company_name": "Acme Corp"
        }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  const { requestId } = await courier.send({
    message: {
      to: { email: "user@example.com" },
      content: {
        version: "2022-01-01",
        elements: [
          {
            type: "meta",
            title: "Welcome to {{company_name}}, {{user_name}}!"
          },
          {
            type: "image",
            src: "https://example.com/welcome-banner.jpg",
            alt_text: "Welcome Banner"
          },
          {
            type: "text",
            content: "Hi {{user_name}}, we're excited to have you join us! Your account is now active and ready to use."
          },
          {
            type: "action",
            content: "Get Started",
            href: "https://app.example.com/dashboard"
          }
        ]
      },
      data: {
        user_name: "Alex",
        company_name: "Acme Corp"
      }
    }
  });
  ```

  ```python Python icon="python" theme={null}
  response = client.send(
    message=courier.ContentMessage(
      to=courier.UserRecipient(email="user@example.com"),
      content={
        "version": "2022-01-01",
        "elements": [
          {
            "type": "meta",
            "title": "Welcome to {{company_name}}, {{user_name}}!"
          },
          {
            "type": "image",
            "src": "https://example.com/welcome-banner.jpg",
            "alt_text": "Welcome Banner"
          },
          {
            "type": "text",
            "content": "Hi {{user_name}}, we're excited to have you join us! Your account is now active and ready to use."
          },
          {
            "type": "action",
            "content": "Get Started",
            "href": "https://app.example.com/dashboard"
          }
        ]
      },
      data={
        "user_name": "Alex",
        "company_name": "Acme Corp"
      }
    )
  )
  ```
</CodeGroup>

<Tip>
  **Pro Tip**: Start with ElementalContentSugar for basic notifications, then upgrade to full Elemental when you need advanced features like conditionals, loops, or complex layouts.
</Tip>

## Use Cases

### Multi-Channel Order Confirmation

Send order confirmations that adapt to each channel—detailed email with product images and order summary, concise SMS with tracking number, and push notification with order status.

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "channel",
      "channel": "email",
      "elements": [
        {
          "type": "meta",
          "title": "Order #{{order_number}} Confirmed"
        },
        {
          "type": "text",
          "content": "Hi {{customer_name}}, your order has been confirmed!"
        },
        {
          "type": "image",
          "src": "{{product_image}}",
          "alt_text": "{{product_name}}"
        },
        {
          "type": "action",
          "content": "Track Order",
          "href": "https://example.com/orders/{{order_number}}"
        }
      ]
    },
    {
      "type": "channel",
      "channel": "sms",
      "elements": [
        {
          "type": "text",
          "content": "Order #{{order_number}} confirmed! Track: {{tracking_url}}"
        }
      ]
    }
  ]
}
```

### Localized Welcome Messages

Welcome new users in their preferred language with automatic locale detection.

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "text",
      "content": "Welcome, {{user_name}}!",
      "locales": {
        "es": {
          "content": "¡Bienvenido, {{user_name}}!"
        },
        "fr": {
          "content": "Bienvenue, {{user_name}} !"
        }
      }
    }
  ]
}
```

### Dynamic Product Lists

Display product recommendations that adapt based on user preferences and inventory.

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "text",
      "content": "Recommended for you:",
      "text_style": "h2"
    },
    {
      "type": "group",
      "loop": "data.recommended_products",
      "elements": [
        {
          "type": "text",
          "content": "{{$.item.name}} - {{$.item.price}}",
          "if": "{{$.item.in_stock}}"
        }
      ]
    }
  ]
}
```

## Related Documentation

<CardGroup cols={2}>
  <Card title="Elements" icon="file-code" href="/platform/content/elemental/elements/index">
    Complete reference for all Elemental element types, including text, image, action, channel, and more.
  </Card>

  <Card title="Control Flow" icon="code" href="/platform/content/elemental/control-flow">
    Learn how to use conditionals (`if`), loops (`loop`), references (`ref`), and channel filtering.
  </Card>

  <Card title="Locales" icon="globe" href="/platform/content/elemental/locales">
    Guide to localizing your Elemental templates for multiple languages and regions.
  </Card>

  <Card title="Export to Elemental" icon="download" href="/platform/content/elemental/export-to-elemental">
    Convert Designer-built notifications into Courier Elemental JSON format.
  </Card>
</CardGroup>
