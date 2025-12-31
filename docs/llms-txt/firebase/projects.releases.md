# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases.md.txt

# REST Resource: projects.releases

- [Resource: Release](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release.SCHEMA_REPRESENTATION)
- [Methods](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#METHODS_SUMMARY)

## Resource: Release

`Release` is a named reference to a `Ruleset`. Once a `Release` refers to a `Ruleset`, rules-enabled services will be able to enforce the `Ruleset`.

|                                       JSON representation                                        ||
|-----------------------------------------------------------------------------------------------|---|
| ``` { "name": string, "rulesetName": string, "createTime": string, "updateTime": string } ``` |

|                                                                                                                                                                                        Fields                                                                                                                                                                                        ||
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | `string` Format: `projects/{project_id}/releases/{release_id}`                                                                                                                                                                                                                                                                                                        |
| `rulesetName` | `string` Name of the `Ruleset` referred to by this `Release`. The `Ruleset` must exist for the `Release` to be created.                                                                                                                                                                                                                                               |
| `createTime`  | `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Time the release was created. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |
| `updateTime`  | `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Time the release was updated. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |

|                                                                                ## Methods                                                                                ||
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| ### [create](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create)               | Create a `Release`.                                       |
| ### [delete](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/delete)               | Delete a `Release` by resource name.                      |
| ### [get](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get)                     | Get a `Release` by name.                                  |
| ### [getExecutable](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable) | Get the `Release` executable to use when enforcing rules. |
| ### [list](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list)                   | List the `Release` values for a project.                  |
| ### [patch](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch)                 | Update a `Release` via PATCH.                             |