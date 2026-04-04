# Source: https://infisical.com/docs/cli/commands/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/tls-cert-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/oidc-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/oci-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/ldap-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/kubernetes-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/jwt-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/gcp-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/azure-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/aws-auth/login.md

# Source: https://infisical.com/docs/api-reference/endpoints/alicloud-auth/login.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Login

> Login with Alibaba Cloud Auth for machine identity



## OpenAPI

````yaml POST /api/v1/auth/alicloud-auth/login
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
  /api/v1/auth/alicloud-auth/login:
    post:
      tags:
        - Alibaba Cloud Auth
      description: Login with Alibaba Cloud Auth for machine identity
      operationId: loginWithAlicloudAuth
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                identityId:
                  type: string
                  description: The ID of the machine identity to login.
                Action:
                  type: string
                  enum:
                    - GetCallerIdentity
                  description: >-
                    The Alibaba Cloud API action. For STS GetCallerIdentity,
                    this should be 'GetCallerIdentity'.
                Format:
                  type: string
                  enum:
                    - JSON
                  description: >-
                    The response format. For STS GetCallerIdentity, this should
                    be 'JSON'.
                Version:
                  type: string
                  description: >-
                    The API version. This should be in 'YYYY-MM-DD' format
                    (e.g., '2015-04-01').
                AccessKeyId:
                  type: string
                  description: The AccessKey ID of the RAM user or STS token.
                organizationSlug:
                  type: string
                  minLength: 1
                  maxLength: 64
                  description: >-
                    When set, this will scope the login session to the specified
                    organization the machine identity has access to. If omitted,
                    the session defaults to the organization where the machine
                    identity was created in.
                SignatureMethod:
                  type: string
                  enum:
                    - HMAC-SHA1
                  description: >-
                    The signature algorithm. For STS GetCallerIdentity, this
                    should be 'HMAC-SHA1'.
                Timestamp:
                  type: string
                  format: date-time
                  description: >-
                    The timestamp of the request in UTC, formatted as
                    'YYYY-MM-DDTHH:mm:ssZ'.
                SignatureVersion:
                  type: string
                  enum:
                    - '1.0'
                  description: >-
                    The signature version. For STS GetCallerIdentity, this
                    should be '1.0'.
                SignatureNonce:
                  type: string
                  description: A unique random string to prevent replay attacks.
                Signature:
                  type: string
                  description: >-
                    The signature string calculated based on the request
                    parameters and AccessKey Secret.
              required:
                - identityId
                - Action
                - Format
                - Version
                - AccessKeyId
                - SignatureMethod
                - Timestamp
                - SignatureVersion
                - SignatureNonce
                - Signature
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
                  accessToken:
                    type: string
                  expiresIn:
                    type: number
                  accessTokenMaxTTL:
                    type: number
                  tokenType:
                    type: string
                    enum:
                      - Bearer
                required:
                  - accessToken
                  - expiresIn
                  - accessTokenMaxTTL
                  - tokenType
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

````