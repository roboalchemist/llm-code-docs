# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends/delete.md.txt

# Method: projects.locations.backends.delete

Deletes a single backend.

### HTTP request

`DELETE https://firebaseapphosting.googleapis.com/v1beta/{name=projects/*/locations/*/backends/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax. To know more about valid error responses that can be thrown by this HTTP request, please refer to the [service error catalog](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/errors)

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Name of the resource in the format: `projects/{project}/locations/{locationId}/backends/{backendId}`. |

### Query parameters

| Parameters ||
|---|---|
| `requestId` | `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |
| `force` | `boolean` Optional. If set to true, any resources for this backend will also be deleted. Otherwise, any children resources will block deletion. |
| `validateOnly` | `boolean` Optional. Indicates that the request should be validated, without persisting the request or updating any resources. |
| `etag` | `string` Optional. If the client provided etag is out of date, delete will be returned FAILED_PRECONDITION error. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations#Operation`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebaseapphosting.backends.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

See also Firebase App Hosting's [IAM Permissions](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) and [Predefined IAM Roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).