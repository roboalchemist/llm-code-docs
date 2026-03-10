# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/cancel.md.txt

# Method: projects.locations.operations.cancel

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/get#google.longrunning.Operations.GetOperation` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations#Operation.FIELDS.error` value with a `https://firebase.google.com/docs/reference/apphosting/rest/v1/Status#FIELDS.code` of `1`, corresponding to `Code.CANCELLED`.

### HTTP request

`POST https://firebaseapphosting.googleapis.com/v1/{name=projects/*/locations/*/operations/*}:cancel`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax. To know more about valid error responses that can be thrown by this HTTP request, please refer to the [service error catalog](https://firebase.google.com/docs/reference/apphosting/rest/v1/errors)

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The name of the operation resource to be cancelled. |

### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebaseapphosting.operations.cancel`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

See also Firebase App Hosting's [IAM Permissions](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) and [Predefined IAM Roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).