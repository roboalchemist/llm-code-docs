# Source: https://docs.knock.app/mapi-reference/message_types/schemas/message_type_variant.md

### MessageTypeVariant

A variant of a message type.

#### Attributes

- **fields** (array) *required* - The field types available for the variant.
- **key** (string) *required* - The unique key string for the variant. Must be at minimum 3 characters and at maximum 255 characters in length. Must be in the format of ^[a-z0-9_-]+$.
- **name** (string) *required* - A name for the variant. Must be at maximum 255 characters in length.

#### Example

```json
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
```

