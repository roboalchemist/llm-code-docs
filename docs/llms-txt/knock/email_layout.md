# Source: https://docs.knock.app/mapi-reference/email_layouts/schemas/email_layout.md

### EmailLayout

A versioned email layout used within an environment.

#### Attributes

- **created_at** (string) *required* - The timestamp of when the email layout was created.
- **environment** (string) - The environment of the email layout.
- **footer_links** (array) - A list of one or more items to show in the footer of the email layout.
- **html_layout** (string) *required* - The complete HTML content of the email layout.
- **key** (string) *required* - The unique key for this email layout.
- **name** (string) *required* - The human-readable name of this email layout.
- **sha** (string) *required* - The SHA of the email layout.
- **text_layout** (string) *required* - The complete plaintext content of the email layout.
- **updated_at** (string) - The timestamp of when the email layout was last updated.

#### Example

```json
{
  "created_at": "2021-01-01T00:00:00Z",
  "environment": "development",
  "footer_links": [
    {
      "text": "Example",
      "url": "http://example.com"
    }
  ],
  "html_layout": "<html><body>Hello, world!</body></html>",
  "key": "transactional",
  "name": "Transactional",
  "sha": "1234567890",
  "text_layout": "Hello, world!",
  "updated_at": "2021-01-01T00:00:00Z"
}
```

