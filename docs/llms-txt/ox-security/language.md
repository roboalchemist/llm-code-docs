# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/language.md

# language

Represents a programming language used in an application, including its usage percentage.

### Examples

```graphql
type Language {
  language: String
  languagePercentage: Float
}
```

### Fields

| Field                      | Description                                 | Supported fields |
| -------------------------- | ------------------------------------------- | ---------------- |
| language `String`          | Name of the programming language            |                  |
| languagePercentage `Float` | Percentage of code written in this language |                  |

### References

#### Fields with this object

* [{} Application.languages](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
