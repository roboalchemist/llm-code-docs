# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-categories.md

# artifactCategories

Information about artifact categories and their severities.

### Examples

```graphql
type ArtifactCategories {
  catId: String
  severities: Severities
  name: String
  score: String
}
```

### Fields

| Field                                                                                                                         | Description                                                          | Supported fields                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| catId `String`                                                                                                                | Unique identifier of the category                                    |                                                                                                                                                                 |
| severities [`Severities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities) | Counts of issues grouped by severity within this category            | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p> |
| name `String`                                                                                                                 | Name of the category                                                 |                                                                                                                                                                 |
| score `String`                                                                                                                | Severity score representing the max severity count for this category |                                                                                                                                                                 |

### References

#### Fields with this object

* [{} ArtifactInfo.categories](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
* [{} ArtifactInfo.artifactCategories](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
