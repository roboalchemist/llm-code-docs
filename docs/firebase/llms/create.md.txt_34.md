# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create.md.txt

# Method: projects.deviceSessions.create

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create#body.aspect)
- [IAM Permissions](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create#body.aspect_1)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create#try-it)

POST /v1/projects/{projectId}/deviceSessions

### HTTP request

`POST https://testing.googleapis.com/v1/{parent=projects/*}/deviceSessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The Compute Engine project under which this device will be allocated. "projects/{projectId}" |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions#DeviceSession`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions#DeviceSession`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `cloudtestservice.devicesession.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).