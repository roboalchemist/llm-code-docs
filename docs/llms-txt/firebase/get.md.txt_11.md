# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/get.md.txt

# Method: projects.apps.debugTokens.get

Gets the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`.

For security reasons, the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken.FIELDS.token` field is never populated in the response.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1beta/{name=projects/*/apps/*/debugTokens/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The relative resource name of the debug token, in the format: projects/{project_number}/apps/{app_id}/debugTokens/{debug_token_id} |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).