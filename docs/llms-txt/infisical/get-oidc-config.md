# Source: https://infisical.com/docs/api-reference/endpoints/organizations/oidc-sso/get-oidc-config.md

# Get OIDC Config

> Get OIDC config

## OpenAPI

````yaml GET /api/v1/sso/oidc/config
paths:
  path: /api/v1/sso/oidc/config
  method: get
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
      query:
        organizationId:
          schema:
            - type: string
              required: true
              description: The ID of the organization to get the OIDC config for.
      header: {}
      cookie: {}
    body: {}
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
              configurationType:
                allOf:
                  - type: string
              discoveryURL:
                allOf:
                  - type: string
                    nullable: true
              isActive:
                allOf:
                  - type: boolean
              orgId:
                allOf:
                  - type: string
                    format: uuid
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
              clientId:
                allOf:
                  - type: string
              clientSecret:
                allOf:
                  - type: string
            requiredProperties:
              - id
              - configurationType
              - isActive
              - orgId
              - clientId
              - clientSecret
            additionalProperties: false
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              issuer: <string>
              authorizationEndpoint: <string>
              jwksUri: <string>
              tokenEndpoint: <string>
              userinfoEndpoint: <string>
              configurationType: <string>
              discoveryURL: <string>
              isActive: true
              orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              allowedEmailDomains: <string>
              manageGroupMemberships: false
              jwtSignatureAlgorithm: RS256
              clientId: <string>
              clientSecret: <string>
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