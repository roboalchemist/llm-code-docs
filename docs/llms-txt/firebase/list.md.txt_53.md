# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list.md.txt

# Method: projects.histories.executions.clusters.list

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list#body.ListScreenshotClustersResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list#try-it)

Lists Screenshot Clusters

Returns the list of screenshot clusters corresponding to an execution. Screenshot clusters are created after the execution is finished. Clusters are created from a set of screenshots. Between any two screenshots, a matching score is calculated based off their metadata that determines how similar they are. Screenshots are placed in the cluster that has screens which have the highest matching scores.

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` A Project id. Required. |
| `historyId` | `string` A History id. Required. |
| `executionId` | `string` An Execution id. Required. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "clusters": [ { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#ScreenshotCluster`) } ] } ``` |

| Fields ||
|---|---|
| `clusters[]` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#ScreenshotCluster`)`` The set of clusters associated with an execution Always set |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).