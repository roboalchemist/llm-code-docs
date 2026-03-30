# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create.md.txt

# Method: projects.apps.debugTokens.create

Creates a new `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken` for the specified app.

For security reasons, after the creation operation completes, the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken.FIELDS.token` field cannot be updated or retrieved, but you can revoke the debug token using `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/delete#google.firebase.appcheck.v1beta.ConfigService.DeleteDebugToken`.

Each app can have a maximum of 20 debug tokens.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1beta/{parent=projects/*/apps/*}/debugTokens`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The relative resource name of the parent app in which the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken` will be created, in the format: projects/{project_number}/apps/{app_id} |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).