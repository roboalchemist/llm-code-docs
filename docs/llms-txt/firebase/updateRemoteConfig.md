# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/updateRemoteConfig.md.txt

Publish a project's Remote Config template.

Pass the ETag returned by [projects.getRemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/getRemoteConfig#google.firebase.remoteconfig.v1.RemoteConfigService.GetRemoteConfig) as an `If-Match` header to ensure the last seen Remote Config template is the one being overwritten by this update. Pass `If-Match: *` to force an update, regardless of the current version.

Returns the published RemoteConfig and the updated ETag as a response header if successful, or an error.

To update the server-side template, use "firebase-server" as the namespace ID in \[UpdateRemoteConfigRequest.name\]. If \[UpdateRemoteConfigRequest.name\] is not provided, the client-side template ('firebase' namespace) is updated.

See the publishing guide for a list of [error codes](https://firebase.google.com/docs/remote-config/use-config-rest#step_5_publish_json_data_to_replace_data_in_the_service).

### HTTP request

`PUT https://firebaseremoteconfig.googleapis.com/v1/{project=projects/*}/remoteConfig`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                           Parameters                                                                            ||
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project` | `string` The Firebase project's Project ID or Project Number, prefixed with "projects/". This field is required if the `name` field is not provided. |

### Query parameters

|                                                                                                                                                                                                                                                                                                                                  Parameters                                                                                                                                                                                                                                                                                                                                   ||
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `validateOnly` | `boolean` Optional. Defaults to `false`. If `true`, the server will only attempt to validate the RemoteConfig. If validation succeeds, the RemoteConfig is not written to the Remote Config server, instead a `200 OK` response is returned. If validation fails, a validation error is returned. Note: other errors may still occur after this boolean is set to `false`, even if getting a `200 OK` when calling with [projects.updateRemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/updateRemoteConfig#google.firebase.remoteconfig.v1.RemoteConfigService.UpdateRemoteConfig) with `validateOnly` set to `true`. |
| `name`         | `string` Optional. The name of the RemoteConfig to update. Format: projects/{project}/namespaces/{namespace}/remoteConfig Project is a Firebase project ID or project number. Namespace is the namespace ID (e.g.: firebase or firebase-server)                                                                                                                                                                                                                                                                                                                                                                                                               |

### Request body

The request body contains an instance of [RemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig).

### Response body

If successful, the response body contains an instance of [RemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).