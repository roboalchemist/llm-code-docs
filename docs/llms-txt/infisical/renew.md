# Source: https://infisical.com/docs/api-reference/endpoints/certificates/renew.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/renew.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Renew

> Perform CA certificate renewal



## OpenAPI

````yaml POST /api/v1/cert-manager/ca/internal/{caId}/renew
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
  /api/v1/cert-manager/ca/internal/{caId}/renew:
    post:
      tags:
        - PKI Certificate Authorities
      description: Perform CA certificate renewal
      operationId: renewCaCertificate
      parameters:
        - schema:
            type: string
          in: path
          name: caId
          required: true
          description: The ID of the CA to renew the CA certificate for.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                type:
                  type: string
                  enum:
                    - existing
                  description: >-
                    The type of behavior to use for the renewal operation.
                    Currently Infisical is only able to renew a CA certificate
                    with the same key pair.
                notAfter:
                  type: string
                  description: >-
                    The expiry date and time for the renewed CA certificate in
                    YYYY-MM-DDTHH:mm:ss.sssZ format.
              required:
                - type
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
                    description: The renewed CA certificate body.
                  certificateChain:
                    type: string
                    description: The certificate chain of the CA.
                  serialNumber:
                    type: string
                    description: The serial number of the renewed CA certificate.
                  certId:
                    type: string
                    description: Certificate ID
                required:
                  - certificate
                  - certificateChain
                  - serialNumber
                  - certId
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