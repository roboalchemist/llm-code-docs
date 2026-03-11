# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/fix-input.md

# fixInput

Represents an input field required for policy fix configuration.

### Examples

```graphql
type FixInput {
  type: String
  name: String
  options: [FixInputOption]
  multiSelect: Boolean
  maxSelect: Int
  minSelect: Int
  displayName: String
}
```

### Fields

| Field                                                                                                                            | Description                                     | Supported fields                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                    | Type of the input                               |                                                                                                                                                                                                    |
| name `String`                                                                                                                    | Name identifier of the input                    |                                                                                                                                                                                                    |
| options [`[FixInputOption]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/fix-input-option) | Options available for the input (if applicable) | <p>name <code>String</code><br>selected <code>Boolean</code><br>metadata <code>String</code><br>info <code>String</code><br>displayName <code>String</code><br>isDisabled <code>Boolean</code></p> |
| multiSelect `Boolean`                                                                                                            | Indicates if multiple selections are allowed    |                                                                                                                                                                                                    |
| maxSelect `Int`                                                                                                                  | Maximum number of selections allowed            |                                                                                                                                                                                                    |
| minSelect `Int`                                                                                                                  | Minimum number of selections required           |                                                                                                                                                                                                    |
| displayName `String`                                                                                                             | Display name for the input shown in the UI      |                                                                                                                                                                                                    |

### References

#### Fields with this object

* [{} PolicyFix.inputs](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/policy-fix)
