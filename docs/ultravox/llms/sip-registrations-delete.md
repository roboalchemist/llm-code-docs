# Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete SIP Registration

> Deletes the specified registration



## OpenAPI

````yaml delete /api/sip/registrations/{registration_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/sip/registrations/{registration_id}:
    delete:
      tags:
        - sip
      operationId: sip_registrations_destroy
      parameters:
        - in: path
          name: registration_id
          schema:
            type: string
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