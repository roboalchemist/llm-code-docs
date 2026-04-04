# Source: https://tyk.io/docs/api-reference/filters/get-a-filter-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a filter by ID

> Get a filter's details by its ID



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /filters/{id}
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
  /filters/{id}:
    get:
      tags:
        - filters
      summary: Get a filter by ID
      description: Get a filter's details by its ID
      parameters:
        - name: id
          in: path
          description: Filter ID
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.FilterResponse'
        '404':
          description: Not Found
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
    api.FilterResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            description:
              type: string
            name:
              type: string
            script:
              type: array
              items:
                type: integer
        id:
          type: string
        type:
          type: string
      description: Filter response model
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