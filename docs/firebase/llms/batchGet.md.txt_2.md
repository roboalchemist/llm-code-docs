# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/batchGet.md.txt

# Method: projects.apps.appAttestConfig.batchGet

Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`s for the specified list of apps.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1/{parent=projects/*}/apps/-/appAttestConfig:batchGet`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent project name shared by all `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`s being retrieved, in the format projects/{project_number} The parent collection in the `name` field of any resource being retrieved must match this field, or the entire batch fails. |

### Query parameters

| Parameters ||
|---|---|
| `names[]` | `string` Required. The relative resource names of the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`s to retrieve, in the format projects/{project_number}/apps/{app_id}/appAttestConfig A maximum of 100 objects can be retrieved in a batch. |

### Request body

The request body must be empty.

### Response body

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/batchGet#google.firebase.appcheck.v1.ConfigService.BatchGetAppAttestConfigs` method.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "configs": [ { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`) } ] } ``` |

| Fields ||
|---|---|
| `configs[]` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`)`` `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`s retrieved. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).