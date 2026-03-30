# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/count-rule.md

# countRule

Rules for counting and aggregating issues in different contexts. Determines how issues are counted based on their type and relationship.

### Examples

```graphql
enum CountRule {
  aggItems
  scaVulnerabilities
  default
  artifactFiles
}
```

### Enum values

| Enum value         | Description                               |
| ------------------ | ----------------------------------------- |
| aggItems           | Count based on aggregated items           |
| scaVulnerabilities | Count based on SCA vulnerability findings |
| default            | Default counting method                   |
| artifactFiles      | Count based on artifact file occurrences  |

### References

#### Fields with this object

* [{} Issue.countRule](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
