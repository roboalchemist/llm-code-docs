# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/undelete.md.txt

# Method: projects.webApps.undelete

Restores the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` to the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`.

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{name=projects/*/webApps/*}:undelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The resource name of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`, in the format: `projects/PROJECT_IDENTIFIER/webApps/APP_ID` <br /> Since an <var translate="no">APP_ID</var> is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: `projects/-/webApps/APP_ID` <br /> Refer to the WebApp [name](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> and <var translate="no">APP_ID</var> values. |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "validateOnly": boolean, "etag": string } ``` |

| Fields ||
|---|---|
| `validateOnly` | `boolean` If set to true, the request is only validated. The App will *not* be undeleted. |
| `etag` | `string` Checksum provided in the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` resource. If provided, this checksum ensures that the client has an up-to-date value before proceeding. |

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).