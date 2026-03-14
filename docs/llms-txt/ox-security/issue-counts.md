# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/issue-counts.md

# issueCounts

Counts of different issue types for an artifact.

### Examples

```graphql
type IssueCounts {
  vulnDepIssues: Int
  vulnDepBaseIssues: Int
  vulnDepInstructionIssues: Int
  vulnDepPublicImageIssues: Int
}
```

### Fields

| Field                          | Description                                                | Supported fields |
| ------------------------------ | ---------------------------------------------------------- | ---------------- |
| vulnDepIssues `Int`            | Count of vulnerability dependency issues                   |                  |
| vulnDepBaseIssues `Int`        | Count of base vulnerability dependency issues              |                  |
| vulnDepInstructionIssues `Int` | Count of instruction-level vulnerability dependency issues |                  |
| vulnDepPublicImageIssues `Int` | Count of public image vulnerability dependency issues      |                  |

### References

#### Fields with this object

* [{} ArtifactInfo.counts](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
