# Source: https://docs.ultravox.ai/api-reference/tools/tools-delete.md

# Delete Tool

> Deletes the specified tool



## OpenAPI

````yaml delete /api/tools/{tool_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/tools/{tool_id}:
    delete:
      tags:
        - tools
      operationId: tools_destroy
      parameters:
        - in: path
          name: tool_id
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