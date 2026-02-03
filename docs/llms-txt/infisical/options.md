# Source: https://infisical.com/docs/api-reference/endpoints/secret-syncs/options.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/options.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/options.md

# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/options.md

# Source: https://infisical.com/docs/api-reference/endpoints/app-connections/options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Options

> List the available App Connection Options.



## OpenAPI

````yaml GET /api/v1/app-connections/options
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
  /api/v1/app-connections/options:
    get:
      tags:
        - App Connections
      description: List the available App Connection Options.
      operationId: listAppConnectionOptions
      parameters:
        - schema:
            type: string
            enum:
              - secret-manager
              - cert-manager
              - kms
              - ssh
              - secret-scanning
              - pam
              - ai
          in: query
          name: projectType
          required: false
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  appConnectionOptions:
                    type: array
                    items:
                      anyOf:
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - AWS
                            app:
                              type: string
                              enum:
                                - aws
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - assume-role
                                  - access-key
                            accessKeyId:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: AWS
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - GitHub
                            app:
                              type: string
                              enum:
                                - github
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - oauth
                                  - github-app
                                  - pat
                            oauthClientId:
                              type: string
                            appClientSlug:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: GitHub
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - GitHub Radar
                            app:
                              type: string
                              enum:
                                - github-radar
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - github-app
                            appClientSlug:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: GitHub Radar
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - GCP
                            app:
                              type: string
                              enum:
                                - gcp
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - service-account-impersonation
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: GCP
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Azure Key Vault
                            app:
                              type: string
                              enum:
                                - azure-key-vault
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - oauth
                                  - client-secret
                            oauthClientId:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Azure Key Vault
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Azure App Configuration
                            app:
                              type: string
                              enum:
                                - azure-app-configuration
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - oauth
                                  - client-secret
                            oauthClientId:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Azure App Configuration
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Azure DevOps
                            app:
                              type: string
                              enum:
                                - azure-devops
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - oauth
                                  - access-token
                                  - client-secret
                            oauthClientId:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Azure DevOps
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Databricks
                            app:
                              type: string
                              enum:
                                - databricks
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - service-principal
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Databricks
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Humanitec
                            app:
                              type: string
                              enum:
                                - humanitec
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Humanitec
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Terraform Cloud
                            app:
                              type: string
                              enum:
                                - terraform-cloud
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Terraform Cloud
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Vercel
                            app:
                              type: string
                              enum:
                                - vercel
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Vercel
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - PostgreSQL
                            app:
                              type: string
                              enum:
                                - postgres
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - username-and-password
                            supportsPlatformManagement:
                              type: boolean
                              enum:
                                - true
                          required:
                            - name
                            - app
                            - methods
                            - supportsPlatformManagement
                          additionalProperties: false
                          title: PostgreSQL
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Microsoft SQL Server
                            app:
                              type: string
                              enum:
                                - mssql
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - username-and-password
                            supportsPlatformManagement:
                              type: boolean
                              enum:
                                - true
                          required:
                            - name
                            - app
                            - methods
                            - supportsPlatformManagement
                          additionalProperties: false
                          title: Microsoft SQL Server
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - MySQL
                            app:
                              type: string
                              enum:
                                - mysql
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - username-and-password
                            supportsPlatformManagement:
                              type: boolean
                              enum:
                                - true
                          required:
                            - name
                            - app
                            - methods
                            - supportsPlatformManagement
                          additionalProperties: false
                          title: MySQL
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Camunda
                            app:
                              type: string
                              enum:
                                - camunda
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - client-credentials
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Camunda
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Auth0
                            app:
                              type: string
                              enum:
                                - auth0
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - client-credentials
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Auth0
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - HCVault
                            app:
                              type: string
                              enum:
                                - hashicorp-vault
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - access-token
                                  - app-role
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Hashicorp Vault
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Azure Client Secrets
                            app:
                              type: string
                              enum:
                                - azure-client-secrets
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - oauth
                                  - client-secret
                                  - certificate
                            oauthClientId:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Azure Client Secrets
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Windmill
                            app:
                              type: string
                              enum:
                                - windmill
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - access-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Windmill
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - LDAP
                            app:
                              type: string
                              enum:
                                - ldap
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - simple-bind
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: LDAP
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - TeamCity
                            app:
                              type: string
                              enum:
                                - teamcity
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - access-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: TeamCity
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - OCI
                            app:
                              type: string
                              enum:
                                - oci
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - access-key
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: OCI
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - OracleDB
                            app:
                              type: string
                              enum:
                                - oracledb
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - username-and-password
                            supportsPlatformManagement:
                              type: boolean
                              enum:
                                - true
                          required:
                            - name
                            - app
                            - methods
                            - supportsPlatformManagement
                          additionalProperties: false
                          title: OracleDB
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - 1Password
                            app:
                              type: string
                              enum:
                                - 1password
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: 1Password
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Heroku
                            app:
                              type: string
                              enum:
                                - heroku
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - auth-token
                                  - oauth
                            oauthClientId:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Heroku
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Render
                            app:
                              type: string
                              enum:
                                - render
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-key
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Render
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Fly.io
                            app:
                              type: string
                              enum:
                                - flyio
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - access-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Fly.io
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - GitLab
                            app:
                              type: string
                              enum:
                                - gitlab
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - oauth
                                  - access-token
                            oauthClientId:
                              type: string
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: GitLab
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Cloudflare
                            app:
                              type: string
                              enum:
                                - cloudflare
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Cloudflare
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Bitbucket
                            app:
                              type: string
                              enum:
                                - bitbucket
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Bitbucket
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Zabbix
                            app:
                              type: string
                              enum:
                                - zabbix
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Zabbix
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Railway
                            app:
                              type: string
                              enum:
                                - railway
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - account-token
                                  - project-token
                                  - team-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Railway
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Checkly
                            app:
                              type: string
                              enum:
                                - checkly
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-key
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Checkly
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - CircleCI
                            app:
                              type: string
                              enum:
                                - circleci
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: CircleCI
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Supabase
                            app:
                              type: string
                              enum:
                                - supabase
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - access-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Supabase
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Digital Ocean
                            app:
                              type: string
                              enum:
                                - digital-ocean
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: DigitalOcean App Platform
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Netlify
                            app:
                              type: string
                              enum:
                                - netlify
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - access-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Netlify
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Northflank
                            app:
                              type: string
                              enum:
                                - northflank
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Northflank
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Okta
                            app:
                              type: string
                              enum:
                                - okta
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Okta
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Azure ADCS
                            app:
                              type: string
                              enum:
                                - azure-adcs
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - username-password
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Azure ADCS
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Redis
                            app:
                              type: string
                              enum:
                                - redis
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - username-and-password
                            supportsPlatformManagement:
                              type: boolean
                              enum:
                                - false
                          required:
                            - name
                            - app
                            - methods
                            - supportsPlatformManagement
                          additionalProperties: false
                          title: Redis
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - MongoDB
                            app:
                              type: string
                              enum:
                                - mongodb
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - username-and-password
                            supportsPlatformManagement:
                              type: boolean
                              enum:
                                - false
                          required:
                            - name
                            - app
                            - methods
                            - supportsPlatformManagement
                          additionalProperties: false
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Laravel Forge
                            app:
                              type: string
                              enum:
                                - laravel-forge
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-token
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Laravel Forge
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Chef
                            app:
                              type: string
                              enum:
                                - chef
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - user-key
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Chef
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - DNS Made Easy
                            app:
                              type: string
                              enum:
                                - dns-made-easy
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-key-secret
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: DNS Made Easy
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Octopus Deploy
                            app:
                              type: string
                              enum:
                                - octopus-deploy
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-key
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: Octopus Deploy
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - Windows
                            app:
                              type: string
                              enum:
                                - smb
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - credentials
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: SMB
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - SSH
                            app:
                              type: string
                              enum:
                                - ssh
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - password
                                  - ssh-key
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: SSH
                        - type: object
                          properties:
                            name:
                              type: string
                              enum:
                                - OpenRouter
                            app:
                              type: string
                              enum:
                                - open-router
                            methods:
                              type: array
                              items:
                                type: string
                                enum:
                                  - api-key
                          required:
                            - name
                            - app
                            - methods
                          additionalProperties: false
                          title: OpenRouter
                required:
                  - appConnectionOptions
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