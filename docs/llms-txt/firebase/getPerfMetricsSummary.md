# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary.md.txt

# Method: projects.histories.executions.steps.getPerfMetricsSummary

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary#try-it)

Retrieves a PerfMetricsSummary.

May return any of the following error code(s): - NOT_FOUND - The specified PerfMetricsSummary does not exist

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                      Parameters                      ||
|---------------|---------------------------------------|
| `projectId`   | `string` The cloud project            |
| `historyId`   | `string` A tool results history ID.   |
| `executionId` | `string` A tool results execution ID. |
| `stepId`      | `string` A tool results step ID.      |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of [PerfMetricsSummary](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#PerfMetricsSummary).

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).