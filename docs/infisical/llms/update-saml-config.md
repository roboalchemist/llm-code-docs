# Source: https://infisical.com/docs/api-reference/endpoints/organizations/saml-sso/update-saml-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update SAML SSO Config

> Update SAML config



## OpenAPI

````yaml PATCH /api/v1/sso/config
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
  /api/v1/sso/config:
    patch:
      tags:
        - SAML SSO
      description: Update SAML config
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                authProvider:
                  type: string
                  enum:
                    - okta-saml
                    - azure-saml
                    - jumpcloud-saml
                    - google-saml
                    - keycloak-saml
                    - auth0-saml
                  description: Authentication provider to use for SAML authentication.
                isActive:
                  type: boolean
                  description: Whether to enable or disable this SAML configuration.
                entryPoint:
                  type: string
                  description: >-
                    The entry point for the SAML authentication. This is the URL
                    that the user will be redirected to after they have
                    authenticated with the SAML provider.
                issuer:
                  type: string
                  description: The SAML provider issuer URL or entity ID.
                cert:
                  type: string
                  description: The certificate to use for SAML authentication.
                enableGroupSync:
                  type: boolean
                  description: >-
                    Whether to enable automatic synchronization of group
                    memberships from the SAML provider to Infisical groups.
                organizationId:
                  type: string
                  description: The ID of the organization to update the SAML config for.
              required:
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
                  orgId:
                    type: string
                    format: uuid
                  isActive:
                    type: boolean
                  lastUsed:
                    type: string
                    format: date-time
                    nullable: true
                  createdAt:
                    type: string
                    format: date-time
                  updatedAt:
                    type: string
                    format: date-time
                  authProvider:
                    type: string
                required:
                  - id
                  - orgId
                  - isActive
                  - createdAt
                  - updatedAt
                  - authProvider
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