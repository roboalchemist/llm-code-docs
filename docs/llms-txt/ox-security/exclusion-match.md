# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion-match.md

# exclusionMatch

Match result for an exclusion.

### Examples

```graphql
type ExclusionMatch {
  key: String!
  value: String!
}
```

### Fields

| Field           | Description                | Supported fields |
| --------------- | -------------------------- | ---------------- |
| key `String!`   | Key field that was matched |                  |
| value `String!` | Value that was matched     |                  |

### References

#### Fields with this object

* [{} Exclusion.exclusionMatch](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion)
