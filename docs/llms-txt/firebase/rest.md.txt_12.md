# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest.md.txt

# Cloud Tool Results API

API to publish and access results from developer tools.

- [REST Resource: v1beta3.projects](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects)
- [REST Resource: v1beta3.projects.histories](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories)
- [REST Resource: v1beta3.projects.histories.executions](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions)
- [REST Resource: v1beta3.projects.histories.executions.clusters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.clusters)
- [REST Resource: v1beta3.projects.histories.executions.environments](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.environments)
- [REST Resource: v1beta3.projects.histories.executions.steps](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.steps)
- [REST Resource:
  v1beta3.projects.histories.executions.steps.perfMetricsSummary](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.steps.perfMetricsSummary)
- [REST Resource: v1beta3.projects.histories.executions.steps.perfSampleSeries](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.steps.perfSampleSeries)
- [REST Resource:
  v1beta3.projects.histories.executions.steps.perfSampleSeries.samples](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.steps.perfSampleSeries.samples)
- [REST Resource: v1beta3.projects.histories.executions.steps.testCases](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.steps.testCases)
- [REST Resource: v1beta3.projects.histories.executions.steps.thumbnails](https://firebase.google.com/docs/test-lab/reference/toolresults/rest#v1beta3.projects.histories.executions.steps.thumbnails)

## Service: toolresults.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://toolresults.googleapis.com/$discovery/rest?version=v1beta3>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://toolresults.googleapis.com`

## REST Resource: [v1beta3.projects](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/getSettings` | `GET /toolresults/v1beta3/projects/{projectId}/settings` Gets the Tool Results settings for a project. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects/initializeSettings` | `POST /toolresults/v1beta3/projects/{projectId}:initializeSettings` Creates resources for settings which have not yet been set. |

## REST Resource: [v1beta3.projects.histories](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/create` | `POST /toolresults/v1beta3/projects/{projectId}/histories` Creates a History. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/get` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}` Gets a History. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories` Lists Histories for a given Project. |

## REST Resource: [v1beta3.projects.histories.executions](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/create` | `POST /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions` Creates an Execution. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/get` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}` Gets an Execution. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions` Lists Executions for a given History. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/patch` | `PATCH /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}` Updates an existing Execution with the supplied partial entity. |

## REST Resource: [v1beta3.projects.histories.executions.clusters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/get` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters/{clusterId}` Retrieves a single screenshot cluster by its ID |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters` Lists Screenshot Clusters Returns the list of screenshot clusters corresponding to an execution. |

## REST Resource: [v1beta3.projects.histories.executions.environments](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/get` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments/{environmentId}` Gets an Environment. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.environments/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments` Lists Environments for a given Execution. |

## REST Resource: [v1beta3.projects.histories.executions.steps](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters` | `GET /toolresults/v1beta3/{name=projects/*/histories/*/executions/*/steps/*}:accessibilityClusters` Lists accessibility clusters for a given Step May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - FAILED_PRECONDITION - if an argument in the request happens to be invalid; e.g. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/create` | `POST /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps` Creates a Step. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/get` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}` Gets a Step. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/getPerfMetricsSummary` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary` Retrieves a PerfMetricsSummary. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps` Lists Steps for a given Execution. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/patch` | `PATCH /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}` Updates an existing Step with the supplied partial entity. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles` | `POST /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles` Publish xml files to an existing Step. |

## REST Resource: [v1beta3.projects.histories.executions.steps.perfMetricsSummary](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary/create` | `POST /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary` Creates a PerfMetricsSummary resource. |

## REST Resource: [v1beta3.projects.histories.executions.steps.perfSampleSeries](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries/create` | `POST /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries` Creates a PerfSampleSeries. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries/get` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}` Gets a PerfSampleSeries. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries` Lists PerfSampleSeries for a given Step. |

## REST Resource: [v1beta3.projects.histories.executions.steps.perfSampleSeries.samples](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/batchCreate` | `POST /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples:batchCreate` Creates a batch of PerfSamples - a client can submit multiple batches of Perf Samples through repeated calls to this method in order to split up a large request payload - duplicates and existing timestamp entries will be ignored. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.samples/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples` Lists the Performance Samples of a given Sample Series - The list results are sorted by timestamps ascending - The default page size is 500 samples; and maximum size allowed 5000 - The response token indicates the last returned PerfSample timestamp - When the results size exceeds the page size, submit a subsequent request including the page token to return the rest of the samples up to the page limit May return any of the following canonical error codes: - OUT_OF_RANGE - The specified request page_token is out of valid range - NOT_FOUND - The containing PerfSampleSeries does not exist |

## REST Resource: [v1beta3.projects.histories.executions.steps.testCases](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/get` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases/{testCaseId}` Gets details of a Test Case for a Step. |
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.testCases/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases` Lists Test Cases attached to a Step. |

## REST Resource: [v1beta3.projects.histories.executions.steps.thumbnails](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list` | `GET /toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/thumbnails` Lists thumbnails of images attached to a step. |