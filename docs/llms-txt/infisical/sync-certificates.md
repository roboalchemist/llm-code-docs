# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/chef/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/azure-key-vault/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/aws-secrets-manager/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/aws-certificate-manager/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/chef/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/azure-key-vault/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/aws-secrets-manager/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/aws-certificate-manager/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/chef/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/azure-key-vault/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/aws-secrets-manager/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/aws-certificate-manager/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/azure-key-vault/sync-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/aws-certificate-manager/sync-certificates.md

# Sync Certificates to AWS Certificate Manager

> Trigger a sync for the specified AWS Certificate Manager PKI Sync.

## OpenAPI

````yaml POST /api/v1/pki/syncs/aws-certificate-manager/{pkiSyncId}/sync
paths:
  path: /api/v1/pki/syncs/aws-certificate-manager/{pkiSyncId}/sync
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
      path:
        pkiSyncId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
            requiredProperties:
              - message
            additionalProperties: false
        examples:
          example:
            value:
              message: <string>
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