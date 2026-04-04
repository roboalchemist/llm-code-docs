# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addGoogleAnalytics.md.txt

# Method: projects.addGoogleAnalytics

Links the specified [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject) with an existing [Google Analytics account](http://www.google.com/analytics/).

Using this call, you can either:

- Specify an `analyticsAccountId` to provision a new Google Analytics property within the specified account and associate the new property with the `FirebaseProject`.
- Specify an existing `analyticsPropertyId` to associate the property with the `FirebaseProject`.

<br />

Note that when you call `projects.addGoogleAnalytics`:

1. The first check determines if any existing data streams in the Google Analytics property correspond to any existing Firebase Apps in the `FirebaseProject` (based on the `packageName` or `bundleId` associated with the data stream). Then, as applicable, the data streams and apps are linked. Note that this auto-linking only applies to `AndroidApps` and `IosApps`.
2. If no corresponding data streams are found for the Firebase Apps, new data streams are provisioned in the Google Analytics property for each of the Firebase Apps. Note that a new data stream is always provisioned for a Web App even if it was previously associated with a data stream in the Analytics property.

<br />

Learn more about the hierarchy and structure of Google Analytics accounts in the [Analytics documentation](https://support.google.com/analytics/answer/9303323).

The result of this call is an [`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations). Poll the `Operation` to track the provisioning process by calling `operations.get` until [`done`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.done) is `true`. When `done` is `true`, the `Operation` has either succeeded or failed. If the `Operation` succeeded, its [`response`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.response) is set to an [AnalyticsDetails](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails#body.AnalyticsDetails); if the `Operation` failed, its [`error`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.error) is set to a [google.rpc.Status](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Status).

To call `projects.addGoogleAnalytics`, a project member must be an Owner for the existing `FirebaseProject` and have the [`Edit` permission](https://support.google.com/analytics/answer/2884495) for the Google Analytics account.

If the `FirebaseProject` already has Google Analytics enabled, and you call `projects.addGoogleAnalytics` using an `analyticsPropertyId` that's different from the currently associated property, then the call will fail. Analytics may have already been enabled in the Firebase console or by specifying `timeZone` and `regionCode` in the call to [`projects.addFirebase`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase).

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{parent=projects/*}:addGoogleAnalytics`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                                             Parameters                                                                                                                                                                                                                                                             ||
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parent` | `string` The resource name of the [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject) to link to an existing Google Analytics account, in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var> Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |

### Request body

The request body contains data with the following structure:

|                                                                                                 JSON representation                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { // Union field `analytics_resource` can be only one of the following: "analyticsAccountId": string, "analyticsPropertyId": string // End of list of possible types for union field `analytics_resource`. } ``` |

|                                                                                                                                                                   Fields                                                                                                                                                                    ||
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Union field `analytics_resource`. Only one Google Analytics resource can be specified in the request body. - To provision a new Google Analytics property and associate it with the `FirebaseProject`, provide `analyticsAccountId`. - To associate an existing Google Analytics property with the `FirebaseProject`, provide `analyticsPropertyId`. <br /> <br /> `analytics_resource` can be only one of the following: ||
| `analytics``Account``Id`  | `string` The ID for the existing [Google Analytics account](http://www.google.com/analytics/) that you want to link with the `FirebaseProject`. Specifying this field will provision a new Google Analytics property in your Google Analytics account and associate the new property with the `FirebaseProject`. |
| `analytics``Property``Id` | `string` The ID for the existing Google Analytics property that you want to associate with the `FirebaseProject`.                                                                                                                                                                                                |

### Response body

If successful, the response body contains an instance of [Operation](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).