# Source: https://docs.knock.app/mapi-reference/templates/schemas/push_template.md

### PushTemplate

A push notification template.

#### Attributes

- **settings** (object) *required* - The [settings](https://docs.knock.app/integrations/sms/settings-and-overrides) for the push template.
- **text_body** (string) *required* - The body of the push notification.
- **title** (string) *required* - The title of the push notification.

#### Example

```json
{
  "settings": {
    "delivery_type": "content",
    "payload_overrides": "{\"name\": \"John\"}"
  },
  "text_body": "Hello, world!",
  "title": "Hello, world!"
}
```

