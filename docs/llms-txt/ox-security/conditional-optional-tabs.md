# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/conditional-optional-tabs.md

# conditionalOptionalTabs

Grouping of optional configuration fields into tabs.

### Examples

```graphql
type ConditionalOptionalTabs {
  tabTitle: String
  tabInputs: [TabInputs]
}
```

### Fields

| Field                                                                                                                        | Description                        | Supported fields                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| tabTitle `String`                                                                                                            | Title of the configuration tab     |                                                                                                                                                |
| tabInputs [`[TabInputs]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/tab-inputs) | Input fields contained in this tab | <p>inputType <a href="../enums/input-types"><code>InputTypes</code></a><br>inputTitle <code>String</code><br>inputName <code>String</code></p> |

### References

#### Fields with this object

* [{} Connector.conditionalOptionalTabs](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
