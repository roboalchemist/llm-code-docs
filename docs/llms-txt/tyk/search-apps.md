# Source: https://tyk.io/docs/api-reference/apps/search-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search apps

> Search for apps based on a search term



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /apps/search
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
  /apps/search:
    get:
      tags:
        - apps
      summary: Search apps
      description: Search for apps based on a search term
      parameters:
        - name: searchTerm
          in: query
          description: Search term
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
                  $ref: '#/components/schemas/api.AppResponse'
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
    api.AppResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            credential_id:
              type: integer
            datasource_ids:
              type: array
              items:
                type: integer
            description:
              type: string
            llm_ids:
              type: array
              items:
                type: integer
            name:
              type: string
            user_id:
              type: integer
        id:
          type: string
        type:
          type: string
      description: App response model
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