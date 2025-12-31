# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects/deleteDefaultBucket.md.txt

# Method: projects.deleteDefaultBucket

Unlinks and deletes the default bucket for the specified Firebase project.

### HTTP request

`DELETE https://firebasestorage.googleapis.com/v1alpha/{name=projects/*/defaultBucket}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                         Parameters                                                                                                                                         ||
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. The name of the default bucket to delete, `projects/{project_id_or_number}/defaultBucket`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`: - `firebasestorage.defaultBucket.delete` |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasestorage.defaultBucket.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).