# Source: https://docs.knock.app/mapi-reference/message_types/schemas/message_type_text_field.md

### MessageTypeTextField

A text field used in a message type.

#### Attributes

- **key** (string) *required* - The unique key of the field.
- **label** (string) *required* - The label of the field.
- **settings** (object) - Settings for the text field.
- **type** (string) *required* - The type of the field.

#### Example

```json
{
  "key": "text_field",
  "label": "Text Field",
  "settings": {
    "description": "A description of the text field",
    "max_length": 100,
    "min_length": 10,
    "placeholder": "A placeholder for the text field",
    "required": true
  },
  "type": "text"
}
```

