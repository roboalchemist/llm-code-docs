# Source: https://infisical.com/docs/api-reference/endpoints/ssh/certificates/sign-key.md

# Sign SSH Public Key

> Sign SSH public key

## OpenAPI

````yaml POST /api/v1/ssh/certificates/sign
paths:
  path: /api/v1/ssh/certificates/sign
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              certificateTemplateId:
                allOf:
                  - type: string
                    minLength: 1
                    description: >-
                      The ID of the SSH certificate template to sign the SSH
                      public key with.
              publicKey:
                allOf:
                  - type: string
                    description: The SSH public key to sign.
              certType:
                allOf:
                  - type: string
                    enum:
                      - user
                      - host
                    default: user
                    description: >-
                      The type of certificate to issue. This can be one of user
                      or host.
              principals:
                allOf:
                  - type: array
                    items:
                      type: string
                    minItems: 1
                    description: >-
                      The list of principals (usernames, hostnames) to include
                      in the certificate.
              ttl:
                allOf:
                  - type: string
                    description: >-
                      The time to live for the certificate such as 1m, 1h, 1d,
                      ... If not specified, the default TTL for the template
                      will be used.
              keyId:
                allOf:
                  - type: string
                    maxLength: 50
                    description: >-
                      The key ID to include in the certificate. If not
                      specified, a default key ID will be generated.
            required: true
            requiredProperties:
              - certificateTemplateId
              - publicKey
              - principals
            additionalProperties: false
        examples:
          example:
            value:
              certificateTemplateId: <string>
              publicKey: <string>
              certType: user
              principals:
                - <string>
              ttl: <string>
              keyId: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              serialNumber:
                allOf:
                  - type: string
                    description: The serial number of the issued SSH certificate.
              signedKey:
                allOf:
                  - type: string
                    description: The SSH certificate or signed SSH public key.
            requiredProperties:
              - serialNumber
              - signedKey
            additionalProperties: false
        examples:
          example:
            value:
              serialNumber: <string>
              signedKey: <string>
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