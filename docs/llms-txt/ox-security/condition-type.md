# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/condition-type.md

# conditionType

Logical operators and comparison conditions used to build complex filters and rules. These conditions can be combined to create sophisticated filtering criteria for issues, allowing for precise control over which issues are included or excluded in queries.

### Examples

```graphql
enum ConditionType {
  AND
  OR
  NOT
  BETWEEN
  CONTAINS
  NOTCONTAINS
  STARTSWITH
}
```

### Enum values

| Enum value  | Description                                                                                                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- |
| AND         | Combines multiple conditions where all must be true with exact matching                                              |
| OR          | Combines multiple conditions where at least one must be true with exact matching                                     |
| NOT         | Negates the condition, matching when the condition is false with exact matching                                      |
| BETWEEN     | Matches values that fall within a specified numeric range                                                            |
| CONTAINS    | Matches if the value contains the specified substring or pattern, behaves like AND but with partial matching         |
| NOTCONTAINS | Matches if the value does not contain the specified substring or pattern, behaves like AND but with partial matching |
| STARTSWITH  | Matches if the value starts with the specified substring or pattern, case-insensitive prefix matching                |

### References

#### Fields with this object

* [{} ConditionalFilters.condition](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/conditional-filters)
