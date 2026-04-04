# Source: https://docs.knock.app/mapi-reference/message_types/schemas/message_type.md

### MessageType

A message type is a schema for a message that maps to a UI component or element within your application.

#### Attributes

- **archived_at** (string) - The timestamp of when the message type was deleted.
- **created_at** (string) *required* - The timestamp of when the message type was created.
- **deleted_at** (string) - The timestamp of when the message type was deleted.
- **description** (string) - An arbitrary string attached to a message type object. Useful for adding notes about the message type for internal purposes. Maximum of 280 characters allowed.
- **environment** (string) *required* - The environment of the message type.
- **icon_name** (string) - The icon name of the message type.
- **key** (string) *required* - The unique key string for the message type object. Must be at minimum 3 characters and at maximum 255 characters in length. Must be in the format of ^[a-z0-9_-]+$.
- **name** (string) *required* - A name for the message type. Must be at maximum 255 characters in length.
- **owner** (string) *required* - The owner of the message type.
- **preview** (string) *required* - An HTML/liquid template for the message type preview.
- **semver** (string) *required* - The semantic version of the message type.
- **sha** (string) *required* - The SHA hash of the message type.
- **updated_at** (string) *required* - The timestamp of when the message type was last updated.
- **valid** (boolean) *required* - Whether the message type is valid.
- **variants** (array) *required* - The variants of the message type.

#### Example

```json
{
  "archived_at": null,
  "created_at": "2021-01-01T00:00:00Z",
  "deleted_at": null,
  "description": "Email message type",
  "environment": "development",
  "icon_name": "email",
  "key": "email",
  "name": "Email",
  "owner": "user",
  "preview": "<div>Hello, world!</div>",
  "semver": "1.0.0",
  "sha": "1234567890",
  "updated_at": "2021-01-01T00:00:00Z",
  "valid": true,
  "variants": [
    {
      "fields": [
        {
          "key": "text_field",
          "label": "My text field",
          "settings": {
            "description": "A description of the text field",
            "max_length": 100,
            "min_length": 10,
            "required": true
          },
          "type": "text"
        }
      ],
      "key": "default",
      "name": "Default"
    }
  ]
}
```

