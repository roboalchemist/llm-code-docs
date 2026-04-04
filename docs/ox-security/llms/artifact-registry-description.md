# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-registry-description.md

# artifactRegistryDescription

Description of an artifact registry.

### Examples

```graphql
type ArtifactRegistryDescription {
  type: String
  name: String
  project: String
  link: String
  hash: String
  tags: [String]
  username: String
  userType: String
  uploadTime: Float
  lastUpdate: Float
  buildTime: Float
}
```

### Fields

| Field              | Description                                               | Supported fields |
| ------------------ | --------------------------------------------------------- | ---------------- |
| type `String`      | Type of the artifact registry                             |                  |
| name `String`      | Name of the artifact registry                             |                  |
| project `String`   | Project or repository name within the registry            |                  |
| link `String`      | URL link to the artifact or registry page                 |                  |
| hash `String`      | Hash or digest of the artifact                            |                  |
| tags `[String]`    | List of tags associated with the artifact                 |                  |
| username `String`  | Username of the user who uploaded or manages the artifact |                  |
| userType `String`  | Type or role of the user                                  |                  |
| uploadTime `Float` | Timestamp (epoch) when the artifact was uploaded          |                  |
| lastUpdate `Float` | Timestamp (epoch) of the last update to the artifact      |                  |
| buildTime `Float`  | Timestamp (epoch) of the artifact's build time            |                  |

### References

#### Fields with this object

* [{} ArtifactInfo.registryDescription](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
