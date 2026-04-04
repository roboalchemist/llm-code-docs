# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cicd-info-location.md

# cicdInfoLocation

Location information for CICD jobs, including the executor, origin, and link.

### Examples

```graphql
type CicdInfoLocation {
  runBy: String
  foundBy: String
  foundIn: String
  link: String
}
```

### Fields

| Field            | Description                                     | Supported fields |
| ---------------- | ----------------------------------------------- | ---------------- |
| runBy `String`   | Entity that ran the CICD job                    |                  |
| foundBy `String` | Source of the CICD job                          |                  |
| foundIn `String` | Context or component where the job was executed |                  |
| link `String`    | Link to the job or related resource             |                  |

### References

#### Fields with this object

* [{} CicdInfo.location](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cicd-info)
