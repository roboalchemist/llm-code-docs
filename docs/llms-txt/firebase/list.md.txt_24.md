# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/list.md.txt

# Method: projects.services.list

Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service` configurations for the specified project.

Only `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`s which were explicitly configured using `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/patch#google.firebase.appcheck.v1.ConfigService.UpdateService` or `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/batchUpdate#google.firebase.appcheck.v1.ConfigService.BatchUpdateServices` will be returned.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1/{parent=projects/*}/services`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The relative resource name of the parent project for which to list each associated `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`, in the format: projects/{project_number} |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`s to return in the response. Only explicitly configured services are returned. The server may return fewer than this at its own discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. |
| `pageToken` | `string` Token returned from a previous call to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/list#google.firebase.appcheck.v1.ConfigService.ListServices` indicating where in the set of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`s to resume listing. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/list#google.firebase.appcheck.v1.ConfigService.ListServices` must match the call that provided the page token; if they do not match, the result is undefined. |

### Request body

The request body must be empty.

### Response body

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/list#google.firebase.appcheck.v1.ConfigService.ListServices` method.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "services": [ { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `services[]` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`)`` The `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`s retrieved. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty or omitted, then this response is the last page of results. This token can be used in a subsequent call to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/list#google.firebase.appcheck.v1.ConfigService.ListServices` to find the next group of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service`s. Page tokens are short-lived and should not be persisted. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).