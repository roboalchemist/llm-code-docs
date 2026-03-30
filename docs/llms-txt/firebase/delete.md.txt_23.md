# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/delete.md.txt

# Method: projects.androidApps.sha.delete

Removes a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate` from the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`.

### HTTP request

`DELETE https://firebase.googleapis.com/v1beta1/{name=projects/*/androidApps/*/sha/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The resource name of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate` to remove from the parent `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`, in the format: `projects/PROJECT_IDENTIFIER/androidApps/APP_ID/sha/SHA_HASH` Refer to the `ShaCertificate` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var>, <var translate="no">APP_ID</var>, and <var translate="no">SHA_HASH</var> values. You can obtain the full resource name of the `ShaCertificate` from the response of [`sha.list`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/list) or the original [`sha.create`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/create). |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).