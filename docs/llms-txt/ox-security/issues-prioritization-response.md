# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issues-prioritization-response.md

# issuesPrioritizationResponse

### Examples

```graphql
type IssuesPrioritizationResponse {
  originalSeverity: [PrioritizationInfo]
  oxPrioritization: [PrioritizationInfo]
  oxAggregation: [PrioritizationInfo]
  slaOverdue: [PrioritizationInfo]
}
```

### Fields

| Field                                                                                                                                            | Description | Supported fields                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------------------------------------------------- |
| originalSeverity [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info) |             | <p>label <code>String</code><br>count <code>Int</code></p> |
| oxPrioritization [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info) |             | <p>label <code>String</code><br>count <code>Int</code></p> |
| oxAggregation [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info)    |             | <p>label <code>String</code><br>count <code>Int</code></p> |
| slaOverdue [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info)       |             | <p>label <code>String</code><br>count <code>Int</code></p> |

### References

#### Queries using this object

* [\<?> getIssuePrioritization](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issue-prioritization)
