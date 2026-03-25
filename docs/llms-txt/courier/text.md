# Source: https://www.courier.com/docs/platform/content/elemental/elements/text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text

> Display text content in your Elemental notifications with rich formatting options. Text elements support inline formatting, links, images, and localization.

## Overview

The text element represents a body of text to be rendered inside of the notification. It's one of the most commonly used elements and supports rich formatting, styling, and can contain inline text content elements (string, link, img) for more complex text structures.

**When to use:**

* Display body text, paragraphs, and descriptions
* Create headings and subheadings
* Show formatted text with styling (bold, italic, colors)
* Include inline links and images within text
* Display dynamic content with Handlebars variables

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "text",
    "content": "Thanks for signing up!"
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
            content: "Thanks for signing up!",
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
                  {"type": "text", "content": "Thanks for signing up!"}
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For text elements, this value must be `"text"`.
</ParamField>

<ParamField path="content" type="string">
  The text content displayed in the notification. Either this field or the `elements` field must be specified. Supports Handlebars variables for dynamic content.
</ParamField>

<ParamField path="elements" type="TextContentElement[]">
  An array of Text Content Elements (string, link, img). Either this field or the `content` field must be specified. Both can also be provided — when both are present, `elements` takes precedence and `content` is ignored. See the [Text Content Elements](#text-content-elements) section below.
</ParamField>

<ParamField path="align" type="string">
  Text alignment. One of `"left"`, `"center"`, or `"right"`. Defaults to `"left"`.
</ParamField>

<ParamField path="text_style" type="string">
  Allows the text to be rendered as a heading level. Can be `"text"`, `"h1"`, `"h2"`, or `"subtext"`. Defaults to `"text"`.
</ParamField>

<ParamField path="color" type="string">
  Specifies the color of text. Can be any valid CSS color value (e.g., `"#007bff"`, `"rgb(0, 123, 255)"`).
</ParamField>

<ParamField path="bold" type="boolean">
  Apply bold formatting to the text.
</ParamField>

<ParamField path="italic" type="boolean">
  Apply italic formatting to the text.
</ParamField>

<ParamField path="strikethrough" type="boolean">
  Apply a strikethrough to the text.
</ParamField>

<ParamField path="underline" type="boolean">
  Apply an underline to the text.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization. Locale entries for text nodes can include `content` (a string), `elements` (a structured array of inline nodes), or both. When both are provided, `elements` takes precedence. See the [Locales documentation](/platform/content/elemental/locales) for more details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The text will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Examples & Variants

### Basic Text

Simple text content:

```json  theme={null}
{
  "type": "text",
  "content": "Thanks for signing up!"
}
```

### Text with Handlebars

Dynamic text with variables:

```json  theme={null}
{
  "type": "text",
  "content": "This is a notification I sent to {{first_name}}"
}
```

Variables come from `message.data` (e.g., `data.first_name`).

### Styled Text

Text with formatting:

```json  theme={null}
{
  "type": "text",
  "content": "Important Notice",
  "text_style": "h2",
  "bold": true,
  "color": "#007bff",
  "align": "center"
}
```

### Localized Text

Text with translations using the `content` string format:

```json  theme={null}
{
  "type": "text",
  "content": "This is a notification I sent to {{first_name}}",
  "locales": {
    "es": {
      "content": "Esta es una notificación que envié a {{first_name}}"
    },
    "fr": {
      "content": "Ceci est une notification que j'ai envoyée à {{first_name}}"
    }
  }
}
```

### Localized Text with Structured Elements

When your text node uses the `elements` array, provide locale translations as `elements` arrays to preserve inline formatting across languages:

```json  theme={null}
{
  "type": "text",
  "elements": [
    { "type": "string", "content": "Your order " },
    { "type": "string", "content": "#{{order.id}}", "bold": true },
    { "type": "string", "content": " has been confirmed." }
  ],
  "locales": {
    "fr": {
      "elements": [
        { "type": "string", "content": "Votre commande " },
        { "type": "string", "content": "#{{order.id}}", "bold": true },
        { "type": "string", "content": " a été confirmée." }
      ]
    }
  }
}
```

### When Both `content` and `elements` Are Present

If a text node includes both `content` and `elements`, only `elements` is used — `content` is ignored. We recommend choosing one format per node to keep your templates clear. The same applies to locale entries.

<Note>
  If a text node uses `elements` but a locale only provides `content`, Courier wraps the content string into a single-element array for backward compatibility. This preserves rendering but loses any inline formatting the original elements may have had. For full formatting fidelity, provide `elements` in your locale translations. See the [Locales documentation](/platform/content/elemental/locales#text-node-locale-resolution) for the full resolution table.
</Note>

### Heading Styles

Use text as headings:

```json  theme={null}
{
  "type": "text",
  "content": "Welcome to Our Platform",
  "text_style": "h1"
},
{
  "type": "text",
  "content": "Get started in minutes",
  "text_style": "subtext"
}
```

## Text Content Elements

The text element can contain an array of text content elements instead of (or in addition to) the `content` field. These sub-elements allow you to create rich, inline text with links, images, and formatted strings.

<Note>
  Text content elements (string, link, img) must be children of a text element. They cannot be used as standalone top-level elements.
</Note>

### String Element

Renders a simple string. Similar to default text behavior but allows for inline formatting within a text element.

**Fields:**

<ParamField path="type" type="string" required>
  The type of element. For string elements, this value must be `"string"`.
</ParamField>

<ParamField path="content" type="string" required>
  The text content displayed in the notification.
</ParamField>

<ParamField path="align" type="string">
  Text alignment. One of `"left"`, `"center"`, or `"right"`.
</ParamField>

<ParamField path="text_style" type="string">
  Allows the text to be rendered as a heading level. Can be `"text"`, `"h1"`, `"h2"`, or `"subtext"`.
</ParamField>

<ParamField path="color" type="string">
  Specifies the color of text. Can be any valid CSS color value.
</ParamField>

<ParamField path="bold" type="boolean">
  Apply bold formatting to the text.
</ParamField>

<ParamField path="italic" type="boolean">
  Apply italic formatting to the text.
</ParamField>

<ParamField path="strikethrough" type="boolean">
  Apply a strikethrough to the text.
</ParamField>

<ParamField path="underline" type="boolean">
  Apply an underline to the text.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization.
</ParamField>

### Link Element

Renders a clickable link within a body of text.

**Fields:**

<ParamField path="type" type="string" required>
  The type of element. For link elements, this value must be `"link"`.
</ParamField>

<ParamField path="content" type="string" required>
  The text content of the link (the clickable text).
</ParamField>

<ParamField path="href" type="string">
  The address to link to. When provided, the link becomes clickable.
</ParamField>

<ParamField path="disable_tracking" type="boolean">
  Disable click tracking for the link. By default, Courier tracks link clicks.
</ParamField>

<ParamField path="align" type="string">
  Text alignment. One of `"left"`, `"center"`, or `"right"`.
</ParamField>

<ParamField path="text_style" type="string">
  Allows the text to be rendered as a heading level. Can be `"text"`, `"h1"`, `"h2"`, or `"subtext"`.
</ParamField>

<ParamField path="color" type="string">
  Specifies the color of text. Can be any valid CSS color value.
</ParamField>

<ParamField path="bold" type="boolean">
  Apply bold formatting to the text.
</ParamField>

<ParamField path="italic" type="boolean">
  Apply italic formatting to the text.
</ParamField>

<ParamField path="strikethrough" type="boolean">
  Apply a strikethrough to the text.
</ParamField>

<ParamField path="underline" type="boolean">
  Apply an underline to the text.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization.
</ParamField>

### Img Element

Renders an image inline within a body of text.

**Fields:**

<ParamField path="type" type="string" required>
  The type of element. For inline image elements, this value must be `"img"`.
</ParamField>

<ParamField path="src" type="string" required>
  The source address of the image. Must be a publicly accessible URL.
</ParamField>

<ParamField path="alt_text" type="string">
  Text used for screen readers and displayed on mouse hover. Important for accessibility.
</ParamField>

<ParamField path="width" type="string">
  How wide the image should render. Can be any valid CSS width value (e.g., `"50px"`, `"100%"`).
</ParamField>

<ParamField path="href" type="string">
  An address to link to. Makes the image clickable.
</ParamField>

<ParamField path="disable_tracking" type="boolean">
  Disable click tracking for the link (if `href` is provided).
</ParamField>

<ParamField path="align" type="string">
  Text alignment. One of `"left"`, `"center"`, or `"right"`.
</ParamField>

<ParamField path="text_style" type="string">
  Allows the text to be rendered as a heading level. Can be `"text"`, `"h1"`, `"h2"`, or `"subtext"`.
</ParamField>

<ParamField path="color" type="string">
  Specifies the color of text (for any text overlay).
</ParamField>

<ParamField path="bold" type="boolean">
  Apply bold formatting (for any text overlay).
</ParamField>

<ParamField path="italic" type="boolean">
  Apply italic formatting (for any text overlay).
</ParamField>

<ParamField path="strikethrough" type="boolean">
  Apply a strikethrough (for any text overlay).
</ParamField>

<ParamField path="underline" type="boolean">
  Apply an underline (for any text overlay).
</ParamField>

<ParamField path="locales" type="object">
  Region-specific content for localization. Can localize `src` and `href`.
</ParamField>

## Examples with Text Content Elements

### Text with Inline Links

Combine strings and links:

```json  theme={null}
{
  "type": "text",
  "elements": [
    { "type": "string", "content": "Hey! " },
    { "type": "link", "content": "Check out this site.", "href": "https://www.example.com" },
    { "type": "string", "content": " It's awesome!" }
  ]
}
```

### Text with Inline Images

Include images within text:

```json  theme={null}
{
  "type": "text",
  "elements": [
    { "type": "string", "content": "Check out this emoji: " },
    { "type": "img", "src": "https://emoji.com/cool-emoji", "width": "20px", "alt_text": "Cool emoji" },
    { "type": "string", "content": " Pretty cool, right?" }
  ]
}
```

### Rich Formatted Text

Mix strings, links, and formatting:

```json  theme={null}
{
  "type": "text",
  "elements": [
    { "type": "string", "content": "Welcome, ", "bold": true },
    { "type": "string", "content": "{{user_name}}", "bold": true, "color": "#007bff" },
    { "type": "string", "content": "! Visit our " },
    { "type": "link", "content": "documentation", "href": "https://docs.example.com", "bold": true },
    { "type": "string", "content": " to get started." }
  ]
}
```

### Text with Multiple Links

Multiple links in one text element:

```json  theme={null}
{
  "type": "text",
  "elements": [
    { "type": "string", "content": "Check out our " },
    { "type": "link", "content": "blog", "href": "https://example.com/blog" },
    { "type": "string", "content": " and " },
    { "type": "link", "content": "documentation", "href": "https://example.com/docs" },
    { "type": "string", "content": " for more information." }
  ]
}
```

## Best Practices

* **Use `content` for simple text**: When you just need plain text, use the `content` field
* **Use `elements` for rich formatting**: Use the `elements` array when you need inline links, images, or complex formatting
* **Avoid specifying both**: When both `content` and `elements` are present, `elements` takes precedence and `content` is ignored. Pick one format per node
* **Match locale format to root format**: If your text node uses `elements`, provide `elements` in your locales to preserve formatting. A `content`-only locale on an `elements` node will work but loses inline formatting
* **Keep text concise**: Long paragraphs can be hard to read, especially in email
* **Use headings appropriately**: Use `text_style` to create proper heading hierarchy
* **Test formatting**: Different channels may render formatting differently

## Channel Support

* **Email**: ✅ Full support with all formatting options
* **Push**: ✅ Supported (formatting may be limited)
* **SMS**: ⚠️ Limited support (plain text only)
* **Inbox**: ✅ Full support with rich formatting

## Related Elements

* [Action Element](/platform/content/elemental/elements/action) - For standalone buttons and links
* [Image Element](/platform/content/elemental/elements/image) - For standalone images
* [Quote Element](/platform/content/elemental/elements/quote) - For quote blocks
* [Group Element](/platform/content/elemental/elements/group) - For grouping text with other elements
* [Locales](/platform/content/elemental/locales) - For localizing text content
* [Control Flow](/platform/content/elemental/control-flow) - For conditional rendering and loops
