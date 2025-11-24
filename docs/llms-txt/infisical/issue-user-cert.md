# Source: https://infisical.com/docs/api-reference/endpoints/ssh/hosts/issue-user-cert.md

# Issue User Certificate

> Issue SSH certificate for user

## OpenAPI

````yaml POST /api/v1/ssh/hosts/{sshHostId}/issue-user-cert
paths:
  path: /api/v1/ssh/hosts/{sshHostId}/issue-user-cert
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
        sshHostId:
          schema:
            - type: string
              required: true
              description: The ID of the SSH host to issue the SSH credentials for.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              loginUser:
                allOf:
                  - type: string
                    description: The login user to issue the SSH credentials for.
            required: true
            requiredProperties:
              - loginUser
            additionalProperties: false
        examples:
          example:
            value:
              loginUser: <string>
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
              privateKey:
                allOf:
                  - type: string
                    description: >-
                      The private key corresponding to the issued SSH
                      certificate.
              publicKey:
                allOf:
                  - type: string
                    description: The public key of the issued SSH certificate.
              keyAlgorithm:
                allOf:
                  - type: string
                    enum:
                      - RSA_2048
                      - RSA_4096
                      - EC_prime256v1
                      - EC_secp384r1
                      - ED25519
                    description: >-
                      The type of public key algorithm and size, in bits, of the
                      key pair for the SSH host.
            requiredProperties:
              - serialNumber
              - signedKey
              - privateKey
              - publicKey
              - keyAlgorithm
            additionalProperties: false
        examples:
          example:
            value:
              serialNumber: <string>
              signedKey: <string>
              privateKey: <string>
              publicKey: <string>
              keyAlgorithm: RSA_2048
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