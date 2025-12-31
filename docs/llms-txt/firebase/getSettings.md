# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings.md.txt

# Method: projects.getSettings

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings#try-it)

Gets the Tool Results settings for a project.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read from project

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/settings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                  Parameters                   ||
|-------------|----------------------------------|
| `projectId` | `string` A Project id. Required. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of [ProjectSettings](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ProjectSettings).

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).