# Source: https://docs.comfy.org/api-reference/registry/get-information-about-the-calling-user.md

# Get information about the calling user.

## OpenAPI

````yaml https://api.comfy.org/openapi get /users
paths:
  path: /users
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
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
              email:
                allOf:
                  - description: The email address for this user.
                    type: string
              id:
                allOf:
                  - description: The unique id for this user.
                    type: string
              isAdmin:
                allOf:
                  - description: Indicates if the user has admin privileges.
                    type: boolean
              isApproved:
                allOf:
                  - description: Indicates if the user is approved.
                    type: boolean
              name:
                allOf:
                  - description: The name for this user.
                    type: string
            refIdentifier: '#/components/schemas/User'
        examples:
          example:
            value:
              email: <string>
              id: <string>
              isAdmin: true
              isApproved: true
              name: <string>
        description: OK
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Not Found
        examples: {}
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````