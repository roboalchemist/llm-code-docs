# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/list.md.txt

# Method: projects.locations.templates.list

Lists PromptTemplates.

### HTTP request

`GET https://firebasevertexai.googleapis.com/v1beta/{parent=projects/*/locations/*}/templates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent resource where this PromptTemplate will be created. Format: projects/{project}/locations/{location} |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. The maximum number of PromptTemplates to return. The service may return fewer than this value. If unspecified, at most 50 PromptTemplates will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. |
| `pageToken` | `string` Optional. A page token, received from a previous `templates.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `templates.list` must match the call that provided the page token. |
| `filter` | `string` Optional. The filter to apply to the list of PromptTemplates. |

### Request body

The request body must be empty.

### Response body

Response message for `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/list#google.firebase.vertexai.v1beta.TemplateService.ListPromptTemplates`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "templates": [ { object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates#PromptTemplate`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `templates[]` | ``object (`https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates#PromptTemplate`)`` The PromptTemplates from the specified parent. |
| `nextPageToken` | `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasevertexai.promptTemplates.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).