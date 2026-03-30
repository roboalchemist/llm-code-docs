# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/delete.md.txt

# Method: projects.sites.delete

Deletes the specified Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` from the specified parent Firebase project.

### HTTP request

`DELETE https://firebasehosting.googleapis.com/v1beta1/{name=projects/*/sites/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The fully-qualified resource name for the Hosting site, in the format: `projects/PROJECT_IDENTIFIER/sites/SITE_ID` Refer to the `Site` [`name`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects#Site.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`: - `firebasehosting.sites.delete` |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).