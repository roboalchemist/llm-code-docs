# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/fetch-ready-file-response.md

# fetchReadyFileResponse

Response object containing information about the status and availability of a requested file.

### Examples

```graphql
type FetchReadyFileResponse {
  downloadLink: String
  isFileReady: Boolean!
  error: Boolean
}
```

### Fields

| Field                  | Description                                                                                          | Supported fields |
| ---------------------- | ---------------------------------------------------------------------------------------------------- | ---------------- |
| downloadLink `String`  | Pre-signed URL for downloading the file. Will be null if the file is not ready or there was an error |                  |
| isFileReady `Boolean!` | Indicates whether the requested file is ready for download                                           |                  |
| error `Boolean`        | Indicates whether an error occurred while checking file status                                       |                  |

### References

#### Queries using this object

* [\<?> fetchThirdPartyIssuesFile](https://docs.ox.security/api-documentation/api-reference/api--file-download/queries/fetch-third-party-issues-file)
