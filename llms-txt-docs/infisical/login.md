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

# Login

> Login with Alibaba Cloud Auth for machine identity

## OpenAPI

````yaml POST /api/v1/auth/alicloud-auth/login
paths:
  path: /api/v1/auth/alicloud-auth/login
  method: post
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
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
              identityId:
                allOf:
                  - type: string
                    description: The ID of the machine identity to login.
              Action:
                allOf:
                  - type: string
                    enum:
                      - GetCallerIdentity
                    description: >-
                      The Alibaba Cloud API action. For STS GetCallerIdentity,
                      this should be 'GetCallerIdentity'.
              Format:
                allOf:
                  - type: string
                    enum:
                      - JSON
                    description: >-
                      The response format. For STS GetCallerIdentity, this
                      should be 'JSON'.
              Version:
                allOf:
                  - type: string
                    description: >-
                      The API version. This should be in 'YYYY-MM-DD' format
                      (e.g., '2015-04-01').
              AccessKeyId:
                allOf:
                  - type: string
                    description: The AccessKey ID of the RAM user or STS token.
              SignatureMethod:
                allOf:
                  - type: string
                    enum:
                      - HMAC-SHA1
                    description: >-
                      The signature algorithm. For STS GetCallerIdentity, this
                      should be 'HMAC-SHA1'.
              Timestamp:
                allOf:
                  - type: string
                    format: date-time
                    description: >-
                      The timestamp of the request in UTC, formatted as
                      'YYYY-MM-DDTHH:mm:ssZ'.
              SignatureVersion:
                allOf:
                  - type: string
                    enum:
                      - '1.0'
                    description: >-
                      The signature version. For STS GetCallerIdentity, this
                      should be '1.0'.
              SignatureNonce:
                allOf:
                  - type: string
                    description: A unique random string to prevent replay attacks.
              Signature:
                allOf:
                  - type: string
                    description: >-
                      The signature string calculated based on the request
                      parameters and AccessKey Secret.
            required: true
            requiredProperties:
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
        examples:
          example:
            value:
              identityId: <string>
              Action: GetCallerIdentity
              Format: JSON
              Version: <string>
              AccessKeyId: <string>
              SignatureMethod: HMAC-SHA1
              Timestamp: '2023-11-07T05:31:56Z'
              SignatureVersion: '1.0'
              SignatureNonce: <string>
              Signature: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              accessToken:
                allOf:
                  - type: string
              expiresIn:
                allOf:
                  - type: number
              accessTokenMaxTTL:
                allOf:
                  - type: number
              tokenType:
                allOf:
                  - type: string
                    enum:
                      - Bearer
            requiredProperties:
              - accessToken
              - expiresIn
              - accessTokenMaxTTL
              - tokenType
            additionalProperties: false
        examples:
          example:
            value:
              accessToken: <string>
              expiresIn: 123
              accessTokenMaxTTL: 123
              tokenType: Bearer
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