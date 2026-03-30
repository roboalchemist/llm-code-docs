# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifact-input.md

# getUnscannedArtifactInput

Input parameters for retrieving a specific unscanned artifact.

### Examples

```graphql
input GetUnscannedArtifactInput {
  artifactId: String
}
```

### Fields

| Field               | Description                                             | Supported fields |
| ------------------- | ------------------------------------------------------- | ---------------- |
| artifactId `String` | Unique identifier of the unscanned artifact to retrieve |                  |

### References

#### Queries using this object

* [\<?> getUnscannedArtifact.getUnscannedArtifactInput](https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-unscanned-artifact)
