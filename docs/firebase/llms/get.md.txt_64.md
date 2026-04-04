# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/get.md.txt

# Method: projects.buckets.get

Gets a single linked storage bucket.

### HTTP request

`GET https://firebasestorage.googleapis.com/v1beta/{name=projects/*/buckets/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name of the bucket, mirrors the ID of the underlying Google Cloud Storage bucket, `projects/{project_number}/buckets/{bucket_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`: - `firebasestorage.buckets.get` |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets#Bucket`.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasestorage.buckets.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).