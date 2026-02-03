# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/sign-intermediate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sign intermediate certificate

> Create intermediate CA certificate from parent CA



## OpenAPI

````yaml POST /api/v1/cert-manager/ca/internal/{caId}/sign-intermediate
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
  /api/v1/cert-manager/ca/internal/{caId}/sign-intermediate:
    post:
      tags:
        - PKI Certificate Authorities
      description: Create intermediate CA certificate from parent CA
      operationId: signIntermediateCa
      parameters:
        - schema:
            type: string
          in: path
          name: caId
          required: true
          description: The ID of the CA to sign the intermediate certificate with.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                csr:
                  type: string
                  minLength: 1
                  description: The pem-encoded CSR to sign with the CA.
                notBefore:
                  type: string
                  description: >-
                    The date and time when the intermediate CA becomes valid in
                    YYYY-MM-DDTHH:mm:ss.sssZ format.
                notAfter:
                  type: string
                  description: >-
                    The date and time when the intermediate CA expires in
                    YYYY-MM-DDTHH:mm:ss.sssZ format.
                maxPathLength:
                  type: number
                  minimum: -1
                  default: -1
                  description: >-
                    The maximum number of intermediate CAs that may follow this
                    CA in the certificate / CA chain. A maxPathLength of -1
                    implies no path limit on the chain.
              required:
                - csr
                - notAfter
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
                  certificate:
                    type: string
                    description: The signed intermediate certificate.
                  certificateChain:
                    type: string
                    description: The certificate chain of the intermediate certificate.
                  issuingCaCertificate:
                    type: string
                    description: The certificate of the issuing CA.
                  serialNumber:
                    type: string
                    description: The serial number of the intermediate certificate.
                required:
                  - certificate
                  - certificateChain
                  - issuingCaCertificate
                  - serialNumber
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