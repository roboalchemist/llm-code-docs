# Source: https://www.courier.com/docs/platform/content/elemental/elements/html.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# HTML

> Include raw HTML content in your Elemental notifications. Use HTML elements for custom formatting, tables, or complex structures not available in standard Elemental elements.

## Overview

The HTML element allows you to include raw HTML content in your notifications. This gives you complete control over the HTML structure and styling when standard Elemental elements don't meet your needs.

**When to use:**

* Custom HTML structures (tables, complex layouts)
* HTML that requires specific formatting not available in Elemental elements
* Legacy HTML content that needs to be preserved
* Custom styling that requires direct HTML/CSS

<Warning>
  HTML elements are only supported in email channels. They will not render in push, SMS, or other channels. For cross-channel compatibility, use standard Elemental elements instead.
</Warning>

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "html",
    "content": "<h1>Hello, <strong>World!</strong></h1>"
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
            type: "html",
            content: "<h1>Welcome!</h1><p>Thanks for signing up.</p>",
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
                      "type": "html",
                      "content": "<h1>Welcome!</h1><p>Thanks for signing up.</p>",
                  }
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For HTML elements, this value must be `"html"`.
</ParamField>

<ParamField path="content" type="string" required>
  The raw HTML content to be included in the notification. This can include any valid HTML markup, including CSS styles.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization. See the [Locales documentation](/platform/content/elemental/locales) for more details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The HTML element will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Examples & Variants

### Simple HTML

Basic HTML content:

```json  theme={null}
{
  "type": "html",
  "content": "<h1>Hello, <strong>World!</strong></h1>"
}
```

### HTML Table

Create custom HTML tables:

```json  theme={null}
{
  "type": "html",
  "content": "<table style='width: 100%; border-collapse: collapse;'><tr><th style='border: 1px solid #ddd; padding: 8px;'>Item</th><th style='border: 1px solid #ddd; padding: 8px;'>Price</th></tr><tr><td style='border: 1px solid #ddd; padding: 8px;'>Product A</td><td style='border: 1px solid #ddd; padding: 8px;'>$99.99</td></tr></table>"
}
```

### HTML with Handlebars

Use Handlebars variables in HTML:

```json  theme={null}
{
  "type": "html",
  "content": "<div><h2>Order #{{order_id}}</h2><p>Total: ${{order_total}}</p></div>"
}
```

### HTML with Localization

Localize HTML content:

```json  theme={null}
{
  "type": "html",
  "content": "<h1>Welcome!</h1>",
  "locales": {
    "es": {
      "content": "<h1>¡Bienvenido!</h1>"
    },
    "fr": {
      "content": "<h1>Bienvenue!</h1>"
    }
  }
}
```

### Channel-Specific HTML

Only render HTML for email:

```json  theme={null}
{
  "type": "html",
  "channels": ["email"],
  "content": "<div style='background: #f5f5f5; padding: 20px;'>Email-only HTML content</div>"
}
```

## Best Practices

* **Use sparingly**: Prefer standard Elemental elements when possible for better cross-channel compatibility
* **Email only**: Remember that HTML elements only work in email channels
* **Test thoroughly**: HTML rendering can vary across email clients; test in multiple clients
* **Use inline styles**: Email clients often strip `<style>` tags, so use inline CSS
* **Keep it simple**: Complex HTML may not render correctly in all email clients

## Channel Support

* **Email**: ✅ Full support
* **Push**: ❌ Not supported
* **SMS**: ❌ Not supported
* **Inbox**: ❌ Not supported

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For text content (cross-channel compatible)
* [Image Element](/platform/content/elemental/elements/image) - For images
* [Channel Element](/platform/content/elemental/elements/channel) - For channel-specific content customization
* [Control Flow](/platform/content/elemental/control-flow) - For conditional rendering
