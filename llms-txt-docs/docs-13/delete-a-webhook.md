# Source: https://docs.solidfi.com/v2/api-reference/webhooks/delete-a-webhook.md

# Delete a Webhook

> Delete a Webhook

## OpenAPI

````yaml delete /v2/webhook/{webhook_id}
paths:
  path: /v2/webhook/{webhook_id}
  method: delete
  servers:
    - url: https://api.sandbox.solidfi.com
    - url: https://api.prod.solidfi.com
  request:
    security: []
    parameters:
      path:
        webhook_id:
          schema:
            - type: string
              required: true
      query: {}
      header:
        api-key:
          schema:
            - type: string
              required: true
              description: >-
                API key is required to call Solid APIs. You can view and manage
                your API keys in the Solid dashboard.
              example: '{{api_key}}'
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The webhook was deleted successfully.
        examples: {}
        description: The webhook was deleted successfully.
  deprecated: false
  type: path
components:
  schemas: {}

````