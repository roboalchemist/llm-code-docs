# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/upload-file-response.md

# uploadFileResponse

Response object containing the status of a file upload request.

### Examples

```graphql
type UploadFileResponse {
  requestId: String!
  success: Boolean!
}
```

### Fields

| Field               | Description                                       | Supported fields |
| ------------------- | ------------------------------------------------- | ---------------- |
| requestId `String!` | Unique identifier for tracking the upload request |                  |
| success `Boolean!`  | Indicates whether the file upload was successful  |                  |

### References

#### Mutations using this object

* [<\~> uploadThirdPartyFile](https://docs.ox.security/api-documentation/api-reference/api--file-download/mutations/upload-third-party-file)
* [<\~> uploadThirdPartyFileBase64](https://docs.ox.security/api-documentation/api-reference/api--file-download/mutations/upload-third-party-file-base64)
