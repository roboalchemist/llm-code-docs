# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.md.txt

# REST Resource: projects.apps.releases

- [Resource: Release](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release.SCHEMA_REPRESENTATION)
- [ReleaseNotes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#ReleaseNotes)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#ReleaseNotes.SCHEMA_REPRESENTATION)
- [Methods](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#METHODS_SUMMARY)

## Resource: Release

A release of a Firebase app.

|                                                                                                                                                    JSON representation                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "releaseNotes": { object (https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#ReleaseNotes) }, "displayVersion": string, "buildVersion": string, "createTime": string, "firebaseConsoleUri": string, "testingUri": string, "binaryDownloadUri": string } ``` |

|                                                                                                                                                                             Fields                                                                                                                                                                             ||
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                   | `string` The name of the release resource. Format: `projects/{projectNumber}/apps/{appId}/releases/{releaseId}`                                                                                                                                                                                                                      |
| `release``Notes`         | `object (`[ReleaseNotes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#ReleaseNotes)`)` Notes of the release.                                                                                                                                                                           |
| `display``Version`       | `string` Output only. Display version of the release. For an Android release, the display version is the `versionName`. For an iOS release, the display version is the `CFBundleShortVersionString`.                                                                                                                                 |
| `build``Version`         | `string` Output only. Build version of the release. For an Android release, the build version is the `versionCode`. For an iOS release, the build version is the `CFBundleVersion`.                                                                                                                                                  |
| `create``Time`           | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the release was created. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |
| `firebase``Console``Uri` | `string` Output only. A link to the Firebase console displaying a single release.                                                                                                                                                                                                                                                    |
| `testing``Uri`           | `string` Output only. A link to the release in the tester web clip or Android app that lets testers (which were granted access to the app) view release notes and install the app onto their devices.                                                                                                                                |
| `binary``Download``Uri`  | `string` Output only. A signed link (which expires in one hour) to directly download the app binary (IPA/APK/AAB) file.                                                                                                                                                                                                              |

## ReleaseNotes

Notes that belong to a release.

|    JSON representation     |
|----------------------------|
| ``` { "text": string } ``` |

|                     Fields                      ||
|--------|-----------------------------------------|
| `text` | `string` The text of the release notes. |

|                                                                          ## Methods                                                                          ||
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| ### [batchDelete](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete) | Deletes releases.                 |
| ### [distribute](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute)   | Distributes a release to testers. |
| ### [get](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/get)                 | Gets a release.                   |
| ### [list](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list)               | Lists releases.                   |
| ### [patch](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch)             | Updates a release.                |