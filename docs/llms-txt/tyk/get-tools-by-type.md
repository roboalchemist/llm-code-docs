# Source: https://tyk.io/docs/api-reference/tools/get-tools-by-type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get tools by type

> Get a list of tools of a specific type



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /tools/by-type
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
  /tools/by-type:
    get:
      tags:
        - tools
      summary: Get tools by type
      description: Get a list of tools of a specific type
      parameters:
        - name: type
          in: query
          description: Tool Type
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
                  $ref: '#/components/schemas/api.ToolResponse'
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