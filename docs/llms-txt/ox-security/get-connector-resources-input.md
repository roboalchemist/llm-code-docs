# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/get-connector-resources-input.md

# getConnectorResourcesInput

Input parameters for retrieving connector resources.

### Examples

```graphql
input GetConnectorResourcesInput {
  connectorID: String!
  credentialsId: String
  featureFlags: JSON
}
```

### Fields

| Field                  | Description                                                | Supported fields |
| ---------------------- | ---------------------------------------------------------- | ---------------- |
| connectorID `String!`  | Unique identifier of the connector to fetch resources from |                  |
| credentialsId `String` | Optional credentials identifier for authentication         |                  |
| featureFlags `JSON`    | Object with feature flags passed from FE                   |                  |

### References

#### Queries using this object

* [\<?> getConnectorResources.getConnectorResourcesInput](https://docs.ox.security/api-documentation/api-reference/api--connectors/queries/get-connector-resources)
