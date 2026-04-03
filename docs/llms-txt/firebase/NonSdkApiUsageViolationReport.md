# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApiUsageViolationReport.md.txt

# NonSdkApiUsageViolationReport

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApiUsageViolationReport#SCHEMA_REPRESENTATION)

Contains a summary and examples of non-sdk API usage violations.

|                                                                                               JSON representation                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "uniqueApis": integer, "minSdkVersion": integer, "targetSdkVersion": integer, "exampleApis": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi) } ] } ``` |

|                                                                                  Fields                                                                                   ||
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniqueApis`       | `integer` Total number of unique Non-SDK API's accessed.                                                                                              |
| `minSdkVersion`    | `integer` Minimum API level required for the application to run.                                                                                      |
| `targetSdkVersion` | `integer` Specifies the API Level on which the application is designed to run.                                                                        |
| `exampleApis[]`    | `object (`[NonSdkApi](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi)`)` Examples of the detected API usages. |