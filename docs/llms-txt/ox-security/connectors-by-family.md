# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connectors-by-family.md

# connectorsByFamily

Grouping of connectors by their family/category.

### Examples

```graphql
type ConnectorsByFamily {
  family: String
  familyDisplayName: String
  connectors: [ConnectorResponse]
}
```

### Fields

| Field                                                                                                                                         | Description                         | Supported fields                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| family `String`                                                                                                                               | Internal family identifier          |                                                                                                                           |
| familyDisplayName `String`                                                                                                                    | User-friendly family name           |                                                                                                                           |
| connectors [`[ConnectorResponse]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector-response) | Connectors belonging to this family | connector [`Connector`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector) |

### References

#### Queries using this object

* [\<?> getConnectorsByFamily](https://docs.ox.security/api-documentation/api-reference/api--connectors/queries/get-connectors-by-family)
