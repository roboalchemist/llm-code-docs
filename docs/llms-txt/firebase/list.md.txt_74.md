# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list.md.txt

# Method: projects.histories.executions.steps.testCases.list

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#body.ListTestCasesResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list#try-it)

Lists Test Cases attached to a Step. Experimental test cases API. Still in active development.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the containing Step does not exist

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` A Project id. Required. |
| `historyId` | `string` A History id. Required. |
| `executionId` | `string` A Execution id Required. |
| `stepId` | `string` A Step id. Note: This step must include a TestExecutionStep. Required. |

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` A continuation token to resume the query at the next item. Optional. |
| `pageSize` | `integer` The maximum number of TestCases to fetch. Default value: 100. The server will use this default if the field is not set or has a value of 0. Optional. |

### Request body

The request body must be empty.

### Response body

Response message for StepService.ListTestCases.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "testCases": [ { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases#TestCase`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `testCases[]` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases#TestCase`)`` List of test cases. |
| `nextPageToken` | `string` |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).