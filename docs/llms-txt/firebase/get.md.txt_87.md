# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get.md.txt

# Method: projects.histories.get

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get#try-it)

Gets a History.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the History does not exist

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` A Project id. Required. |
| `historyId` | `string` A History id. Required. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories#History`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).