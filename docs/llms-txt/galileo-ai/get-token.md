# Source: https://docs.galileo.ai/api-reference/auth/get-token.md

# Get Token

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json get /v1/token
paths:
  path: /v1/token
  method: get
  servers:
    - url: https://api.acme.rungalileo.io
      description: Galileo Public APIs - acme
  request:
    security:
      - title: APIKeyHeader
        parameters:
          query: {}
          header:
            Galileo-API-Key:
              type: apiKey
          cookie: {}
      - title: OAuth2PasswordBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: oauth2
          cookie: {}
      - title: HTTPBasic
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path: {}
      query:
        organization_id:
          schema:
            - type: string
              required: false
              title: Organization Id
              format: uuid4
            - type: 'null'
              required: false
              title: Organization Id
        organization_slug:
          schema:
            - type: string
              required: false
              title: Organization Slug
            - type: 'null'
              required: false
              title: Organization Slug
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              access_token:
                allOf:
                  - type: string
                    title: Access Token
              token_type:
                allOf:
                  - type: string
                    title: Token Type
                    default: bearer
              expires_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Expires At
            title: GetTokenResponse
            refIdentifier: '#/components/schemas/GetTokenResponse'
            requiredProperties:
              - access_token
              - expires_at
        examples:
          example:
            value:
              access_token: <string>
              token_type: bearer
              expires_at: '2023-11-07T05:31:56Z'
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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