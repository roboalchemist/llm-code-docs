# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/zabbix/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/windmill/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/vercel/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/terraform-cloud/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/teamcity/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/supabase/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/ssh/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/smb/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/render/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/redis/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/railway/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/postgres/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/oracledb/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/openrouter/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/okta/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/octopus-deploy/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/oci/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/northflank/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/netlify/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/mysql/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/mssql/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/mongodb/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/ldap/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/laravel-forge/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/humanitec/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/heroku/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/hashicorp-vault/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/gitlab/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/github/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/github-radar/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/gcp/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/flyio/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/digital-ocean/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/databricks/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/cloudflare/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/chef/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/camunda/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/bitbucket/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/azure-key-vault/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/azure-devops/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/azure-client-secret/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/azure-app-configuration/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/azure-adcs/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/aws/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/auth0/available.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/1password/available.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Available

> List the 1Password Connections the current user has permission to establish connections within this project.



## OpenAPI

````yaml GET /api/v1/app-connections/1password/available
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
  /api/v1/app-connections/1password/available:
    get:
      tags:
        - App Connections
      description: >-
        List the 1Password Connections the current user has permission to
        establish connections within this project.
      operationId: listOnePasswordAvailableAppConnections
      parameters:
        - schema:
            type: string
          in: query
          name: projectId
          required: false
          description: The ID of the project to list 1Password Connections from.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  appConnections:
                    type: array
                    items:
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
                        projectId:
                          type: string
                          nullable: true
                        orgId:
                          type: string
                      required:
                        - app
                        - name
                        - id
                        - orgId
                      additionalProperties: false
                required:
                  - appConnections
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