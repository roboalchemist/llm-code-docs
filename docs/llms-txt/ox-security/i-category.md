# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-category.md

# iCategory

Represents a category classification for an issue.

### Examples

```graphql
type ICategory {
  name: String
  categoryId: Int
  subCategoryName: String
  subCategoryComment: String
}
```

### Fields

| Field                       | Description                                   | Supported fields |
| --------------------------- | --------------------------------------------- | ---------------- |
| name `String`               | Name of the category                          |                  |
| categoryId `Int`            | Numeric identifier of the category            |                  |
| subCategoryName `String`    | Name of the sub-category within the category  |                  |
| subCategoryComment `String` | Comment or description about the sub-category |                  |

### References

#### Fields with this object

* [{} Issue.category](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
