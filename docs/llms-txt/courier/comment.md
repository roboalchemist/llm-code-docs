# Source: https://www.courier.com/docs/platform/content/elemental/elements/comment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Comment

> Add non-rendered comments to your Elemental templates for documentation and organization. Comments are not included in the final notification output.

## Overview

The comment element allows you to include comments in your Elemental structure that won't be rendered in the final output. This is useful for documenting your templates, adding notes for team members, or organizing complex Elemental structures.

**When to use:**

* Document complex template logic
* Add notes for other developers
* Organize and label sections of your template
* Include metadata that shouldn't appear in notifications

<Note>
  Comments are completely ignored during rendering and will never appear in the final notification output, regardless of channel.
</Note>

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "comment",
    "comment": "This is a comment that won't be rendered in the output"
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
            type: "comment",
            comment: "Welcome section - shown to all new users",
          },
          {
            type: "text",
            content: "Welcome to our platform!",
          },
          {
            type: "comment",
            comment: "CTA section - only shown to free tier users",
          },
          {
            type: "action",
            content: "Upgrade",
            href: "https://example.com/upgrade",
            if: "{{user.plan}} === 'free'",
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
                      "type": "comment",
                      "comment": "Welcome section - shown to all new users",
                  },
                  {"type": "text", "content": "Welcome to our platform!"},
                  {
                      "type": "comment",
                      "comment": "CTA section - only shown to free tier users",
                  },
                  {
                      "type": "action",
                      "content": "Upgrade",
                      "href": "https://example.com/upgrade",
                      "if": "{{user.plan}} === 'free'",
                  },
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For comment elements, this value must be `"comment"`.
</ParamField>

<ParamField path="comment" type="string">
  The comment text. This is the documentation or note you want to include. It will not be rendered in the final output.
</ParamField>

<ParamField path="object" type="any">
  An optional object that can be included with the comment. Useful for storing metadata, structured notes, or additional context that won't be rendered.
</ParamField>

## Examples & Variants

### Simple Comment

Add a basic text comment:

```json  theme={null}
{
  "type": "comment",
  "comment": "This section handles order confirmations"
}
```

### Comment with Metadata

Include structured data with your comment:

```json  theme={null}
{
  "type": "comment",
  "comment": "A/B test variant A - shows promotional content",
  "object": {
    "test_id": "promo_ab_test",
    "variant": "A",
    "author": "team-marketing",
    "last_updated": "2024-01-15"
  }
}
```

### Organizing Template Sections

Use comments to organize and label different sections:

```json  theme={null}
{
  "version": "2022-01-01",
  "elements": [
    {
      "type": "comment",
      "comment": "=== HEADER SECTION ==="
    },
    {
      "type": "meta",
      "title": "Order Confirmation"
    },
    {
      "type": "image",
      "src": "https://example.com/logo.png"
    },
    {
      "type": "comment",
      "comment": "=== MAIN CONTENT ==="
    },
    {
      "type": "text",
      "content": "Your order has been confirmed!"
    },
    {
      "type": "comment",
      "comment": "=== FOOTER SECTION ==="
    },
    {
      "type": "text",
      "content": "Questions? Contact support@example.com"
    }
  ]
}
```

### Documenting Conditional Logic

Document complex conditional logic:

```json  theme={null}
{
  "type": "comment",
  "comment": "Show upgrade CTA only for free tier users who haven't seen this in the last 30 days"
},
{
  "type": "action",
  "content": "Upgrade to Pro",
  "href": "https://example.com/upgrade",
  "if": "{{user.plan}} === 'free' && {{user.last_upgrade_prompt}} < {{now - 30 days}}"
}
```

## Use Cases

### Template Documentation

Document the purpose and structure of your templates for team members:

```json  theme={null}
{
  "type": "comment",
  "comment": "Welcome email template v2.3 - Updated 2024-01-15 by @jane.doe"
}
```

### A/B Testing Metadata

Store test variant information:

```json  theme={null}
{
  "type": "comment",
  "comment": "A/B test: Welcome message variant",
  "object": {
    "experiment": "welcome_message_2024",
    "variant": "B",
    "start_date": "2024-01-01"
  }
}
```

### Development Notes

Add notes during development:

```json  theme={null}
{
  "type": "comment",
  "comment": "TODO: Add localization for Spanish and French"
}
```

## Best Practices

* **Use descriptive comments**: Make comments clear and helpful for future developers
* **Organize sections**: Use comments to visually separate different parts of your template
* **Document complex logic**: Explain why certain conditionals or logic exist
* **Include metadata**: Use the `object` field to store structured information about the template

## Related Elements

* [Group Element](/platform/content/elemental/elements/group) - For organizing elements together
* [Control Flow](/platform/content/elemental/control-flow) - For conditional rendering logic
* [Elemental Overview](/platform/content/elemental/elemental-overview) - For understanding Elemental structure
