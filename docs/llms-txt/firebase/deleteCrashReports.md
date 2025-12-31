# Source: https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports.md.txt

# Method: projects.apps.users.deleteCrashReports

- [HTTP request](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#body.DeleteUserCrashReportsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#try-it)

Enqueues a request to permanently remove crash reports associated with the specified user. All reports belonging to the specified user will be deleted typically within 24 hours of receiving the crash report.

### HTTP request

`DELETE https://firebasecrashlytics.googleapis.com/v1alpha/{name=projects/*/apps/*/users/*/crashReports}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                                                                                                                                                                                                                                           Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. Resource name for user reports, in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/apps/`<var translate="no">APP_ID</var>`/users/`<var translate="no">USER_ID</var>`/crashReports` - <var translate="no">PROJECT_IDENTIFIER</var>: The Firebase project's project number (recommended) or its project ID. Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). - <var translate="no">APP_ID</var>: The globally unique, Firebase-assigned identifier for the Firebase App. This is not your package name or bundle ID. Learn how to [find your app ID](https://firebase.google.com/support/faq/#find-app-id). - <var translate="no">USER_ID</var>: The user ID set using the Crashlytics SDK. Learn how to [set user identifiers](https://firebase.google.com/docs/crashlytics/customize-crash-reports#set-user-ids). |

### Request body

The request body must be empty.

### Response body

Response message for the [users.deleteCrashReports](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports#google.firebase.crashlytics.v1alpha.FirebaseCrashlytics.DeleteUserCrashReports) method. All crash reports associated with the specified user will be deleted typically within 24 hours of receiving the crash report.

If successful, the response body contains data with the following structure:

|           JSON representation            |
|------------------------------------------|
| ``` { "targetCompleteTime": string } ``` |

|                                                                                                                                                                                   Fields                                                                                                                                                                                    ||
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `target``Complete``Time` | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Target time to complete the delete crash reports operation. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).