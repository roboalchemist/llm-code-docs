# Source: https://infisical.com/docs/api-reference/endpoints/organizations/oidc-sso/create-oidc-config.md

# Create OIDC Config

> Create OIDC config

## OpenAPI

````yaml POST /api/v1/sso/oidc/config
paths:
  path: /api/v1/sso/oidc/config
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              allowedEmailDomains:
                allOf:
                  - type: string
                    default: ''
                    description: >-
                      A list of allowed email domains that users can use to
                      authenticate with. This field is comma separated.
              configurationType:
                allOf:
                  - type: string
                    enum:
                      - custom
                      - discoveryURL
                    description: The configuration type to use for the OIDC configuration.
              issuer:
                allOf:
                  - type: string
                    default: ''
                    description: >-
                      The issuer for the OIDC configuration. This is only
                      supported when the OIDC configuration type is set to
                      'custom'.
              discoveryURL:
                allOf:
                  - type: string
                    default: ''
                    description: The URL of the OIDC discovery endpoint.
              authorizationEndpoint:
                allOf:
                  - type: string
                    default: ''
                    description: >-
                      The authorization endpoint to use for OIDC authorization.
                      This is only supported when the OIDC configuration type is
                      set to 'custom'.
              jwksUri:
                allOf:
                  - type: string
                    default: ''
                    description: The URL of the OIDC JWKS endpoint.
              tokenEndpoint:
                allOf:
                  - type: string
                    default: ''
                    description: The token endpoint to use for OIDC token exchange.
              userinfoEndpoint:
                allOf:
                  - type: string
                    default: ''
                    description: >-
                      The userinfo endpoint to get user information from the
                      OIDC provider.
              clientId:
                allOf:
                  - type: string
                    description: The client ID to use for OIDC authentication.
              clientSecret:
                allOf:
                  - type: string
                    description: The client secret to use for OIDC authentication.
              isActive:
                allOf:
                  - type: boolean
                    description: Whether to enable or disable this OIDC configuration.
              organizationId:
                allOf:
                  - type: string
                    description: The ID of the organization to create the OIDC config for.
              manageGroupMemberships:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      Whether to manage group memberships for the OIDC
                      configuration. If enabled, users will automatically be
                      assigned groups when they sign in, based on which groups
                      they are a member of in the OIDC provider.
              jwtSignatureAlgorithm:
                allOf:
                  - type: string
                    enum:
                      - RS256
                      - HS256
                      - RS512
                      - EdDSA
                    default: RS256
                    description: The algorithm to use for JWT signature verification.
            required: true
            requiredProperties:
              - configurationType
              - clientId
              - clientSecret
              - isActive
              - organizationId
            additionalProperties: false
        examples:
          example:
            value:
              allowedEmailDomains: ''
              configurationType: custom
              issuer: ''
              discoveryURL: ''
              authorizationEndpoint: ''
              jwksUri: ''
              tokenEndpoint: ''
              userinfoEndpoint: ''
              clientId: <string>
              clientSecret: <string>
              isActive: true
              organizationId: <string>
              manageGroupMemberships: false
              jwtSignatureAlgorithm: RS256
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
              issuer:
                allOf:
                  - type: string
                    nullable: true
              authorizationEndpoint:
                allOf:
                  - type: string
                    nullable: true
              configurationType:
                allOf:
                  - type: string
              discoveryURL:
                allOf:
                  - type: string
                    nullable: true
              jwksUri:
                allOf:
                  - type: string
                    nullable: true
              tokenEndpoint:
                allOf:
                  - type: string
                    nullable: true
              userinfoEndpoint:
                allOf:
                  - type: string
                    nullable: true
              orgId:
                allOf:
                  - type: string
                    format: uuid
              isActive:
                allOf:
                  - type: boolean
              allowedEmailDomains:
                allOf:
                  - type: string
                    nullable: true
              manageGroupMemberships:
                allOf:
                  - type: boolean
                    default: false
              jwtSignatureAlgorithm:
                allOf:
                  - type: string
                    default: RS256
            requiredProperties:
              - id
              - configurationType
              - orgId
              - isActive
            additionalProperties: false
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              issuer: <string>
              authorizationEndpoint: <string>
              configurationType: <string>
              discoveryURL: <string>
              jwksUri: <string>
              tokenEndpoint: <string>
              userinfoEndpoint: <string>
              orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              isActive: true
              allowedEmailDomains: <string>
              manageGroupMemberships: false
              jwtSignatureAlgorithm: RS256
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