# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templateStreamGenerateContent.md.txt

# Method: projects.locations.templates.templateStreamGenerateContent

Generate content with multimodal inputs and streaming outputs using a server-side prompt template.

### HTTP request

`POST https://firebasevertexai.googleapis.com/v1beta/{name=projects/*/locations/*/templates/*}:templateStreamGenerateContent`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Name of the template to use in the request. projects/project-id/location/location-name/template/template-id |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "inputs": { object } } ``` |

| Fields ||
|---|---|
| `inputs` | ``object (`https://protobuf.dev/reference/protobuf/google.protobuf#struct` format)`` Optional. Client provided data that can be used when rendering the template. When calling via JSON/http surfaces this should be wire compatible with an arbitrary JSON object. |

### Response body

If successful, the response body contains a stream of `GenerateContentResponse` instances.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).