# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.md.txt

# REST Resource: projects.namespaces

## Resource: Namespace

The namespace of the RemoteConfig.

| JSON representation |
|---|
| ``` { "name": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. Identifier. The name of the namespace. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/get` | Gets a namespace object by name. |
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/getRemoteConfig` | Get a project's Remote Config template and associated ETag header. |
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/list` | Lists all available namespaces for a given Firebase project. |
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/updateRemoteConfig` | Publish a project's Remote Config template. |