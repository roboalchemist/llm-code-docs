# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/fetch-third-party-file-list-response.md

# fetchThirdPartyFileListResponse

### Examples

```graphql
type FetchThirdPartyFileListResponse {
  files: [ThirdPartyFile!]
  error: Boolean
}
```

### Fields

| Field                                                                                                                                   | Description            | Supported fields                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| files [`[ThirdPartyFile!]`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/third-party-file) | List of uploaded files | <p>requestId <code>String!</code><br>tool <code>String!</code><br>status <code>String!</code><br>metadata <a href="metadata-entry"><code>\[MetadataEntry!]</code></a></p> |
| error `Boolean`                                                                                                                         |                        |                                                                                                                                                                           |

### References

#### Queries using this object

* [\<?> fetchListOfThirdPartyIssueFiles](https://docs.ox.security/api-documentation/api-reference/api--file-download/queries/fetch-list-of-third-party-issue-files)
