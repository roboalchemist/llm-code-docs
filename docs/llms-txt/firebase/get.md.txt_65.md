# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get.md.txt

# Method: projects.releases.get

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get#body.response_body)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get#try-it)

Get a `Release` by name.

### HTTP request

`GET https://firebaserules.googleapis.com/v1/{name=projects/*/releases/**}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name of the `Release`. Format: `projects/{project_id}/releases/{release_id}` |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`
- `https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).