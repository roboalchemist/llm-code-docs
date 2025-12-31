# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ProjectSettings.md.txt

# ProjectSettings

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ProjectSettings#SCHEMA_REPRESENTATION)

Per-project settings for the Tool Results service.

|                 JSON representation                 |
|-----------------------------------------------------|
| ``` { "name": string, "defaultBucket": string } ``` |

|                                                                                      Fields                                                                                      ||
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`          | `string` The name of the project's settings. Always of the form: projects/{project-id}/settings In update request: never set In response: always set            |
| `defaultBucket` | `string` The name of the Google Cloud Storage bucket to which results are written. By default, this is unset. In update request: optional In response: optional |