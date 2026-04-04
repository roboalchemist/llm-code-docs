# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments/list.md.txt

# Method: projects.namespaces.experiments.list

List all experiments for a project.

--- **BETA:** This API is in a Beta launch stage. It is intended for public testing and feedback. While expected to be stable, interfaces may change

## with notice, and it may not be subject to the same SLAs as stable features.

### HTTP request

`GET https://firebaseremoteconfig.googleapis.com/v1/{parent=projects/*/namespaces/*}/experiments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent project for which to list experiments. Format: projects/{project}/namespaces/{namespace} |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` Optional. Filter expression following AIP-160 The following filters are supported: name: String. The experiment name. |
| `pageSize` | `integer` Optional. The maximum number of items to return per page. If not specified, defaults to 100. |
| `pageToken` | `string` Optional. The token for the specific page to retrieve. |

### Request body

The request body must be empty.

### Response body

Response message for experiments.list.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "experiments": [ { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#Experiment`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `experiments[]` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#Experiment`)`` List of experiments |
| `nextPageToken` | `string` Token for the next page |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).