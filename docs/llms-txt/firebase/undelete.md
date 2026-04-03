# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/undelete.md.txt

# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/undelete.md.txt

# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/undelete.md.txt

# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/undelete.md.txt

# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/undelete.md.txt

# Method: projects.androidApps.undelete

Restores the specified [AndroidApp](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp) to the [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject).

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{name=projects/*/androidApps/*}:undelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                                                                                                                                                                                    Parameters                                                                                                                                                                                                                                                                                                                                                                                                    ||
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. The resource name of the [AndroidApp](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp), in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/androidApps/`<var translate="no">APP_ID</var> <br /> Since an <var translate="no">APP_ID</var> is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: `projects/-/androidApps/`<var translate="no">APP_ID</var> <br /> Refer to the AndroidApp [name](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> and <var translate="no">APP_ID</var> values. |

### Request body

The request body contains data with the following structure:

|                 JSON representation                 |
|-----------------------------------------------------|
| ``` { "validateOnly": boolean, "etag": string } ``` |

|                                                                                                                                        Fields                                                                                                                                         ||
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `validate``Only` | `boolean` If set to true, the request is only validated. The App will *not* be undeleted.                                                                                                                                                                           |
| `etag`           | `string` Checksum provided in the [AndroidApp](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp) resource. If provided, this checksum ensures that the client has an up-to-date value before proceeding. |

### Response body

If successful, the response body contains an instance of [Operation](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).