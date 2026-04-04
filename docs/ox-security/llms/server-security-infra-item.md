# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/server-security-infra-item.md

# serverSecurityInfraItem

Security infrastructure coverage item with coverage percentages.

### Examples

```graphql
type ServerSecurityInfraItem {
  label: String
  clientCoverage: Float
  oxCoverage: Float
  noCoverage: Float
  notApplicable: Float
}
```

### Fields

| Field                  | Description                                                    | Supported fields |
| ---------------------- | -------------------------------------------------------------- | ---------------- |
| label `String`         | Label or name of the security infrastructure component         |                  |
| clientCoverage `Float` | Percentage of coverage provided by client-side security tools  |                  |
| oxCoverage `Float`     | Percentage of coverage provided by OX Security platform        |                  |
| noCoverage `Float`     | Percentage of assets with no security coverage                 |                  |
| notApplicable `Float`  | Percentage of assets where security coverage is not applicable |                  |

### References

#### Fields with this object

* [{} Application.secInfrastructure](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
