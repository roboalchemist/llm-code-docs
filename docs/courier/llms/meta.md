# Source: https://www.courier.com/docs/platform/content/elemental/elements/meta.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Meta

> Set metadata for your notifications including titles and subjects. Meta elements are used by channels like email (subject line) and push (notification title).

## Overview

The meta element contains information describing the notification that may be used by a particular channel or provider. The most important field is the `title` field, which is used as the title for channels that support it (email subject lines, push notification titles, etc.).

**When to use:**

* Set email subject lines
* Set push notification titles
* Provide channel-specific titles
* Include metadata for notification processing

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "meta",
    "title": "Thank you for signing up!"
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
            type: "meta",
            title: "Welcome to our platform!",
          },
          {
            type: "text",
            content: "Thanks for signing up.",
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
                  {"type": "meta", "title": "Welcome to our platform!"},
                  {"type": "text", "content": "Thanks for signing up."},
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For meta elements, this value must be `"meta"`.
</ParamField>

<ParamField path="title" type="string">
  The title to be displayed by supported channels:

  * **Email**: Used as the email subject line
  * **Push**: Used as the push notification title
  * **Inbox**: Used as the notification title

  This field supports Handlebars variables for dynamic content.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization. Can localize the `title` field. See the [Locales documentation](/platform/content/elemental/locales) for more details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The meta element will only be applied for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Examples & Variants

### Basic Title

Simple title for email subject or push notification:

```json  theme={null}
{
  "type": "meta",
  "title": "Thank you for signing up!"
}
```

### Dynamic Title with Handlebars

Use variables in the title:

```json  theme={null}
{
  "type": "meta",
  "title": "Hello, {{first_name}} {{last_name}}"
}
```

The variables come from `message.data` (e.g., `data.first_name`, `data.last_name`).

### Channel-Specific Titles

Different titles for different channels:

```json  theme={null}
{
  "type": "meta",
  "channels": ["email"],
  "title": "Order Confirmation - Check Your Email"
},
{
  "type": "meta",
  "channels": ["push"],
  "title": "Order Confirmed!"
},
{
  "type": "meta",
  "channels": ["sms"],
  "title": "Order #{{order_id}} confirmed"
}
```

### Localized Titles

Localize titles for different languages:

```json  theme={null}
{
  "type": "meta",
  "title": "Welcome!",
  "locales": {
    "es": {
      "title": "¡Bienvenido!"
    },
    "fr": {
      "title": "Bienvenue!"
    },
    "de": {
      "title": "Willkommen!"
    }
  }
}
```

### Combined Dynamic and Localized

Use both Handlebars and localization:

```json  theme={null}
{
  "type": "meta",
  "title": "Order #{{order_id}} Confirmed",
  "locales": {
    "es": {
      "title": "Pedido #{{order_id}} Confirmado"
    },
    "fr": {
      "title": "Commande #{{order_id}} Confirmée"
    }
  }
}
```

### Multiple Meta Elements

Use multiple meta elements for different purposes:

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "meta",
      "channels": ["email"],
      "title": "Your Weekly Newsletter"
    },
    {
      "type": "meta",
      "channels": ["push"],
      "title": "New Newsletter Available"
    },
    {
      "type": "text",
      "content": "Check out this week's updates..."
    }
  ]
}
```

## Channel Usage

### Email

The `title` field becomes the email subject line. This is one of the most important fields for email deliverability and open rates.

```json  theme={null}
{
  "type": "meta",
  "title": "Your order has shipped!"
}
```

### Push Notifications

The `title` field becomes the push notification title. Keep it concise (typically 40-60 characters).

```json  theme={null}
{
  "type": "meta",
  "title": "New message from John"
}
```

### SMS

Meta elements are typically not used for SMS, as SMS doesn't support titles/subjects.

### Inbox

The `title` field is used as the notification title in the inbox.

## Best Practices

* **Keep titles concise**: Especially for push notifications (40-60 characters recommended)
* **Use dynamic content**: Include relevant information like order numbers, names, etc.
* **Localize titles**: Provide translations for all supported languages
* **Test subject lines**: Email subject lines significantly impact open rates
* **Channel-specific optimization**: Tailor titles for each channel's requirements
* **Avoid spam triggers**: Don't use all caps, excessive punctuation, or spam keywords

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For notification body content
* [Channel Element](/platform/content/elemental/elements/channel) - For channel-specific content customization
* [Locales](/platform/content/elemental/locales) - For localizing titles
* [Control Flow](/platform/content/elemental/control-flow) - For channel-specific meta elements
