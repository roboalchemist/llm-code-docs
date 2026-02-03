# Source: https://docs.ultravox.ai/api-reference/sip/sip-registrations-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List SIP Registrations

> Lists SIP registrations for your account



## OpenAPI

````yaml get /api/sip/registrations
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/sip/registrations:
    get:
      tags:
        - sip
      operationId: sip_registrations_list
      parameters:
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedSipRegistrationList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedSipRegistrationList:
      type: object
      required:
        - results
      properties:
        next:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cD00ODY%3D"
        previous:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3
        results:
          type: array
          items:
            $ref: '#/components/schemas/SipRegistration'
        total:
          type: integer
          example: 123
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