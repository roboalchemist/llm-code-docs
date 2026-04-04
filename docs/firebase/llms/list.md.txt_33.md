# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/list.md.txt

# Method: projects.locations.services.connectors.list

Lists Connectors in a given project and location.

### HTTP request

`GET https://firebasedataconnect.googleapis.com/v1beta/{parent=projects/*/locations/*/services/*}/connectors`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. Value of parent. |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. |
| `pageToken` | `string` Optional. A page token, received from a previous `connectors.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `connectors.list` must match the call that provided the page token. |
| `filter` | `string` Optional. Filtering results. |
| `orderBy` | `string` Optional. Hint for how to order the results. |

### Request body

The request body must be empty.

### Response body

Message for response to listing Connectors.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "connectors": [ { object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors#Connector`) } ], "nextPageToken": string, "unreachable": [ string ] } ``` |

| Fields ||
|---|---|
| `connectors[]` | ``object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors#Connector`)`` The list of Connectors. |
| `nextPageToken` | `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable[]` | `string` Locations that could not be reached. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasedataconnect.connectors.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).