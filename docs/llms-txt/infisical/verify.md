# Source: https://infisical.com/docs/api-reference/endpoints/kms/signing/verify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify Signature

> Verify data signatures with a KMS key.



## OpenAPI

````yaml POST /api/v1/kms/keys/{keyId}/verify
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/kms/keys/{keyId}/verify:
    post:
      tags:
        - KMS Signing
      description: Verify data signatures with a KMS key.
      operationId: verifyWithKmsKey
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: keyId
          required: true
          description: The ID of the key to verify the data with.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                isDigest:
                  type: boolean
                  default: false
                  description: Whether the data is already digested or not.
                data:
                  type: string
                  description: >-
                    The data in string format to be verified (base64 encoded).
                    For data larger than 4096 bytes you must first create a
                    digest of the data and then pass the digest in the data
                    parameter.
                signature:
                  type: string
                  description: The signature to be verified (base64 encoded).
                signingAlgorithm:
                  type: string
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
              required:
                - data
                - signature
                - signingAlgorithm
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  signatureValid:
                    type: boolean
                  keyId:
                    type: string
                    format: uuid
                  signingAlgorithm:
                    type: string
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
                required:
                  - signatureValid
                  - keyId
                  - signingAlgorithm
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false

````