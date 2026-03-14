# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-single-sbom-library-input.md

# getSingleSbomLibraryInput

Defines input parameters for retrieving a single SBOM library.

### Examples

```graphql
input GetSingleSbomLibraryInput {
  scanId: String
  appId: String
  library: String
  libraryName: String
  triggerPackage: String
  libId: String
}
```

### Fields

| Field                   | Description                                    | Supported fields |
| ----------------------- | ---------------------------------------------- | ---------------- |
| scanId `String`         | Scan identifier containing the library         |                  |
| appId `String`          | Application identifier containing the library  |                  |
| library `String`        | Library identifier or name                     |                  |
| libraryName `String`    | Specific library name to retrieve              |                  |
| triggerPackage `String` | Package that triggered this library dependency |                  |
| libId `String`          | Internal library identifier                    |                  |

### References

#### Queries using this object

* [\<?> getSingleSbomLibrary.getSingleSbomLibraryInput](https://docs.ox.security/api-documentation/api-reference/api--sbom/queries/get-single-sbom-library)
