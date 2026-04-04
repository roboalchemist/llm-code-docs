# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/list-ca-certs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List CA certificates

> Get list of past and current CA certificates for a CA



## OpenAPI

````yaml GET /api/v1/cert-manager/ca/internal/{caId}/ca-certificates
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
  /api/v1/cert-manager/ca/internal/{caId}/ca-certificates:
    get:
      tags:
        - PKI Certificate Authorities
      description: Get list of past and current CA certificates for a CA
      operationId: getCaCertificates
      parameters:
        - schema:
            type: string
          in: path
          name: caId
          required: true
          description: The ID of the CA to get the CA certificates for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    certificate:
                      type: string
                      description: The certificate body of the CA certificate.
                    certificateChain:
                      type: string
                      description: The certificate chain of the CA certificate.
                    serialNumber:
                      type: string
                      description: The serial number of the CA certificate.
                    certId:
                      type: string
                      description: Certificate ID
                    version:
                      type: number
                      description: >-
                        The version of the CA certificate. The version is
                        incremented for each CA renewal operation.
                  required:
                    - certificate
                    - certificateChain
                    - serialNumber
                    - certId
                    - version
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