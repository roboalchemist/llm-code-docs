# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts/get.md.txt

# Method: projects.namespaces.rollouts.get

Get details about a rollout experiment.

--- **BETA:** This API is in a Beta launch stage. It is intended for public testing and feedback. While expected to be stable, interfaces may change

## with notice, and it may not be subject to the same SLAs as stable features.

### HTTP request

`GET https://firebaseremoteconfig.googleapis.com/v1/{name=projects/*/namespaces/*/rollouts/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the rollout to get. Format: projects/{project}/namespaces/{namespace}/rollouts/{rolloutId} |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts#Rollout`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).