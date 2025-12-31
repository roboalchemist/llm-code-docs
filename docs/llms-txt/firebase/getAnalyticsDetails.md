# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails.md.txt

# Method: projects.getAnalyticsDetails

Gets the Google Analytics details currently associated with the specified [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject).

If the `FirebaseProject` is not yet linked to Google Analytics, then the response to `projects.getAnalyticsDetails` is `NOT_FOUND`.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/{name=projects/*/analyticsDetails}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                             Parameters                                                                                                                                                                                                                                              ||
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` The resource name of the [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject), in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/analyticsDetails` Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

|                                                                                                                                                         JSON representation                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "analyticsProperty": { object (https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails#AnalyticsProperty) }, "streamMappings": [ { object (https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails#StreamMapping) } ] } ``` |

|                                                                                                                                                                                                                                                                      Fields                                                                                                                                                                                                                                                                      ||
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `analytics``Property` | `object (`[AnalyticsProperty](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails#AnalyticsProperty)`)` The Analytics Property object associated with the specified `FirebaseProject`. This object contains the details of the Google Analytics property associated with the Project.                                                                                                                                                                                |
| `stream``Mappings[]`  | `object (`[StreamMapping](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails#StreamMapping)`)` - For `AndroidApps` and `IosApps`: a map of `app` to `streamId` for each Firebase App in the specified `FirebaseProject`. Each `app` and `streamId` appears only once. - For `WebApps`: a map of `app` to `streamId` and `measurementId` for each `WebApp` in the specified `FirebaseProject`. Each `app`, `streamId`, and `measurementId` appears only once. <br /> |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/cloud-platform.read-only`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## AnalyticsProperty

Details of a Google Analytics property

|                              JSON representation                              |
|-------------------------------------------------------------------------------|
| ``` { "id": string, "displayName": string, "analyticsAccountId": string } ``` |

|                                                                                                                                                                                                                                                                     Fields                                                                                                                                                                                                                                                                     ||
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                     | `string` The globally unique, Google-assigned identifier of the Google Analytics property associated with the specified `FirebaseProject`. If you called [`projects.addGoogleAnalytics`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addGoogleAnalytics) to link the `FirebaseProject` with a Google Analytics account, the value in this `id` field is the same as the ID of the property either specified or provisioned with that call to `projects.addGoogleAnalytics`. |
| `display``Name`          | `string` The display name of the Google Analytics property associated with the specified `FirebaseProject`.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `analytics``Account``Id` | `string` Output only. The ID of the [Google Analytics account](https://www.google.com/analytics/) for the Google Analytics property associated with the specified [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject).                                                                                                                                                                                                                           |

## StreamMapping

A mapping of a Firebase App to a Google Analytics data stream

|                          JSON representation                           |
|------------------------------------------------------------------------|
| ``` { "app": string, "streamId": string, "measurementId": string } ``` |

|                                                                                                                                                                                                                                                                                                                                            Fields                                                                                                                                                                                                                                                                                                                                            ||
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app`             | `string` The resource name of the Firebase App associated with the Google Analytics data stream, in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/androidApps/`<var translate="no">APP_ID</var> or `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/iosApps/`<var translate="no">APP_ID</var> or `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/webApps/`<var translate="no">APP_ID</var> Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |
| `stream``Id`      | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` The unique Google-assigned identifier of the Google Analytics data stream associated with the Firebase App. Learn more about Google Analytics data streams in the [Analytics documentation](https://support.google.com/analytics/answer/9303323).                                                                                                                                                                                                                                                                                                                                     |
| `measurement``Id` | `string` Applicable for Firebase Web Apps only. The unique Google-assigned identifier of the Google Analytics web stream associated with the Firebase Web App. Firebase SDKs use this ID to interact with Google Analytics APIs. Learn more about this ID and Google Analytics web streams in the [Analytics documentation](https://support.google.com/analytics/answer/9304153).                                                                                                                                                                                                                                                                                         |