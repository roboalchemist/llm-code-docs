# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list.md.txt

# Method: projects.groups.list

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#body.ListGroupsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list#try-it)

List groups.

### HTTP request

`GET https://firebaseappdistribution.googleapis.com/v1/{parent=projects/*}/groups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The name of the project resource, which is the parent of the group resources. Format: `projects/{projectNumber}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `parent`: - `firebaseappdistro.testers.list` |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. The maximum number of groups to return. The service may return fewer than this value. The valid range is \[1-1000\]; If unspecified (0), at most 25 groups are returned. Values above 1000 are coerced to 1000. |
| `pageToken` | `string` Optional. A page token, received from a previous `groups.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `groups.list` must match the call that provided the page token. |

### Request body

The request body must be empty.

### Response body

The response message for `groups.list`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "groups": [ { object (`https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `groups[]` | ``object (`https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups#Group`)`` The groups listed. |
| `nextPageToken` | `string` A short-lived token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).