# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/sbom-lib-filters.md

# sbomLibFilters

Defines filter criteria for searching and filtering SBOM libraries.

### Examples

```graphql
input SBOMLibFilters {
  libForSearch: [String]
  libraryNames: [String]
  libraryVersions: [String]
  apps: [String]
  appIds: [String]
  source: [String]
  dependencyTypes: [String]
  licenses: [String]
  packageNames: [String]
  copyrights: [String]
  severities: [String]
  packageInfos: [String]
  malicious: [String]
  packageManagers: [String]
  cve: [String]
  languages: [String]
  os: [String]
  registryName: [String]
  baseImage: [String]
  image: [String]
  reachability: [String]
  tags: [String]
  imageSource: [String]
  licenseIssue: [Boolean]
  sbomImageTags: [String]
  runtimeStatus: [String]
}
```

### Fields

| Field                      | Description                                       | Supported fields |
| -------------------------- | ------------------------------------------------- | ---------------- |
| libForSearch `[String]`    | Filter by library for search                      |                  |
| libraryNames `[String]`    | Filter by specific library names                  |                  |
| libraryVersions `[String]` | Filter by specific library versions               |                  |
| apps `[String]`            | Filter by application names                       |                  |
| appIds `[String]`          | Filter by application identifiers                 |                  |
| source `[String]`          | Filter by library source (npm, Maven, PyPI, etc.) |                  |
| dependencyTypes `[String]` | Filter by dependency types (direct, transitive)   |                  |
| licenses `[String]`        | Filter by license types                           |                  |
| packageNames `[String]`    | Filter by package names                           |                  |
| copyrights `[String]`      | Filter by copyright information                   |                  |
| severities `[String]`      | Filter by vulnerability severity levels           |                  |
| packageInfos `[String]`    | Filter by package information categories          |                  |
| malicious `[String]`       | Filter by malicious software                      |                  |
| packageManagers `[String]` | Filter by package managers                        |                  |
| cve `[String]`             | Filter by CVE identifiers                         |                  |
| languages `[String]`       | Filter by programming languages                   |                  |
| os `[String]`              | Filter by operating systems                       |                  |
| registryName `[String]`    | Filter by container registry names                |                  |
| baseImage `[String]`       | Filter by base container images                   |                  |
| image `[String]`           | Filter by container images                        |                  |
| reachability `[String]`    | Filter by code reachability status                |                  |
| tags `[String]`            | Filter by tags                                    |                  |
| imageSource `[String]`     | Filter by image source                            |                  |
| licenseIssue `[Boolean]`   | Filter by license compliance issues               |                  |
| sbomImageTags `[String]`   | Filter by image tags                              |                  |
| runtimeStatus `[String]`   | Filter by runtime status (eBPF loading state)     |                  |

### References

#### Fields with this object

* [{} GetApplicationsSbom.filters](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-applications-sbom)
* [{} SbomVulnerableLibrariesInput.filters](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/sbom-vulnerable-libraries-input)
