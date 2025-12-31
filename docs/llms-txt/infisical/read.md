# Source: https://infisical.com/docs/api-reference/endpoints/ssh/hosts/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/groups/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/certificate-templates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/ca/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki-alerts/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/acme/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/hosts/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/groups/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/certificate-templates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/ca/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki-alerts/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/acme/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/hosts/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/groups/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/certificate-templates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/ca/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki-collections/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/acme/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/hosts/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/groups/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/certificate-templates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/ssh/ca/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki-collections/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificates/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/internal/read.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/acme/read.md

# Read

## OpenAPI

````yaml GET /api/v1/pki/ca/acme/{caName}
paths:
  path: /api/v1/pki/ca/acme/{caName}
  method: get
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
        caName:
          schema:
            - type: string
              required: true
      query:
        projectId:
          schema:
            - type: string
              required: true
              format: uuid
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              projectId:
                allOf:
                  - type: string
              enableDirectIssuance:
                allOf:
                  - type: boolean
                    default: true
              name:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
                    format: uuid
              status:
                allOf:
                  - type: string
                    enum:
                      - active
                      - disabled
                      - pending-certificate
              type:
                allOf:
                  - type: string
                    enum:
                      - acme
              configuration:
                allOf:
                  - type: object
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
            requiredProperties:
              - projectId
              - name
              - id
              - status
              - type
              - configuration
            additionalProperties: false
        examples:
          example:
            value:
              projectId: <string>
              enableDirectIssuance: true
              name: <string>
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              status: active
              type: acme
              configuration:
                dnsAppConnectionId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                dnsProviderConfig:
                  provider: route53
                  hostedZoneId: <string>
                directoryUrl: <string>
                accountEmail: <string>
                eabKid: <string>
                eabHmacKey: <string>
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