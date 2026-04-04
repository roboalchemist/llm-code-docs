# Source: https://planetscale.com/docs/api/reference/list_roles.md

# List roles

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_branch`, `delete_branch`, `create_branch`, `connect_production_branch`, `connect_branch`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `manage_passwords`, `manage_production_branch_passwords` |
| Database | `manage_passwords`, `manage_production_branch_passwords` |
| Branch | `manage_passwords` |



## OpenAPI

````yaml get /organizations/{organization}/databases/{database}/branches/{branch}/roles
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
  /organizations/{organization}/databases/{database}/branches/{branch}/roles:
    get:
      tags:
        - Roles
      summary: List roles
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_branch`, `delete_branch`, `create_branch`, `connect_production_branch`, `connect_branch`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `manage_passwords`,
        `manage_production_branch_passwords` |

        | Database | `manage_passwords`, `manage_production_branch_passwords` |

        | Branch | `manage_passwords` |
      operationId: list_roles
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization that owns this resource
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the database that owns this resource
          schema:
            type: string
        - name: branch
          in: path
          required: true
          description: The name of the branch that owns this resource
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
          description: Returns roles
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
                          description: The ID of the role
                        name:
                          type: string
                          description: The name of the role
                        access_host_url:
                          type: string
                          description: The database connection string
                        private_access_host_url:
                          type: string
                          description: >-
                            The database connection string for private
                            connections
                        private_connection_service_name:
                          type: string
                          description: The service name to set up private connectivity
                        username:
                          type: string
                          description: The database user name
                        password:
                          type: string
                          description: The plain text password, available only after create
                        database_name:
                          type: string
                          description: The database name
                        created_at:
                          type: string
                          description: When the role was created
                        updated_at:
                          type: string
                          description: When the role was updated
                        deleted_at:
                          type: string
                          description: When the role was deleted
                        expires_at:
                          type: string
                          description: When the role expires
                        dropped_at:
                          type: string
                          description: When the role was dropped
                        disabled_at:
                          type: string
                          description: When the role was disabled
                        drop_failed:
                          type: string
                          description: Error message available when dropping the role fails
                        expired:
                          type: boolean
                          description: True if the credentials are expired
                        default:
                          type: boolean
                          description: Whether the role is the default postgres user
                        ttl:
                          type: integer
                          description: Number of seconds before the credentials expire
                        inherited_roles:
                          items:
                            type: string
                            enum:
                              - pscale_managed
                              - pg_checkpoint
                              - pg_create_subscription
                              - pg_maintain
                              - pg_monitor
                              - pg_read_all_data
                              - pg_read_all_settings
                              - pg_read_all_stats
                              - pg_signal_backend
                              - pg_stat_scan_tables
                              - pg_use_reserved_connections
                              - pg_write_all_data
                              - postgres
                          type: array
                          description: Database roles these credentials inherit
                        branch:
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
                        actor:
                          type: object
                          properties:
                            id:
                              type: string
                              description: The ID of the actor
                            display_name:
                              type: string
                              description: The name of the actor
                            avatar_url:
                              type: string
                              description: The URL of the actor's avatar
                          additionalProperties: false
                          required:
                            - id
                            - display_name
                            - avatar_url
                      additionalProperties: false
                      required:
                        - id
                        - name
                        - access_host_url
                        - private_access_host_url
                        - private_connection_service_name
                        - username
                        - password
                        - database_name
                        - created_at
                        - updated_at
                        - deleted_at
                        - expires_at
                        - dropped_at
                        - disabled_at
                        - drop_failed
                        - expired
                        - default
                        - ttl
                        - inherited_roles
                        - branch
                        - actor
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