# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/get.md.txt

# Method: projects.namespaces.get

Gets a namespace object by name.

The namespace provided in \[GetNamespaceRequest.name\] must be "firebase" (for the client-side template) or "firebase-server" (for the server-side template).

### HTTP request

`GET https://firebaseremoteconfig.googleapis.com/v1/{name=projects/*/namespaces/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the namespace to get. Format: projects/{project}/namespaces/{namespace} |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces#Namespace`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).