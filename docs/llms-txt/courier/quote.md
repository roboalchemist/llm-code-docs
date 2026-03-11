# Source: https://www.courier.com/docs/platform/content/elemental/elements/quote.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quote

> Render quote blocks in your Elemental notifications. Quote elements support styling, alignment, and localization for highlighting important text or testimonials.

## Overview

The quote element renders a quote block, typically used to highlight important text, testimonials, or call attention to specific content. Quote blocks can be styled with borders, colors, and different text styles.

**When to use:**

* Display testimonials or customer reviews
* Highlight important quotes or statements
* Emphasize key information
* Create visually distinct text blocks

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "quote",
    "content": "The future belongs to those who believe in the beauty of their dreams"
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
            type: "quote",
            content: "The future belongs to those who believe in the beauty of their dreams",
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
                      "type": "quote",
                      "content": "The future belongs to those who believe in the beauty of their dreams",
                  }
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For quote elements, this value must be `"quote"`.
</ParamField>

<ParamField path="content" type="string" required>
  The text value of the quote. This field supports Handlebars variables for dynamic content.
</ParamField>

<ParamField path="align" type="string">
  Alignment of the quote. One of `"center"`, `"left"`, `"right"`, or `"full"`. Defaults to `"left"`.
</ParamField>

<ParamField path="border_color" type="string">
  CSS border color property for the quote block. Can be any valid CSS color value (e.g., `"#007bff"`, `"rgb(0, 123, 255)"`).
</ParamField>

<ParamField path="text_style" type="string">
  Text style for the quote. One of `"text"`, `"h1"`, `"h2"`, or `"subtext"`. Defaults to `"text"`.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization. See the [Locales documentation](/platform/content/elemental/locales) for more details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The quote will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Examples & Variants

### Basic Quote

Simple quote block:

```json  theme={null}
{
  "type": "quote",
  "content": "The future belongs to those who believe in the beauty of their dreams"
}
```

### Styled Quote

Quote with border and styling:

```json  theme={null}
{
  "type": "quote",
  "content": "Customer satisfaction is our top priority",
  "border_color": "#007bff",
  "text_style": "h2",
  "align": "center"
}
```

### Quote with Handlebars

Dynamic quote content:

```json  theme={null}
{
  "type": "quote",
  "content": "{{customer_name}} said: \"{{testimonial}}\""
}
```

### Localized Quote

Quote with translations:

```json  theme={null}
{
  "type": "quote",
  "content": "Quality is not an act, it is a habit",
  "locales": {
    "es": {
      "content": "La calidad no es un acto, es un hábito"
    },
    "fr": {
      "content": "La qualité n'est pas un acte, c'est une habitude"
    }
  }
}
```

### Testimonial Quote

Quote styled as a testimonial:

```json  theme={null}
{
  "type": "quote",
  "content": "\"This product changed my life!\" - {{customer_name}}",
  "border_color": "#4CAF50",
  "text_style": "h2",
  "align": "center"
}
```

### Channel-Specific Quote

Show quotes only for specific channels:

```json  theme={null}
{
  "type": "quote",
  "channels": ["email"],
  "content": "Full testimonial with detailed feedback...",
  "border_color": "#007bff"
}
```

## Best Practices

* **Keep quotes concise**: Long quotes can be hard to read, especially in email
* **Use appropriate styling**: Border colors and text styles help quotes stand out
* **Consider context**: Quotes work well for testimonials, important notices, or highlighted information
* **Test alignment**: Different alignments can affect readability across channels

## Channel Support

* **Email**: ✅ Full support with styling and borders
* **Push**: ✅ Supported (may render as plain text in some cases)
* **SMS**: ⚠️ Limited support (may render as plain text)
* **Inbox**: ✅ Full support

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For regular text content
* [Group Element](/platform/content/elemental/elements/group) - For grouping quotes with other elements
* [Locales](/platform/content/elemental/locales) - For localizing quote content
* [Control Flow](/platform/content/elemental/control-flow) - For conditional rendering
