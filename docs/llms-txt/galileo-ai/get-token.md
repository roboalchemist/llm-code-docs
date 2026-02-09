# Source: https://docs.galileo.ai/api-reference/auth/get-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Token



## OpenAPI

````yaml https://api.staging.galileo.ai/public/v1/openapi.json get /v1/token
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/token:
    get:
      tags:
        - auth
      summary: Get Token
      operationId: get_token_v1_token_get
      parameters:
        - name: organization_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: uuid4
              - type: 'null'
            title: Organization Id
        - name: organization_slug
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Organization Slug
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTokenResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - APIKeyHeader: []
        - OAuth2PasswordBearer: []
        - HTTPBasic: []
components:
  schemas:
    GetTokenResponse:
      properties:
        access_token:
          type: string
          title: Access Token
        token_type:
          type: string
          title: Token Type
          default: bearer
        expires_at:
          type: string
          format: date-time
          title: Expires At
      type: object
      required:
        - access_token
        - expires_at
      title: GetTokenResponse
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
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: Galileo-API-Key
    OAuth2PasswordBearer:
      type: oauth2
      flows:
        password:
          scopes: {}
          tokenUrl: https://api.staging.galileo.ai/login
    HTTPBasic:
      type: http
      scheme: basic

````