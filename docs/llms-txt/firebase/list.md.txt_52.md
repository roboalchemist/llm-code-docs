# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list.md.txt

# Method: projects.deviceSessions.list

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.ListDeviceSessionsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.aspect)
- [IAM Permissions](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#body.aspect_1)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list#try-it)

GET /v1/projects/{projectId}/deviceSessions Lists device Sessions owned by the project user.

### HTTP request

`GET https://testing.googleapis.com/v1/{parent=projects/*}/deviceSessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The name of the parent to request, e.g. "projects/{projectId}" |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. The maximum number of DeviceSessions to return. |
| `pageToken` | `string` Optional. A continuation token for paging. |
| `filter` | `string` Optional. If specified, responses will be filtered by the given filter. Allowed fields are: sessionState. |

### Request body

The request body must be empty.

### Response body

A list of device sessions.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "deviceSessions": [ { object (`https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions#DeviceSession`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `deviceSessions[]` | ``object (`https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions#DeviceSession`)`` The sessions matching the specified filter in the given cloud project. |
| `nextPageToken` | `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `cloudtestservice.devicesession.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).