# Source: https://docs.ultravox.ai/api-reference/other/models-get.md

# List Models

> Retrieves the list of all available models that can be used for inference



## OpenAPI

````yaml get /api/models
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/models:
    get:
      tags:
        - models
      operationId: models_list
      parameters:
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedModelAliasList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedModelAliasList:
      type: object
      required:
        - results
      properties:
        next:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cD00ODY%3D"
        previous:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3
        results:
          type: array
          items:
            $ref: '#/components/schemas/ModelAlias'
        total:
          type: integer
          example: 123
    ModelAlias:
      type: object
      properties:
        name:
          type: string
          readOnly: true
          description: The alias name.
      required:
        - name
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt