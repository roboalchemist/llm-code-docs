# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/extra-info-container.md

# extraInfoContainer

Container holding additional context info for an issue or evidence.

### Examples

```graphql
type ExtraInfoContainer {
  layerSha: String
  layerNum: Int
  artifactName: String
  sha: String
  registryName: String
}
```

### Fields

| Field                 | Description                                             | Supported fields |
| --------------------- | ------------------------------------------------------- | ---------------- |
| layerSha `String`     | SHA identifier of the container layer                   |                  |
| layerNum `Int`        | Number of the container layer                           |                  |
| artifactName `String` | Name of the artifact related to this info               |                  |
| sha `String`          | SHA identifier of the artifact or related item          |                  |
| registryName `String` | Name of the registry from which the artifact originates |                  |

### References

#### Fields with this object

* [{} SeverityChangedReason.extraInfoContainer](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-changed-reason)
