# Source: https://www.courier.com/docs/platform/content/elemental/elements/divider.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Divider

> Render dividing lines between elements in your Elemental notifications. Divider elements help separate content sections with customizable styling.

## Overview

The divider element renders a dividing line (horizontal rule) between elements, helping to visually separate content sections in your notifications. Dividers are simple but effective for improving readability and organization.

**When to use:**

* Separate distinct sections of content
* Create visual breaks between related items
* Improve readability in long notifications
* Organize grouped content visually

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "divider",
    "color": "#800080"
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
            type: "text",
            content: "Welcome to our platform!",
            text_style: "h1",
          },
          {
            type: "divider",
            color: "#e0e0e0",
          },
          {
            type: "text",
            content: "Here's what you need to know...",
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
                  {"type": "text", "content": "Welcome to our platform!", "text_style": "h1"},
                  {"type": "divider", "color": "#e0e0e0"},
                  {"type": "text", "content": "Here's what you need to know..."},
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For divider elements, this value must be `"divider"`.
</ParamField>

<ParamField path="color" type="string">
  The CSS color to render the divider line with. Can be any valid CSS color value (e.g., `"#e0e0e0"`, `"rgb(224, 224, 224)"`, `"gray"`). Defaults to a standard gray color if not specified.
</ParamField>

<ParamField path="border_width" type="string">
  Border width in pixels for the divider line (e.g., `"1px"`, `"2px"`). Controls the thickness of the divider.
</ParamField>

<ParamField path="padding" type="string">
  Padding around the divider. Can be any valid CSS padding value (e.g., `"10px"`, `"20px 10px"`).
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The divider will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Examples & Variants

### Basic Divider

Simple divider with default styling:

```json  theme={null}
{
  "type": "divider"
}
```

### Styled Divider

Divider with custom color:

```json  theme={null}
{
  "type": "divider",
  "color": "#800080"
}
```

### Thick Divider

Divider with custom width:

```json  theme={null}
{
  "type": "divider",
  "color": "#007bff",
  "border_width": "3px"
}
```

### Divider with Padding

Divider with spacing:

```json  theme={null}
{
  "type": "divider",
  "color": "#e0e0e0",
  "padding": "20px 0"
}
```

### Section Separator

Using dividers to separate content sections:

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "text",
      "content": "Order Summary",
      "text_style": "h2"
    },
    {
      "type": "text",
      "content": "Item 1: $29.99"
    },
    {
      "type": "text",
      "content": "Item 2: $49.99"
    },
    {
      "type": "divider",
      "color": "#cccccc"
    },
    {
      "type": "text",
      "content": "Total: $79.98",
      "bold": true
    }
  ]
}
```

### Channel-Specific Divider

Show divider only for specific channels:

```json  theme={null}
{
  "type": "divider",
  "channels": ["email"],
  "color": "#e0e0e0"
}
```

## Best Practices

* **Use sparingly**: Too many dividers can make notifications cluttered
* **Match brand colors**: Use divider colors that match your brand palette
* **Consider spacing**: Add padding to dividers for better visual separation
* **Channel considerations**: Some channels (like SMS) may not render dividers, so don't rely on them for critical content separation

## Channel Support

* **Email**: ✅ Full support with styling
* **Push**: ⚠️ Limited support (may render as plain text or be ignored)
* **SMS**: ❌ Not supported (dividers are not rendered)
* **Inbox**: ✅ Full support with styling

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For content sections separated by dividers
* [Group Element](/platform/content/elemental/elements/group) - For grouping content with dividers
* [Control Flow](/platform/content/elemental/control-flow) - For conditional rendering
