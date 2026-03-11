# Source: https://tyk.io/docs/api-reference/users/create-a-new-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new user

> Create a new user with the provided information

## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml post /users
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
  /users:
    post:
      tags:
        - users
      summary: Create a new user
      description: Create a new user with the provided information
      requestBody:
        description: User information
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/api.UserInput'
        required: true
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.UserResponse'
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
    api.UserInput:
      type: object
      properties:
        data:
          type: object
          properties:
            attributes:
              type: object
              properties:
                email:
                  type: string
                name:
                  type: string
                password:
                  type: string
            type:
              type: string
      description: User input model
    api.UserResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            email:
              type: string
            name:
              type: string
        id:
          type: string
        type:
          type: string
      description: User response model
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
