# Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-get.md

# Get SIP Registration

> Gets details for the specified registration



## OpenAPI

````yaml get /api/sip/registrations/{registration_id}
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
    get:
      tags:
        - sip
      operationId: sip_registrations_retrieve
      parameters:
        - in: path
          name: registration_id
          schema:
            type: string
          required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SipRegistration'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    SipRegistration:
      type: object
      properties:
        registrationId:
          type: string
          readOnly: true
        created:
          type: string
          format: date-time
          readOnly: true
        username:
          type: string
          description: The SIP username to register as.
          maxLength: 60
        password:
          type: string
          writeOnly: true
          description: The SIP password for username.
        proxy:
          type: string
          description: The SIP server to register with.
          maxLength: 100
        outboundProxy:
          type: string
          nullable: true
          description: >-
            A proxy used to reach your SIP server for registration. Most often
            unset, but may be used if you need to register as `alice@trunk.com`
            using `proxy.trunk.com` for example.
          maxLength: 100
        authUser:
          type: string
          nullable: true
          description: >-
            The authentication username, if different from the SIP username.
            Most often unset.
          maxLength: 60
      required:
        - created
        - password
        - proxy
        - registrationId
        - username
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt