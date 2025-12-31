# Source: https://docs.embedchain.ai/examples/rest-api/create.md

# Create app

> Create a new app using App ID

## OpenAPI

````yaml post /create
paths:
  path: /create
  method: post
  request:
    security: []
    parameters:
      path: {}
      query:
        app_id:
          schema:
            - type: string
              required: true
              title: App Id
      header: {}
      cookie: {}
    body:
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              config:
                allOf:
                  - type: string
                    format: binary
                    title: Config
            title: Body_create_app_using_default_config_create_post
            refIdentifier: >-
              #/components/schemas/Body_create_app_using_default_config_create_post
        examples:
          example:
            value: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              response:
                allOf:
                  - type: string
                    title: Response
            title: DefaultResponse
            refIdentifier: '#/components/schemas/DefaultResponse'
            requiredProperties:
              - response
        examples:
          example:
            value:
              response: <string>
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