# Source: https://infisical.com/docs/api-reference/endpoints/kms/signing/verify.md

# Verify Signature

> Verify data signatures with a KMS key.

## OpenAPI

````yaml POST /api/v1/kms/keys/{keyId}/verify
paths:
  path: /api/v1/kms/keys/{keyId}/verify
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
              description: The ID of the key to verify the data with.
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              isDigest:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether the data is already digested or not.
              data:
                allOf:
                  - type: string
                    description: >-
                      The data in string format to be verified (base64 encoded).
                      For data larger than 4096 bytes you must first create a
                      digest of the data and then pass the digest in the data
                      parameter.
              signature:
                allOf:
                  - type: string
                    description: The signature to be verified (base64 encoded).
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
            required: true
            requiredProperties:
              - data
              - signature
              - signingAlgorithm
            additionalProperties: false
        examples:
          example:
            value:
              isDigest: false
              data: <string>
              signature: <string>
              signingAlgorithm: RSASSA_PSS_SHA_512
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              signatureValid:
                allOf:
                  - type: boolean
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
              - signatureValid
              - keyId
              - signingAlgorithm
            additionalProperties: false
        examples:
          example:
            value:
              signatureValid: true
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