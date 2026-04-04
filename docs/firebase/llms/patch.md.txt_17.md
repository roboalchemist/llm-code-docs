# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch.md.txt

# Method: projects.groups.patch

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch#try-it)

Update a group.

### HTTP request

`PATCH https://firebaseappdistribution.googleapis.com/v1/{group.name=projects/*/groups/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `group.name` | `string` The name of the group resource. Format: `projects/{projectNumber}/groups/{group_alias}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `name`: - `firebaseappdistro.testers.update` |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` The list of fields to update. This is a comma-separated list of fully qualified names of fields. Example: `"displayName"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).