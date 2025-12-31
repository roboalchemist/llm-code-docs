# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters.md.txt

# REST Resource: projects.histories.executions.clusters

- [Resource: ScreenshotCluster](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#ScreenshotCluster)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#ScreenshotCluster.SCHEMA_REPRESENTATION)
- [Screen](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#Screen)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#Screen.SCHEMA_REPRESENTATION)
- [Methods](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#METHODS_SUMMARY)

## Resource: ScreenshotCluster

|                                                                                                                                                                        JSON representation                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "clusterId": string, "keyScreen": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#Screen) }, "activity": string, "screens": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#Screen) } ] } ``` |

|                                                                                                                                                                                                                      Fields                                                                                                                                                                                                                       ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `clusterId` | `string` A unique identifier for the cluster. Note: This field is used in responses only. Any value specified here in a request is ignored.                                                                                                                                                                                                                                                                                          |
| `keyScreen` | `object (`[Screen](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#Screen)`)` A singular screen that represents the cluster as a whole. This screen will act as the "cover" of the entire cluster. When users look at the clusters, only the key screen from each cluster will be shown. Which screen is the key screen is determined by the ClusteringAlgorithm |
| `activity`  | `string` A string that describes the activity of every screen in the cluster.                                                                                                                                                                                                                                                                                                                                                        |
| `screens[]` | `object (`[Screen](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters#Screen)`)` Full list of screens.                                                                                                                                                                                                                                                              |

## Screen

|                                    JSON representation                                    |
|-------------------------------------------------------------------------------------------|
| ``` { "fileReference": string, "model": string, "version": string, "locale": string } ``` |

|                                             Fields                                             ||
|-----------------|-------------------------------------------------------------------------------|
| `fileReference` | `string` File reference of the png file. Required.                            |
| `model`         | `string` Model of the device that the screenshot was taken on. Required.      |
| `version`       | `string` OS version of the device that the screenshot was taken on. Required. |
| `locale`        | `string` Locale of the device that the screenshot was taken on. Required.     |

|                                                                                                               ## Methods                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| ### [get](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/get)   | Retrieves a single screenshot cluster by its ID                                                  |
| ### [list](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.clusters/list) | Lists Screenshot Clusters Returns the list of screenshot clusters corresponding to an execution. |