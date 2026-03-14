# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-changed-extra-info.md

# severityChangedExtraInfo

Additional contextual information for a severity change event.

### Examples

```graphql
type SeverityChangedExtraInfo {
  key: String
  value: String
  link: String
  snippet: SnippetInfo
  iconLink: String
  callBranch: [String]
}
```

### Fields

| Field                                                                                                                   | Description                                                         | Supported fields                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| key `String`                                                                                                            | Key or label describing the extra info                              |                                                                                                                                       |
| value `String`                                                                                                          | Value or content related to the key                                 |                                                                                                                                       |
| link `String`                                                                                                           | Optional hyperlink related to this extra info                       |                                                                                                                                       |
| snippet [`SnippetInfo`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/snippet-info) | Code snippet context associated with the extra info                 | <p>snippetLineNumber <code>Int</code><br>language <code>String</code><br>text <code>String</code><br>fileName <code>String</code></p> |
| iconLink `String`                                                                                                       | URL to an icon representing this info                               |                                                                                                                                       |
| callBranch `[String]`                                                                                                   | Call branch stack or related trace information as a list of strings |                                                                                                                                       |

### References

#### Fields with this object

* [{} SeverityChangedReason.extraInfo](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-changed-reason)
