# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel.md.txt

# Method: projects.deviceSessions.cancel

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel#body.aspect)
- [IAM Permissions](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel#body.aspect_1)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel#try-it)

POST /v1/projects/{projectId}/deviceSessions/{device_session_id}:cancel Changes the DeviceSession to state FINISHED and terminates all connections. Canceled sessions are not deleted and can be retrieved or listed by the user until they expire based on the 28 day deletion policy.

### HTTP request

`POST https://testing.googleapis.com/v1/{name=projects/*/deviceSessions/*}:cancel`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Name of the DeviceSession, e.g. "projects/{projectId}/deviceSessions/{session_id}" |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `cloudtestservice.devicesession.cancel`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).