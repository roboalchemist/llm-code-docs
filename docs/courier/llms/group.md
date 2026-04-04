# Source: https://www.courier.com/docs/platform/content/elemental/elements/group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Group

> Group multiple elements together for conditional rendering, looping, and organization. Groups are essential for applying control flow logic to multiple elements at once.

## Overview

The group element allows you to group multiple elements together. This is particularly useful when used in combination with control flow properties like `if` and `loop` to conditionally render or repeat multiple elements as a unit.

**When to use:**

* Apply conditional logic to multiple elements at once
* Loop over multiple elements together
* Organize related elements into logical sections
* Create reusable element blocks

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "group",
    "elements": [
      {
        "type": "text",
        "content": "Welcome!"
      },
      {
        "type": "action",
        "content": "Get Started",
        "href": "https://example.com/start"
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
            type: "group",
            elements: [
              {
                type: "text",
                content: "Welcome to our platform!",
              },
              {
                type: "action",
                content: "Get Started",
                href: "https://example.com/start",
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
                      "type": "group",
                      "elements": [
                          {"type": "text", "content": "Welcome to our platform!"},
                          {
                              "type": "action",
                              "content": "Get Started",
                              "href": "https://example.com/start",
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
  The type of element. For group elements, this value must be `"group"`.
</ParamField>

<ParamField path="elements" type="CourierElement[]" required>
  An array of Elemental elements to group together. All elements in this array will be rendered together as a unit.
</ParamField>

<ParamField path="if" type="string">
  A condition that determines whether the entire group should be rendered. See [Control Flow documentation](/platform/content/elemental/control-flow#conditional-rendering) for details.
</ParamField>

<ParamField path="loop" type="string">
  An expression that allows the entire group to be repeated multiple times. See [Control Flow documentation](/platform/content/elemental/control-flow#looping) for details.
</ParamField>

<ParamField path="ref" type="string">
  A reference identifier for the group. See [Control Flow documentation](/platform/content/elemental/control-flow#references) for details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The group will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Examples & Variants

### Conditional Group

Show or hide multiple elements based on a condition:

```json  theme={null}
{
  "type": "group",
  "if": "{{user.plan}} === 'premium'",
  "elements": [
    {
      "type": "text",
      "content": "**Premium Features**",
      "text_style": "h2"
    },
    {
      "type": "text",
      "content": "You have access to all premium features!"
    },
    {
      "type": "action",
      "content": "Explore Features",
      "href": "https://example.com/premium"
    }
  ]
}
```

### Looping Group

Repeat a group of elements for each item in an array:

```json  theme={null}
{
  "type": "group",
  "loop": "data.products",
  "elements": [
    {
      "type": "text",
      "content": "# {{$.item.name}}",
      "text_style": "h2"
    },
    {
      "type": "divider"
    },
    {
      "type": "text",
      "content": "Description: {{$.item.description}}"
    },
    {
      "type": "text",
      "content": "Price: ${{$.item.price}}",
      "bold": true
    },
    {
      "type": "action",
      "content": "View Product",
      "href": "https://example.com/products/{{$.item.id}}"
    }
  ]
}
```

### Channel-Specific Group

Show different groups of elements for different channels:

```json  theme={null}
{
  "type": "group",
  "channels": ["email"],
  "elements": [
    {
      "type": "text",
      "content": "Full email content with details..."
    },
    {
      "type": "action",
      "content": "View Full Details",
      "href": "https://example.com/details"
    }
  ]
},
{
  "type": "group",
  "channels": ["push", "sms"],
  "elements": [
    {
      "type": "text",
      "content": "Short summary for mobile channels"
    }
  ]
}
```

### Nested Groups

Group elements within groups for complex structures:

```json  theme={null}
{
  "type": "group",
  "if": "{{order.items.length}} > 0",
  "elements": [
    {
      "type": "text",
      "content": "Order Items",
      "text_style": "h2"
    },
    {
      "type": "group",
      "loop": "data.order.items",
      "elements": [
        {
          "type": "text",
          "content": "{{$.item.name}} - ${{$.item.price}}"
        }
      ]
    },
    {
      "type": "text",
      "content": "Total: ${{order.total}}",
      "bold": true
    }
  ]
}
```

### Organizing Sections

Use groups to organize different sections of your notification:

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "group",
      "elements": [
        {
          "type": "image",
          "src": "https://example.com/logo.png"
        },
        {
          "type": "text",
          "content": "Welcome!",
          "text_style": "h1"
        }
      ]
    },
    {
      "type": "divider"
    },
    {
      "type": "group",
      "elements": [
        {
          "type": "text",
          "content": "Your account has been created successfully."
        },
        {
          "type": "action",
          "content": "Get Started",
          "href": "https://example.com/dashboard"
        }
      ]
    }
  ]
}
```

## Best Practices

* **Use for conditional blocks**: Group elements that should appear or disappear together
* **Organize logically**: Group related elements to improve template readability
* **Combine with loops**: Use groups to repeat multiple elements as a unit
* **Avoid unnecessary nesting**: Only nest groups when you need different conditions at different levels

## Related Elements

* [Control Flow](/platform/content/elemental/control-flow) - Learn about `if`, `loop`, `ref`, and `channels` properties
* [Channel Element](/platform/content/elemental/elements/channel) - For channel-specific content customization
* [Columns Element](/platform/content/elemental/elements/columns) - For multi-column layouts
* [Text Element](/platform/content/elemental/elements/text) - For text content within groups
* [Action Element](/platform/content/elemental/elements/action) - For buttons and links within groups
