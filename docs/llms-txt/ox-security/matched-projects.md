# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/matched-projects.md

# matchedProjects

Represents matched projects for an application according to a specific tool.

### Examples

```graphql
type MatchedProjects {
  toolName: String
  matchedProjects: [MatchedProject]
}
```

### Fields

| Field                                                                                                                                         | Description                                   | Supported fields                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------- |
| toolName `String`                                                                                                                             | The name of the tool that matched the project |                                                                                   |
| matchedProjects [`[MatchedProject]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/matched-project) | The list of matched projects                  | <p>externalToolProject <code>String</code><br>matchMethod <code>String</code></p> |

### References

#### Fields with this object

* [{} Application.matchedProjects](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
