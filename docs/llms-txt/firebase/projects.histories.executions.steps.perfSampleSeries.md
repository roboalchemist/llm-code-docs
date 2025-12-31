# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries.md.txt

# REST Resource: projects.histories.executions.steps.perfSampleSeries

- [Resource: PerfSampleSeries](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#PerfSampleSeries)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#PerfSampleSeries.SCHEMA_REPRESENTATION)
- [BasicPerfSampleSeries](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#BasicPerfSampleSeries)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#BasicPerfSampleSeries.SCHEMA_REPRESENTATION)
- [PerfUnit](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#PerfUnit)
- [SampleSeriesLabel](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#SampleSeriesLabel)
- [Methods](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#METHODS_SUMMARY)

## Resource: PerfSampleSeries

Resource representing a collection of performance samples (or data points)

|                                                                                                                                                                                                                         JSON representation                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "projectId": string, "historyId": string, "executionId": string, "stepId": string, "sampleSeriesId": string, // Union field `perf_sample_series` can be only one of the following: "basicPerfSampleSeries": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#BasicPerfSampleSeries) } // End of list of possible types for union field `perf_sample_series`. } ``` |

|                                                                                                                             Fields                                                                                                                              ||
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `projectId`             | `string` The cloud project Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                               |
| `historyId`             | `string` A tool results history ID. Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                      |
| `executionId`           | `string` A tool results execution ID. Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                    |
| `stepId`                | `string` A tool results step ID. Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                         |
| `sampleSeriesId`        | `string` A sample series id Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                              |
| Union field `perf_sample_series`. `perf_sample_series` can be only one of the following:                                                                                                                                                                        ||
| `basicPerfSampleSeries` | `object (`[BasicPerfSampleSeries](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#BasicPerfSampleSeries)`)` Basic series represented by a line chart |

## BasicPerfSampleSeries

Encapsulates the metadata for basic sample series represented by a line chart

|                                                                                                                                                                                                                               JSON representation                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "perfMetricType": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfMetricType), "perfUnit": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#PerfUnit), "sampleSeriesLabel": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#SampleSeriesLabel) } ``` |

|                                                                                                  Fields                                                                                                  ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `perfMetricType`    | `enum (`[PerfMetricType](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfMetricType)`)`                                                            |
| `perfUnit`          | `enum (`[PerfUnit](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#PerfUnit)`)`                   |
| `sampleSeriesLabel` | `enum (`[SampleSeriesLabel](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries#SampleSeriesLabel)`)` |

## PerfUnit

The unit corresponding to the series of data points in this collection

|          Enums           ||
|-----------------------|---|
| `perfUnitUnspecified` |   |
| `kibibyte`            |   |
| `percent`             |   |
| `bytesPerSecond`      |   |
| `framesPerSecond`     |   |
| `byte`                |   |

## SampleSeriesLabel

Label to identify a given performance sample series

|                         Enums                         ||
|-------------------------------|------------------------|
| `sampleSeriesTypeUnspecified` |                        |
| `memoryRssPrivate`            | Memory sample series   |
| `memoryRssShared`             |                        |
| `memoryRssTotal`              |                        |
| `memoryTotal`                 |                        |
| `cpuUser`                     | CPU sample series      |
| `cpuKernel`                   |                        |
| `cpuTotal`                    |                        |
| `ntBytesTransferred`          | Network sample series  |
| `ntBytesReceived`             |                        |
| `networkSent`                 |                        |
| `networkReceived`             |                        |
| `graphicsFrameRate`           | Graphics sample series |

|                                                                                            ## Methods                                                                                            ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| ### [create](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries/create) | Creates a PerfSampleSeries.              |
| ### [get](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries/get)       | Gets a PerfSampleSeries.                 |
| ### [list](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfSampleSeries/list)     | Lists PerfSampleSeries for a given Step. |