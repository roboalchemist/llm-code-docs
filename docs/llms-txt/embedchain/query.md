# Source: https://docs.embedchain.ai/examples/rest-api/query.md

# Source: https://docs.embedchain.ai/api-reference/app/query.md

# Source: https://docs.embedchain.ai/examples/rest-api/query.md

# Source: https://docs.embedchain.ai/api-reference/app/query.md

# Source: https://docs.embedchain.ai/examples/rest-api/query.md

# Query app

> Query an app

## OpenAPI

````yaml post /{app_id}/query
paths:
  path: /{app_id}/query
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
              query:
                allOf:
                  - type: string
                    title: Query
                    description: The query that you want to ask the App.
                    default: ''
            required: true
            title: QueryApp
            refIdentifier: '#/components/schemas/QueryApp'
            example:
              query: Who is Elon Musk?
        examples:
          example:
            value:
              query: Who is Elon Musk?
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