# Source: https://planetscale.com/docs/api/reference/get_database.md

# Get a database

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_database`, `delete_database`, `write_database`, `read_branch`, `delete_branch`, `create_branch`, `delete_production_branch`, `connect_branch`, `connect_production_branch`, `delete_branch_password`, `delete_production_branch_password`, `read_deploy_request`, `create_deploy_request`, `approve_deploy_request`, `read_schema_recommendations`, `close_schema_recommendations`, `read_comment`, `create_comment`, `restore_backup`, `restore_production_branch_backup`, `read_backups`, `write_backups`, `delete_backups`, `delete_production_branch_backups`, `write_branch_vschema`, `write_production_branch_vschema`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `read_databases` |
| Database | `read_database` |



## OpenAPI

````yaml get /organizations/{organization}/databases/{database}
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
  /organizations/{organization}/databases/{database}:
    get:
      tags:
        - Databases
      summary: Get a database
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_database`, `delete_database`, `write_database`, `read_branch`, `delete_branch`, `create_branch`, `delete_production_branch`, `connect_branch`, `connect_production_branch`, `delete_branch_password`, `delete_production_branch_password`, `read_deploy_request`, `create_deploy_request`, `approve_deploy_request`, `read_schema_recommendations`, `close_schema_recommendations`, `read_comment`, `create_comment`, `restore_backup`, `restore_production_branch_backup`, `read_backups`, `write_backups`, `delete_backups`, `delete_production_branch_backups`, `write_branch_vschema`, `write_production_branch_vschema`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `read_databases` |

        | Database | `read_database` |
      operationId: get_database
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization the database belongs to
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the database
          schema:
            type: string
      responses:
        '200':
          description: Returns a database
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the database
                  url:
                    type: string
                    description: The URL to the database API endpoint
                  branches_url:
                    type: string
                    description: The URL to retrieve this database's branches via the API
                  branches_count:
                    type: integer
                    description: The total number of database branches
                  open_schema_recommendations_count:
                    type: integer
                    description: The total number of schema recommendations
                  development_branches_count:
                    type: integer
                    description: The total number of database development branches
                  production_branches_count:
                    type: integer
                    description: The total number of database production branches
                  issues_count:
                    type: integer
                    description: The total number of ongoing issues within a database
                  multiple_admins_required_for_deletion:
                    type: boolean
                    description: If the database requires multiple admins for deletion
                  ready:
                    type: boolean
                    description: If the database is ready to be used
                  at_backup_restore_branches_limit:
                    type: boolean
                    description: >-
                      If the database has reached its backup restored branch
                      limit
                  at_development_branch_usage_limit:
                    type: boolean
                    description: If the database has reached its development branch limit
                  data_import:
                    type: object
                    properties:
                      state:
                        type: string
                        description: State of the data import
                      import_check_errors:
                        type: string
                        description: Errors encountered during the import check
                      started_at:
                        type: string
                        description: When the import started
                      finished_at:
                        type: string
                        description: When the import finished
                      data_source:
                        type: object
                        properties:
                          hostname:
                            type: string
                            description: Hostname of the data source
                          port:
                            type: integer
                            description: Port of the data source
                          database:
                            type: string
                            description: Database name of the data source
                        additionalProperties: false
                        required:
                          - hostname
                          - port
                          - database
                    additionalProperties: false
                    required:
                      - state
                      - import_check_errors
                      - started_at
                      - finished_at
                      - data_source
                  region:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The ID of the region
                      provider:
                        type: string
                        description: Provider for the region (ex. AWS)
                      enabled:
                        type: boolean
                        description: Whether or not the region is currently active
                      public_ip_addresses:
                        items:
                          type: string
                        type: array
                        description: Public IP addresses for the region
                      display_name:
                        type: string
                        description: Name of the region
                      location:
                        type: string
                        description: Location of the region
                      slug:
                        type: string
                        description: The slug of the region
                      current_default:
                        type: boolean
                        description: >-
                          True if the region is the default for new branch
                          creation
                    additionalProperties: false
                    required:
                      - id
                      - provider
                      - enabled
                      - public_ip_addresses
                      - display_name
                      - location
                      - slug
                      - current_default
                  html_url:
                    type: string
                    description: The URL to see this database's branches in the web UI
                  name:
                    type: string
                    description: Name of the database
                  state:
                    type: string
                    enum:
                      - pending
                      - importing
                      - sleep_in_progress
                      - sleeping
                      - awakening
                      - import_ready
                      - ready
                    description: State of the database
                  sharded:
                    type: boolean
                    description: If the database is sharded
                  default_branch_shard_count:
                    type: integer
                    description: Number of shards in the default branch
                  default_branch_read_only_regions_count:
                    type: integer
                    description: Number of read only regions in the default branch
                  default_branch_table_count:
                    type: integer
                    description: Number of tables in the default branch schema
                  default_branch:
                    type: string
                    description: The default branch for the database
                  require_approval_for_deploy:
                    type: boolean
                    description: >-
                      Whether an approval is required to deploy schema changes
                      to this database
                  resizing:
                    type: boolean
                    description: True if a branch is currently resizing
                  resize_queued:
                    type: boolean
                    description: True if a branch has a queued resize request
                  allow_data_branching:
                    type: boolean
                    description: >-
                      Whether seeding branches with data is enabled for all
                      branches
                  foreign_keys_enabled:
                    type: boolean
                    description: Whether foreign key constraints are enabled
                  automatic_migrations:
                    type: boolean
                    description: >-
                      Whether to automatically manage Rails migrations during
                      deploy requests
                  restrict_branch_region:
                    type: boolean
                    description: Whether to restrict branch creation to one region
                  insights_raw_queries:
                    type: boolean
                    description: Whether raw SQL queries are collected
                  plan:
                    type: string
                    description: The database plan
                  insights_enabled:
                    type: boolean
                    description: True if query insights is enabled for the database
                  production_branch_web_console:
                    type: boolean
                    description: Whether web console is enabled for production branches
                  migration_table_name:
                    type: string
                    description: Table name to use for copying schema migration data
                  migration_framework:
                    type: string
                    description: Framework used for applying migrations
                  created_at:
                    type: string
                    description: When the database was created
                  updated_at:
                    type: string
                    description: When the database was last updated
                  schema_last_updated_at:
                    type: string
                    description: When the default branch schema was last changed.
                  kind:
                    type: string
                    enum:
                      - mysql
                      - postgresql
                    description: The kind of database
                additionalProperties: false
                required:
                  - id
                  - url
                  - branches_url
                  - branches_count
                  - open_schema_recommendations_count
                  - development_branches_count
                  - production_branches_count
                  - issues_count
                  - multiple_admins_required_for_deletion
                  - ready
                  - at_backup_restore_branches_limit
                  - at_development_branch_usage_limit
                  - data_import
                  - region
                  - html_url
                  - name
                  - state
                  - sharded
                  - default_branch_shard_count
                  - default_branch_read_only_regions_count
                  - default_branch_table_count
                  - default_branch
                  - require_approval_for_deploy
                  - resizing
                  - resize_queued
                  - allow_data_branching
                  - foreign_keys_enabled
                  - automatic_migrations
                  - restrict_branch_region
                  - insights_raw_queries
                  - plan
                  - insights_enabled
                  - production_branch_web_console
                  - migration_table_name
                  - migration_framework
                  - created_at
                  - updated_at
                  - schema_last_updated_at
                  - kind
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