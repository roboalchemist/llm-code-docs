# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/removeAnalytics.md.txt

# Method: projects.removeAnalytics

Unlinks the specified [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject) from its Google Analytics account.

This call removes the association of the specified `FirebaseProject` with its current Google Analytics property. However, this call does not delete the Google Analytics resources, such as the Google Analytics property or any data streams.

These resources may be re-associated later to the `FirebaseProject` by calling [`projects.addGoogleAnalytics`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addGoogleAnalytics) and specifying the same `analyticsPropertyId`. For Android Apps and iOS Apps, this call re-links data streams with their corresponding apps. However, for Web Apps, this call provisions a *new* data stream for each Web App.

To call `projects.removeAnalytics`, a project member must be an Owner for the `FirebaseProject`.

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{parent=projects/*}:removeAnalytics`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                                           Parameters                                                                                                                                                                                                                                                           ||
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parent` | `string` The resource name of the [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject) to unlink from its Google Analytics account, in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var> Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |

### Request body

The request body contains data with the following structure:

|            JSON representation            |
|-------------------------------------------|
| ``` { "analyticsPropertyId": string } ``` |

|                                                                                                                                                                                                                          Fields                                                                                                                                                                                                                          ||
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `analytics``Property``Id` | `string` Optional. The ID of the Google Analytics property associated with the specified `FirebaseProject`. - If not set, then the Google Analytics property that is currently associated with the specified `FirebaseProject` is removed. - If set, and the specified `FirebaseProject` is currently associated with a *different* Google Analytics property, then the response is a `412 Precondition Failed` error. <br /> |

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).