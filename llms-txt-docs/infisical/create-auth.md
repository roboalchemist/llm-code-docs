# Source: https://infisical.com/docs/api-reference/endpoints/integrations/create-auth.md

# Create Auth

> Create the integration authentication object required for syncing secrets.

## OpenAPI

````yaml POST /api/v1/integration-auth/access-token
paths:
  path: /api/v1/integration-auth/access-token
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
              workspaceId:
                allOf:
                  - type: string
                    description: The ID of the project to create the integration auth for.
              integration:
                allOf:
                  - type: string
                    description: The slug of integration for the auth object.
              accessId:
                allOf:
                  - type: string
                    description: >-
                      The unique authorized access ID of the external
                      integration provider.
              accessToken:
                allOf:
                  - type: string
                    description: >-
                      The unique authorized access token of the external
                      integration provider.
              awsAssumeIamRoleArn:
                allOf:
                  - type: string
                    format: uri
                    description: The AWS IAM Role to be assumed by Infisical.
              url:
                allOf:
                  - type: string
                    format: uri
              namespace:
                allOf:
                  - type: string
              refreshToken:
                allOf:
                  - type: string
                    description: The refresh token for integration authorization.
            required: true
            requiredProperties:
              - workspaceId
              - integration
            additionalProperties: false
        examples:
          example:
            value:
              workspaceId: <string>
              integration: <string>
              accessId: <string>
              accessToken: <string>
              awsAssumeIamRoleArn: <string>
              url: <string>
              namespace: <string>
              refreshToken: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              integrationAuth:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      projectId:
                        type: string
                      integration:
                        type: string
                      teamId:
                        type: string
                        nullable: true
                      url:
                        type: string
                        nullable: true
                      namespace:
                        type: string
                        nullable: true
                      accountId:
                        type: string
                        nullable: true
                      metadata:
                        nullable: true
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                    required:
                      - id
                      - projectId
                      - integration
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            requiredProperties:
              - integrationAuth
            additionalProperties: false
        examples:
          example:
            value:
              integrationAuth:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                projectId: <string>
                integration: <string>
                teamId: <string>
                url: <string>
                namespace: <string>
                accountId: <string>
                metadata: <any>
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
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