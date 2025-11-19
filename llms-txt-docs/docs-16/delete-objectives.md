# Source: https://docs.tavus.io/api-reference/objectives/delete-objectives.md

# Delete Objective

> This endpoint deletes a single objective by its unique identifier.


## OpenAPI

````yaml delete /v2/objectives/{objectives_id}
paths:
  path: /v2/objectives/{objectives_id}
  method: delete
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path:
        objectives_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the objective.
              example: o12345
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: NO CONTENT - Objective deleted successfully
        examples: {}
        description: NO CONTENT - Objective deleted successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid objectives_id
        examples:
          example:
            value:
              error: Invalid objectives_id
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Objective not found
        examples:
          example:
            value:
              error: Objective not found
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````