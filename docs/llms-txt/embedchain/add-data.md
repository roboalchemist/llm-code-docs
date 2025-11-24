# Source: https://docs.embedchain.ai/examples/rest-api/add-data.md

# Add data

> Add a data source to an app.

## OpenAPI

````yaml post /{app_id}/add
paths:
  path: /{app_id}/add
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              source:
                allOf:
                  - type: string
                    title: Source
                    description: The source that you want to add to the App.
                    default: ''
              data_type:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Data Type
                    description: >-
                      The type of data to add, remove it if you want Embedchain
                      to detect it automatically.
                    default: ''
            required: true
            title: SourceApp
            refIdentifier: '#/components/schemas/SourceApp'
            example:
              source: https://en.wikipedia.org/wiki/Elon_Musk
        examples:
          example:
            value:
              source: https://en.wikipedia.org/wiki/Elon_Musk
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