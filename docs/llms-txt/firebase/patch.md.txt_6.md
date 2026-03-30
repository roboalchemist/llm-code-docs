# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/patch.md.txt

# Method: projects.apps.debugTokens.patch

Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken`.

For security reasons, the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken.FIELDS.token` field cannot be updated, nor will it be populated in the response, but you can revoke the debug token using `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/delete#google.firebase.appcheck.v1.ConfigService.DeleteDebugToken`.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1/{debugToken.name=projects/*/apps/*/debugTokens/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `debugToken.name` | `string` Required. The relative resource name of the debug token, in the format: projects/{project_number}/apps/{app_id}/debugTokens/{debug_token_id} |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken` to update. Example: `displayName`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).