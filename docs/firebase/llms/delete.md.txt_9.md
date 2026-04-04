# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/delete.md.txt

# Method: projects.apps.debugTokens.delete

Deletes the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`.

A deleted debug token cannot be used to exchange for an App Check token. Use this method when you suspect the secret `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken.FIELDS.token` has been compromised or when you no longer need the debug token.

### HTTP request

`DELETE https://firebaseappcheck.googleapis.com/v1beta/{name=projects/*/apps/*/debugTokens/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The relative resource name of the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken` to delete, in the format: projects/{project_number}/apps/{app_id}/debugTokens/{debug_token_id} |

### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).