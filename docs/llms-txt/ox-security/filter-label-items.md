# Source: https://docs.ox.security/api-documentation/api-reference/api--filters/types/objects/filter-label-items.md

# filterLabelItems

Filter labels.

### Examples

```graphql
type FilterLabelItems {
  id: String
  label: String
}
```

### Fields

| Field          | Description                  | Supported fields |
| -------------- | ---------------------------- | ---------------- |
| id `String`    | Filter identifier            |                  |
| label `String` | Display label for the filter |                  |

### References

#### Queries using this object

* [\<?> getFilterLabels](https://docs.ox.security/api-documentation/api-reference/api--filters/queries/get-filter-labels)
