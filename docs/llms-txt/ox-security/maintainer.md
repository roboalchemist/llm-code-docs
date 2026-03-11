# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/maintainer.md

# maintainer

Represents a maintainer of a software library.

### Examples

```graphql
type Maintainer {
  name: String
  email: String
}
```

### Fields

| Field          | Description                     | Supported fields |
| -------------- | ------------------------------- | ---------------- |
| name `String`  | Name of the maintainer          |                  |
| email `String` | Email address of the maintainer |                  |

### References

#### Fields with this object

* [{} SbomLib.maintainersList](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-lib)
