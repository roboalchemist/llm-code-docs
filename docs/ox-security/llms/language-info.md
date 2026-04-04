# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/language-info.md

# languageInfo

Information about the programming language related to the issue.

### Examples

```graphql
type LanguageInfo {
  name: String
  version: String
}
```

### Fields

| Field            | Description                                     | Supported fields |
| ---------------- | ----------------------------------------------- | ---------------- |
| name `String`    | Name of the programming language                |                  |
| version `String` | Version of the language or package manager used |                  |

### References

#### Fields with this object

* [{} Issue.languageInfo](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
