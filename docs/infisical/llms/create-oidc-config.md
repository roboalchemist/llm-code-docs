# Source: https://infisical.com/docs/api-reference/endpoints/organizations/oidc-sso/create-oidc-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create OIDC Config

> Create OIDC config



## OpenAPI

````yaml POST /api/v1/sso/oidc/config
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
  /api/v1/sso/oidc/config:
    post:
      tags:
        - OIDC SSO
      description: Create OIDC config
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                allowedEmailDomains:
                  type: string
                  default: ''
                  description: >-
                    A list of allowed email domains that users can use to
                    authenticate with. This field is comma separated.
                configurationType:
                  type: string
                  enum:
                    - custom
                    - discoveryURL
                  description: The configuration type to use for the OIDC configuration.
                issuer:
                  type: string
                  default: ''
                  description: >-
                    The issuer for the OIDC configuration. This is only
                    supported when the OIDC configuration type is set to
                    'custom'.
                discoveryURL:
                  type: string
                  default: ''
                  description: The URL of the OIDC discovery endpoint.
                authorizationEndpoint:
                  type: string
                  default: ''
                  description: >-
                    The authorization endpoint to use for OIDC authorization.
                    This is only supported when the OIDC configuration type is
                    set to 'custom'.
                jwksUri:
                  type: string
                  default: ''
                  description: The URL of the OIDC JWKS endpoint.
                tokenEndpoint:
                  type: string
                  default: ''
                  description: The token endpoint to use for OIDC token exchange.
                userinfoEndpoint:
                  type: string
                  default: ''
                  description: >-
                    The userinfo endpoint to get user information from the OIDC
                    provider.
                clientId:
                  type: string
                  description: The client ID to use for OIDC authentication.
                clientSecret:
                  type: string
                  description: The client secret to use for OIDC authentication.
                isActive:
                  type: boolean
                  description: Whether to enable or disable this OIDC configuration.
                organizationId:
                  type: string
                  description: The ID of the organization to create the OIDC config for.
                manageGroupMemberships:
                  type: boolean
                  default: false
                  description: >-
                    Whether to manage group memberships for the OIDC
                    configuration. If enabled, users will automatically be
                    assigned groups when they sign in, based on which groups
                    they are a member of in the OIDC provider.
                jwtSignatureAlgorithm:
                  type: string
                  enum:
                    - RS256
                    - HS256
                    - RS512
                    - EdDSA
                  default: RS256
                  description: The algorithm to use for JWT signature verification.
              required:
                - configurationType
                - clientId
                - clientSecret
                - isActive
                - organizationId
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
                  id:
                    type: string
                    format: uuid
                  issuer:
                    type: string
                    nullable: true
                  authorizationEndpoint:
                    type: string
                    nullable: true
                  configurationType:
                    type: string
                  discoveryURL:
                    type: string
                    nullable: true
                  jwksUri:
                    type: string
                    nullable: true
                  tokenEndpoint:
                    type: string
                    nullable: true
                  userinfoEndpoint:
                    type: string
                    nullable: true
                  orgId:
                    type: string
                    format: uuid
                  isActive:
                    type: boolean
                  allowedEmailDomains:
                    type: string
                    nullable: true
                  manageGroupMemberships:
                    type: boolean
                    default: false
                  jwtSignatureAlgorithm:
                    type: string
                    default: RS256
                required:
                  - id
                  - configurationType
                  - orgId
                  - isActive
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
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````