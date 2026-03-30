# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-categories.md

# appCategories

Represents category information for an application, including severities and scores.

### Examples

```graphql
type AppCategories {
  categoryName: String
  categoryId: String
  catId: Int
  severities: AppSeverities
  score: Float
  severityScore: String
  total: Float
  isNa: Boolean
  reason: [String]
}
```

### Fields

| Field                                                                                                                                | Description                                      | Supported fields                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| categoryName `String`                                                                                                                | The name of the category                         |                                                                                                                                                                 |
| categoryId `String`                                                                                                                  | The unique identifier of the category            |                                                                                                                                                                 |
| catId `Int`                                                                                                                          | The numeric identifier of the category           |                                                                                                                                                                 |
| severities [`AppSeverities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-severities) | Severity counts for issues within this category  | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p> |
| score `Float`                                                                                                                        | The risk or severity score for the category      |                                                                                                                                                                 |
| severityScore `String`                                                                                                               | A string representation of the severity score    |                                                                                                                                                                 |
| total `Float`                                                                                                                        | The total count of issues within the category    |                                                                                                                                                                 |
| ~~isNa `Boolean`~~ ⚠️                                                                                                                | **Deprecated**: This field is not used anymore   |                                                                                                                                                                 |
| reason `[String]`                                                                                                                    | Reasons or comments associated with the category |                                                                                                                                                                 |

### References

#### Fields with this object

* [{} Application.categories](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
