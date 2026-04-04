# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/rollback.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/rollback.md.txt

# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig/rollback.md.txt

Roll back a project's published Remote Config template to the one specified by the provided version number.

A rollback is equivalent to getting a previously published Remote Config template, and re-publishing it using a force update. Returns the published RemoteConfig and the updated ETag as a response header if successful, or an error.

To roll back the server-side template, use "firebase-server" as the namespace ID in \[RollbackRemoteConfigRequest.name\]. If \[RollbackRemoteConfigRequest.name\] is not provided, the client-side template ('firebase' namespace) is rolled back.

See the publishing guide for a list of [error codes](https://firebase.google.com/docs/remote-config/use-config-rest#step_5_publish_json_data_to_replace_data_in_the_service). In particular, note that the method returns an error with HTTP Status 404 if the requested [versionNumber](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig/rollback#body.request_body.FIELDS.version_number) to rollback to is not found.

### HTTP request

`POST https://firebaseremoteconfig.googleapis.com/v1/{project=projects/*}/remoteConfig:rollback`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                           Parameters                                                                            ||
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project` | `string` The Firebase project's Project ID or Project Number, prefixed with "projects/". This field is required if the `name` field is not provided. |

### Request body

The request body contains data with the following structure:

|                 JSON representation                 |
|-----------------------------------------------------|
| ``` { "versionNumber": string, "name": string } ``` |

|                                                                                                                                                                                     Fields                                                                                                                                                                                     ||
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `versionNumber` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Required. The version number of the [RemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig) to roll back to. The specified version number must be less than the current version number, and not have been deleted due to staleness. |
| `name`          | `string` Optional. The name of the RemoteConfig to rollback. Format: projects/{project}/namespaces/{namespace}/remoteConfig Project is a Firebase project ID or project number. Namespace is the namespace ID (e.g.: firebase or firebase-server)                                                                                                             |

### Response body

If successful, the response body contains an instance of [RemoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).