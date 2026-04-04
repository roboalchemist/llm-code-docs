# Source: https://docs.galileo.ai/api-reference/auth/login-social.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Login Social



## OpenAPI

````yaml https://api.staging.galileo.ai/public/v1/openapi.json post /v1/login/social
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/login/social:
    post:
      tags:
        - auth
      summary: Login Social
      operationId: login_social_v1_login_social_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SocialLoginRequest'
              examples:
                - id_token: token1234
                  provider: google
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
    SocialLoginRequest:
      properties:
        id_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Id Token
        access_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Access Token
        provider:
          $ref: '#/components/schemas/SocialProvider'
      type: object
      required:
        - provider
      title: SocialLoginRequest
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
    SocialProvider:
      type: string
      enum:
        - google
        - github
        - okta
        - azure-ad
        - custom
      title: SocialProvider
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