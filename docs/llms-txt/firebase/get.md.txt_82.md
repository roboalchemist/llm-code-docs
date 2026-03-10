# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/get.md.txt

# Method: projects.iosApps.get

Gets the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp`.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/{name=projects/*/iosApps/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The resource name of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp`, in the format: `projects/PROJECT_IDENTIFIER/iosApps/APP_ID` <br /> Since an <var translate="no">APP_ID</var> is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: `projects/-/iosApps/APP_ID` <br /> Refer to the `IosApp` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> and <var translate="no">APP_ID</var> values. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp`.

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