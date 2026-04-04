# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/optional-connector-input.md

# optionalConnectorInput

Additional configurable input fields for connectors.

### Examples

```graphql
type OptionalConnectorInput {
  name: String
  credsTypes: [CredentialsType]
  inputType: InputTypes
  key: String
  ffKey: String
  value: String
}
```

### Fields

| Field                                                                                                                                   | Description                                       | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------- |
| name `String`                                                                                                                           | Display name of the input field                   |                  |
| credsTypes [`[CredentialsType]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/credentials-type) | Types of credentials this input is applicable for |                  |
| inputType [`InputTypes`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/input-types)              | Type of input field (text, checkbox, etc.)        |                  |
| key `String`                                                                                                                            | Unique identifier for the input field             |                  |
| ffKey `String`                                                                                                                          | Feature flag key associated with this input       |                  |
| value `String`                                                                                                                          | Default or current value of the input             |                  |

### References

#### Fields with this object

* [{} Connector.optionalInputFields](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
