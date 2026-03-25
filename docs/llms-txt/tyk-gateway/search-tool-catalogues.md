# Source: https://tyk.io/docs/api-reference/tool-catalogues/search-tool-catalogues.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search tool catalogues

> Search for tool catalogues using a query string

## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /tool-catalogues/search
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
  /tool-catalogues/search:
    get:
      tags:
        - tool-catalogues
      summary: Search tool catalogues
      description: Search for tool catalogues using a query string
      parameters:
        - name: query
          in: query
          description: Search query
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
                  $ref: '#/components/schemas/api.ToolCatalogueResponse'
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
components:
  schemas:
    api.ToolCatalogueResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            icon:
              type: string
            long_description:
              type: string
            name:
              type: string
            short_description:
              type: string
            tags:
              type: array
              items:
                $ref: '#/components/schemas/api.TagResponse'
            tools:
              type: array
              items:
                $ref: '#/components/schemas/api.ToolResponse'
        id:
          type: string
        type:
          type: string
      description: Tool Catalogue response model
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
    api.TagResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            name:
              type: string
        id:
          type: string
        type:
          type: string
      description: Tag response model
    api.ToolResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            auth_key:
              type: string
            auth_schema_name:
              type: string
            description:
              type: string
            name:
              type: string
            oas_spec:
              type: array
              items:
                type: integer
            operations:
              type: array
              items:
                type: string
            privacy_score:
              type: integer
            tool_type:
              type: string
        id:
          type: string
        type:
          type: string
      description: Tool response model
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
