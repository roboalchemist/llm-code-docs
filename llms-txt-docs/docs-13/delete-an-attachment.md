# Source: https://docs.solidfi.com/v2/api-reference/attachments/delete-an-attachment.md

# Delete an Attachment

> Delete an Attachment

## OpenAPI

````yaml delete /v2/attachment/{attachment_id}
paths:
  path: /v2/attachment/{attachment_id}
  method: delete
  servers:
    - url: https://api.sandbox.solidfi.com
    - url: https://api.prod.solidfi.com
  request:
    security: []
    parameters:
      path:
        attachment_id:
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
            description: The attachment was deleted successfully.
        examples: {}
        description: The attachment was deleted successfully.
  deprecated: false
  type: path
components:
  schemas: {}

````