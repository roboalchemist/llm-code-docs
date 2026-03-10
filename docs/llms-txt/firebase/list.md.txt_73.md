# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list.md.txt

# Method: projects.histories.executions.steps.perfSampleSeries.samples.list

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#body.ListPerfSamplesResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list#try-it)

Lists the Performance Samples of a given Sample Series - The list results are sorted by timestamps ascending - The default page size is 500 samples; and maximum size allowed 5000 - The response token indicates the last returned PerfSample timestamp - When the results size exceeds the page size, submit a subsequent request including the page token to return the rest of the samples up to the page limit

May return any of the following canonical error codes: - OUT_OF_RANGE - The specified request pageToken is out of valid range - NOT_FOUND - The containing PerfSampleSeries does not exist

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` The cloud project |
| `historyId` | `string` A tool results history ID. |
| `executionId` | `string` A tool results execution ID. |
| `stepId` | `string` A tool results step ID. |
| `sampleSeriesId` | `string` A sample series id |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The default page size is 500 samples, and the maximum size is 5000. If the pageSize is greater than 5000, the effective page size will be 5000 |
| `pageToken` | `string` Optional, the nextPageToken returned in the previous response |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "perfSamples": [ { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `perfSamples[]` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample`)`` |
| `nextPageToken` | `string` Optional, returned if result size exceeds the page size specified in the request (or the default page size, 500, if unspecified). It indicates the last sample timestamp to be used as pageToken in subsequent request |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).