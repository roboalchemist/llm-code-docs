# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/sca-fix-type.md

# scaFixType

Types of fixes available for SCA vulnerabilities.

### Examples

```graphql
enum ScaFixType {
  UNKNOWN
  UNAVAILABLE
  MAJOR
  MINOR
  PATCH
}
```

### Enum values

| Enum value  | Description                                                            |
| ----------- | ---------------------------------------------------------------------- |
| UNKNOWN     | Fix type cannot be determined                                          |
| UNAVAILABLE | No fix is currently available                                          |
| MAJOR       | Requires a major version update which may include breaking changes     |
| MINOR       | Requires a minor version update with backward-compatible functionality |
| PATCH       | Requires a patch version update with backward-compatible bug fixes     |

### References

#### Fields with this object

* [{} IssueFilters.scaFixType](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issue-filters)
* [{} Issue.scaFixType](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
