# Source: https://infisical.com/docs/api-reference/endpoints/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki-alerts/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/acme/read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Read



## OpenAPI

````yaml GET /api/v1/cert-manager/ca/acme/{id}
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
  /api/v1/cert-manager/ca/acme/{id}:
    get:
      tags:
        - PKI Certificate Authorities
      operationId: getAcmeCertificateAuthorityV1
      parameters:
        - schema:
            type: string
          in: path
          name: id
          required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  projectId:
                    type: string
                  enableDirectIssuance:
                    type: boolean
                    default: true
                  name:
                    type: string
                  id:
                    type: string
                    format: uuid
                  status:
                    type: string
                    enum:
                      - active
                      - disabled
                      - pending-certificate
                  type:
                    type: string
                    enum:
                      - acme
                  configuration:
                    type: object
                    properties:
                      dnsAppConnectionId:
                        type: string
                        format: uuid
                        description: >-
                          The ID of the App Connection to use for creating and
                          managing DNS TXT records required for ACME domain
                          validation. This connection must have permissions to
                          create and delete TXT records in your DNS provider
                          (e.g., Route53) for the ACME challenge process.
                      dnsProviderConfig:
                        type: object
                        properties:
                          provider:
                            type: string
                            enum:
                              - route53
                              - cloudflare
                              - dns-made-easy
                            description: >-
                              The DNS provider for the ACME Certificate
                              Authority.
                          hostedZoneId:
                            type: string
                            minLength: 1
                            description: >-
                              The hosted zone ID for the ACME Certificate
                              Authority.
                        required:
                          - provider
                          - hostedZoneId
                        additionalProperties: false
                      directoryUrl:
                        type: string
                        format: uri
                        minLength: 1
                        description: The directory URL for the ACME Certificate Authority.
                      accountEmail:
                        type: string
                        minLength: 1
                        description: The email address for the ACME Certificate Authority.
                      eabKid:
                        type: string
                        maxLength: 64
                        description: >-
                          The External Account Binding (EAB) Key ID for the ACME
                          Certificate Authority. Required if the ACME provider
                          uses EAB.
                      eabHmacKey:
                        type: string
                        maxLength: 512
                        description: >-
                          The External Account Binding (EAB) HMAC key for the
                          ACME Certificate Authority. Required if the ACME
                          provider uses EAB.
                    required:
                      - dnsAppConnectionId
                      - dnsProviderConfig
                      - directoryUrl
                      - accountEmail
                    additionalProperties: false
                required:
                  - projectId
                  - name
                  - id
                  - status
                  - type
                  - configuration
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