# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/delete.md.txt

# Method: projects.locations.templates.delete

Deletes a PromptTemplate.

### HTTP request

`DELETE https://firebasevertexai.googleapis.com/v1beta/{name=projects/*/locations/*/templates/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the PromptTemplate resource to be deleted. Format: projects/{project}/locations/{location}/templates/{promptTemplate} |

### Query parameters

| Parameters ||
|---|---|
| `etag` | `string` Optional. The etag of the PromptTemplate. If this is provided, it must match the server's etag for the operation to succeed. |
| `validateOnly` | `boolean` Optional. If set to true, the request will be validated but not executed. |
| `allowMissing` | `boolean` Optional. If set to true and the PromptTemplate does not exist, the method will still succeed. |

### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasevertexai.promptTemplates.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).