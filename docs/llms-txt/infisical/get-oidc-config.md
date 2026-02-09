# Source: https://infisical.com/docs/api-reference/endpoints/organizations/oidc-sso/get-oidc-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get OIDC Config

> Get OIDC config



## OpenAPI

````yaml GET /api/v1/sso/oidc/config
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
    get:
      tags:
        - OIDC SSO
      description: Get OIDC config
      parameters:
        - schema:
            type: string
          in: query
          name: organizationId
          required: true
          description: The ID of the organization to get the OIDC config for.
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
                  jwksUri:
                    type: string
                    nullable: true
                  tokenEndpoint:
                    type: string
                    nullable: true
                  userinfoEndpoint:
                    type: string
                    nullable: true
                  configurationType:
                    type: string
                  discoveryURL:
                    type: string
                    nullable: true
                  isActive:
                    type: boolean
                  orgId:
                    type: string
                    format: uuid
                  allowedEmailDomains:
                    type: string
                    nullable: true
                  manageGroupMemberships:
                    type: boolean
                    default: false
                  jwtSignatureAlgorithm:
                    type: string
                    default: RS256
                  clientId:
                    type: string
                  clientSecret:
                    type: string
                required:
                  - id
                  - configurationType
                  - isActive
                  - orgId
                  - clientId
                  - clientSecret
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