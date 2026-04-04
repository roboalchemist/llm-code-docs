# Source: https://tyk.io/docs/api-reference/tools/get-a-tool-by-id.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a tool by ID

> Get details of a tool by its ID

## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /tools/{id}
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
  /tools/{id}:
    get:
      tags:
        - tools
      summary: Get a tool by ID
      description: Get details of a tool by its ID
      parameters:
        - name: id
          in: path
          description: Tool ID
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ToolResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
      security:
        - BearerAuth: []
components:
  schemas:
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
