# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/previous-target-values.md

# previousTargetValues

Stores previous values of Agentic Pentest target configuration before modification.

### Examples

```graphql
type PreviousTargetValues {
  title: String
  domainType: String
  targetUrl: String
  env: String
  authMethod: String
}
```

### Fields

| Field               | Description                                  | Supported fields |
| ------------------- | -------------------------------------------- | ---------------- |
| title `String`      | Previous title of the Agentic Pentest target |                  |
| domainType `String` | Previous domain type classification          |                  |
| targetUrl `String`  | Previous target URL being scanned            |                  |
| env `String`        | Previous environment classification          |                  |
| authMethod `String` | Previous authentication method used          |                  |

### References

#### Fields with this object

* [{} AuditLog.previousValues](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
