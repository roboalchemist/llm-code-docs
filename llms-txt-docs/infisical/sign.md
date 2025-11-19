# Source: https://infisical.com/docs/api-reference/endpoints/kms/signing/sign.md

# Sign Data

> Sign data with a KMS key.

## OpenAPI

````yaml POST /api/v1/kms/keys/{keyId}/sign
paths:
  path: /api/v1/kms/keys/{keyId}/sign
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
        keyId:
          schema:
            - type: string
              required: true
              description: The ID of the key to sign the data with.
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              signingAlgorithm:
                allOf:
                  - type: string
                    enum:
                      - RSASSA_PSS_SHA_512
                      - RSASSA_PSS_SHA_384
                      - RSASSA_PSS_SHA_256
                      - RSASSA_PKCS1_V1_5_SHA_512
                      - RSASSA_PKCS1_V1_5_SHA_384
                      - RSASSA_PKCS1_V1_5_SHA_256
                      - ECDSA_SHA_512
                      - ECDSA_SHA_384
                      - ECDSA_SHA_256
              isDigest:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      Whether the data is already digested or not. Please be
                      aware that if you are passing a digest the algorithm used
                      to create the digest must match the signing algorithm used
                      to sign the digest.
              data:
                allOf:
                  - type: string
                    description: The data in string format to be signed (base64 encoded).
            required: true
            requiredProperties:
              - signingAlgorithm
              - data
            additionalProperties: false
        examples:
          example:
            value:
              signingAlgorithm: RSASSA_PSS_SHA_512
              isDigest: false
              data: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              signature:
                allOf:
                  - type: string
              keyId:
                allOf:
                  - type: string
                    format: uuid
              signingAlgorithm:
                allOf:
                  - type: string
                    enum:
                      - RSASSA_PSS_SHA_512
                      - RSASSA_PSS_SHA_384
                      - RSASSA_PSS_SHA_256
                      - RSASSA_PKCS1_V1_5_SHA_512
                      - RSASSA_PKCS1_V1_5_SHA_384
                      - RSASSA_PKCS1_V1_5_SHA_256
                      - ECDSA_SHA_512
                      - ECDSA_SHA_384
                      - ECDSA_SHA_256
            requiredProperties:
              - signature
              - keyId
              - signingAlgorithm
            additionalProperties: false
        examples:
          example:
            value:
              signature: <string>
              keyId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              signingAlgorithm: RSASSA_PSS_SHA_512
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