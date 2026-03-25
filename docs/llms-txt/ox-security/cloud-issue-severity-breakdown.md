# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-issue-severity-breakdown.md

# cloudIssueSeverityBreakdown

Represents a breakdown of issues for a single policy category with severity counts.

### Examples

```graphql
type CloudIssueSeverityBreakdown {
  name: String
  severities: Severities
}
```

### Fields

| Field                                                                                                                         | Description                       | Supported fields                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name `String`                                                                                                                 | Name of the policy category       |                                                                                                                                                                 |
| severities [`Severities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities) | Severity counts for this category | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p> |

### References

#### Fields with this object

* [{} CloudItem.issueSeverityBreakdown](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)
