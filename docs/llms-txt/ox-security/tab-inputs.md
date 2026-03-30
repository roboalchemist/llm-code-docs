# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/tab-inputs.md

# tabInputs

Configuration input field within a tab.

### Examples

```graphql
type TabInputs {
  inputType: InputTypes
  inputTitle: String
  inputName: String
}
```

### Fields

| Field                                                                                                                      | Description                                | Supported fields |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ---------------- |
| inputType [`InputTypes`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/input-types) | Type of input field (text, checkbox, etc.) |                  |
| inputTitle `String`                                                                                                        | Display title for the input field          |                  |
| inputName `String`                                                                                                         | Internal name for the input field          |                  |

### References

#### Fields with this object

* [{} ConditionalOptionalTabs.tabInputs](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/conditional-optional-tabs)
