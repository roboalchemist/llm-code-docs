# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/list.md.txt

# Method: projects.apps.debugTokens.list

Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`s for the specified app.

For security reasons, the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken.FIELDS.token` field is never populated in the response.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1beta/{parent=projects/*/apps/*}/debugTokens`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The relative resource name of the parent app for which to list each associated `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`, in the format: projects/{project_number}/apps/{app_id} |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`s to return in the response. Note that an app can have at most 20 debug tokens. The server may return fewer than this at its own discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. |
| `pageToken` | `string` Token returned from a previous call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/list#google.firebase.appcheck.v1beta.ConfigService.ListDebugTokens` indicating where in the set of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`s to resume listing. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/list#google.firebase.appcheck.v1beta.ConfigService.ListDebugTokens` must match the call that provided the page token; if they do not match, the result is undefined. |

### Request body

The request body must be empty.

### Response body

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/list#google.firebase.appcheck.v1beta.ConfigService.ListDebugTokens` method.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "debugTokens": [ { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `debugTokens[]` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`)`` The `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`s retrieved. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty or omitted, then this response is the last page of results. This token can be used in a subsequent call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/list#google.firebase.appcheck.v1beta.ConfigService.ListDebugTokens` to find the next group of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`s. Page tokens are short-lived and should not be persisted. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).