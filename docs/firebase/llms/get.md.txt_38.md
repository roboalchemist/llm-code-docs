# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds/get.md.txt

# Method: projects.locations.backends.builds.get

Gets information about a build.

### HTTP request

`GET https://firebaseapphosting.googleapis.com/v1/{name=projects/*/locations/*/backends/*/builds/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax. To know more about valid error responses that can be thrown by this HTTP request, please refer to the [service error catalog](https://firebase.google.com/docs/reference/apphosting/rest/v1/errors)

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Name of the resource in the format: `projects/{project}/locations/{locationId}/backends/{backendId}/builds/{buildId}`. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds#Build`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebaseapphosting.builds.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

See also Firebase App Hosting's [IAM Permissions](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) and [Predefined IAM Roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).