# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/third-party-file.md

# thirdPartyFile

### Examples

```graphql
type ThirdPartyFile {
  requestId: String!
  tool: String!
  status: String!
  metadata: [MetadataEntry!]
}
```

### Fields

| Field                                                                                                                                   | Description                                                                | Supported fields                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| requestId `String!`                                                                                                                     | Unique identifier for the file request                                     |                                                                      |
| tool `String!`                                                                                                                          | Name of the tool that generated the file                                   |                                                                      |
| status `String!`                                                                                                                        | File Status                                                                |                                                                      |
| metadata [`[MetadataEntry!]`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/metadata-entry) | File metadata, may contain error information in case of validation failure | <p>path <code>\[String!]!</code><br>message <code>String!</code></p> |

### References

#### Fields with this object

* [{} FetchThirdPartyFileListResponse.files](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/fetch-third-party-file-list-response)
