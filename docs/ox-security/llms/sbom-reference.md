# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-reference.md

# sbomReference

Represents a reference to a package dependency within the SBOM.

### Examples

```graphql
type SbomReference {
  triggerPackage: String
  location: String
  locationLink: String
  dependencyType: String
  dependencyLevel: Int
  commit: SbomCommit
  fileName: String
}
```

### Fields

| Field                                                                                                                | Description                                                          | Supported fields                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| triggerPackage `String`                                                                                              | The package that triggered the dependency                            |                                                                                                                  |
| location `String`                                                                                                    | Location path of the dependency within the SBOM                      |                                                                                                                  |
| locationLink `String`                                                                                                | URL link to the dependency location                                  |                                                                                                                  |
| dependencyType `String`                                                                                              | Type of the dependency                                               |                                                                                                                  |
| dependencyLevel `Int`                                                                                                | Level of the dependency in the dependency graph (distance from root) |                                                                                                                  |
| commit [`SbomCommit`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-commit) | Commit information associated with this reference                    | <p>commitedAt <code>String</code><br>committerName <code>String</code><br>committerEmail <code>String</code></p> |
| fileName `String`                                                                                                    | File name where the dependency is declared or found                  |                                                                                                                  |

### References

#### Fields with this object

* [{} SbomLib.references](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-lib)
