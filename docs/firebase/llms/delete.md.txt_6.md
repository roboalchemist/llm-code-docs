# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete.md.txt

# Method: projects.groups.delete

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete#try-it)

Delete a group.

### HTTP request

`DELETE https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/groups/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the group resource. Format: `projects/{projectNumber}/groups/{group_alias}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `name`: - `firebaseappdistro.testers.update` |

### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).