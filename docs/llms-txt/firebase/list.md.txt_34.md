# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/list.md.txt

# Method: projects.locations.services.schemas.list

Lists Schemas in a given project and location. Note that only `schemas/main` is supported, so this will always return at most one Schema.

### HTTP request

`GET https://firebasedataconnect.googleapis.com/v1beta/{parent=projects/*/locations/*/services/*}/schemas`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. Value of parent. |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. |
| `pageToken` | `string` Optional. A page token, received from a previous `schemas.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `schemas.list` must match the call that provided the page token. |
| `filter` | `string` Optional. Filtering results. |
| `orderBy` | `string` Optional. Hint for how to order the results. |

### Request body

The request body must be empty.

### Response body

Message for response to listing Schemas.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "schemas": [ { object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#Schema`) } ], "nextPageToken": string, "unreachable": [ string ] } ``` |

| Fields ||
|---|---|
| `schemas[]` | ``object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#Schema`)`` The list of Schemas. |
| `nextPageToken` | `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable[]` | `string` Locations that could not be reached. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasedataconnect.schemas.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).