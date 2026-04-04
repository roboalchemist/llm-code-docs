# Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Webhook

> Deletes the specified webhook configuration



## OpenAPI

````yaml delete /api/webhooks/{webhook_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/webhooks/{webhook_id}:
    delete:
      tags:
        - webhooks
      operationId: webhooks_destroy
      parameters:
        - in: path
          name: webhook_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '204':
          description: No response body
      security:
        - apiKeyAuth: []
components:
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````