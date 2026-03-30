# Source: https://docs.knock.app/mapi-reference/templates/schemas/chat_template.md

### ChatTemplate

A chat template.

#### Attributes

- **json_body** (string) - A JSON template for the chat notification message payload. Only present if not using the markdown body.
- **markdown_body** (string) *required* - The markdown body of the chat template.
- **summary** (string) - The summary of the chat template. Used by some chat apps in their push notifications.

#### Example

```json
{
  "json_body": null,
  "markdown_body": "**Hello**, world!",
  "summary": "Hello, world!"
}
```

