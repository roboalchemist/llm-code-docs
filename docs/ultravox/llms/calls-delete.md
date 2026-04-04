# Source: https://docs.ultravox.ai/api-reference/calls/calls-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Call

> Deletes the specified call

Also deletes all associated messages, recordings, and stages.


## OpenAPI

````yaml delete /api/calls/{call_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}:
    delete:
      tags:
        - calls
      operationId: calls_destroy
      parameters:
        - in: path
          name: call_id
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