# Source: https://docs.galileo.ai/api-reference/auth/login-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Login Email



## OpenAPI

````yaml https://api.staging.galileo.ai/public/v1/openapi.json post /v1/login
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/login:
    post:
      tags:
        - auth
      summary: Login Email
      operationId: login_email_v1_login_post
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Body_login_email_v1_login_post'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Token'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_login_email_v1_login_post:
      properties:
        grant_type:
          anyOf:
            - type: string
              pattern: ^password$
            - type: 'null'
          title: Grant Type
        username:
          type: string
          title: Username
        password:
          type: string
          format: password
          title: Password
        scope:
          type: string
          title: Scope
          default: ''
        client_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Client Id
        client_secret:
          anyOf:
            - type: string
            - type: 'null'
          format: password
          title: Client Secret
      type: object
      required:
        - username
        - password
      title: Body_login_email_v1_login_post
    Token:
      properties:
        access_token:
          type: string
          title: Access Token
        token_type:
          type: string
          title: Token Type
          default: bearer
      type: object
      required:
        - access_token
      title: Token
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````