# Source: https://docs.embedchain.ai/examples/rest-api/delete.md

# Source: https://docs.embedchain.ai/api-reference/app/delete.md

# Source: https://docs.embedchain.ai/examples/rest-api/delete.md

# Delete app

> Delete an existing app

## OpenAPI

````yaml delete /{app_id}/delete
paths:
  path: /{app_id}/delete
  method: delete
  request:
    security: []
    parameters:
      path:
        app_id:
          schema:
            - type: string
              required: true
              title: App Id
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