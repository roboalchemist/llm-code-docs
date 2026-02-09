# Source: https://infisical.com/docs/api-reference/endpoints/kms/signing/signing-algorithms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Signing Algorithms

> List all available signing algorithms for a KMS key



## OpenAPI

````yaml GET /api/v1/kms/keys/{keyId}/signing-algorithms
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
  /api/v1/kms/keys/{keyId}/signing-algorithms:
    get:
      tags:
        - KMS Signing
      description: List all available signing algorithms for a KMS key
      operationId: listKmsKeySigningAlgorithms
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: keyId
          required: true
          description: >-
            The ID of the key to list the signing algorithms for. The key must
            be for signing and verifying.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  signingAlgorithms:
                    type: array
                    items:
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
                  - signingAlgorithms
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