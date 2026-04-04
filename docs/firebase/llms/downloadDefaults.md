# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig/downloadDefaults.md.txt

Get a project's current Remote Config template parameters and default values in JSON, property list (plist), or XML format.

To download the server-side template defaults, use "firebase-server" as the namespace ID in \[DownloadDefaultsRequest.name\]. If \[DownloadDefaultsRequest.name\] is not provided, the client-side template defaults ('firebase' namespace) are downloaded.

### HTTP request

`GET https://firebaseremoteconfig.googleapis.com/v1/{project=projects/*}/remoteConfig:downloadDefaults`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                  Parameters                                                   ||
|-----------|----------------------------------------------------------------------------------------------------|
| `project` | `string` Required. The Firebase project's Project ID or Project Number, prefixed with "projects/". |

### Query parameters

|                                                                                                                                Parameters                                                                                                                                ||
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `format` | `enum (`[Format](https://firebase.google.com/docs/reference/remote-config/rest/v1/Format)`)` Required. The file structure to return.                                                                                                                           |
| `name`   | `string` Optional. The name of the RemoteConfig to get defaults from. Format: projects/{project}/namespaces/{namespace}/remoteConfig Project is a Firebase project ID or project number. Namespace is the namespace ID (e.g.: 'firebase' or 'firebase-server') |

### Request body

The request body must be empty.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).