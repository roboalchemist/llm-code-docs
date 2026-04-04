# Source: https://planetscale.com/docs/api/reference/list_deploy_operations.md

# List deploy operations

> List deploy operations for a deploy request
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_deploy_request`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `read_deploy_requests` |
| Database | `read_deploy_requests` |



## OpenAPI

````yaml get /organizations/{organization}/databases/{database}/deploy-requests/{number}/operations
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
  /organizations/{organization}/databases/{database}/deploy-requests/{number}/operations:
    get:
      tags:
        - Deploy requests
      summary: List deploy operations
      description: >-
        List deploy operations for a deploy request

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_deploy_request`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `read_deploy_requests` |

        | Database | `read_deploy_requests` |
      operationId: list_deploy_operations
      parameters:
        - name: number
          in: path
          required: true
          description: The number of the deploy request
          schema:
            type: integer
        - name: organization
          in: path
          required: true
          description: The name of the deploy request's organization
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the deploy request's database
          schema:
            type: string
        - name: page
          in: query
          description: If provided, specifies the page offset of returned results
          schema:
            type: integer
            default: 1
        - name: per_page
          in: query
          description: If provided, specifies the number of returned results
          schema:
            type: integer
            default: 25
      responses:
        '200':
          description: Returns deploy operations for the deploy request
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  current_page:
                    type: integer
                    description: The current page number
                  next_page:
                    type: integer
                    description: The next page number
                  next_page_url:
                    type: string
                    description: The next page of results
                  prev_page:
                    type: integer
                    description: The previous page number
                  prev_page_url:
                    type: string
                    description: The previous page of results
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The ID for the deploy operation
                        state:
                          type: string
                          enum:
                            - pending
                            - queued
                            - in_progress
                            - complete
                            - cancelled
                            - error
                          description: The state of the deploy operation
                        keyspace_name:
                          type: string
                          description: The keyspace modified by the deploy operation
                        table_name:
                          type: string
                          description: >-
                            The name of the table modifed by the deploy
                            operation
                        operation_name:
                          type: string
                          description: The operation name of the deploy operation
                        eta_seconds:
                          type: number
                          description: >-
                            The estimated seconds until completion for the
                            deploy operation
                        progress_percentage:
                          type: number
                          description: The percent completion for the deploy operation
                        deploy_error_docs_url:
                          type: string
                          description: >-
                            A link to documentation explaining the deploy error,
                            if present
                        ddl_statement:
                          type: string
                          description: The DDL statement for the deploy operation
                        syntax_highlighted_ddl:
                          type: string
                          description: >-
                            A syntax-highlighted DDL statement for the deploy
                            operation
                        created_at:
                          type: string
                          description: When the deploy operation was created
                        updated_at:
                          type: string
                          description: When the deploy operation was last updated
                        throttled_at:
                          type: string
                          description: When the deploy operation was last throttled
                        can_drop_data:
                          type: boolean
                          description: >-
                            Whether or not the deploy operation is capable of
                            dropping data
                        table_locked:
                          type: boolean
                          description: >-
                            Whether or not the table modified by the deploy
                            operation is currently locked
                        table_recently_used:
                          type: boolean
                          description: >-
                            Whether or not the table modified by the deploy
                            operation was recently used
                        table_recently_used_at:
                          type: string
                          description: >-
                            When the table modified by the deploy operation was
                            last used
                        removed_foreign_key_names:
                          items:
                            type: string
                          type: array
                          description: Names of foreign keys removed by this operation
                        deploy_errors:
                          type: string
                          description: Deploy errors for the deploy operation
                      additionalProperties: false
                      required:
                        - id
                        - state
                        - keyspace_name
                        - table_name
                        - operation_name
                        - eta_seconds
                        - progress_percentage
                        - deploy_error_docs_url
                        - ddl_statement
                        - syntax_highlighted_ddl
                        - created_at
                        - updated_at
                        - throttled_at
                        - can_drop_data
                        - table_locked
                        - table_recently_used
                        - table_recently_used_at
                        - removed_foreign_key_names
                        - deploy_errors
                additionalProperties: false
                required:
                  - current_page
                  - next_page
                  - next_page_url
                  - prev_page
                  - prev_page_url
                  - data
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