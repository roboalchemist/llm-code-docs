# Source: https://docs.argil.ai/api-reference/endpoint/webhooks.delete.md

# Delete a webhook

> Deletes a single webhook identified by its ID.

## OpenAPI

````yaml delete /webhooks/{id}
paths:
  path: /webhooks/{id}
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
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Successfully deleted webhook
        examples: {}
        description: Successfully deleted webhook
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
        description: Webhook not found
  deprecated: false
  type: path
components:
  schemas: {}

````