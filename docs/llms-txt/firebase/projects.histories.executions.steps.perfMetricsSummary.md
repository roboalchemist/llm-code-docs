# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary.md.txt

# REST Resource: projects.histories.executions.steps.perfMetricsSummary

- [Resource: PerfMetricsSummary](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#PerfMetricsSummary)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#PerfMetricsSummary.SCHEMA_REPRESENTATION)
- [PerfEnvironment](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#PerfEnvironment)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#PerfEnvironment.SCHEMA_REPRESENTATION)
- [CPUInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#CPUInfo)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#CPUInfo.SCHEMA_REPRESENTATION)
- [MemoryInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#MemoryInfo)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#MemoryInfo.SCHEMA_REPRESENTATION)
- [AppStartTime](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#AppStartTime)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#AppStartTime.SCHEMA_REPRESENTATION)
- [GraphicsStats](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#GraphicsStats)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#GraphicsStats.SCHEMA_REPRESENTATION)
- [Bucket](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#Bucket)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#Bucket.SCHEMA_REPRESENTATION)
- [Methods](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#METHODS_SUMMARY)

## Resource: PerfMetricsSummary

A summary of perf metrics collected and performance environment info

|                                                                                                                                                                                                                                                                                                                                                                            JSON representation                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "projectId": string, "historyId": string, "executionId": string, "stepId": string, "perfMetrics": [ enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfMetricType) ], "perfEnvironment": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#PerfEnvironment) }, "appStartTime": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#AppStartTime) }, "graphicsStats": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#GraphicsStats) } } ``` |

|                                                                                                                                                                                   Fields                                                                                                                                                                                   ||
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `projectId`                      | `string` The cloud project Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                                                                                                                                 |
| `historyId`                      | `string` A tool results history ID. Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                                                                                                                        |
| `executionId`                    | `string` A tool results execution ID. Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                                                                                                                      |
| `stepId`                         | `string` A tool results step ID. Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                                                                                                                           |
| `perfMetrics[]`                  | `enum (`[PerfMetricType](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfMetricType)`)` Set of resource collected                                                                                                                                                                                       |
| `perfEnvironment`                | `object (`[PerfEnvironment](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#PerfEnvironment)`)` Describes the environment in which the performance metrics were collected                                                                            |
| `appStartTime`                   | `object (`[AppStartTime](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#AppStartTime)`)`                                                                                                                                                            |
| `graphicsStats` **(deprecated)** | `object (`[GraphicsStats](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#GraphicsStats)`)` | This item is deprecated! Graphics statistics for the entire run. Statistics are reset at the beginning of the run and collected at the end of the run. |

## PerfEnvironment

Encapsulates performance environment info

|                                                                                                                                                                    JSON representation                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "cpuInfo": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#CPUInfo) }, "memoryInfo": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#MemoryInfo) } } ``` |

|                                                                                                         Fields                                                                                                          ||
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cpuInfo`    | `object (`[CPUInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#CPUInfo)`)` CPU related environment info          |
| `memoryInfo` | `object (`[MemoryInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#MemoryInfo)`)` Memory related environment info |

## CPUInfo

|                                  JSON representation                                  |
|---------------------------------------------------------------------------------------|
| ``` { "cpuProcessor": string, "cpuSpeedInGhz": number, "numberOfCores": integer } ``` |

|                                               Fields                                                ||
|-----------------|------------------------------------------------------------------------------------|
| `cpuProcessor`  | `string` description of the device processor ie '1.8 GHz hexa core 64-bit ARMv8-A' |
| `cpuSpeedInGhz` | `number` the CPU clock speed in GHz                                                |
| `numberOfCores` | `integer` the number of CPU cores                                                  |

## MemoryInfo

|                            JSON representation                             |
|----------------------------------------------------------------------------|
| ``` { "memoryTotalInKibibyte": string, "memoryCapInKibibyte": string } ``` |

|                                                                                 Fields                                                                                  ||
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `memoryTotalInKibibyte` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total memory available on the device in KiB                |
| `memoryCapInKibibyte`   | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Maximum memory that can be allocated to the process in KiB |

## AppStartTime

|                                                                                                                    JSON representation                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "initialDisplayTime": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration) }, "fullyDrawnTime": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration) } } ``` |

|                                                                                                                                                                                            Fields                                                                                                                                                                                             ||
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `initialDisplayTime` | `object (`[Duration](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration)`)` The time from app start to the first displayed activity being drawn, as reported in Logcat. See <https://developer.android.com/topic/performance/launch-time.html#time-initial>                                                                          |
| `fullyDrawnTime`     | `object (`[Duration](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration)`)` Optional. The time from app start to reaching the developer-reported "fully drawn" time. This is only stored if the app includes a call to Activity.reportFullyDrawn(). See <https://developer.android.com/topic/performance/launch-time.html#time-full> |

## GraphicsStats

Graphics statistics for the App. The information is collected from 'adb shell dumpsys graphicsstats'. For more info see: <https://developer.android.com/training/testing/performance.html> Statistics will only be present for API 23+.

|                                                                                                                                                                                                                           JSON representation                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "totalFrames": string, "jankyFrames": string, "p50Millis": string, "p90Millis": string, "p95Millis": string, "p99Millis": string, "missedVsyncCount": string, "highInputLatencyCount": string, "slowUiThreadCount": string, "slowBitmapUploadCount": string, "slowDrawCount": string, "buckets": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#Bucket) } ] } ``` |

|                                                                                                                                                 Fields                                                                                                                                                  ||
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `totalFrames`           | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total frames rendered by package.                                                                                                                                                          |
| `jankyFrames`           | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total frames with slow render time. Should be \<= totalFrames.                                                                                                                             |
| `p50Millis`             | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` 50th percentile frame render time in milliseconds.                                                                                                                                         |
| `p90Millis`             | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` 90th percentile frame render time in milliseconds.                                                                                                                                         |
| `p95Millis`             | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` 95th percentile frame render time in milliseconds.                                                                                                                                         |
| `p99Millis`             | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` 99th percentile frame render time in milliseconds.                                                                                                                                         |
| `missedVsyncCount`      | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total "missed vsync" events.                                                                                                                                                               |
| `highInputLatencyCount` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total "high input latency" events.                                                                                                                                                         |
| `slowUiThreadCount`     | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total "slow UI thread" events.                                                                                                                                                             |
| `slowBitmapUploadCount` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total "slow bitmap upload" events.                                                                                                                                                         |
| `slowDrawCount`         | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Total "slow draw" events.                                                                                                                                                                  |
| `buckets[]`             | `object (`[Bucket](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary#Bucket)`)` Histogram of frame render times. There should be 154 buckets ranging from \[5ms, 6ms) to \[4950ms, infinity) |

## Bucket

|                   JSON representation                    |
|----------------------------------------------------------|
| ``` { "renderMillis": string, "frameCount": string } ``` |

|                                                                     Fields                                                                      ||
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| `renderMillis` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Lower bound of render time in milliseconds. |
| `frameCount`   | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Number of frames in the bucket.             |

|                                                                                            ## Methods                                                                                            ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| ### [create](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.perfMetricsSummary/create) | Creates a PerfMetricsSummary resource. |