# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/extra-info.md

# extraInfo

### Examples

```graphql
type ExtraInfo {
  key: String
  val: String
  value: String
  snippet: ExtraInfoSnippet
  link: String
  callBranch: [String]
  iconLink: String
  tags: [String]
}
```

### Fields

| Field                                                                                                                                    | Description                                                         | Supported fields                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key `String`                                                                                                                             | Key name of the extra info                                          |                                                                                                                                                                            |
| val `String`                                                                                                                             | Value associated with the key                                       |                                                                                                                                                                            |
| value `String`                                                                                                                           | Alternate value field, often redundant with 'val'                   |                                                                                                                                                                            |
| snippet [`ExtraInfoSnippet`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/extra-info-snippet) | Code snippet context associated with the extra info                 | <p>detectionType <code>String</code><br>fileName <code>String</code><br>snippetLineNumber <code>Int</code><br>language <code>String</code><br>text <code>String</code></p> |
| link `String`                                                                                                                            | Optional hyperlink related to this extra info                       |                                                                                                                                                                            |
| callBranch `[String]`                                                                                                                    | Call branch stack or related trace information as a list of strings |                                                                                                                                                                            |
| iconLink `String`                                                                                                                        | URL to an icon representing this info                               |                                                                                                                                                                            |
| tags `[String]`                                                                                                                          | List of tags associated with this extra info                        |                                                                                                                                                                            |

### References

#### Fields with this object

* [{} SbomLib.extraInfo](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-lib)
* [{} Issue.extraInfo](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
