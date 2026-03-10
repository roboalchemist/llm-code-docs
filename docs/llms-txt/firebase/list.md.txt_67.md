# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/list.md.txt

# Method: projects.androidApps.sha.list

Lists the SHA-1 and SHA-256 certificates for the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/{parent=projects/*/androidApps/*}/sha`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` The resource name of the parent `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp` for which to list each associated `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate`, in the format: `projects/PROJECT_IDENTIFIER/androidApps/APP_ID` <br /> Since an <var translate="no">APP_ID</var> is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: `projects/-/androidApps/APP_ID` <br /> Refer to the `AndroidApp` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> and <var translate="no">APP_ID</var> values. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "certificates": [ { object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate`) } ] } ``` |

| Fields ||
|---|---|
| `certificates[]` | ``object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate`)`` The list of each `ShaCertificate` associated with the `AndroidApp`. |

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