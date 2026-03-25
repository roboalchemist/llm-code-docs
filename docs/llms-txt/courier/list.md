# Source: https://www.courier.com/docs/platform/content/elemental/elements/list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List

> Create ordered and unordered lists in your Elemental notifications. Lists support nesting up to 5 levels deep and can use loops for dynamic content generation.

## Overview

The list element allows you to create ordered (numbered) or unordered (bulleted) lists in your notifications. Lists support nesting up to 5 levels deep, enabling complex hierarchical structures. Both parent and nested lists can independently use loops for dynamic content generation.

**When to use:**

* Display ordered sequences (steps, rankings)
* Show unordered items (features, benefits, options)
* Create nested hierarchical structures
* Display dynamic lists from data (products, items, etc.)

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "list",
    "list_type": "unordered",
    "elements": [
      {
        "type": "list-item",
        "elements": [
          { "type": "string", "content": "First item" }
        ]
      },
      {
        "type": "list-item",
        "elements": [
          { "type": "string", "content": "Second item" }
        ]
      }
    ]
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
            type: "list",
            list_type: "unordered",
            elements: [
              {
                type: "list-item",
                elements: [
                  { type: "string", content: "Feature 1" },
                ],
              },
              {
                type: "list-item",
                elements: [
                  { type: "string", content: "Feature 2" },
                ],
              },
            ],
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
                      "type": "list",
                      "list_type": "unordered",
                      "elements": [
                          {
                              "type": "list-item",
                              "elements": [{"type": "string", "content": "Feature 1"}],
                          },
                          {
                              "type": "list-item",
                              "elements": [{"type": "string", "content": "Feature 2"}],
                          },
                      ],
                  }
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For list elements, this value must be `"list"`.
</ParamField>

<ParamField path="list_type" type="string" required>
  The type of list. Can be `"ordered"` (numbered) or `"unordered"` (bulleted).
</ParamField>

<ParamField path="elements" type="ListItemElement[]" required>
  An array of list item elements. Each element must be of type `"list-item"`. See the [List Item Fields](#list-item-fields) section below.
</ParamField>

<ParamField path="imgSrc" type="string">
  Allows bullets to be rendered using a custom image (for unordered lists only). The image URL will be used as the bullet point.
</ParamField>

<ParamField path="imgHref" type="string">
  URL for the bullet image, if used. Makes the bullet image clickable.
</ParamField>

<ParamField path="loop" type="string">
  An expression that allows the list to be dynamically generated from data. See [Control Flow documentation](/platform/content/elemental/control-flow#looping) for details.
</ParamField>

<ParamField path="if" type="string">
  A condition that determines whether the list should be rendered. See [Control Flow documentation](/platform/content/elemental/control-flow#conditional-rendering) for details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The list will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## List Item Fields

Each item in the `elements` array must be a list item element with the following properties:

<ParamField path="type" type="string" required>
  The type of element. For list items, this value must be `"list-item"`.
</ParamField>

<ParamField path="elements" type="CourierElement[]" required>
  Content of the list item. Can include:

  * `string` elements for text
  * `link` elements for clickable links
  * `img` elements for inline images
  * Nested `list` elements for sub-lists
</ParamField>

<ParamField path="background_color" type="string">
  Background color for the list item. Can be any valid CSS color value.
</ParamField>

<ParamField path="loop" type="string">
  An expression that allows the list item to be repeated. See [Control Flow documentation](/platform/content/elemental/control-flow#looping) for details.
</ParamField>

<ParamField path="if" type="string">
  A condition that determines whether the list item should be rendered. See [Control Flow documentation](/platform/content/elemental/control-flow#conditional-rendering) for details.
</ParamField>

## Examples & Variants

### Unordered List

Simple bulleted list:

```json  theme={null}
{
  "type": "list",
  "list_type": "unordered",
  "elements": [
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Feature 1" }
      ]
    },
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Feature 2" }
      ]
    },
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Feature 3" }
      ]
    }
  ]
}
```

### Ordered List

Numbered list:

```json  theme={null}
{
  "type": "list",
  "list_type": "ordered",
  "elements": [
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Step 1: Sign up" }
      ]
    },
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Step 2: Verify email" }
      ]
    },
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Step 3: Get started" }
      ]
    }
  ]
}
```

### Nested Lists

Lists can be nested up to 5 levels deep:

```json  theme={null}
{
  "type": "list",
  "list_type": "unordered",
  "elements": [
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Fruits" },
        {
          "type": "list",
          "list_type": "ordered",
          "elements": [
            {
              "type": "list-item",
              "elements": [
                { "type": "string", "content": "Apple" }
              ]
            },
            {
              "type": "list-item",
              "elements": [
                { "type": "string", "content": "Banana" }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Vegetables" },
        {
          "type": "list",
          "list_type": "ordered",
          "elements": [
            {
              "type": "list-item",
              "elements": [
                { "type": "string", "content": "Carrot" }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### List Items with Links

Include clickable links in list items:

```json  theme={null}
{
  "type": "list",
  "list_type": "unordered",
  "elements": [
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "View our " },
        { "type": "link", "content": "documentation", "href": "https://example.com/docs" },
        { "type": "string", "content": " for more info" }
      ]
    }
  ]
}
```

### Dynamic Lists with Loops

Generate lists from data:

```json  theme={null}
{
  "type": "list",
  "list_type": "unordered",
  "elements": [
    {
      "type": "list-item",
      "loop": "data.products",
      "elements": [
        { "type": "string", "content": "{{$.item.name}} - ${{$.item.price}}" }
      ]
    }
  ]
}
```

### Nested Dynamic Lists

Dynamic lists with nested loops:

```json  theme={null}
{
  "type": "list",
  "list_type": "unordered",
  "elements": [
    {
      "type": "list-item",
      "loop": "data.categories",
      "elements": [
        { "type": "string", "content": "{{$.item.name}}" },
        {
          "type": "list",
          "list_type": "ordered",
          "elements": [
            {
              "type": "list-item",
              "loop": "$.item.products",
              "elements": [
                { "type": "string", "content": "{{$.item}}" }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### Custom Bullet Images

Use custom images for bullets:

```json  theme={null}
{
  "type": "list",
  "list_type": "unordered",
  "imgSrc": "https://example.com/custom-bullet.png",
  "imgHref": "https://example.com",
  "elements": [
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Item with custom bullet" }
      ]
    }
  ]
}
```

### Styled List Items

List items with background colors:

```json  theme={null}
{
  "type": "list",
  "list_type": "unordered",
  "elements": [
    {
      "type": "list-item",
      "background_color": "#f0f0f0",
      "elements": [
        { "type": "string", "content": "Highlighted item" }
      ]
    },
    {
      "type": "list-item",
      "elements": [
        { "type": "string", "content": "Regular item" }
      ]
    }
  ]
}
```

## Best Practices

* **Use appropriate list types**: Use ordered lists for sequences (steps, rankings) and unordered lists for collections (features, options)
* **Limit nesting depth**: While 5 levels are supported, 2-3 levels are usually sufficient for readability
* **Keep items concise**: Long list items can be hard to scan
* **Use loops for dynamic content**: Generate lists from data rather than hardcoding items
* **Consider mobile**: Long lists may need special formatting for mobile devices

<Note>
  Lists can be nested up to 5 levels deep. Nested lists can have different list types (ordered/unordered) than their parent lists.
</Note>

## Channel Support

* **Email**: ✅ Full support with proper list rendering
* **Push**: ✅ Supported (may render as plain text in some cases)
* **SMS**: ⚠️ Limited support (may render as plain text)
* **Inbox**: ✅ Full support

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For text content within list items
* [Group Element](/platform/content/elemental/elements/group) - For grouping list items with other elements
* [Control Flow](/platform/content/elemental/control-flow) - For loops and conditional rendering
* [Text Content Elements](/platform/content/elemental/elements/text#text-content-elements) - For string, link, and img elements within list items
