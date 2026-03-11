# Source: https://www.courier.com/docs/platform/content/elemental/elements/columns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Columns

> Create multi-column layouts in your Elemental notifications. Columns support flexible widths, styling, and responsive behavior for email and other channels.

## Overview

The columns element allows you to create multi-column layouts in your notifications. It acts as a container for a row of columns, enabling side-by-side content organization. Each column can have independent styling, width, and content.

**When to use:**

* Create side-by-side layouts (e.g., product images with descriptions)
* Build responsive multi-column grids
* Organize content in structured layouts
* Display data in tabular-like formats

<Note>
  **Email Client Compatibility**: Column styling uses MJML patterns for maximum email client compatibility. Border radius and borders render correctly in most modern email clients, with graceful degradation in older clients. The `gap` property automatically calculates proper spacing by inserting spacer columns between content columns.
</Note>

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "columns",
    "elements": [
      {
        "type": "column",
        "width": "50%",
        "elements": [
          {
            "type": "image",
            "src": "https://example.com/product.png"
          }
        ]
      },
      {
        "type": "column",
        "width": "50%",
        "elements": [
          {
            "type": "text",
            "content": "Product Name",
            "text_style": "h2"
          },
          {
            "type": "text",
            "content": "$99.99"
          }
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
            type: "columns",
            elements: [
              {
                type: "column",
                width: "50%",
                elements: [
                  {
                    type: "image",
                    src: "https://example.com/product.png",
                  },
                ],
              },
              {
                type: "column",
                width: "50%",
                elements: [
                  {
                    type: "text",
                    content: "Product Name",
                    text_style: "h2",
                  },
                  {
                    type: "text",
                    content: "$99.99",
                  },
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
                      "type": "columns",
                      "elements": [
                          {
                              "type": "column",
                              "width": "50%",
                              "elements": [
                                  {
                                      "type": "image",
                                      "src": "https://example.com/product.png",
                                  }
                              ],
                          },
                          {
                              "type": "column",
                              "width": "50%",
                              "elements": [
                                  {"type": "text", "content": "Product Name", "text_style": "h2"},
                                  {"type": "text", "content": "$99.99"},
                              ],
                          },
                      ],
                  }
              ],
          },
      }
  )
  ```
</CodeGroup>

## Columns Element Fields

<ParamField path="type" type="string" required>
  The type of element. For columns elements, this value must be `"columns"`.
</ParamField>

<ParamField path="elements" type="CourierColumn[]" required>
  An array of column elements. Each element must be of type `"column"`. See the [Column Element](#column-element) section below for column properties.
</ParamField>

<ParamField path="background_color" type="string">
  Background color for the columns container. Can be any valid CSS color value (e.g., `"#f5f5f5"`, `"rgb(245,245,245)"`).
</ParamField>

<ParamField path="border_width" type="string">
  Border width for the columns container (e.g., `"1px"`, `"2px"`).
</ParamField>

<ParamField path="border_color" type="string">
  Border color for the columns container (e.g., `"#cccccc"`, `"rgb(204,204,204)"`).
</ParamField>

<ParamField path="border_radius" type="string">
  Border radius for rounded corners on the container (e.g., `"5px"`, `"10px"`).
</ParamField>

<ParamField path="gap" type="string">
  Spacing between columns. Automatically inserts spacer columns with exact width (e.g., `"10px"`, `"15px"`).
</ParamField>

<ParamField path="padding" type="string">
  Inner padding for the entire columns container. Can use CSS shorthand (e.g., `"10px"`, `"20px 10px"`).
</ParamField>

<ParamField path="vertical_align" type="string">
  Alignment of columns within the row. One of `"top"`, `"middle"`, or `"bottom"`. Defaults to `"top"`.
</ParamField>

## Column Element

Each child in the `elements` array of a columns element must be of type `column`. This allows for independent styling and width control for each column.

### Column Fields

<ParamField path="type" type="string" required>
  The type of element. For column elements, this value must be `"column"`.
</ParamField>

<ParamField path="elements" type="CourierElement[]" required>
  The content blocks inside this specific column. Can include any Elemental elements (text, image, action, etc.).
</ParamField>

<ParamField path="width" type="string">
  The width of the column. Can be:

  * Percentage: `"50%"`, `"33.33%"`
  * Fixed: `"200px"`, `"300px"`
  * Auto: `"auto"` (takes remaining space)
</ParamField>

<ParamField path="background_color" type="string">
  Hex code or CSS color for the column background (e.g., `"#F4F7FF"`, `"rgb(244,247,255)"`).
</ParamField>

<ParamField path="border_width" type="string">
  Border width for this specific column (e.g., `"1px"`, `"2px"`).
</ParamField>

<ParamField path="border_color" type="string">
  Border color for this specific column (e.g., `"#cccccc"`, `"rgb(204,204,204)"`).
</ParamField>

<ParamField path="border_radius" type="string">
  Border radius for rounded corners on this column (e.g., `"5px"`, `"10px"`).
</ParamField>

<ParamField path="padding" type="string">
  CSS padding shorthand for the column (e.g., `"10px"`, `"20px 10px"`).
</ParamField>

<ParamField path="vertical_align" type="string">
  Overrides the parent's vertical alignment for this specific column. One of `"top"`, `"middle"`, or `"bottom"`.
</ParamField>

## Examples & Variants

### Two-Column Layout

Basic sidebar and main content layout:

```json  theme={null}
{
  "type": "columns",
  "elements": [
    {
      "type": "column",
      "width": "30%",
      "background_color": "#F4F7FF",
      "padding": "20px",
      "elements": [
        {
          "type": "image",
          "src": "https://example.com/avatar.png",
          "width": "50px"
        },
        {
          "type": "text",
          "content": "User Profile",
          "text_style": "subtext"
        }
      ]
    },
    {
      "type": "column",
      "width": "70%",
      "padding": "20px",
      "elements": [
        {
          "type": "text",
          "content": "Welcome to the platform!",
          "text_style": "h2"
        },
        {
          "type": "text",
          "content": "We are excited to have you here. Your account is now active."
        },
        {
          "type": "action",
          "content": "Get Started",
          "href": "https://example.com/start",
          "style": "button"
        }
      ]
    }
  ]
}
```

### Equal-Width Columns

Three equal columns with middle vertical alignment:

```json  theme={null}
{
  "type": "columns",
  "vertical_align": "middle",
  "gap": "15px",
  "elements": [
    {
      "type": "column",
      "width": "33.33%",
      "elements": [
        {
          "type": "text",
          "content": "Column 1",
          "text_style": "h3"
        },
        {
          "type": "text",
          "content": "Content for first column"
        }
      ]
    },
    {
      "type": "column",
      "width": "33.33%",
      "elements": [
        {
          "type": "text",
          "content": "Column 2",
          "text_style": "h3"
        },
        {
          "type": "text",
          "content": "Content for second column"
        }
      ]
    },
    {
      "type": "column",
      "width": "33.33%",
      "elements": [
        {
          "type": "text",
          "content": "Column 3",
          "text_style": "h3"
        },
        {
          "type": "text",
          "content": "Content for third column"
        }
      ]
    }
  ]
}
```

### Styled Container with Borders

Columns container with styling:

```json  theme={null}
{
  "type": "columns",
  "padding": "20px",
  "background_color": "#f5f5f5",
  "border_width": "2px",
  "border_color": "#cccccc",
  "border_radius": "8px",
  "gap": "15px",
  "elements": [
    {
      "type": "column",
      "width": "50%",
      "elements": [
        {
          "type": "text",
          "content": "Left Column"
        }
      ]
    },
    {
      "type": "column",
      "width": "50%",
      "elements": [
        {
          "type": "text",
          "content": "Right Column"
        }
      ]
    }
  ]
}
```

### Individual Column Styling

Each column with its own styling:

```json  theme={null}
{
  "type": "columns",
  "elements": [
    {
      "type": "column",
      "width": "50%",
      "border_width": "2px",
      "border_color": "#4CAF50",
      "border_radius": "10px",
      "padding": "15px",
      "background_color": "#ffffff",
      "elements": [
        {
          "type": "text",
          "content": "**Featured Product**",
          "text_style": "h3"
        },
        {
          "type": "image",
          "src": "https://example.com/product.jpg"
        },
        {
          "type": "action",
          "content": "View Details",
          "href": "https://example.com/product",
          "style": "button"
        }
      ]
    },
    {
      "type": "column",
      "width": "50%",
      "border_width": "2px",
      "border_color": "#2196F3",
      "border_radius": "10px",
      "padding": "15px",
      "background_color": "#ffffff",
      "elements": [
        {
          "type": "text",
          "content": "**Special Offer**",
          "text_style": "h3"
        },
        {
          "type": "text",
          "content": "Get 20% off your first order!"
        },
        {
          "type": "action",
          "content": "Shop Now",
          "href": "https://example.com/shop",
          "style": "button"
        }
      ]
    }
  ]
}
```

### Product Card Layout

Complete product card with image and details:

```json  theme={null}
{
  "type": "columns",
  "padding": "25px",
  "background_color": "#ffffff",
  "border_width": "1px",
  "border_color": "#e0e0e0",
  "border_radius": "12px",
  "gap": "20px",
  "vertical_align": "middle",
  "elements": [
    {
      "type": "column",
      "width": "40%",
      "border_width": "1px",
      "border_color": "#4CAF50",
      "border_radius": "8px",
      "padding": "20px",
      "background_color": "#f1f8f4",
      "elements": [
        {
          "type": "image",
          "src": "https://example.com/product-image.jpg",
          "href": "https://example.com/product",
          "width": "100%"
        }
      ]
    },
    {
      "type": "column",
      "width": "60%",
      "elements": [
        {
          "type": "text",
          "content": "**Premium Product Name**",
          "text_style": "h2"
        },
        {
          "type": "text",
          "content": "High-quality product with exceptional features. Perfect for everyday use."
        },
        {
          "type": "text",
          "content": "**$149.99**",
          "bold": true
        },
        {
          "type": "action",
          "content": "Add to Cart",
          "href": "https://example.com/cart",
          "background_color": "#4CAF50",
          "style": "button"
        }
      ]
    }
  ]
}
```

## Best Practices

* **Use percentages for widths**: Percentages work better across different screen sizes than fixed widths
* **Keep column count reasonable**: 2-3 columns work best for email; more columns can be cramped
* **Test responsive behavior**: Columns stack on mobile devices, so ensure content works in single-column view
* **Use gap for spacing**: The `gap` property provides consistent spacing between columns
* **Consider vertical alignment**: Use `vertical_align` to align content when columns have different heights

## Channel Support

* **Email**: Full support with MJML rendering for maximum compatibility
* **Push**: Limited support; columns may render as stacked content
* **SMS**: Not supported; use single-column layouts
* **Inbox**: Full support with responsive behavior

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For text content within columns
* [Image Element](/platform/content/elemental/elements/image) - For images within columns
* [Action Element](/platform/content/elemental/elements/action) - For buttons and links within columns
* [Group Element](/platform/content/elemental/elements/group) - For grouping elements within columns
* [Control Flow](/platform/content/elemental/control-flow) - For conditional columns and loops
