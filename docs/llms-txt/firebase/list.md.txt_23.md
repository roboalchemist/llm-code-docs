# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/list.md.txt

# Method: projects.services.resourcePolicies.list

Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configurations for the specified project and service.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1/{parent=projects/*/services/*}/resourcePolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The relative resource name of the parent `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service` for which to list each associated `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy`, in the format: projects/{project_number}/services/{service_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `oauth2.googleapis.com` (Google Identity for iOS) |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` objects to return in the response. The server may return fewer than this at its own discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. |
| `pageToken` | `string` Token returned from a previous call to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/list#google.firebase.appcheck.v1.ConfigService.ListResourcePolicies` indicating where in the set of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` objects to resume listing. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/list#google.firebase.appcheck.v1.ConfigService.ListResourcePolicies` must match the call that provided the page token; if they do not match, the result is undefined. |
| `filter` | `string` Optional. Filters the results by the specified rule. For the exact syntax of this field, please consult the [AIP-160](https://google.aip.dev/160) standard. Currently, since the only fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` resource are the scalar fields `enforcementMode` and `targetResource`, this method does not support the traversal operator (`.`) or the has operator (`:`). Here are some examples of valid filters: - `enforcementMode = ENFORCED` - `targetResource = "//oauth2.googleapis.com/projects/12345/oauthClients/<some_oauth_client_id>"` - `enforcementMode = ENFORCED AND targetResource = "//oauth2.googleapis.com/projects/12345/oauthClients/<some_oauth_client_id>"` |

### Request body

The request body must be empty.

### Response body

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/list#google.firebase.appcheck.v1.ConfigService.ListResourcePolicies` method.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "resourcePolicies": [ { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `resourcePolicies[]` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy`)`` The `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` objects retrieved. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty or omitted, then this response is the last page of results. This token can be used in a subsequent call to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/list#google.firebase.appcheck.v1.ConfigService.ListResourcePolicies` to find the next group of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` objects. Page tokens are short-lived and should not be persisted. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).