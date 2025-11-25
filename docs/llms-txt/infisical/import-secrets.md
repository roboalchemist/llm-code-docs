# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/zabbix/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/windmill/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/vercel/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/teamcity/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/render/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/railway/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/oci-vault/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/northflank/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/laravel-forge/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/hashicorp-vault/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/gcp-secret-manager/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/chef/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/bitbucket/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-key-vault/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-devops/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-app-configuration/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/aws-secrets-manager/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/aws-parameter-store/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/1password/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/zabbix/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/windmill/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/vercel/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/teamcity/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/render/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/railway/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/oci-vault/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/northflank/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/laravel-forge/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/hashicorp-vault/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/gcp-secret-manager/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/chef/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/bitbucket/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-key-vault/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-devops/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-app-configuration/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/aws-secrets-manager/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/aws-parameter-store/import-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/1password/import-secrets.md

# Import Secrets

> Import secrets from the specified 1Password Sync destination.

## OpenAPI

````yaml POST /api/v1/secret-syncs/1password/{syncId}/import-secrets
paths:
  path: /api/v1/secret-syncs/1password/{syncId}/import-secrets
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
        syncId:
          schema:
            - type: string
              required: true
              description: The ID of the 1Password Sync to trigger importing secrets for.
              format: uuid
      query:
        importBehavior:
          schema:
            - type: enum<string>
              enum:
                - prioritize-source
                - prioritize-destination
              required: true
              description: >-
                Specify whether Infisical should prioritize secret values from
                Infisical or 1Password.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              secretSync:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      description:
                        type: string
                        nullable: true
                      isAutoSyncEnabled:
                        type: boolean
                        default: true
                      version:
                        type: number
                        default: 1
                      projectId:
                        type: string
                      folderId:
                        type: string
                        format: uuid
                        nullable: true
                      connectionId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      syncStatus:
                        type: string
                        nullable: true
                      lastSyncJobId:
                        type: string
                        nullable: true
                      lastSyncMessage:
                        type: string
                        nullable: true
                      lastSyncedAt:
                        type: string
                        format: date-time
                        nullable: true
                      importStatus:
                        type: string
                        nullable: true
                      lastImportJobId:
                        type: string
                        nullable: true
                      lastImportMessage:
                        type: string
                        nullable: true
                      lastImportedAt:
                        type: string
                        format: date-time
                        nullable: true
                      removeStatus:
                        type: string
                        nullable: true
                      lastRemoveJobId:
                        type: string
                        nullable: true
                      lastRemoveMessage:
                        type: string
                        nullable: true
                      lastRemovedAt:
                        type: string
                        format: date-time
                        nullable: true
                      syncOptions:
                        type: object
                        properties:
                          initialSyncBehavior:
                            type: string
                            enum:
                              - overwrite-destination
                              - import-prioritize-source
                              - import-prioritize-destination
                            description: >-
                              Specify how Infisical should resolve the initial
                              sync to the 1Password destination.
                          keySchema:
                            type: string
                            description: >-
                              Specify the format to use for structuring secret
                              keys in the 1Password destination.
                          disableSecretDeletion:
                            type: boolean
                            description: >-
                              Enable this flag to prevent removal of secrets
                              from the 1Password destination when syncing.
                        required:
                          - initialSyncBehavior
                        additionalProperties: false
                        description: Optional parameters to modify how secrets are synced.
                      connection:
                        type: object
                        properties:
                          app:
                            type: string
                            enum:
                              - 1password
                          name:
                            type: string
                          id:
                            type: string
                            format: uuid
                        required:
                          - app
                          - name
                          - id
                        additionalProperties: false
                      environment:
                        type: object
                        properties:
                          slug:
                            type: string
                          name:
                            type: string
                          id:
                            type: string
                            format: uuid
                        required:
                          - slug
                          - name
                          - id
                        additionalProperties: false
                        nullable: true
                      folder:
                        type: object
                        properties:
                          id:
                            type: string
                          path:
                            type: string
                        required:
                          - id
                          - path
                        additionalProperties: false
                        nullable: true
                      destination:
                        type: string
                        enum:
                          - 1password
                      destinationConfig:
                        type: object
                        properties:
                          vaultId:
                            type: string
                            minLength: 1
                            description: The ID of the 1Password vault to sync secrets to.
                          valueLabel:
                            type: string
                            description: >-
                              The label of the entry that holds the secret
                              value.
                        required:
                          - vaultId
                        additionalProperties: false
                    required:
                      - id
                      - name
                      - projectId
                      - connectionId
                      - createdAt
                      - updatedAt
                      - syncOptions
                      - connection
                      - environment
                      - folder
                      - destination
                      - destinationConfig
                    additionalProperties: false
                    title: 1Password
            requiredProperties:
              - secretSync
            additionalProperties: false
        examples:
          example:
            value:
              secretSync:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                description: <string>
                isAutoSyncEnabled: true
                version: 1
                projectId: <string>
                folderId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                connectionId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                syncStatus: <string>
                lastSyncJobId: <string>
                lastSyncMessage: <string>
                lastSyncedAt: '2023-11-07T05:31:56Z'
                importStatus: <string>
                lastImportJobId: <string>
                lastImportMessage: <string>
                lastImportedAt: '2023-11-07T05:31:56Z'
                removeStatus: <string>
                lastRemoveJobId: <string>
                lastRemoveMessage: <string>
                lastRemovedAt: '2023-11-07T05:31:56Z'
                syncOptions:
                  initialSyncBehavior: overwrite-destination
                  keySchema: <string>
                  disableSecretDeletion: true
                connection:
                  app: 1password
                  name: <string>
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                environment:
                  slug: <string>
                  name: <string>
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                folder:
                  id: <string>
                  path: <string>
                destination: 1password
                destinationConfig:
                  vaultId: <string>
                  valueLabel: <string>
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