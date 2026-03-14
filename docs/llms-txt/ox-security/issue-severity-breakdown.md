# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/issue-severity-breakdown.md

# issueSeverityBreakdown

### Examples

```graphql
type IssueSeverityBreakdown {
  name: String
  tab: String
  severities: Severities
}
```

### Fields

| Field                                                                                                                         | Description | Supported fields                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name `String`                                                                                                                 |             |                                                                                                                                                                 |
| tab `String`                                                                                                                  |             |                                                                                                                                                                 |
| severities [`Severities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities) |             | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p> |

### References

#### Fields with this object

* [{} ArtifactInfo.issueSeverityBreakdown](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
