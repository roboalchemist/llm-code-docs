# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/extra-info-snippet.md

# extraInfoSnippet

Represents a code or text snippet related to a severity change.

### Examples

```graphql
type ExtraInfoSnippet {
  detectionType: String
  fileName: String
  snippetLineNumber: Int
  language: String
  text: String
}
```

### Fields

| Field                   | Description                                             | Supported fields |
| ----------------------- | ------------------------------------------------------- | ---------------- |
| detectionType `String`  | The type of detection that identified the snippet       |                  |
| fileName `String`       | The name of the file containing the snippet             |                  |
| snippetLineNumber `Int` | The line number in the file where the snippet was found |                  |
| language `String`       | The programming language of the snippet                 |                  |
| text `String`           | The text content of the snippet                         |                  |

### References

#### Fields with this object

* [{} ApplicationExtraInfo.snippet](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-extra-info)
* [{} ExtraInfo.snippet](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/extra-info)
