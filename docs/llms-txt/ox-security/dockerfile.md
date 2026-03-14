# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/dockerfile.md

# dockerfile

Represents a Dockerfile in an application.

### Examples

```graphql
type Dockerfile {
  path: String
}
```

### Fields

| Field         | Description                                  | Supported fields |
| ------------- | -------------------------------------------- | ---------------- |
| path `String` | The path to the Dockerfile in the repository |                  |

### References

#### Fields with this object

* [{} Application.dockerfiles](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
