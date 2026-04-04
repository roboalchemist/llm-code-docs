# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/matched-project.md

# matchedProject

Represents a matched project for an application.

### Examples

```graphql
type MatchedProject {
  externalToolProject: String
  matchMethod: String
}
```

### Fields

| Field                        | Description                              | Supported fields |
| ---------------------------- | ---------------------------------------- | ---------------- |
| externalToolProject `String` | The name of the project that was matched |                  |
| matchMethod `String`         | The method used to match the project     |                  |

### References

#### Fields with this object

* [{} MatchedProjects.matchedProjects](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/matched-projects)
