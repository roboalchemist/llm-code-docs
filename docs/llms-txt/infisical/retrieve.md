# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/token-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/tls-cert-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/oidc-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/oci-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/ldap-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/kubernetes-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/jwt-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/gcp-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/azure-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/aws-auth/retrieve.md

# Source: https://infisical.com/docs/api-reference/endpoints/alicloud-auth/retrieve.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve

> Retrieve Alibaba Cloud Auth configuration on machine identity



## OpenAPI

````yaml GET /api/v1/auth/alicloud-auth/identities/{identityId}
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
  /api/v1/auth/alicloud-auth/identities/{identityId}:
    get:
      tags:
        - Alibaba Cloud Auth
      description: Retrieve Alibaba Cloud Auth configuration on machine identity
      operationId: getAlicloudAuth
      parameters:
        - schema:
            type: string
          in: path
          name: identityId
          required: true
          description: The ID of the machine identity to retrieve the auth method for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  identityAliCloudAuth:
                    type: object
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
                required:
                  - identityAliCloudAuth
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