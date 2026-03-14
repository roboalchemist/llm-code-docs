# Source: https://tyk.io/docs/api-reference/catalogues/search-catalogues-by-name-stub.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search catalogues by name stub

> Search for catalogues using a name stub



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /catalogues/search-by-stub
openapi: 3.0.1
info:
  title: AI Studio API
  description: This is the API for the AI Studio user and group management system.
  termsOfService: http://swagger.io/terms/
  contact:
    name: API Support
    url: http://www.swagger.io/support
    email: support@tyk.io
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
  version: '1.0'
servers:
  - url: //localhost:8080/api/v1
security:
  - BearerAuth: []
paths:
  /catalogues/search-by-stub:
    get:
      tags:
        - catalogues
      summary: Search catalogues by name stub
      description: Search for catalogues using a name stub
      parameters:
        - name: stub
          in: query
          description: Name stub to search for
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/api.CatalogueResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
      security:
        - BearerAuth: []
components:
  schemas:
    api.CatalogueResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            llm_names:
              type: array
              items:
                type: string
            name:
              type: string
        id:
          type: string
        type:
          type: string
      description: Catalogue response model
    api.ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              detail:
                type: string
              title:
                type: string
      description: Error response model
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).