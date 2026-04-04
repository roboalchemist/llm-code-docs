# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list.md.txt

# Method: projects.apps.releases.list

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#body.ListReleasesResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list#try-it)

Lists releases. By default, sorts by `createTime` in descending order.

### HTTP request

`GET https://firebaseappdistribution.googleapis.com/v1/{parent=projects/*/apps/*}/releases`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The name of the app resource, which is the parent of the release resources. Format: `projects/{projectNumber}/apps/{appId}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the Firebase project that owns the specified resource `parent`: - `firebaseappdistro.releases.list` |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of releases to return. The service may return fewer than this value. The valid range is \[1-100\]; If unspecified (0), at most 25 releases are returned. Values above 100 are coerced to 100. |
| `pageToken` | `string` A page token, received from a previous `releases.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `releases.list` must match the call that provided the page token. |
| `orderBy` | `string` The fields used to order releases. Supported fields: - `createTime` To specify descending order for a field, append a "desc" suffix, for example, `createTime desc`. If this parameter is not set, releases are ordered by `createTime` in descending order. |
| `filter` | `string` The expression to filter releases listed in the response. To learn more about filtering, refer to [Google's AIP-160 standard](http://aip.dev/160). Supported fields: - `releaseNotes.text` supports `=` (can contain a wildcard character (`*`) at the beginning or end of the string) - `createTime` supports `<`, `<=`, `>` and `>=`, and expects an RFC-3339 formatted string Examples: - `createTime <= "2021-09-08T00:00:00+04:00"` - `releaseNotes.text="fixes" AND createTime >= "2021-09-08T00:00:00.0Z"` - `releaseNotes.text="*v1.0.0-rc*"` |

### Request body

The request body must be empty.

### Response body

The response message for `releases.list`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "releases": [ { object (`https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `releases[]` | ``object (`https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release`)`` The releases |
| `nextPageToken` | `string` A short-lived token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).