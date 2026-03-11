# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/types/enums/sbom-lib-sort-fields.md

# sbomLibSortFields

Defines fields available for sorting SBOM library listings.

### Examples

```graphql
enum SbomLibSortFields {
  LibraryName
  Licenses
  LicenseIssue
  CVE
  NotUsed
  NotUpdated
  NotMaintained
  NotPopular
  Source
  AppName
  Forks
  Stars
  PackageName
  LibraryVersion
  Language
  Copyright
  Dependency
  LatestVersion
  LatestVersionDate
  PackageManager
  CopyrightLink
  OpenIssues
  Maintainers
  SHA
  SourceLink
  Malicious
  UsedVersionReleaseDate
  ProjectDescription
}
```

### Enum values

| Enum value             | Description                                   |
| ---------------------- | --------------------------------------------- |
| LibraryName            | Sort by library name                          |
| Licenses               | Sort by license type                          |
| LicenseIssue           | Sort by presence of license compliance issues |
| CVE                    | Sort by presence of known vulnerabilities     |
| NotUsed                | Sort by usage status                          |
| NotUpdated             | Sort by update status                         |
| NotMaintained          | Sort by maintenance status                    |
| NotPopular             | Sort by popularity metrics                    |
| Source                 | Sort by package source                        |
| AppName                | Sort by application name                      |
| Forks                  | Sort by number of forks                       |
| Stars                  | Sort by number of stars                       |
| PackageName            | Sort by package name                          |
| LibraryVersion         | Sort by library version                       |
| Language               | Sort by programming language                  |
| Copyright              | Sort by copyright information                 |
| Dependency             | Sort by dependency type                       |
| LatestVersion          | Sort by latest version                        |
| LatestVersionDate      | Sort by latest version date                   |
| PackageManager         | Sort by package manager                       |
| CopyrightLink          | Sort by copyright link                        |
| OpenIssues             | Sort by number of open issues                 |
| Maintainers            | Sort by number of maintainers                 |
| SHA                    | Sort by SHA hash                              |
| SourceLink             | Sort by source link                           |
| Malicious              | Sort by malicious software                    |
| UsedVersionReleaseDate | Sort by used version release date             |
| ProjectDescription     | Sort by project description                   |

### References

#### Fields with this object

* [{} SbomLibSortInput.fields](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/sbom-lib-sort-input)
