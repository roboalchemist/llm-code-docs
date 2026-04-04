# Source: https://docs.knock.app/mapi-reference/translations/schemas/translation.md

### Translation

A translation object.

#### Attributes

- **content** (string) *required* - A JSON encoded string containing the key-value pairs of translation references and translation strings.
- **format** (string) *required* - Indicates whether content is a JSON encoded object string or a string in the PO format.
- **inserted_at** (string) *required* - The timestamp of when the translation was created.
- **locale_code** (string) *required* - The locale code for the translation object.
- **namespace** (string) *required* - An optional namespace for the translation to help categorize your translations.
- **updated_at** (string) *required* - The timestamp of when the translation was last updated.

#### Example

```json
{
  "content": "{\"hello\":\"Hello, world!\"}",
  "format": "json",
  "inserted_at": "2021-01-01T00:00:00Z",
  "locale_code": "en",
  "namespace": "my_app",
  "updated_at": "2021-01-01T00:00:00Z"
}
```

