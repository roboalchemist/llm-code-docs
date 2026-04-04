# Source: https://planetscale.com/docs/api/reference/disable_safe_migrations.md

# Disable safe migrations for a branch

> 




## OpenAPI

````yaml delete /organizations/{organization}/databases/{database}/branches/{branch}/safe-migrations
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
  /organizations/{organization}/databases/{database}/branches/{branch}/safe-migrations:
    delete:
      tags:
        - Database branches
      summary: Disable safe migrations for a branch
      description: |+

      operationId: disable_safe_migrations
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization the branch belongs to
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the database the branch belongs to
          schema:
            type: string
        - name: branch
          in: path
          required: true
          description: The name of the branch
          schema:
            type: string
      responses:
        '200':
          description: Returns the branch with safe migrations disabled
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the branch
                  name:
                    type: string
                    description: The name of the branch
                  created_at:
                    type: string
                    description: When the branch was created
                  updated_at:
                    type: string
                    description: When the branch was last updated
                  deleted_at:
                    type: string
                    description: When the branch was deleted
                  restore_checklist_completed_at:
                    type: string
                    description: >-
                      When a user last marked a backup restore checklist as
                      completed
                  schema_last_updated_at:
                    type: string
                    description: When the schema for the branch was last updated
                  kind:
                    type: string
                    enum:
                      - mysql
                      - postgresql
                    description: The kind of branch
                  mysql_address:
                    type: string
                    description: The MySQL address for the branch
                  mysql_edge_address:
                    type: string
                    description: The address of the MySQL provider for the branch
                  state:
                    type: string
                    enum:
                      - pending
                      - sleep_in_progress
                      - sleeping
                      - awakening
                      - ready
                    description: The current state of the branch
                  direct_vtgate:
                    type: boolean
                    description: >-
                      True if the branch allows passwords to connect directly to
                      a vtgate, bypassing load balancers
                  vtgate_size:
                    type: string
                    description: The size of the vtgate cluster for the branch
                  vtgate_count:
                    type: integer
                    description: The number of vtgate instances in the branch
                  cluster_name:
                    type: string
                    description: The SKU representing the branch's cluster size
                  cluster_iops:
                    type: integer
                    description: IOPS for the cluster
                  ready:
                    type: boolean
                    description: Whether or not the branch is ready to serve queries
                  schema_ready:
                    type: boolean
                    description: Whether or not the schema is ready for queries
                  metal:
                    type: boolean
                    description: Whether or not this is a metal database
                  production:
                    type: boolean
                    description: Whether or not the branch is a production branch
                  safe_migrations:
                    type: boolean
                    description: Whether or not the branch has safe migrations enabled
                  sharded:
                    type: boolean
                    description: Whether or not the branch is sharded
                  shard_count:
                    type: integer
                    description: The number of shards in the branch
                  stale_schema:
                    type: boolean
                    description: Whether or not the branch has a stale schema
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
                  restored_from_branch:
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
                  private_edge_connectivity:
                    type: boolean
                    description: True if private connections are enabled
                  has_replicas:
                    type: boolean
                    description: True if the branch has replica servers
                  has_read_only_replicas:
                    type: boolean
                    description: True if the branch has read-only replica servers
                  html_url:
                    type: string
                    description: Planetscale app URL for the branch
                  url:
                    type: string
                    description: Planetscale API URL for the branch
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
                  parent_branch:
                    type: string
                    description: >-
                      The name of the parent branch from which the branch was
                      created
                additionalProperties: false
                required:
                  - id
                  - name
                  - created_at
                  - updated_at
                  - deleted_at
                  - restore_checklist_completed_at
                  - schema_last_updated_at
                  - kind
                  - mysql_address
                  - mysql_edge_address
                  - state
                  - direct_vtgate
                  - vtgate_size
                  - vtgate_count
                  - cluster_name
                  - cluster_iops
                  - ready
                  - schema_ready
                  - metal
                  - production
                  - safe_migrations
                  - sharded
                  - shard_count
                  - stale_schema
                  - actor
                  - restored_from_branch
                  - private_edge_connectivity
                  - has_replicas
                  - has_read_only_replicas
                  - html_url
                  - url
                  - region
                  - parent_branch
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