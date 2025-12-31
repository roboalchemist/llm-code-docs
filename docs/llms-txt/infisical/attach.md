# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/token-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/tls-cert-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oidc-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oci-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/ldap-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/kubernetes-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/jwt-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/gcp-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/azure-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/aws-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/alicloud-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/token-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/tls-cert-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oidc-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oci-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/ldap-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/kubernetes-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/jwt-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/gcp-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/azure-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/aws-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/alicloud-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/token-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/tls-cert-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oidc-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oci-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/ldap-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/kubernetes-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/jwt-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/gcp-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/azure-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/aws-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/alicloud-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/token-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/tls-cert-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oidc-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/oci-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/ldap-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/kubernetes-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/jwt-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/gcp-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/azure-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/aws-auth/attach.md

# Source: https://infisical.com/docs/api-reference/endpoints/alicloud-auth/attach.md

# Attach

> Attach Alibaba Cloud Auth configuration onto machine identity

## OpenAPI

````yaml POST /api/v1/auth/alicloud-auth/identities/{identityId}
paths:
  path: /api/v1/auth/alicloud-auth/identities/{identityId}
  method: post
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: An access token in Infisical
          cookie: {}
    parameters:
      path:
        identityId:
          schema:
            - type: string
              required: true
              description: The ID of the machine identity to attach the configuration onto.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              allowedArns:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 500
                    description: >-
                      The comma-separated list of trusted ARNs that are allowed
                      to authenticate with Infisical.
              accessTokenTrustedIps:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        ipAddress:
                          type: string
                      required:
                        - ipAddress
                      additionalProperties: false
                    minItems: 1
                    default:
                      - ipAddress: 0.0.0.0/0
                      - ipAddress: '::/0'
                    description: >-
                      The IPs or CIDR ranges that access tokens can be used
                      from.
              accessTokenTTL:
                allOf:
                  - type: integer
                    minimum: 0
                    maximum: 315360000
                    default: 2592000
                    description: The lifetime for an access token in seconds.
              accessTokenMaxTTL:
                allOf:
                  - type: integer
                    minimum: 1
                    maximum: 315360000
                    default: 2592000
                    description: The maximum lifetime for an access token in seconds.
              accessTokenNumUsesLimit:
                allOf:
                  - type: integer
                    minimum: 0
                    default: 0
                    description: >-
                      The maximum number of times that an access token can be
                      used.
            required: true
            requiredProperties:
              - allowedArns
            additionalProperties: false
        examples:
          example:
            value:
              allowedArns: <string>
              accessTokenTrustedIps:
                - ipAddress: 0.0.0.0/0
                - ipAddress: '::/0'
              accessTokenTTL: 2592000
              accessTokenMaxTTL: 2592000
              accessTokenNumUsesLimit: 0
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              identityAliCloudAuth:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      accessTokenTTL:
                        type: number
                        default: 7200
                      accessTokenMaxTTL:
                        type: number
                        default: 7200
                      accessTokenNumUsesLimit:
                        type: number
                        default: 0
                      accessTokenTrustedIps: {}
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      identityId:
                        type: string
                        format: uuid
                      type:
                        type: string
                      allowedArns:
                        type: string
                    required:
                      - id
                      - createdAt
                      - updatedAt
                      - identityId
                      - type
                      - allowedArns
                    additionalProperties: false
            requiredProperties:
              - identityAliCloudAuth
            additionalProperties: false
        examples:
          example:
            value:
              identityAliCloudAuth:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                accessTokenTTL: 7200
                accessTokenMaxTTL: 7200
                accessTokenNumUsesLimit: 0
                accessTokenTrustedIps: <any>
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                identityId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                type: <string>
                allowedArns: <string>
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