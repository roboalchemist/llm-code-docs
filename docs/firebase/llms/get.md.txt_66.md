# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get.md.txt

# Method: projects.deviceSessions.get

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get#body.aspect)
- [IAM Permissions](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get#body.aspect_1)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get#try-it)

GET /v1/projects/{projectId}/deviceSessions/{device_session_id} Return a DeviceSession, which documents the allocation status and whether the device is allocated. Clients making requests from this API must poll deviceSessions.get.

### HTTP request

`GET https://testing.googleapis.com/v1/{name=projects/*/deviceSessions/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Name of the DeviceSession, e.g. "projects/{projectId}/deviceSessions/{session_id}" |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions#DeviceSession`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `cloudtestservice.devicesession.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).