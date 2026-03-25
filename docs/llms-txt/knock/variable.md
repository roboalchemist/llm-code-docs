# Source: https://docs.knock.app/mapi-reference/variables/schemas/variable.md

### Variable

An environment variable object.

#### Attributes

- **description** (string) - The description of the variable.
- **inserted_at** (string) *required* - The timestamp of when the variable was created.
- **key** (string) *required* - The key of the variable.
- **type** (string) *required* - The type of the variable.
- **updated_at** (string) *required* - The timestamp of when the variable was last updated.
- **value** (string) *required* - The value of the variable.

#### Example

```json
{
  "description": "This is a description of my variable.",
  "inserted_at": "2021-01-01T00:00:00Z",
  "key": "my_variable",
  "type": "public",
  "updated_at": "2021-01-01T00:00:00Z",
  "value": "my_value"
}
```

