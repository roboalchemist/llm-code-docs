# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/zabbix/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/windmill/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/vercel/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/terraform-cloud/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/teamcity/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/supabase/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/render/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/railway/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/octopus-deploy/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/oci-vault/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/northflank/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/netlify/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/laravel-forge/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/humanitec/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/heroku/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/hashicorp-vault/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/gitlab/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/github/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/gcp-secret-manager/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/flyio/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/digital-ocean-app-platform/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/databricks/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/cloudflare-workers/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/cloudflare-pages/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/circleci/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/chef/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/checkly/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/camunda/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/bitbucket/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-key-vault/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-devops/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/azure-app-configuration/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/aws-secrets-manager/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/aws-parameter-store/remove-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/1password/remove-secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove Secrets

> Remove previously synced secrets from the specified 1Password Sync destination.



## OpenAPI

````yaml POST /api/v1/secret-syncs/1password/{syncId}/remove-secrets
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
  /api/v1/secret-syncs/1password/{syncId}/remove-secrets:
    post:
      tags:
        - Secret Syncs
      description: >-
        Remove previously synced secrets from the specified 1Password Sync
        destination.
      operationId: removeOnePasswordSecretSyncSecrets
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: syncId
          required: true
          description: The ID of the 1Password Sync to trigger removing secrets for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  secretSync:
                    type: object
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
                required:
                  - secretSync
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