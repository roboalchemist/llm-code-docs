# Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-delete.md

# Delete Scheduled Call Batch

> Deletes a scheduled call batch



## OpenAPI

````yaml delete /api/agents/{agent_id}/scheduled_batches/{batch_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/agents/{agent_id}/scheduled_batches/{batch_id}:
    delete:
      tags:
        - agents
      operationId: agents_scheduled_batches_destroy
      parameters:
        - in: path
          name: agent_id
          schema:
            type: string
            format: uuid
          required: true
        - in: path
          name: batch_id
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt