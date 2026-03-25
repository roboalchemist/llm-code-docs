# Source: https://tyk.io/docs/api-reference/groups/add-a-tool-catalogue-to-a-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a tool catalogue to a group

> Add a tool catalogue to a specific group



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml post /groups/{id}/tool-catalogues
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
  /groups/{id}/tool-catalogues:
    post:
      tags:
        - groups
      summary: Add a tool catalogue to a group
      description: Add a tool catalogue to a specific group
      parameters:
        - name: id
          in: path
          description: Group ID
          required: true
          schema:
            type: integer
      requestBody:
        description: Tool Catalogue to add
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/api.GroupToolCatalogueInput'
        required: true
      responses:
        '204':
          description: No Content
          content: {}
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
    api.GroupToolCatalogueInput:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
            type:
              type: string
      description: Group-ToolCatalogue relationship input model
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