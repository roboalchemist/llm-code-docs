# Source: https://www.courier.com/docs/platform/content/elemental/elements/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Elements Reference

> Complete reference for all Courier Elemental element types. Each element has its own dedicated documentation page with examples, properties, and use cases.

## Overview

Courier Elemental provides a comprehensive set of reusable content elements that you can combine to build structured, cross-channel notification templates. Each element type serves a specific purpose and supports rich properties, conditional logic, and localization.

## Element Categories

### Channel & Structure Elements

Elements for channel-specific customization and structure.

* **[Channel](/platform/content/elemental/elements/channel)** - Channel-specific content customization
* **[Meta](/platform/content/elemental/elements/meta)** - Metadata like titles and subjects

### Content Elements

Elements for displaying text, images, and interactive content.

* **[Text](/platform/content/elemental/elements/text)** - Text content with rich formatting options
* **[Action](/platform/content/elemental/elements/action)** - Clickable buttons and links
* **[Image](/platform/content/elemental/elements/image)** - Embedded images with optional links
* **[Quote](/platform/content/elemental/elements/quote)** - Quote blocks with styling options
* **[HTML](/platform/content/elemental/elements/html)** - Raw HTML content

### Layout Elements

Elements for organizing and structuring content.

* **[Columns](/platform/content/elemental/elements/columns)** - Multi-column layouts
* **[Group](/platform/content/elemental/elements/group)** - Group elements together for conditional logic
* **[List](/platform/content/elemental/elements/list)** - Ordered and unordered lists with nesting support
* **[Divider](/platform/content/elemental/elements/divider)** - Visual dividers between content

### Advanced Elements

Elements for advanced templating and development.

* **[Jsonnet](/platform/content/elemental/elements/jsonnet)** - Jsonnet templates for programmatic content generation
* **[Comment](/platform/content/elemental/elements/comment)** - Non-rendered comments for documentation

## Quick Reference

| Element                                                 | Description                 | Common Use Case                          |
| ------------------------------------------------------- | --------------------------- | ---------------------------------------- |
| [Action](/platform/content/elemental/elements/action)   | Clickable buttons and links | Call-to-action buttons, navigation links |
| [Channel](/platform/content/elemental/elements/channel) | Channel-specific content    | Different content per email/push/SMS     |
| [Columns](/platform/content/elemental/elements/columns) | Multi-column layouts        | Side-by-side content, product grids      |
| [Comment](/platform/content/elemental/elements/comment) | Non-rendered comments       | Documentation, notes                     |
| [Divider](/platform/content/elemental/elements/divider) | Visual dividers             | Separating sections                      |
| [Group](/platform/content/elemental/elements/group)     | Group elements together     | Conditional blocks, loops                |
| [HTML](/platform/content/elemental/elements/html)       | Raw HTML content            | Custom HTML structures                   |
| [Image](/platform/content/elemental/elements/image)     | Embedded images             | Logos, product images, illustrations     |
| [Jsonnet](/platform/content/elemental/elements/jsonnet) | Jsonnet templates           | Programmatic JSON generation             |
| [List](/platform/content/elemental/elements/list)       | Ordered/unordered lists     | Product lists, feature lists             |
| [Meta](/platform/content/elemental/elements/meta)       | Metadata (titles, subjects) | Email subjects, push titles              |
| [Quote](/platform/content/elemental/elements/quote)     | Quote blocks                | Testimonials, highlighted text           |
| [Text](/platform/content/elemental/elements/text)       | Text content                | Body text, headings, descriptions        |

## Common Patterns

### Control Flow

All elements support control flow properties:

* `if` - Conditional rendering
* `loop` - Repeat elements
* `ref` - Reference elements

See the [Control Flow documentation](/platform/content/elemental/control-flow) for details.

### Localization

Many elements support the `locales` property for multi-language content:

* `content` - Localized text content
* `title` - Localized titles (meta element)
* `href` - Localized URLs (action, image elements)

See the [Locales documentation](/platform/content/elemental/locales) for details.

## Related Documentation

<CardGroup cols={2}>
  <Card title="Elemental Overview" icon="file-code" href="/platform/content/elemental/elemental-overview">
    Learn about Courier Elemental and its key capabilities.
  </Card>

  <Card title="Control Flow" icon="code" href="/platform/content/elemental/control-flow">
    Use conditionals, loops, and references in your elements.
  </Card>

  <Card title="Locales" icon="globe" href="/platform/content/elemental/locales">
    Localize your element content for multiple languages.
  </Card>
</CardGroup>
