# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers.md.txt

# REST Resource: projects.testers

- [Resource: Tester](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers#Tester)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers#Tester.SCHEMA_REPRESENTATION)
- [Methods](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers#METHODS_SUMMARY)

## Resource: Tester

A person that can be invited to test apps in a Firebase project.

|                                         JSON representation                                         |
|-----------------------------------------------------------------------------------------------------|
| ``` { "name": string, "displayName": string, "groups": [ string ], "lastActivityTime": string } ``` |

|                                                                                                                                                                                                                                                                           Fields                                                                                                                                                                                                                                                                            ||
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                 | `string` The name of the tester resource. Format: `projects/{projectNumber}/testers/{email_address}`                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `display``Name`        | `string` The name of the tester associated with the Google account used to accept the tester invitation.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `groups[]`             | `string` The resource names of the groups this tester belongs to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `last``Activity``Time` | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the tester was last active. This is the most recent time the tester installed one of the apps. If they've never installed one or if the release no longer exists, this is the time the tester was added to the project. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |

|                                                                         ## Methods                                                                         ||
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| ### [batchAdd](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd)       | Batch adds testers.                   |
| ### [batchRemove](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove) | Batch removes testers.                |
| ### [list](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/list)               | Lists testers and their resource ids. |
| ### [patch](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch)             | Update a tester.                      |