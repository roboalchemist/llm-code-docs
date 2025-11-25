# Source: https://infisical.com/docs/api-reference/endpoints/certificates/renew.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/renew.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificates/renew.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/renew.md

# Renew

> Perform CA certificate renewal

## OpenAPI

````yaml POST /api/v1/pki/ca/{caId}/renew
paths:
  path: /api/v1/pki/ca/{caId}/renew
  method: post
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
    parameters:
      path:
        caId:
          schema:
            - type: string
              required: true
              description: The ID of the CA to renew the CA certificate for.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - existing
                    description: >-
                      The type of behavior to use for the renewal operation.
                      Currently Infisical is only able to renew a CA certificate
                      with the same key pair.
              notAfter:
                allOf:
                  - type: string
                    description: >-
                      The expiry date and time for the renewed CA certificate in
                      YYYY-MM-DDTHH:mm:ss.sssZ format.
            required: true
            requiredProperties:
              - type
              - notAfter
            additionalProperties: false
        examples:
          example:
            value:
              type: existing
              notAfter: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              certificate:
                allOf:
                  - type: string
                    description: The renewed CA certificate body.
              certificateChain:
                allOf:
                  - type: string
                    description: The certificate chain of the CA.
              serialNumber:
                allOf:
                  - type: string
                    description: The serial number of the renewed CA certificate.
            requiredProperties:
              - certificate
              - certificateChain
              - serialNumber
            additionalProperties: false
        examples:
          example:
            value:
              certificate: <string>
              certificateChain: <string>
              serialNumber: <string>
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````