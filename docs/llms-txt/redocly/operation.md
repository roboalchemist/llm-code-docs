# Source: https://redocly.com/learn/openapi/openapi-visual-reference/operation.md

# Operation Object

details
summary

Excerpt from the OpenAPI 3.1 specification about the Operation object

## Operation Object

Describes a single API operation on a path.

### Fixed Fields

| Field Name | Type | Description |
|  --- | --- | --- |
| tags | [`string`] | A list of tags for API documentation control. Tags can be used for logical grouping of operations by resources or any other qualifier. |
| summary | `string` | A short summary of what the operation does. |
| description | `string` | A verbose explanation of the operation behavior. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation. |
| externalDocs | [External Documentation Object](/learn/openapi/openapi-visual-reference/external-docs) | Additional external documentation for this operation. |
| operationId | `string` | Unique string used to identify the operation. The id MUST be unique among all operations described in the API. The operationId value is **case-sensitive**. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions. |
| parameters | [[Parameter Object](/learn/openapi/openapi-visual-reference/parameter) | [Reference Object](/learn/openapi/openapi-visual-reference/reference)] | A list of parameters that are applicable for this operation. If a parameter is already defined at the [Path Item](/learn/openapi/openapi-visual-reference/path-item), the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a [name](/learn/openapi/openapi-visual-reference/parameter) and [location](/learn/openapi/openapi-visual-reference/parameter). The list can use the [Reference Object](/learn/openapi/openapi-visual-reference/reference) to link to parameters that are defined at the [OpenAPI Object's components/parameters](/learn/openapi/openapi-visual-reference/parameters). |
| requestBody | [Request Body Object](/learn/openapi/openapi-visual-reference/request-body) | [Reference Object](/learn/openapi/openapi-visual-reference/reference) | The request body applicable for this operation.  The `requestBody` is fully supported in HTTP methods where the HTTP 1.1 specification [RFC7231](https://tools.ietf.org/html/rfc7231#section-4.3.1) has explicitly defined semantics for request bodies.  In other cases where the HTTP spec is vague (such as [GET](https://tools.ietf.org/html/rfc7231#section-4.3.1), [HEAD](https://tools.ietf.org/html/rfc7231#section-4.3.2) and [DELETE](https://tools.ietf.org/html/rfc7231#section-4.3.5)), `requestBody` is permitted but does not have well-defined semantics and SHOULD be avoided if possible. |
| responses | [Responses Object](/learn/openapi/openapi-visual-reference/responses) | The list of possible responses as they are returned from executing this operation. |
| callbacks | Map[`string`, [Callback Object](/learn/openapi/openapi-visual-reference/callbacks) | [Reference Object](/learn/openapi/openapi-visual-reference/reference)] | A map of possible out-of band callbacks related to the parent operation. The key is a unique identifier for the Callback Object. Each value in the map is a [Callback Object](/learn/openapi/openapi-visual-reference/callbacks) that describes a request that may be initiated by the API provider and the expected responses. |
| deprecated | `boolean` | Declares this operation to be deprecated. Consumers SHOULD refrain from usage of the declared operation. Default value is `false`. |
| security | [[Security Requirement Object](/learn/openapi/openapi-visual-reference/security)] | A declaration of which security mechanisms can be used for this operation. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement (`{}`) can be included in the array. This definition overrides any declared top-level [`security`](/learn/openapi/openapi-visual-reference/security). To remove a top-level security declaration, an empty array can be used. |
| servers | [[Server Object](/learn/openapi/openapi-visual-reference/servers)] | An alternative `server` array to service this operation. If an alternative `server` object is specified at the Path Item Object or Root level, it will be overridden by this value. |


This object MAY be extended with [Specification Extensions](/learn/openapi/openapi-visual-reference/specification-extensions).

### Operation Object Example


```json
{
  "tags": [
    "pet"
  ],
  "summary": "Updates a pet in the store with form data",
  "operationId": "updatePetWithForm",
  "parameters": [
    {
      "name": "petId",
      "in": "path",
      "description": "ID of pet that needs to be updated",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "requestBody": {
    "content": {
      "application/x-www-form-urlencoded": {
        "schema": {
          "type": "object",
          "properties": {
            "name": {
              "description": "Updated name of the pet",
              "type": "string"
            },
            "status": {
              "description": "Updated status of the pet",
              "type": "string"
            }
          },
          "required": ["status"]
        }
      }
    }
  },
  "responses": {
    "200": {
      "description": "Pet updated.",
      "content": {
        "application/json": {},
        "application/xml": {}
      }
    },
    "405": {
      "description": "Method Not Allowed",
      "content": {
        "application/json": {},
        "application/xml": {}
      }
    }
  },
  "security": [
    {
      "petstore_auth": [
        "write:pets",
        "read:pets"
      ]
    }
  ]
}
```


```yaml
tags:
- pet
summary: Updates a pet in the store with form data
operationId: updatePetWithForm
parameters:
- name: petId
  in: path
  description: ID of pet that needs to be updated
  required: true
  schema:
    type: string
requestBody:
  content:
    'application/x-www-form-urlencoded':
      schema:
       type: object
       properties:
          name:
            description: Updated name of the pet
            type: string
          status:
            description: Updated status of the pet
            type: string
       required:
         - status
responses:
  '200':
    description: Pet updated.
    content:
      'application/json': {}
      'application/xml': {}
  '405':
    description: Method Not Allowed
    content:
      'application/json': {}
      'application/xml': {}
security:
- petstore_auth:
  - write:pets
  - read:pets
```

The operation is the granular unit for each API.
Redocly renders each operations http method and summary in the sidebar navigation in the order they are defined by default.

## Visuals

The operation object includes many other types. See [Media Type Object](/learn/openapi/openapi-visual-reference/media-type), [Parameter](/learn/openapi/openapi-visual-reference/parameter), [Request body](/learn/openapi/openapi-visual-reference/request-body), [Responses](/learn/openapi/openapi-visual-reference/responses), [Servers](/learn/openapi/openapi-visual-reference/servers), [Security](/learn/openapi/openapi-visual-reference/security) for types that are included in an operation. In addition, the operation has an `operationId`, `summary`, and `description`.

### `operationId`

The `operationId` is path segment or path fragment in deep links to a specific operation.

![operationId in URL](/assets/operation-operation-id.8dd9cd80e0f539d67d1c921c0efd76834958256736bbacb14495bdbf5d85bd47.6f948c6e.png)

### `summary`

The `summary` displays in the sidebar navigation and the heading in the main panel.

![operation-summary-description](/assets/operation-summary-description.66797910424243dc7650226517f30feca667c6c1dff6e8716614f6853399558a.6f948c6e.png)

### `description`

The `description` displays under the `summary` in the main panel.
The description renders Markdown into HTML.
Use Markdown to style content.

![operation-summary-description](/assets/operation-summary-description.66797910424243dc7650226517f30feca667c6c1dff6e8716614f6853399558a.6f948c6e.png)

## Types

- `Operation`


The `Operation` type is filled with properties.


```js
const Operation: NodeType = {
  properties: {
    tags: {
      type: 'array',
      items: { type: 'string' },
    },
    summary: { type: 'string' },
    description: { type: 'string' },
    externalDocs: 'ExternalDocs',
    operationId: { type: 'string' },
    parameters: listOf('Parameter'),
    security: listOf('SecurityRequirement'),
    servers: listOf('Server'),
    requestBody: 'RequestBody',
    responses: 'ResponsesMap',
    deprecated: { type: 'boolean' },
    callbacks: mapOf('Callback'),
    'x-codeSamples': listOf('XCodeSample'),
    'x-code-samples': listOf('XCodeSample'), // deprecated
  },
  required: ['responses'],
};
```