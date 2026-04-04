# Source: https://planetscale.com/docs/api/reference/create_backup.md

# Create a backup

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `write_backups`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `write_backups` |
| Database | `write_backups` |
| Branch | `write_backups` |



## OpenAPI

````yaml post /organizations/{organization}/databases/{database}/branches/{branch}/backups
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
  /organizations/{organization}/databases/{database}/branches/{branch}/backups:
    post:
      tags:
        - Backups
      summary: Create a backup
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `write_backups`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `write_backups` |

        | Database | `write_backups` |

        | Branch | `write_backups` |
      operationId: create_backup
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Name for the backup
                retention_unit:
                  type: string
                  enum:
                    - hour
                    - day
                    - week
                    - month
                    - year
                  description: Unit for the retention period of the backup
                retention_value:
                  type: integer
                  description: >-
                    Value between `1` and `1000` for the retention period of the
                    backup (i.e retention_value `6` and retention_unit `hour`
                    means 6 hours)
                emergency:
                  type: boolean
                  description: >-
                    Whether the backup is an immediate backup that may affect
                    database performance. Emergency backups are only supported
                    for PostgreSQL databases.
              additionalProperties: false
      responses:
        '201':
          description: Returns the created database branch backup
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the backup
                  name:
                    type: string
                    description: The name of the backup
                  state:
                    type: string
                    enum:
                      - pending
                      - running
                      - success
                      - failed
                      - canceled
                      - ignored
                    description: The current state of the backup
                  size:
                    type: integer
                    description: The size of the backup in bytes
                  estimated_storage_cost:
                    type: number
                    description: The estimated storage cost of the backup
                  created_at:
                    type: string
                    description: When the backup was created
                  updated_at:
                    type: string
                    description: When the backup was last updated
                  started_at:
                    type: string
                    description: When the backup started
                  expires_at:
                    type: string
                    description: When the backup expires
                  completed_at:
                    type: string
                    description: When the backup completed
                  deleted_at:
                    type: string
                    description: When the backup was deleted
                  pvc_size:
                    type: integer
                    description: Size of the PVC used for the backup
                  protected:
                    type: boolean
                    description: Whether or not the backup is protected from deletion
                  required:
                    type: boolean
                    description: Whether or not the backup policy is required
                  restored_branches:
                    type: array
                    items:
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
                  backup_policy:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The ID of the backup policy
                      name:
                        type: string
                        description: The name of the backup policy
                      target:
                        type: string
                        enum:
                          - production
                          - development
                        description: >-
                          Whether the policy is for production or development
                          branches
                      retention_value:
                        type: integer
                        description: >-
                          A number value for the retention period of the backup
                          policy
                      retention_unit:
                        type: string
                        description: The unit for the retention period of the backup policy
                      frequency_value:
                        type: integer
                        description: A number value for the frequency of the backup policy
                      frequency_unit:
                        type: string
                        description: The unit for the frequency of the backup policy
                      schedule_time:
                        type: string
                        description: >-
                          The time of day that the backup is scheduled, in HH:MM
                          format
                      schedule_day:
                        type: integer
                        description: >-
                          Day of the week that the backup is scheduled. 0 is
                          Sunday, 6 is Saturday
                      schedule_week:
                        type: integer
                        description: >-
                          Week of the month that the backup is scheduled. 0 is
                          the first week, 3 is the fourth week
                      created_at:
                        type: string
                        description: When the backup policy was created
                      updated_at:
                        type: string
                        description: When the backup policy was last updated
                      last_ran_at:
                        type: string
                        description: When the backup was last run
                      next_run_at:
                        type: string
                        description: When the backup will next run
                      required:
                        type: boolean
                        description: Whether the policy is a required system backup
                    additionalProperties: false
                    required:
                      - id
                      - name
                      - target
                      - retention_value
                      - retention_unit
                      - frequency_value
                      - frequency_unit
                      - schedule_time
                      - schedule_day
                      - schedule_week
                      - created_at
                      - updated_at
                      - last_ran_at
                      - next_run_at
                      - required
                  schema_snapshot:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The ID of the schema snapshot
                      name:
                        type: string
                        description: The name of the schema snapshot
                      created_at:
                        type: string
                        description: When the schema snapshot was created
                      updated_at:
                        type: string
                        description: When the schema snapshot was last updated
                      linted_at:
                        type: string
                        description: When the schema snapshot was last linted
                      url:
                        type: string
                        description: The URL to the schema snapshot in the PlanetScale app
                    additionalProperties: false
                    required:
                      - id
                      - name
                      - created_at
                      - updated_at
                      - linted_at
                      - url
                  database_branch:
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
                additionalProperties: false
                required:
                  - id
                  - name
                  - state
                  - size
                  - estimated_storage_cost
                  - created_at
                  - updated_at
                  - started_at
                  - expires_at
                  - completed_at
                  - deleted_at
                  - pvc_size
                  - protected
                  - required
                  - restored_branches
                  - actor
                  - backup_policy
                  - schema_snapshot
                  - database_branch
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