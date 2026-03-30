# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/get.md.txt

# Method: projects.locations.templates.get

Gets a PromptTemplate.

### HTTP request

`GET https://firebasevertexai.googleapis.com/v1beta/{name=projects/*/locations/*/templates/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the PromptTemplate resource. Format: projects/{project}/locations/{location}/templates/{promptTemplate} |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates#PromptTemplate`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasevertexai.promptTemplates.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).