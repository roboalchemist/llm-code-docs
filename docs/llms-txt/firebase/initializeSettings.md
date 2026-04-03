# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings.md.txt

# Method: projects.initializeSettings

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings#try-it)

Creates resources for settings which have not yet been set.

Currently, this creates a single resource: a Google Cloud Storage bucket, to be used as the default bucket for this project. The bucket is created in an FTL-own storage project. Except for in rare cases, calling this method in parallel from multiple clients will only create a single bucket. In order to avoid unnecessary storage charges, the bucket is configured to automatically delete objects older than 90 days.

The bucket is created with the following permissions: - Owner access for owners of central storage project (FTL-owned) - Writer access for owners/editors of customer project - Reader access for viewers of customer project The default ACL on objects created in the bucket is: - Owner access for owners of central storage project - Reader access for owners/editors/viewers of customer project See Google Cloud Storage documentation for more details.

If there is already a default bucket set and the project can access the bucket, this call does nothing. However, if the project doesn't have the permission to access the bucket or the bucket is deleted, a new bucket will be created.

May return any canonical error codes, including the following:

- PERMISSION_DENIED - if the user is not authorized to write to project
- Any error code raised by Google Cloud Storage

### HTTP request

`POST https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}:initializeSettings`

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