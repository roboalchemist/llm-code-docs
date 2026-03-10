# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch.md.txt

# Method: projects.deviceSessions.patch

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#body.aspect)
- [IAM Permissions](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#body.aspect_1)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch#try-it)

PATCH /v1/projects/{projectId}/deviceSessions/deviceSessionId}:updateDeviceSession Updates the current device session to the fields described by the updateMask.

### HTTP request

`PATCH https://testing.googleapis.com/v1/{deviceSession.name=projects/*/deviceSessions/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `deviceSession.name` | `string` Optional. Name of the DeviceSession, e.g. "projects/{projectId}/deviceSessions/{session_id}" |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. The list of fields to update. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions#DeviceSession`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions#DeviceSession`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `cloudtestservice.devicesession.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).