# Source: https://docs.knock.app/mapi-reference/partials/schemas/partial.md

### Partial

A partial is a reusable piece of content that can be used in a template.

#### Attributes

- **content** (string) *required* - The partial content.
- **description** (string) - An arbitrary string attached to a partial object. Useful for adding notes about the partial for internal purposes. Maximum of 280 characters allowed.
- **environment** (string) - The slug of the environment in which the partial exists.
- **icon_name** (string) - The name of the icon to be used in the visual editor.
- **input_schema** (array) - The field types available for the partial.
- **inserted_at** (string) *required* - The timestamp of when the partial was created.
- **key** (string) *required* - The unique key string for the partial object. Must be at minimum 3 characters and at maximum 255 characters in length. Must be in the format of ^[a-z0-9_-]+$.
- **name** (string) *required* - A name for the partial. Must be at maximum 255 characters in length.
- **type** (string) *required* - The partial type. One of 'html', 'json', 'markdown', 'text'.
- **updated_at** (string) *required* - The timestamp of when the partial was last updated.
- **valid** (boolean) *required* - Whether the partial and its content are in a valid state.
- **visual_block_enabled** (boolean) - Indicates whether the partial can be used in the visual editor. Only applies to HTML partials.

#### Example

```json
{
  "content": "<p>Hello, world!</p>",
  "description": "This is a test partial",
  "environment": "development",
  "icon_name": "icon-name",
  "input_schema": [
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
  "inserted_at": "2021-01-01T00:00:00Z",
  "key": "my-partial",
  "name": "My Partial",
  "type": "html",
  "updated_at": "2021-01-01T00:00:00Z",
  "valid": true,
  "visual_block_enabled": true
}
```

