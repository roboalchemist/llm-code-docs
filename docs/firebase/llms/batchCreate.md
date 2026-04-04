# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate.md.txt

# Method: projects.histories.executions.steps.perfSampleSeries.samples.batchCreate

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#body.BatchCreatePerfSamplesResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate#try-it)

Creates a batch of PerfSamples - a client can submit multiple batches of Perf Samples through repeated calls to this method in order to split up a large request payload - duplicates and existing timestamp entries will be ignored. - the batch operation may partially succeed - the set of elements successfully inserted is returned in the response (omits items which already existed in the database).

May return any of the following canonical error codes: - NOT_FOUND - The containing PerfSampleSeries does not exist

### HTTP request

`POST https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples:batchCreate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                       Parameters                        ||
|------------------|---------------------------------------|
| `projectId`      | `string` The cloud project            |
| `historyId`      | `string` A tool results history ID.   |
| `executionId`    | `string` A tool results execution ID. |
| `stepId`         | `string` A tool results step ID.      |
| `sampleSeriesId` | `string` A sample series id           |

### Request body

The request body contains data with the following structure:

|                                                         JSON representation                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "perfSamples": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample) } ] } ``` |

|                                                                                                   Fields                                                                                                    ||
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `perfSamples[]` | `object (`[PerfSample](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample)`)` The set of PerfSamples to create should not include existing timestamps |

### Response body

If successful, the response body contains data with the following structure:

|                                                         JSON representation                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "perfSamples": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample) } ] } ``` |

|                                                               Fields                                                                ||
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| `perfSamples[]` | `object (`[PerfSample](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample)`)` |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).