# Source: https://docs.comfy.org/api-reference/registry/validate-if-a-publisher-username-is-available.md

# Validate if a publisher username is available

> Checks if the publisher username is already taken.

## OpenAPI

````yaml https://api.comfy.org/openapi get /publishers/validate
paths:
  path: /publishers/validate
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path: {}
      query:
        username:
          schema:
            - type: string
              required: true
              description: The publisher username to validate.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              isAvailable:
                allOf:
                  - description: True if the username is available, false otherwise.
                    type: boolean
        examples:
          example:
            value:
              isAvailable: true
        description: Username validation result
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
              message:
                allOf:
                  - &ref_1
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_2
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Invalid input, such as missing username in the query.
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas: {}

````