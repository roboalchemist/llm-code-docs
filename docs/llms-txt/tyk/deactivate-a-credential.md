# Source: https://tyk.io/docs/api-reference/credentials/deactivate-a-credential.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deactivate a credential

> Deactivate a credential by its ID



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml post /credentials/{id}/deactivate
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
  /credentials/{id}/deactivate:
    post:
      tags:
        - credentials
      summary: Deactivate a credential
      description: Deactivate a credential by its ID
      parameters:
        - name: id
          in: path
          description: Credential ID
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.CredentialResponse'
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
    api.CredentialResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            active:
              type: boolean
            key_id:
              type: string
            secret:
              type: string
        id:
          type: string
        type:
          type: string
      description: Credential response model
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