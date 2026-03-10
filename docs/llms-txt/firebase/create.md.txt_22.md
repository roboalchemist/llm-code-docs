# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/create.md.txt

# Method: projects.androidApps.create

Requests the creation of a new `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp` in the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`.

The result of this call is an `Operation` which can be used to track the provisioning process. The `Operation` is automatically deleted after completion, so there is no need to call `operations.delete`.

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{parent=projects/*}/androidApps`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` The resource name of the parent `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` in which to create an `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`, in the format: `projects/PROJECT_IDENTIFIER/androidApps` Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).