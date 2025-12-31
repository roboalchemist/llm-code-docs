# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig/listVersions.md.txt

Get a list of [Remote Config template versions](https://firebase.google.com/docs/reference/remote-config/rest/v1/Version) that have been published, sorted in reverse chronological order.

Only the last 300 versions are stored.

All versions that correspond to non-active Remote Config templates (i.e., all except the template that is being fetched by clients) are also deleted if they are older than 90 days.

To list server-side template versions, use "firebase-server" as the namespace ID in \[ListVersionsRequest.parent\]. If \[ListVersionsRequest.parent\] is not provided, the client-side template versions ('firebase' namespace) are listed.

### HTTP request

`GET https://firebaseremoteconfig.googleapis.com/v1/{project=projects/*}/remoteConfig:listVersions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                  Parameters                                                   ||
|-----------|----------------------------------------------------------------------------------------------------|
| `project` | `string` Required. The Firebase project's Project ID or Project Number, prefixed with "projects/". |

### Query parameters

|                                                                                                                                                                                                                                                   Parameters                                                                                                                                                                                                                                                    ||
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pageSize`         | `integer` Optional. The maximum number of items to return per page.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `pageToken`        | `string` Optional. The nextPageToken value returned from a previous List request, if any.                                                                                                                                                                                                                                                                                                                                                                                                   |
| `endVersionNumber` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Optional. Specify the newest version number to include in the results. If specified, must be greater than zero. Defaults to the newest version.                                                                                                                                                                                                                                                         |
| `startTime`        | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Specify the earliest update time to include in the results; any entries updated before this time are omitted. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.    |
| `endTime`          | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Specify the latest update time to include in the results; any entries updated on or after this time are omitted. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `parent`           | `string` Optional. The resource name of the RemoteConfig to list versions for. Format: projects/{project}/namespaces/{namespace}/remoteConfig Project is a Firebase project ID or project number. Namespace is the namespace ID (e.g.: 'firebase' or 'firebase-server')                                                                                                                                                                                                                     |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of [ListVersionsResponse](https://firebase.google.com/docs/reference/remote-config/rest/v1/ListVersionsResponse).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).