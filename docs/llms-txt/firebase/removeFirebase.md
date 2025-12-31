# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/removeFirebase.md.txt

# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/removeFirebase.md.txt

# Method: projects.buckets.removeFirebase

Unlinks a linked Google Cloud Storage bucket from a Firebase project.

### HTTP request

`POST https://firebasestorage.googleapis.com/v1beta/{bucket=projects/*/buckets/*}:removeFirebase`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                    Parameters                                                                                                                                                                     ||
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bucket` | `string` Required. Resource name of the bucket, mirrors the ID of the underlying Google Cloud Storage bucket, `projects/{project_number}/buckets/{bucket_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `bucket`: - `firebasestorage.buckets.removeFirebase` |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `bucket` resource:

- `firebasestorage.buckets.removeFirebase`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).