# Source: https://infisical.com/docs/api-reference/endpoints/organizations/saml-sso/create-saml-config.md

# Create SAML SSO Config

> Create SAML config

## OpenAPI

````yaml POST /api/v1/sso/config
paths:
  path: /api/v1/sso/config
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
              organizationId:
                allOf:
                  - type: string
                    description: The ID of the organization to create the SAML config for.
              authProvider:
                allOf:
                  - type: string
                    enum:
                      - okta-saml
                      - azure-saml
                      - jumpcloud-saml
                      - google-saml
                      - keycloak-saml
                      - auth0-saml
                    description: Authentication provider to use for SAML authentication.
              isActive:
                allOf:
                  - type: boolean
                    description: Whether to enable or disable this SAML configuration.
              entryPoint:
                allOf:
                  - type: string
                    description: >-
                      The entry point for the SAML authentication. This is the
                      URL that the user will be redirected to after they have
                      authenticated with the SAML provider.
              issuer:
                allOf:
                  - type: string
                    description: The SAML provider issuer URL or entity ID.
              cert:
                allOf:
                  - type: string
                    description: The certificate to use for SAML authentication.
              enableGroupSync:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to enable automatic synchronization of group
                      memberships from the SAML provider to Infisical groups.
            required: true
            requiredProperties:
              - organizationId
              - authProvider
              - isActive
              - entryPoint
              - issuer
              - cert
            additionalProperties: false
        examples:
          example:
            value:
              organizationId: <string>
              authProvider: okta-saml
              isActive: true
              entryPoint: <string>
              issuer: <string>
              cert: <string>
              enableGroupSync: true
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
              orgId:
                allOf:
                  - type: string
                    format: uuid
              isActive:
                allOf:
                  - type: boolean
              lastUsed:
                allOf:
                  - type: string
                    format: date-time
                    nullable: true
              createdAt:
                allOf:
                  - type: string
                    format: date-time
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              authProvider:
                allOf:
                  - type: string
            requiredProperties:
              - id
              - orgId
              - isActive
              - createdAt
              - updatedAt
              - authProvider
            additionalProperties: false
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              isActive: true
              lastUsed: '2023-11-07T05:31:56Z'
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
              authProvider: <string>
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