# Source: https://planetscale.com/docs/api/reference/update_branch_change_request.md

# Upsert a change request

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `write_database`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `write_databases` |
| Database | `write_database` |



## OpenAPI

````yaml patch /organizations/{organization}/databases/{database}/branches/{branch}/changes
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
  /organizations/{organization}/databases/{database}/branches/{branch}/changes:
    patch:
      tags:
        - Branch changes
      summary: Upsert a change request
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `write_database`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `write_databases` |

        | Database | `write_database` |
      operationId: update_branch_change_request
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                cluster_size:
                  type: string
                  description: >-
                    The size of the cluster. Available sizes can be found using
                    the 'List cluster sizes' endpoint.
                replicas:
                  type: integer
                  description: The total number of replicas
                parameters:
                  type: object
                  additionalProperties: true
                  description: >-
                    Cluster configuration parameters nested by namespace (e.g.,
                    {"pgconf": {"max_connections": "200"}}). Use the 'List
                    cluster parameters' endpoint to retrieve available
                    parameters. Supported namespaces include 'patroni',
                    'pgconf', and 'pgbouncer'.
              additionalProperties: false
      responses:
        '200':
          description: Returns the branch change request
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the branch change request
                  restart:
                    items:
                      type: integer
                    type: array
                    description: The ports requiring a restart when changes are applied
                  state:
                    type: string
                    enum:
                      - queued
                      - pending
                      - resizing
                      - canceled
                      - completed
                    description: The state of the branch change request
                  started_at:
                    type: string
                    description: The time the branch change request started
                  completed_at:
                    type: string
                    description: The time the branch change request completed
                  created_at:
                    type: string
                    description: The time the branch change request was created
                  updated_at:
                    type: string
                    description: The time the branch change request was last updated
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
                  cluster_name:
                    type: string
                    description: The SKU representing the branch cluster
                  cluster_display_name:
                    type: string
                    description: The SKU representing the branch cluster for display
                  cluster_metal:
                    type: boolean
                    description: Whether or not this is a metal database
                  replicas:
                    type: integer
                    description: The total number of replicas
                  parameters:
                    type: object
                    additionalProperties: true
                    description: The branch parameters
                  previous_cluster_name:
                    type: string
                    description: The previous SKU representing the branch cluster
                  previous_cluster_display_name:
                    type: string
                    description: >-
                      The previous SKU representing the branch cluster for
                      display
                  previous_cluster_metal:
                    type: boolean
                    description: Whether or not the previous SKU was a metal database
                  previous_replicas:
                    type: integer
                    description: The previous total number of replicas
                  previous_parameters:
                    type: object
                    additionalProperties: true
                    description: The previous branch parameters
                  minimum_storage_bytes:
                    type: integer
                    description: The minimum storage size in bytes
                  maximum_storage_bytes:
                    type: integer
                    description: The maximum storage size in bytes
                  storage_autoscaling:
                    type: boolean
                    description: Whether storage autoscaling is enabled
                  storage_shrinking:
                    type: boolean
                    description: >-
                      Whether storage shrinking is enabled when autoscaling is
                      enabled
                  storage_type:
                    type: string
                    enum:
                      - gp3
                      - io2
                      - pd_ssd
                    description: The storage type (gp3 or io2)
                  storage_iops:
                    type: integer
                    description: The storage IOPS
                  storage_throughput_mibs:
                    type: integer
                    description: The storage throughput in MiB/s
                  previous_minimum_storage_bytes:
                    type: integer
                    description: The previous minimum storage size in bytes
                  previous_maximum_storage_bytes:
                    type: integer
                    description: The previous maximum storage size in bytes
                  previous_storage_autoscaling:
                    type: boolean
                    description: Whether storage autoscaling was previously enabled
                  previous_storage_shrinking:
                    type: boolean
                    description: Whether storage shrinking was previously enabled
                  previous_storage_type:
                    type: string
                    description: The previous storage type
                  previous_storage_iops:
                    type: integer
                    description: The previous storage IOPS
                  previous_storage_throughput_mibs:
                    type: integer
                    description: The previous storage throughput in MiB/s
                additionalProperties: false
                required:
                  - id
                  - restart
                  - state
                  - started_at
                  - completed_at
                  - created_at
                  - updated_at
                  - actor
                  - cluster_name
                  - cluster_display_name
                  - cluster_metal
                  - replicas
                  - parameters
                  - previous_cluster_name
                  - previous_cluster_display_name
                  - previous_cluster_metal
                  - previous_replicas
                  - previous_parameters
                  - minimum_storage_bytes
                  - maximum_storage_bytes
                  - storage_autoscaling
                  - storage_shrinking
                  - storage_type
                  - storage_iops
                  - storage_throughput_mibs
                  - previous_minimum_storage_bytes
                  - previous_maximum_storage_bytes
                  - previous_storage_autoscaling
                  - previous_storage_shrinking
                  - previous_storage_type
                  - previous_storage_iops
                  - previous_storage_throughput_mibs
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