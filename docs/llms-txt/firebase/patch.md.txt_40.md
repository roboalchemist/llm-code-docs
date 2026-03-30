# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.traffic/patch.md.txt

# Method: projects.locations.backends.traffic.patch

Updates a backend's traffic.

### HTTP request

`PATCH https://firebaseapphosting.googleapis.com/v1/{traffic.name=projects/*/locations/*/backends/*/traffic}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax. To know more about valid error responses that can be thrown by this HTTP request, please refer to the [service error catalog](https://firebase.google.com/docs/reference/apphosting/rest/v1/errors)

### Path parameters

| Parameters ||
|---|---|
| `traffic.name` | `string` Identifier. The resource name of the backend's traffic. Format: `projects/{project}/locations/{locationId}/backends/{backendId}/traffic`. |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Optional. Field mask is used to specify the fields to be overwritten in the traffic resource by the update. The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |
| `requestId` | `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |
| `validateOnly` | `boolean` Optional. Indicates that the request should be validated, without persisting the request or updating any resources. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.traffic#Traffic`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations#Operation`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebaseapphosting.traffic.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

See also Firebase App Hosting's [IAM Permissions](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) and [Predefined IAM Roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).