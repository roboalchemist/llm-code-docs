# Source: https://docs.tavus.io/api-reference/personas/delete-persona.md

# Delete Persona

> This endpoint deletes a single persona by its unique identifier.


## OpenAPI

````yaml delete /v2/personas/{persona_id}
paths:
  path: /v2/personas/{persona_id}
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
        persona_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the persona.
              example: pf3073f2dcc1
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: NO CONTENT
        examples: {}
        description: NO CONTENT
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid persona_id
        examples:
          example:
            value:
              error: Invalid persona_id
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
  deprecated: false
  type: path
components:
  schemas: {}

````