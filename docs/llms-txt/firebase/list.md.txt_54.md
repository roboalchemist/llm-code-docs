# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list.md.txt

# Method: projects.histories.executions.environments.list

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#body.ListEnvironmentsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list#try-it)

Lists Environments for a given Execution.

The Environments are sorted by display name.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the containing Execution does not exist

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` Required. A Project id. |
| `historyId` | `string` Required. A History id. |
| `executionId` | `string` Required. An Execution id. |

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` A continuation token to resume the query at the next item. |
| `pageSize` | `integer` The maximum number of Environments to fetch. Default value: 25. The server will use this default if the field is not set or has a value of 0. |

### Request body

The request body must be empty.

### Response body

Response message for EnvironmentService.ListEnvironments.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "projectId": string, "historyId": string, "executionId": string, "environments": [ { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments#Environment`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `projectId` | `string` A Project id. Always set. |
| `historyId` | `string` A History id. Always set. |
| `executionId` | `string` A Execution id Always set. |
| `environments[]` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments#Environment`)`` Environments. Always set. |
| `nextPageToken` | `string` A continuation token to resume the query at the next item. Will only be set if there are more Environments to fetch. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).