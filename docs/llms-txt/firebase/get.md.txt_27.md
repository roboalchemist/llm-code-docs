# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get.md.txt

# Method: projects.apps.releases.operations.get

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get#try-it)

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

### HTTP request

`GET https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*/operations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The name of the operation resource. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations#Operation`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).