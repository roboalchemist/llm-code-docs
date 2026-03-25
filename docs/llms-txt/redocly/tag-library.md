# Source: https://redocly.com/docs/realm/content/markdoc-tags/tag-library.md

# Source: https://redocly.com/learn/markdoc/tags/tag-library.md

# Markdoc Tag Library

This page contains a comprehensive list of Markdoc tags with links to deeper resources where you can see how to use them. Some tags are built into Markdoc while others are Redocly-specific. We use badges to indicate a tag's availability:

| Badge | Meaning |
|  --- | --- |
|   | Tags built into Redocly products and available for customers to use in their projects. |
|   | Tags built into Markdoc's core that are available to *all* Markdoc users. |


## Admonition 

Use the Admonition tag to highlight important information. Choose from multiple pre-defined types like info, warning, and success.

Additional information and syntax: [Admonition tag](/learn/markdoc/tags/admonition)

**Example admonition element:**

Read this thing!
This tag is useful for drawing attention.

## Cards 

Use cards to help users navigate your documentation by grouping information and links in a pre-built UI card.
Choose from several pre-defined styles and formats.

Additional information and syntax: [Cards tag](/learn/markdoc/tags/cards)

**Example cards element:**

Card title
Add content *inside the card*.

Card title
Use links, Markdown, even other **Markdoc tags**.

## Code Snippet 

Use the Code Snippet tag to render a code sample from an external file in a configurable code block element.

Additional information and syntax: [Code Snippet tag](/learn/markdoc/tags/code-snippet)

**Example code snippet element:**

museum-redocly.yaml
- group: Markdoc Tag Library
  page: tags/tag-library.md
  items:
  - separator: Built-in tags
  - page: tags/partial.md
    label: Partial
  - page: tags/table.md
    label: Table
  - separator: Redocly Tags
  - page: tags/admonition.md
    label: Admonition
  - page: tags/cards.md
    label: Cards
  - page: tags/code-snippet.md
    label: Code Snippet
  - page: tags/img.md
    label: Image 
  - page: tags/inline-svg.md
    label: Inline SVG
  - page: tags/json-schema.md
    label: JSON Schema
  - page: tags/openapi-code-sample.md
    label: OpenAPI Code Sample
  - page: tags/replay-openapi.md
    label: Replay OpenAPI
  - page: tags/tabs.md
    label: Tabs

## Inline SVG 

Use the inline SVG tag to render an SVG element inline with your writing.

Additional information and syntax: [Inline SVG tag](/learn/markdoc/tags/inline-svg)

**Example inline SVG element:**

This tag is so cool it's scary .

## JSON Schema 

Use the JSON Schema tag to render an existing or inline schema in a configurable, readable layout.

Additional information and syntax: [JSON Schema tag](/learn/markdoc/tags/json-schema)

**Example JSON schema element:**

## OpenAPI Code Sample 

Use the OpenAPI Code sample tag to render a code sample for an API operation from an OpenAPI description.

Additional information and syntax: [OpenAPI Code Sample tag](/learn/markdoc/tags/openapi-code-sample)

## Partial 

Use the Partial tag to render the content from another file.

Additional information and syntax: [Partial tag](/learn/markdoc/tags/partial)

**Example partial element:**

Hello, World! â ð.

This content is *written in a separate file*. **Neat.**

## Replay OpenAPI 

Allow users to send live calls to your API using the Replay OpenAPI tag.

Additional information and syntax: [Replay OpenAPI tag](/learn/markdoc/tags/replay-openapi)

**Example element:**

## Table 

Use the Table tag to create tables using a list-based syntax that allows for easy injection of rich content, like bulleted lists and code samples.

Additional information and syntax: [Table tag](/learn/markdoc/tags/table)

**Example table element:**

| Heading 1 | Heading 2 |
|  --- | --- |
| Row 1 Cell 1 | Row 1 Cell 2 |
| Row 2 Cell 1 | Row 2 cell 2 |


## Tabs 

Use the tabs tag to organize content into a series of tabs that users can switch between.

Additional information and syntax: [Tabs tag](/learn/markdoc/tags/tabs)

Fruits
- Tomato (it's both!)
- Blueberry
- Kiwi
- Banana


Vegetables
- Tomato (it's both!)
- Broccoli
- Spinach
- Asparagus