# Source: https://docs.tavus.io/api-reference/guardrails/delete-guardrails.md

# Delete Guardrails

> This endpoint deletes a single set of guardrails by its unique identifier.


## OpenAPI

````yaml delete /v2/guardrails/{guardrails_id}
paths:
  path: /v2/guardrails/{guardrails_id}
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
        guardrails_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the guardrails.
              example: g12345
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: NO CONTENT - Guardrails deleted successfully
        examples: {}
        description: NO CONTENT - Guardrails deleted successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid guardrails_id
        examples:
          example:
            value:
              error: Invalid guardrails_id
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
                    example: Guardrails not found
        examples:
          example:
            value:
              error: Guardrails not found
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````