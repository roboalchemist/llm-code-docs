# Source: https://planetscale.com/docs/api/reference/workflow_switch_replicas.md

# Switch replica traffic

> 




## OpenAPI

````yaml patch /organizations/{organization}/databases/{database}/workflows/{number}/switch-replicas
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
  /organizations/{organization}/databases/{database}/workflows/{number}/switch-replicas:
    patch:
      tags:
        - Workflows
      summary: Switch replica traffic
      description: |+

      operationId: workflow_switch_replicas
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization the workflow belongs to
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the database the workflow belongs to
          schema:
            type: string
        - name: number
          in: path
          required: true
          description: The sequence number of the workflow
          schema:
            type: integer
      responses:
        '200':
          description: Returns a workflow
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the workflow
                  name:
                    type: string
                    description: The name of the workflow
                  number:
                    type: integer
                    description: The sequence number of the workflow
                  state:
                    type: string
                    enum:
                      - pending
                      - copying
                      - running
                      - stopped
                      - verifying_data
                      - verified_data
                      - switching_replicas
                      - switched_replicas
                      - switching_primaries
                      - switched_primaries
                      - reversing_traffic
                      - reversing_traffic_for_cancel
                      - cutting_over
                      - cutover
                      - reversed_cutover
                      - completed
                      - cancelling
                      - cancelled
                      - error
                    description: The state of the workflow
                  created_at:
                    type: string
                    description: When the workflow was created
                  updated_at:
                    type: string
                    description: When the workflow was last updated
                  started_at:
                    type: string
                    description: When the workflow was started
                  completed_at:
                    type: string
                    description: When the workflow was completed
                  cancelled_at:
                    type: string
                    description: When the workflow was cancelled
                  reversed_at:
                    type: string
                    description: When the workflow was reversed
                  retried_at:
                    type: string
                    description: When the workflow was retried
                  data_copy_completed_at:
                    type: string
                    description: When the data copy was completed
                  cutover_at:
                    type: string
                    description: When the cutover was completed
                  replicas_switched:
                    type: boolean
                    description: Whether or not the replicas have been switched
                  primaries_switched:
                    type: boolean
                    description: Whether or not the primaries have been switched
                  switch_replicas_at:
                    type: string
                    description: When the replicas were switched
                  switch_primaries_at:
                    type: string
                    description: When the primaries were switched
                  verify_data_at:
                    type: string
                    description: When the data was verified
                  workflow_type:
                    type: string
                    enum:
                      - move_tables
                    description: The type of the workflow
                  workflow_subtype:
                    type: string
                    description: The subtype of the workflow
                  defer_secondary_keys:
                    type: boolean
                    description: Whether or not secondary keys are deferred
                  on_ddl:
                    type: string
                    enum:
                      - IGNORE
                      - STOP
                      - EXEC
                      - EXEC_IGNORE
                    description: The behavior when DDL changes during the workflow
                  workflow_errors:
                    type: string
                    description: The errors that occurred during the workflow
                  may_retry:
                    type: boolean
                    description: Whether or not the workflow may be retried
                  may_restart:
                    type: boolean
                    description: Whether or not the workflow may be restarted
                  verified_data_stale:
                    type: boolean
                    description: Whether or not the verified data is stale
                  sequence_tables_applied:
                    type: boolean
                    description: Whether or not sequence tables have been created
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
                  verify_data_by:
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
                  reversed_by:
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
                  switch_replicas_by:
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
                  switch_primaries_by:
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
                  cancelled_by:
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
                  completed_by:
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
                  retried_by:
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
                  cutover_by:
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
                  reversed_cutover_by:
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
                  source_keyspace:
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
                  target_keyspace:
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
                  global_keyspace:
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
                  - number
                  - state
                  - created_at
                  - updated_at
                  - started_at
                  - completed_at
                  - cancelled_at
                  - reversed_at
                  - retried_at
                  - data_copy_completed_at
                  - cutover_at
                  - replicas_switched
                  - primaries_switched
                  - switch_replicas_at
                  - switch_primaries_at
                  - verify_data_at
                  - workflow_type
                  - workflow_subtype
                  - defer_secondary_keys
                  - on_ddl
                  - workflow_errors
                  - may_retry
                  - may_restart
                  - verified_data_stale
                  - sequence_tables_applied
                  - actor
                  - verify_data_by
                  - reversed_by
                  - switch_replicas_by
                  - switch_primaries_by
                  - cancelled_by
                  - completed_by
                  - retried_by
                  - cutover_by
                  - reversed_cutover_by
                  - branch
                  - source_keyspace
                  - target_keyspace
                  - global_keyspace
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