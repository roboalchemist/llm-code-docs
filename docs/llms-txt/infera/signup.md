# Source: https://docs.infera.org/api-reference/endpoint/signup.md

# Signup

## OpenAPI

````yaml post /signup_user
paths:
  path: /signup_user
  method: post
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              email:
                allOf:
                  - type: string
                    format: email
                    title: Email
            required: true
            title: SignupRequest
            refIdentifier: '#/components/schemas/SignupRequest'
            requiredProperties:
              - email
        examples:
          example:
            value:
              email: jsmith@example.com
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
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