# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/remove.md.txt

# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/remove.md.txt

# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/remove.md.txt

# Method: projects.androidApps.remove

Removes the specified [AndroidApp](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp) from the [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject).

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{name=projects/*/androidApps/*}:remove`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                                                                                                                                                                                    Parameters                                                                                                                                                                                                                                                                                                                                                                                                    ||
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. The resource name of the [AndroidApp](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp), in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/androidApps/`<var translate="no">APP_ID</var> <br /> Since an <var translate="no">APP_ID</var> is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: `projects/-/androidApps/`<var translate="no">APP_ID</var> <br /> Refer to the AndroidApp [name](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> and <var translate="no">APP_ID</var> values. |

### Request body

The request body contains data with the following structure:

|                                        JSON representation                                         |
|----------------------------------------------------------------------------------------------------|
| ``` { "allowMissing": boolean, "validateOnly": boolean, "etag": string, "immediate": boolean } ``` |

|                                                                                                                                                                                                                                                                                                                                             Fields                                                                                                                                                                                                                                                                                                                                              ||
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `allow``Missing` | `boolean` If set to true, and the App is not found, the request will succeed but no action will be taken on the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `validate``Only` | `boolean` If set to true, the request is only validated. The App will *not* be removed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `etag`           | `string` Checksum provided in the [AndroidApp](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp) resource. If provided, this checksum ensures that the client has an up-to-date value before proceeding.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `immediate`      | `boolean` Determines whether to *immediately* delete the [AndroidApp](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp). If set to true, the App is immediately deleted from the Project and cannot be undeleted (that is, restored to the Project). If not set, defaults to false, which means the App will be set to expire in 30 days. Within the 30 days, the App may be restored to the Project using [androidApps.undelete](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/undelete#google.firebase.service.v1beta1.AndroidAppService.UndeleteAndroidApp). |

### Response body

If successful, the response body contains an instance of [Operation](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).