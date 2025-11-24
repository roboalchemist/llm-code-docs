# Source: https://docs.galileo.ai/api-reference/auth/login-email.md

# Login Email

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json post /v1/login
paths:
  path: /v1/login
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
      cookie: {}
    body:
      application/x-www-form-urlencoded:
        schemaArray:
          - type: object
            properties:
              grant_type:
                allOf:
                  - anyOf:
                      - type: string
                        pattern: ^password$
                      - type: 'null'
                    title: Grant Type
              username:
                allOf:
                  - type: string
                    title: Username
              password:
                allOf:
                  - type: string
                    format: password
                    title: Password
              scope:
                allOf:
                  - type: string
                    title: Scope
                    default: ''
              client_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Client Id
              client_secret:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    format: password
                    title: Client Secret
            required: true
            title: Body_login_email_v1_login_post
            refIdentifier: '#/components/schemas/Body_login_email_v1_login_post'
            requiredProperties:
              - username
              - password
        examples:
          example:
            value:
              grant_type: <string>
              username: <string>
              password: <string>
              scope: ''
              client_id: <string>
              client_secret: <string>
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