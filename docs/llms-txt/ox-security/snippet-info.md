# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/snippet-info.md

# snippetInfo

Information about a code snippet related to an issue or severity change.

### Examples

```graphql
type SnippetInfo {
  snippetLineNumber: Int
  language: String
  text: String
  fileName: String
}
```

### Fields

| Field                   | Description                                   | Supported fields |
| ----------------------- | --------------------------------------------- | ---------------- |
| snippetLineNumber `Int` | Line number of the snippet in the source file |                  |
| language `String`       | Programming language of the snippet           |                  |
| text `String`           | Text content of the code snippet              |                  |
| fileName `String`       | Name of the file containing the snippet       |                  |

### References

#### Fields with this object

* [{} SeverityChangedExtraInfo.snippet](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-changed-extra-info)
