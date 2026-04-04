# Source: https://firebase.google.com/docs/reference/remote-config/rest.md.txt

# Firebase Remote Config API

The Firebase Remote Config API lets developers change the behavior and appearance of their apps without requiring users to download an app update. It is an alternative to, but can be used in tandem with, the Firebase console at <https://console.firebase.google.com>.

## Service: firebaseremoteconfig.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebaseremoteconfig.googleapis.com/$discovery/rest?version=v1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebaseremoteconfig.googleapis.com`

## REST Resource: [v1.projects](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/getRemoteConfig` | `GET /v1/{project=projects/*}/remoteConfig` Get a project's Remote Config template and associated ETag header. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/updateRemoteConfig` | `PUT /v1/{project=projects/*}/remoteConfig` Publish a project's Remote Config template. |

## REST Resource: [v1.projects.namespaces](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/get` | `GET /v1/{name=projects/*/namespaces/*}` Gets a namespace object by name. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/getRemoteConfig` | `GET /v1/{name=projects/*/namespaces/*/remoteConfig}` Get a project's Remote Config template and associated ETag header. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/list` | `GET /v1/{parent=projects/*}/namespaces` Lists all available namespaces for a given Firebase project. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/updateRemoteConfig` | `PUT /v1/{name=projects/*/namespaces/*/remoteConfig}` Publish a project's Remote Config template. |

## REST Resource: [v1.projects.namespaces.experiments](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments/delete` | `DELETE /v1/{name=projects/*/namespaces/*/experiments/*}` Delete an experiment. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments/get` | `GET /v1/{name=projects/*/namespaces/*/experiments/*}` Get information about an existing experiment. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments/list` | `GET /v1/{parent=projects/*/namespaces/*}/experiments` List all experiments for a project. |

## REST Resource: [v1.projects.namespaces.remoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.remoteConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.remoteConfig/downloadDefaults` | `GET /v1/{name=projects/*/namespaces/*/remoteConfig}:downloadDefaults` Get a project's current Remote Config template parameters and default values in JSON, property list (plist), or XML format. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.remoteConfig/listVersions` | `GET /v1/{parent=projects/*/namespaces/*/remoteConfig}:listVersions` Get a list of `https://firebase.google.com/docs/reference/remote-config/rest/v1/Version` that have been published, sorted in reverse chronological order. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.remoteConfig/rollback` | `POST /v1/{name=projects/*/namespaces/*/remoteConfig}:rollback` Roll back a project's published Remote Config template to the one specified by the provided version number. |

## REST Resource: [v1.projects.namespaces.rollouts](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts/delete` | `DELETE /v1/{name=projects/*/namespaces/*/rollouts/*}` Delete a rollout experiment. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts/get` | `GET /v1/{name=projects/*/namespaces/*/rollouts/*}` Get details about a rollout experiment. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts/list` | `GET /v1/{parent=projects/*/namespaces/*}/rollouts` Get a list of all rollouts for a project. |

## REST Resource: [v1.projects.remoteConfig](https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig/downloadDefaults` | `GET /v1/{project=projects/*}/remoteConfig:downloadDefaults` Get a project's current Remote Config template parameters and default values in JSON, property list (plist), or XML format. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig/listVersions` | `GET /v1/{project=projects/*}/remoteConfig:listVersions` Get a list of `https://firebase.google.com/docs/reference/remote-config/rest/v1/Version` that have been published, sorted in reverse chronological order. |
| `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.remoteConfig/rollback` | `POST /v1/{project=projects/*}/remoteConfig:rollback` Roll back a project's published Remote Config template to the one specified by the provided version number. |