# Source: https://tyk.io/docs/api-reference/datasources/search-datasources.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search datasources

> Search for datasources using a query string

## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /datasources/search
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
  /datasources/search:
    get:
      tags:
        - datasources
      summary: Search datasources
      description: Search for datasources using a query string
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
                  $ref: '#/components/schemas/api.DatasourceResponse'
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
    api.DatasourceResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            active:
              type: boolean
            db_conn_api_key:
              type: string
            db_conn_string:
              type: string
            db_name:
              type: string
            db_source_type:
              type: string
            embed_api_key:
              type: string
            embed_model:
              type: string
            embed_url:
              type: string
            embed_vendor:
              type: string
            icon:
              type: string
            long_description:
              type: string
            name:
              type: string
            privacy_score:
              type: integer
            short_description:
              type: string
            tags:
              type: array
              items:
                $ref: '#/components/schemas/api.TagResponse'
            url:
              type: string
            user_id:
              type: integer
        id:
          type: string
        type:
          type: string
      description: Datasource response model
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
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
