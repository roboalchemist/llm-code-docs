# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/getRemoteConfig.md.txt

Get a project's Remote Config template and associated ETag header. Returns the requested RemoteConfig as the payload and an ETag as a response header. The REST resource name for a Remote Config template is in the format: `projects/{projectId}/namespaces/{namespace_id}/remoteConfig`.

To retrieve the server-side template, use "firebase-server" as the namespace ID in \[GetRemoteConfigRequest.name\]. If \[GetRemoteConfigRequest.name\] is not provided, the client-side template ('firebase' namespace) is returned.

### HTTP request

`GET https://firebaseremoteconfig.googleapis.com/v1/{project=projects/*}/remoteConfig`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                  Parameters                                                   ||
|-----------|----------------------------------------------------------------------------------------------------|
| `project` | `string` Required. The Firebase project's Project ID or Project Number, prefixed with "projects/". |

### Query parameters

|                                                                                                                            Parameters                                                                                                                             ||
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `versionNumber` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Optional. Version number of the RemoteConfig to look up. If not specified, the latest RemoteConfig will be returned.                                         |
| `name`          | `string` Optional. The name of the RemoteConfig to get. Format: projects/{project}/namespaces/{namespace}/remoteConfig Project is a Firebase project ID or project number. Namespace is the namespace ID (e.g.: 'firebase' or 'firebase-server') |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of [RemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).