# Source: https://docs.argil.ai/api-reference/endpoint/videos.delete.md

# Delete a Video by id

> Delete a single Video identified by its id

## OpenAPI

````yaml delete /videos/{id}
paths:
  path: /videos/{id}
  method: delete
  servers:
    - url: https://api.argil.ai/v1
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: API key to be included in the x-api-key header
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The id of the Video to delete
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
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Success'
        examples:
          example:
            value:
              message: <string>
        description: Success message.
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: integer
                    format: int32
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Video not found
  deprecated: false
  type: path
components:
  schemas: {}

````