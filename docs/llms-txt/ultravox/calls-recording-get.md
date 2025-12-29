# Source: https://docs.ultravox.ai/api-reference/calls/calls-recording-get.md

# Get Call Recording

> Returns a link to the recording of the call



## OpenAPI

````yaml get /api/calls/{call_id}/recording
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/recording:
    get:
      tags:
        - calls
      description: Returns or redirects to a recording of the call.
      operationId: calls_recording_retrieve
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '200':
          content:
            audio/wav:
              schema:
                type: string
                format: binary
          description: ''
        '302':
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