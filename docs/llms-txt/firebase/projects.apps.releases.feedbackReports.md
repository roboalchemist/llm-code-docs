# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports.md.txt

# REST Resource: projects.apps.releases.feedbackReports

- [Resource: FeedbackReport](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports#FeedbackReport)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports#FeedbackReport.SCHEMA_REPRESENTATION)
- [Methods](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports#METHODS_SUMMARY)

## Resource: FeedbackReport

A feedback report submitted by a tester for a release.

|                                                            JSON representation                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "tester": string, "text": string, "screenshotUri": string, "firebaseConsoleUri": string, "createTime": string } ``` |

|                                                                                                                                                                                   Fields                                                                                                                                                                                    ||
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                   | `string` The name of the feedback report resource. Format: `projects/{projectNumber}/apps/{app}/releases/{release}/feedbackReports/{feedback_report}`                                                                                                                                                                                             |
| `tester`                 | `string` Output only. The resource name of the tester who submitted the feedback report.                                                                                                                                                                                                                                                          |
| `text`                   | `string` Output only. The text of the feedback report.                                                                                                                                                                                                                                                                                            |
| `screenshot``Uri`        | `string` Output only. A signed link (which expires in one hour) that lets you directly download the screenshot.                                                                                                                                                                                                                                   |
| `firebase``Console``Uri` | `string` Output only. A link to the Firebase console displaying the feedback report.                                                                                                                                                                                                                                                              |
| `create``Time`           | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the feedback report was created. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |

|                                                                         ## Methods                                                                          ||
|---------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| ### [delete](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/delete) | Deletes a feedback report. |
| ### [get](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get)       | Gets a feedback report.    |
| ### [list](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list)     | Lists feedback reports.    |