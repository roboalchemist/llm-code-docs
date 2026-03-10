# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.md.txt

# REST Resource: projects

## Resource: FirebaseProject

A `FirebaseProject` is the top-level Firebase entity. It is the container for Firebase Apps, Firebase Hosting sites, storage systems (Firebase Realtime Database, Cloud Firestore, Cloud Storage buckets), and other Firebase and Google Cloud resources.

You create a `FirebaseProject` by calling `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase#google.firebase.service.v1beta1.FirebaseProjectService.AddFirebase` and specifying an *existing* [Google Cloud `Project`](https://cloud.google.com/resource-manager/reference/rest/v1/projects). This adds Firebase resources to the existing Google Cloud `Project`.

Since a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` is actually also a Google Cloud `Project`, a `FirebaseProject` has the same underlying Google Cloud identifiers (`projectNumber` and `projectId`). This allows for easy interop with Google APIs.

| JSON representation |
|---|
| ``` { "name": string, "projectId": string, "projectNumber": string, "displayName": string, "state": enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#State`), "annotations": { string: string, ... }, "etag": string } ``` |

| Fields ||
|---|---|
| `name` | `string` The resource name of the Project, in the format: `projects/PROJECT_IDENTIFIER` <var translate="no">PROJECT_IDENTIFIER</var>: the Project's [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for <var translate="no">PROJECT_IDENTIFIER</var> in any response body will be the `ProjectId`. |
| `projectId` | `string` Output only. Immutable. A user-assigned unique identifier for the Project. This identifier may appear in URLs or names for some Firebase resources associated with the Project, but it should generally be treated as a convenience alias to reference the Project. |
| `projectNumber` | `string (https://developers.google.com/discovery/v1/type-format format)` Output only. Immutable. The globally unique, Google-assigned canonical identifier for the Project. Use this identifier when configuring integrations and/or making API calls to Firebase or third-party services. |
| `displayName` | `string` The user-assigned display name of the Project. |
| `state` | ``enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#State`)`` Output only. The lifecycle state of the Project. |
| `annotations` | `map (key: string, value: string)` A set of user-defined annotations for the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. Learn more about annotations in Google's [AIP-128 standard](https://google.aip.dev/128#annotations). These annotations are intended solely for developers and client-side tools. Firebase services will not mutate this annotations set. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| `etag` | `string` This checksum is computed by the server based on the value of other fields, and it may be sent with update requests to ensure the client has an up-to-date value before proceeding. Learn more about `etag` in Google's [AIP-154 standard](https://google.aip.dev/154#declarative-friendly-resources). This etag is strongly validated. |

## State

The possible lifecycle states of the Project. Learn more about states in Google's [AIP-216 standard](https://google.aip.dev/216).

| Enums ||
|---|---|
| `STATE_UNSPECIFIED` | Unspecified state. |
| `ACTIVE` | The Project is active. |
| `DELETED` | The Project has been soft-deleted. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase` | Adds Firebase resources and enables Firebase services in the specified existing [Google Cloud `Project`](https://cloud.google.com/resource-manager/reference/rest/v1/projects). |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addGoogleAnalytics` | Links the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` with an existing [Google Analytics account](http://www.google.com/analytics/). |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/get` | Gets the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAdminSdkConfig` | Gets the configuration artifact associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`, which can be used by servers to simplify initialization. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails` | Gets the Google Analytics details currently associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/list` | Lists each `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` accessible to the caller. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/patch` | Updates the attributes of the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/removeAnalytics` | Unlinks the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` from its Google Analytics account. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/searchApps` | Lists all available Apps for the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |