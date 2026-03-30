# Source: https://www.speakeasy.com/md/openapi/paths.md

# Paths Object in OpenAPI

The `paths` object is a map of [Path Item Objects](/openapi/paths#path-item-object) that describes the available paths and operations for the API.

Each path is a relative path to the servers defined in the [Servers](/openapi/servers) object, either at the document, path, or operation level. For example, if a server is defined as `https://speakeasy.bar/api` and a path is defined as `/drinks`, the full URL to the path would be `https://speakeasy.bar/api/drinks`, where the path is appended to the server URL.

Example:

```yaml
paths:
  /drinks:
    get: ... # operation definition
  /drink:
    get: ... # operation definition
    put: ... # operation definition
    post: ... # operation definition
    delete: ... # operation definition
```

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `/{path}` | [Path Item Object](/openapi/paths#path-item-object) |  | A relative path to an individual endpoint, where the path **_must_** begin with a `/`. |
| `x-*` | [Extensions](/openapi/extensions) |  | Any number of extension fields can be added to the paths object that can be used by tooling and vendors. |

## Path Item Object in OpenAPI

A Path Item Object describes the operations available on a single path. This is generally a map of HTTP methods to [Operation Objects](/openapi/paths/operations) that describe the operations available.

It is possible to override the [Servers](/openapi/servers) defined at the document level for a specific path by providing a list of [Server Objects](/openapi/servers) at the path level.

It is also possible to provide a list of [Parameters](/openapi/paths/parameters) that are common to all operations defined on the path.

Example:

```yaml
paths:
  /drinks:
    summary: Various operations for browsing and searching drinks
    description:
    servers: # Override the servers defined at the document level and apply to all operations defined on this path
      - url: https://drinks.speakeasy.bar
        description: The drinks server
    parameters: # Define a list of parameters that are common to all operations defined on this path
      - name: type
        in: query
        schema:
          type: string
          enum:
            - cocktail
            - mocktail
            - spirit
            - beer
            - wine
            - cider
    get: ... # operation definition
```

Or:

```yaml
paths:
  /drinks:
    $ref: "#/components/pathItems/drinks" # Reference a Path Item Object defined in the Components Object allowing for reuse in different paths
components:
  pathItems:
    drinks:
      servers:
        - url: https://drinks.speakeasy.bar
          description: The drinks server
      parameters:
        - name: type
          in: query
          schema:
            type: string
            enum:
              - cocktail
              - mocktail
              - spirit
              - beer
              - wine
              - cider
      get: ... # operation definition
```

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `$ref` | String |  | Allows for referencing a [Path Item Object](/openapi/paths#path-item-object) defined in the [Components Object](/openapi/components) under the `pathItems` field. If used, no other fields should be set. |
| `summary` | String |  | A short summary of what the path item represents. This may contain [CommonMark syntax](https://spec.commonmark.org/) to provide a rich description. |
| `description` | String |  | A description of the path item. This may contain [CommonMark syntax](https://spec.commonmark.org/) to provide a rich description. |
| `servers` | [Servers](/openapi/servers) |  | A list of [Server Objects](/openapi/servers) that override the servers defined at the document level. Applies to all operations defined on this path. |
| `parameters` | [Parameters](/openapi/paths/parameters) |  | A list of [Parameter Objects](/openapi/paths/parameters#parameter-object) that are common to all operations defined on this path. |
| `get` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`GET` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET). |
| `put` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`PUT` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT). |
| `post` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`POST` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST). |
| `delete` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`DELETE` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE). |
| `options` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`OPTIONS` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS). |
| `head` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`HEAD` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD). |
| `patch` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`PATCH` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH). |
| `trace` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the [`TRACE` HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/TRACE). |
| `query` | [Operation Object](/openapi/paths/operations) |  | An operation associated with the `QUERY` HTTP method. Safe and idempotent, like `GET`, but allows a request body for complex queries. Available in OpenAPI v3.2.0+. |
| `additionalOperations` | Map[String, [Operation Object](/openapi/paths/operations)] |  | A map of non-standard HTTP methods to Operation Objects, enabling documentation of custom methods beyond those defined by the specification. Available in OpenAPI v3.2.0+. |
| `x-*` | [Extensions](/openapi/extensions) |  | Any number of extension fields can be added to the Path Item Object that can be used by tooling and vendors. |

The order of fields above is recommended but is not significant to the order in which the endpoints should be used.

## OpenAPI 3.2 path features

OpenAPI 3.2.0 introduces several new capabilities for path items.

### The QUERY HTTP method

The `QUERY` method is a safe, idempotent HTTP method that allows clients to send query criteria in the request body rather than encoding complex parameters in the URL. This is useful for operations that require structured or lengthy query parameters that exceed practical URL length limits.

```yaml
paths:
  /drinks:
    query:
      operationId: searchDrinks
      summary: Search for drinks with complex criteria
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                ingredients:
                  type: array
                  items:
                    type: string
                minRating:
                  type: number
      responses:
        "200":
          description: A list of matching drinks
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/Drink"
```

### Additional operations

The `additionalOperations` field allows defining non-standard HTTP methods as Operation Objects. This is useful for APIs that use custom HTTP methods beyond the standard set.

```yaml
paths:
  /drinks/{drinkId}:
    additionalOperations:
      BREW:
        operationId: brewDrink
        summary: Brew a specific drink
        parameters:
          - name: drinkId
            in: path
            required: true
            schema:
              type: string
        responses:
          "200":
            description: Drink brewed successfully
```

### The querystring field

OpenAPI 3.2.0 also introduces the `querystring` field on Operation Objects, which allows defining all query parameters as a single Schema Object instead of listing individual `parameters` with `in: query`. This simplifies the definition of operations with many query parameters or complex query structures.

```yaml
paths:
  /drinks:
    get:
      operationId: listDrinks
      summary: List available drinks
      querystring:
        type: object
        properties:
          type:
            type: string
            enum: [cocktail, mocktail, spirit, beer, wine, cider]
          limit:
            type: integer
            default: 20
          offset:
            type: integer
            default: 0
      responses:
        "200":
          description: A list of drinks
```
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
