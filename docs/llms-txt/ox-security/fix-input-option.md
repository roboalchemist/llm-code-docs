# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/fix-input-option.md

# fixInputOption

Represents a selectable option for a FixInput.

### Examples

```graphql
type FixInputOption {
  name: String
  selected: Boolean
  metadata: String
  info: String
  displayName: String
  isDisabled: Boolean
}
```

### Fields

| Field                | Description                                 | Supported fields |
| -------------------- | ------------------------------------------- | ---------------- |
| name `String`        | Name identifier of the option               |                  |
| selected `Boolean`   | Indicates if this option is selected        |                  |
| metadata `String`    | Additional metadata related to the option   |                  |
| info `String`        | Informational text describing the option    |                  |
| displayName `String` | Display name for the option shown in the UI |                  |
| isDisabled `Boolean` | Indicates if the option is disabled         |                  |

### References

#### Fields with this object

* [{} FixInput.options](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/fix-input)
