# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/create.md.txt

# Method: projects.locations.templates.create

Creates a new PromptTemplate.

### HTTP request

`POST https://firebasevertexai.googleapis.com/v1beta/{parent=projects/*/locations/*}/templates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent resource where this PromptTemplate will be created. Format: projects/{project}/locations/{location} |

### Query parameters

| Parameters ||
|---|---|
| `validateOnly` | `boolean` Optional. If set to true, the request will be validated but not executed. |
| `promptTemplateId` | `string` Optional. The unique ID to use for the PromptTemplate, which will become the final component of the PromptTemplate's resource name. It can contain only lowercase letters, numbers, and hyphens, with the first character a letter, the last a letter or a number, and a 63-character maximum. If not provided, a system-generated ID will be used. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates#PromptTemplate`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates#PromptTemplate`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasevertexai.promptTemplates.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).