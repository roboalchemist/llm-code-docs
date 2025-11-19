# Source: https://docs.turso.tech/api-reference/tokens/validate.md

# Validate API Token

> Validates an API token belonging to a user.

## OpenAPI

````yaml GET /v1/auth/validate
paths:
  path: /v1/auth/validate
  method: get
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              exp:
                allOf:
                  - type: integer
                    description: >-
                      The time of expiration for the provided token in unix
                      epoch seconds, or `-1` if there is no expiration.
                    example: 999
        examples:
          example:
            value:
              exp: 999
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````