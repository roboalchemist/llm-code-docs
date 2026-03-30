# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclude-application-input.md

# excludeApplicationInput

Input for excluding an application.

### Examples

```graphql
input ExcludeApplicationInput {
  appId: String!
  appName: String!
  comment: String
}
```

### Fields

| Field             | Description                        | Supported fields |
| ----------------- | ---------------------------------- | ---------------- |
| appId `String!`   | ID of the application to exclude   |                  |
| appName `String!` | Name of the application to exclude |                  |
| comment `String`  | Comment explaining the exclusion   |                  |

### References

#### Mutations using this object

* [<\~> excludeApplications.input](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/exclude-applications)
