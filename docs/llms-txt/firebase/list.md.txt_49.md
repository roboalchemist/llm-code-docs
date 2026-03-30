# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/list.md.txt

# Method: projects.buckets.list

Lists the linked Cloud Storage for Firebase buckets for the specified Firebase project.

### HTTP request

`GET https://firebasestorage.googleapis.com/v1alpha/{parent=projects/*}/buckets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. Resource name of the parent Firebase project, `projects/{project_id_or_number}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`: - `firebasestorage.buckets.list` |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of buckets to return. If not set, the server will use a reasonable default. |
| `pageToken` | `string` A page token, received from a previous `buckets.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `buckets.list` must match the call that provided the page token. |

### Request body

The request body must be empty.

### Response body

The response returned by `buckets.list`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "buckets": [ { object (`https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets#Bucket`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `buckets[]` | ``object (`https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets#Bucket`)`` The list of linked buckets. |
| `nextPageToken` | `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasestorage.buckets.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).