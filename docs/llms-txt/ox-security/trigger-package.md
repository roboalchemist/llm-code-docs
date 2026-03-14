# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/trigger-package.md

# triggerPackage

Details of a package that triggered the SCA vulnerability.

### Examples

```graphql
type TriggerPackage {
  scaTriggerPkg: String
  fileName: String
}
```

### Fields

| Field                  | Description                                      | Supported fields |
| ---------------------- | ------------------------------------------------ | ---------------- |
| scaTriggerPkg `String` | Name of the triggering package                   |                  |
| fileName `String`      | File name associated with the triggering package |                  |

### References

#### Fields with this object

* [{} Issue.scaTriggerPkgs](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
