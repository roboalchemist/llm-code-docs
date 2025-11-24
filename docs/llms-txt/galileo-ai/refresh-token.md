# Source: https://docs.galileo.ai/api-reference/auth/refresh-token.md

# Refresh Token

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json post /v1/refresh_token
paths:
  path: /v1/refresh_token
  method: post
  servers:
    - url: https://api.acme.rungalileo.io
      description: Galileo Public APIs - acme
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie:
        refresh_token:
          schema:
            - type: string
              required: true
              title: Refresh Token
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
            title: Token
            refIdentifier: '#/components/schemas/Token'
            requiredProperties:
              - access_token
        examples:
          example:
            value:
              access_token: <string>
              token_type: bearer
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