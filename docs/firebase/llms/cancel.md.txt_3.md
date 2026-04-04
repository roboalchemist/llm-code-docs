# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations/cancel.md.txt

# Method: projects.locations.operations.cancel

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use `Operations.GetOperation` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations#Operation.FIELDS.error` value with a `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations#Status.FIELDS.code` of 1, corresponding to `Code.CANCELLED`.

### HTTP request

`POST https://firebasedataconnect.googleapis.com/v1beta/{name=projects/*/locations/*/operations/*}:cancel`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The name of the operation resource to be cancelled. |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasedataconnect.operations.cancel`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).