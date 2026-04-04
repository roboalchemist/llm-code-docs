# Source: https://redocly.com/learn/openapi/openapi-visual-reference/path-item.md

# Path Item Object

details
summary

Excerpt from the OpenAPI 3.1 specification about the Path Item object

## Path Item Object

Describes the operations available on a single path.
A Path Item MAY be empty, due to ACL constraints.
The path itself is still exposed to the documentation viewer but they will not know which operations and parameters are available.

### Fixed Fields

| Field Name | Type | Description |
|  --- | --- | --- |
| `$ref` | `string` | Allows for a referenced definition of this path item. The referenced structure MUST be in the form of a [Path Item Object](/learn/openapi/openapi-visual-reference/path-item).  In case a Path Item Object field appears both in the defined object and the referenced object, the behavior is undefined. See the rules for resolving [Relative References](/learn/openapi/openapi-visual-reference/reference). |
| summary | `string` | An optional, string summary, intended to apply to all operations in this path. |
| description | `string` | An optional, string description, intended to apply to all operations in this path. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation. |
| get | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a GET operation on this path. |
| put | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a PUT operation on this path. |
| post | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a POST operation on this path. |
| delete | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a DELETE operation on this path. |
| options | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a OPTIONS operation on this path. |
| head | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a HEAD operation on this path. |
| patch | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a PATCH operation on this path. |
| trace | [Operation Object](/learn/openapi/openapi-visual-reference/operation) | A definition of a TRACE operation on this path. |
| servers | [[Server Object](/learn/openapi/openapi-visual-reference/servers)] | An alternative `server` array to service all operations in this path. |
| parameters | [[Parameter Object](/learn/openapi/openapi-visual-reference/parameters) | [Reference Object](/learn/openapi/openapi-visual-reference/reference)] | A list of parameters that are applicable for all the operations described under this path. These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a [name](/learn/openapi/openapi-visual-reference/parameter) and [location](/learn/openapi/openapi-visual-reference/parameter). The list can use the [Reference Object](/learn/openapi/openapi-visual-reference/reference) to link to parameters that are defined at the [OpenAPI Object's components/parameters](/learn/openapi/openapi-visual-reference/parameters). |


This object MAY be extended with [Specification Extensions](/learn/openapi/openapi-visual-reference/specification-extensions).

### Path Item Object Example


```json
{
  "get": {
    "description": "Returns pets based on ID",
    "summary": "Find pets by ID",
    "operationId": "getPetsById",
    "responses": {
      "200": {
        "description": "pet response",
        "content": {
          "*/*": {
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Pet"
              }
            }
          }
        }
      },
      "default": {
        "description": "error payload",
        "content": {
          "text/html": {
            "schema": {
              "$ref": "#/components/schemas/ErrorModel"
            }
          }
        }
      }
    }
  },
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "description": "ID of pet to use",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "style": "simple"
    }
  ]
}
```


```yaml
get:
  description: Returns pets based on ID
  summary: Find pets by ID
  operationId: getPetsById
  responses:
    '200':
      description: pet response
      content:
        '*/*' :
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Pet'
    default:
      description: error payload
      content:
        'text/html':
          schema:
            $ref: '#/components/schemas/ErrorModel'
parameters:
- name: id
  in: path
  description: ID of pet to use
  required: true
  schema:
    type: array
    items:
      type: string
  style: simple
```

## Visuals

Redocly renders each operation.
The HTTP method renders as a badge in the sidebar navigation as well as next to the operation summary.

Redocly renders the path within each path item's corresponding operations.

![root path item](/assets/paths-root-path.6ac67e5b6c3619862147f688dc91509eccfa6bab6d9ae0f2f3e410d017169958.6f948c6e.png)

![results path item](/assets/paths-results.46ff11033a9dfe493f3b5c17c7c58da3a1fca3ad04d779a25a1bed4c6bf6a19f.6f948c6e.png)

## Types

- `PathItem`



```js
const PathItem: NodeType = {
  properties: {
    $ref: { type: 'string' },
    servers: listOf('Server'),
    parameters: listOf('Parameter'),
    summary: { type: 'string' },
    description: { type: 'string' },
    get: 'Operation',
    put: 'Operation',
    post: 'Operation',
    delete: 'Operation',
    options: 'Operation',
    head: 'Operation',
    patch: 'Operation',
    trace: 'Operation',
  },
};
```

The `PathItem` type has a close relationship to the [`Operation` type](/learn/openapi/openapi-visual-reference/operation).


```mermaid
erDiagram
          Paths ||..o{ PathItem : has
          PathItem ||..o{ Parameter : has
          PathItem ||..|{ Operation : has
          PathItem ||..o{ Server : has
```