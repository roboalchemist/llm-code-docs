# Source: https://docs.ultravox.ai/api-reference/calls/calls-sip-logs-get.md

# Get Sip Logs for a call

> Redirects to the SIP logs for a call, if available. This is only available for calls with sip medium and only after the call has ended.



## OpenAPI

````yaml get /api/calls/{call_id}/sip_logs
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/sip_logs:
    get:
      tags:
        - calls
      description: Redirects to sip logs for the call, if available.
      operationId: calls_sip_logs_retrieve
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '302':
          description: No response body
        '404':
          description: No response body
        '425':
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