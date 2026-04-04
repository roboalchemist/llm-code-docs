# Source: https://planetscale.com/docs/api/reference/get_current_user.md

# Get current user

> Get the user associated with this service token
### Authorization
A   OAuth token must have at least one of the following   scopes in order to use this API endpoint:

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| User | `read_user` |



## OpenAPI

````yaml get /user
openapi: 3.0.1
info:
  title: PlanetScale API
  description: |-

    <p>PlanetScale API</p>
    &copy; 2025 PlanetScale, Inc.
  version: v1
  x-copyright: '&copy; 2025 PlanetScale, Inc.'
servers:
  - url: https://api.planetscale.com/v1
security:
  - ApiKeyHeader:
      - Authorization
tags:
  - name: Backups
    description: |2
                Resources for managing database branch backups.
  - name: Branch changes
    description: |2
                Resources for managing cluster changes.
  - name: Cluster extensions
    description: |2
                Resources for managing cluster extension configuration.
  - name: Branch log signatures
    description: |2
                Resources for retrieving branch log access signatures.
  - name: Cluster parameters
    description: |2
                Resources for managing cluster configuration parameters.
  - name: Database branch keyspaces
    description: |2
                Resources for managing keyspaces.
  - name: Database branch passwords
    description: |2
                Resources for managing database branch passwords.
  - name: Database Postgres IP restrictions
    description: |2
                Resources for managing Postgres IP restriction entries for databases.

                Note: This endpoint is only available for PostgreSQL databases. For MySQL databases, use the Database Branch Passwords endpoint.
  - name: Databases
    description: |2
                  Resources for managing databases within an organization.
  - name: Keyspace VSchemas
    description: |2
                Resources for managing VSchemas within a keyspace.
  - name: OAuth applications
    description: |2
                Resources for managing OAuth applications.
  - name: OAuth tokens
    description: |2
                Resources for managing OAuth tokens.
  - name: Organization members
    description: |2
                Resources for managing organization members and their roles.
  - name: Organizations
    description: |2
                  Resources for managing organizations.
  - name: Bouncer resizes
    description: |2
                Resources for managing Postgres bouncer resize requests.
  - name: Bouncers
    description: |2
                Resources for managing postgres bouncers.
  - name: Roles
    description: |2
                Resources for managing role credentials.
  - name: Query Insights reports
    description: |2
                Resources for downloading query insights data.
  - name: Service tokens
    description: |2
                API endpoints for managing service tokens within an organization.
  - name: Users
    description: |2
                Resources for managing users.
  - name: Workflows
    description: |2
                API endpoints for managing workflows.
  - name: Deploy requests
    description: |2
                  Resources for managing deploy requests.
  - name: Webhooks
    description: |2
                  Resources for managing database webhooks.
  - name: Invoices
    description: |2
                  Resources for managing invoices.
  - name: Organization teams
    description: |2
                  Resources for managing teams within an organization. Teams allow you to group members and grant them access to specific databases.

                  Note: Teams managed through SSO/directory services cannot be modified via API.
paths:
  /user:
    get:
      tags:
        - Users
      summary: Get current user
      description: >-
        Get the user associated with this service token

        ### Authorization

        A   OAuth token must have at least one of the following   scopes in
        order to use this API endpoint:


        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | User | `read_user` |
      operationId: get_current_user
      responses:
        '200':
          description: Returns the user associated with this service token
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the user
                  display_name:
                    type: string
                    description: The display name of the user
                  name:
                    type: string
                    description: The name of the user
                  email:
                    type: string
                    description: The email of the user
                  avatar_url:
                    type: string
                    description: The URL source of the user's avatar
                  created_at:
                    type: string
                    description: When the user was created
                  updated_at:
                    type: string
                    description: When the user was last updated
                  two_factor_auth_configured:
                    type: boolean
                    description: >-
                      Whether or not the user has configured two factor
                      authentication
                  default_organization:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The ID for the resource
                      name:
                        type: string
                        description: The name for the resource
                      created_at:
                        type: string
                        description: When the resource was created
                      updated_at:
                        type: string
                        description: When the resource was last updated
                      deleted_at:
                        type: string
                        description: When the resource was deleted, if deleted
                    additionalProperties: false
                    required:
                      - id
                      - name
                      - created_at
                      - updated_at
                      - deleted_at
                  sso:
                    type: boolean
                    description: Whether or not the user is managed by SSO
                  managed:
                    type: boolean
                    description: >-
                      Whether or not the user is managed by an authentication
                      provider
                  directory_managed:
                    type: boolean
                    description: Whether or not the user is managed by a SSO directory
                  email_verified:
                    type: boolean
                    description: Whether or not the user is verified by email
                additionalProperties: false
                required:
                  - id
                  - display_name
                  - name
                  - email
                  - avatar_url
                  - created_at
                  - updated_at
                  - two_factor_auth_configured
                  - default_organization
                  - sso
                  - managed
                  - directory_managed
                  - email_verified
        '401':
          description: Unauthorized
        '403':
          description: Forbidden
        '404':
          description: Not Found
        '500':
          description: Internal Server Error
components:
  securitySchemes:
    ApiKeyHeader:
      type: apiKey
      in: header
      name: Authorization

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt