# Source: https://planetscale.com/docs/api/reference/list_keyspaces.md

# Get keyspaces

> 
### Authorization
A service token   must have at least one of the following access   in order to use this API endpoint:

**Service Token Accesses**
 `read_branch`





## OpenAPI

````yaml get /organizations/{organization}/databases/{database}/branches/{branch}/keyspaces
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
  /organizations/{organization}/databases/{database}/branches/{branch}/keyspaces:
    get:
      tags:
        - Database branch keyspaces
      summary: Get keyspaces
      description: >+

        ### Authorization

        A service token   must have at least one of the following access   in
        order to use this API endpoint:


        **Service Token Accesses**
         `read_branch`

      operationId: list_keyspaces
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
          description: Returns keyspaces
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
                          description: The ID of the keyspace
                        name:
                          type: string
                          description: Name of the keyspace
                        shards:
                          type: integer
                          description: The number of keyspace shards
                        sharded:
                          type: boolean
                          description: If the keyspace is sharded
                        replicas:
                          type: integer
                          description: Total number of replicas in the keyspace
                        extra_replicas:
                          type: integer
                          description: Number of extra replicas in the keyspace
                        created_at:
                          type: string
                          description: When the keyspace was created
                        updated_at:
                          type: string
                          description: When the keyspace was last updated
                        cluster_name:
                          type: string
                          description: The SKU representing the keyspace cluster size
                        cluster_display_name:
                          type: string
                          description: >-
                            The SKU representing the keyspace cluster size for
                            display
                        resizing:
                          type: boolean
                          description: Is the keyspace currently resizing
                        resize_pending:
                          type: boolean
                          description: Is the keyspace awaiting a resize
                        ready:
                          type: boolean
                          description: Is the keyspace provisioned and serving traffic
                        metal:
                          type: boolean
                          description: Is the keyspace running on metal instances
                        default:
                          type: boolean
                          description: Is this the default keyspace for the branch
                        imported:
                          type: boolean
                          description: Is this keyspace used in an import
                        vector_pool_allocation:
                          type: number
                          description: >-
                            Percentage of buffer pool memory allocated to vector
                            indexes
                        replication_durability_constraints:
                          type: object
                          properties:
                            strategy:
                              type: string
                              enum:
                                - available
                                - lag
                                - always
                              description: The replication durability strategy
                          additionalProperties: false
                          required:
                            - strategy
                        vreplication_flags:
                          type: object
                          properties:
                            optimize_inserts:
                              type: boolean
                              description: Enable optimized inserts
                            allow_no_blob_binlog_row_image:
                              type: boolean
                              description: Allow no blob binlog row image
                            vplayer_batching:
                              type: boolean
                              description: Enable VPlayer batching
                          additionalProperties: false
                          required:
                            - optimize_inserts
                            - allow_no_blob_binlog_row_image
                            - vplayer_batching
                      additionalProperties: false
                      required:
                        - id
                        - name
                        - shards
                        - sharded
                        - replicas
                        - extra_replicas
                        - created_at
                        - updated_at
                        - cluster_name
                        - cluster_display_name
                        - resizing
                        - resize_pending
                        - ready
                        - metal
                        - default
                        - imported
                        - vector_pool_allocation
                        - replication_durability_constraints
                        - vreplication_flags
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