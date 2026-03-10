# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create.md.txt

# Method: projects.groups.create

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create#try-it)

Create a group.

### HTTP request

`POST https://firebaseappdistribution.googleapis.com/v1/{parent=projects/*}/groups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The name of the project resource, which is the parent of the group resource. Format: `projects/{projectNumber}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `parent`: - `firebaseappdistro.testers.update` |

### Query parameters

| Parameters ||
|---|---|
| `groupId` | `string` Optional. The "alias" to use for the group, which will become the final component of the group's resource name. This value must be unique per project. The field is named `groupId` to comply with AIP guidance for user-specified IDs. This value should be 4-63 characters, and valid characters are `/[a-z][0-9]-/`. If not set, it will be generated based on the display name. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).