# Source: https://www.courier.com/docs/platform/content/elemental/elements/action.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Action

> Create clickable buttons and links in your Elemental notifications. Action elements support styling, alignment, and localization.

## Overview

The action element allows users to execute actions in your notifications. It can be rendered as either a button or a link, depending on the channel and styling options you choose.

**When to use:**

* Add call-to-action buttons (e.g., "Sign Up", "View Order", "Confirm Email")
* Create clickable links within notifications
* Provide interactive elements that direct users to specific URLs

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "action",
    "content": "Click me",
    "href": "https://example.com"
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
            type: "action",
            content: "View Dashboard",
            href: "https://app.example.com/dashboard",
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
                      "type": "action",
                      "content": "View Dashboard",
                      "href": "https://app.example.com/dashboard",
                  }
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For action elements, this value must be `"action"`.
</ParamField>

<ParamField path="content" type="string" required>
  The text content of the action shown to the user. This is the label displayed on the button or link.
</ParamField>

<ParamField path="href" type="string" required>
  The target URL of the action. When clicked, the user will be directed to this URL.
</ParamField>

<ParamField path="action_id" type="string">
  A unique identifier used to identify the action when it is executed. Useful for tracking and analytics.
</ParamField>

<ParamField path="align" type="string">
  The alignment of the action button. One of `"center"`, `"left"`, `"right"`, or `"full"`. Defaults to `"center"`.
</ParamField>

<ParamField path="background_color" type="string">
  The background color of the action button. Can be any valid CSS color value (e.g., `"#007bff"`, `"rgb(0, 123, 255)"`).
</ParamField>

<ParamField path="style" type="string">
  The visual style of the action. Can be `"button"` or `"link"`. Defaults to `"button"`.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization. See the [Locales documentation](/platform/content/elemental/locales) for more details.
</ParamField>

## Examples & Variants

### Button Style

The default button style renders as a clickable button:

```json  theme={null}
{
  "type": "action",
  "content": "Get Started",
  "href": "https://example.com/start",
  "style": "button"
}
```

### Link Style

Use link style for a more subtle, text-based link:

```json  theme={null}
{
  "type": "action",
  "content": "Learn more",
  "href": "https://example.com/docs",
  "style": "link"
}
```

### Styled Button

Customize the button appearance with colors and alignment:

```json  theme={null}
{
  "type": "action",
  "content": "Sign Up Now",
  "href": "https://example.com/signup",
  "style": "button",
  "background_color": "#007bff",
  "align": "center"
}
```

### With Localization

Localize action content and URLs:

```json  theme={null}
{
  "type": "action",
  "content": "View Dashboard",
  "href": "https://app.example.com/dashboard",
  "locales": {
    "es": {
      "content": "Ver Panel",
      "href": "https://app.example.com/es/dashboard"
    },
    "fr": {
      "content": "Voir le Tableau de Bord",
      "href": "https://app.example.com/fr/dashboard"
    }
  }
}
```

### With Conditional Logic

Show different actions based on conditions:

```json  theme={null}
{
  "type": "action",
  "content": "Upgrade Account",
  "href": "https://example.com/upgrade",
  "if": "{{user.plan}} === 'free'"
}
```

## Channel Support

Action elements are supported across all channels:

* **Email**: Renders as a button or link depending on style
* **Push**: Renders as a clickable action button
* **SMS**: Renders as a clickable link
* **Inbox**: Renders as an interactive button

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For non-interactive text content
* [Image Element](/platform/content/elemental/elements/image) - For images that can also link via `href`
* [Control Flow](/platform/content/elemental/control-flow) - For conditional rendering and loops
* [Locales](/platform/content/elemental/locales) - For localizing action content and URLs
