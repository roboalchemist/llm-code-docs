# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig/batchGet.md.txt

# Method: projects.apps.playIntegrityConfig.batchGet

Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`s for the specified list of apps.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1beta/{parent=projects/*}/apps/-/playIntegrityConfig:batchGet`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent project name shared by all `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`s being retrieved, in the format projects/{project_number} The parent collection in the `name` field of any resource being retrieved must match this field, or the entire batch fails. |

### Query parameters

| Parameters ||
|---|---|
| `names[]` | `string` Required. The relative resource names of the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`s to retrieve, in the format projects/{project_number}/apps/{app_id}/playIntegrityConfig A maximum of 100 objects can be retrieved in a batch. |

### Request body

The request body must be empty.

### Response body

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig/batchGet#google.firebase.appcheck.v1beta.ConfigService.BatchGetPlayIntegrityConfigs` method.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "configs": [ { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`) } ] } ``` |

| Fields ||
|---|---|
| `configs[]` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`)`` `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`s retrieved. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).