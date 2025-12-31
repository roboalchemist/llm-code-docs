# Source: https://planetscale.com/docs/api/reference/get_deployment.md

# Get a deployment

> Get the deployment for a deploy request
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

````yaml get /organizations/{organization}/databases/{database}/deploy-requests/{number}/deployment
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
  /organizations/{organization}/databases/{database}/deploy-requests/{number}/deployment:
    get:
      tags:
        - Deploy requests
      summary: Get a deployment
      description: >-
        Get the deployment for a deploy request

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
      operationId: get_deployment
      parameters:
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
        - name: number
          in: path
          required: true
          description: The number of the deploy request
          schema:
            type: integer
      responses:
        '200':
          description: Returns the deployment for a deploy request
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the deployment
                  auto_cutover:
                    type: boolean
                    description: >-
                      Whether or not to automatically cutover once deployment is
                      finished
                  auto_delete_branch:
                    type: boolean
                    description: >-
                      Whether or not to automatically delete the head branch
                      once deployment is finished
                  created_at:
                    type: string
                    description: When the deployment was created
                  cutover_at:
                    type: string
                    description: When the cutover for the deployment was initiated
                  cutover_expiring:
                    type: boolean
                    description: Whether or not the deployment cutover will expire soon
                  deploy_check_errors:
                    type: string
                    description: Deploy check errors for the deployment
                  finished_at:
                    type: string
                    description: When the deployment was finished
                  queued_at:
                    type: string
                    description: When the deployment was queued
                  ready_to_cutover_at:
                    type: string
                    description: When the deployment was ready for cutover
                  started_at:
                    type: string
                    description: When the deployment was started
                  state:
                    type: string
                    enum:
                      - pending
                      - ready
                      - no_changes
                      - queued
                      - submitting
                      - in_progress
                      - pending_cutover
                      - in_progress_vschema
                      - in_progress_cancel
                      - in_progress_cutover
                      - complete
                      - complete_cancel
                      - complete_error
                      - complete_pending_revert
                      - in_progress_revert
                      - in_progress_revert_vschema
                      - complete_revert
                      - complete_revert_error
                      - cancelled
                      - error
                    description: The state the deployment is in
                  submitted_at:
                    type: string
                    description: When the deployment was submitted
                  updated_at:
                    type: string
                    description: When the deployment was last updated
                  into_branch:
                    type: string
                    description: >-
                      The name of the base branch the deployment will be merged
                      into
                  deploy_request_number:
                    type: integer
                    description: >-
                      The number of the deploy request associated with this
                      deployment
                  deployable:
                    type: boolean
                    description: Whether the deployment is deployable
                  preceding_deployments:
                    items:
                      type: object
                      additionalProperties: true
                    type: array
                    description: The deployments ahead of this one in the queue
                  deploy_operations:
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
                  deploy_operation_summaries:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The ID for the deploy operation summary
                        created_at:
                          type: string
                          description: When the deploy operation summary was created
                        deploy_errors:
                          type: string
                          description: Deploy errors for the deploy operation summary
                        ddl_statement:
                          type: string
                          description: The DDL statement for the deploy operation summary
                        eta_seconds:
                          type: integer
                          description: >-
                            The estimated seconds until completion for the
                            deploy operation summary
                        keyspace_name:
                          type: string
                          description: >-
                            The keyspace modified by the deploy operation
                            summary
                        operation_name:
                          type: string
                          description: The operation name of the deploy operation summary
                        progress_percentage:
                          type: number
                          description: >-
                            The percent completion for the deploy operation
                            summary
                        state:
                          type: string
                          enum:
                            - pending
                            - in_progress
                            - complete
                            - cancelled
                            - error
                          description: The state of the deploy operation summary
                        syntax_highlighted_ddl:
                          type: string
                          description: >-
                            A syntax-highlighted DDL statement for the deploy
                            operation summary
                        table_name:
                          type: string
                          description: >-
                            The name of the table modifed by the deploy
                            operation summary
                        table_recently_used_at:
                          type: string
                          description: >-
                            When the table modified by the deploy operation
                            summary was last used
                        throttled_at:
                          type: string
                          description: When the deploy operation summary was last throttled
                        removed_foreign_key_names:
                          items:
                            type: string
                          type: array
                          description: >-
                            Names of foreign keys removed by this operation
                            summary
                        shard_count:
                          type: integer
                          description: >-
                            The number of shards in the keyspace modified by the
                            deploy operation summary
                        shard_names:
                          items:
                            type: string
                          type: array
                          description: >-
                            Names of shards in the keyspace modified by the
                            deploy operation summary
                        can_drop_data:
                          type: boolean
                          description: >-
                            Whether or not the deploy operation summary is
                            capable of dropping data
                        table_recently_used:
                          type: boolean
                          description: >-
                            Whether or not the table modified by the deploy
                            operation summary was recently used
                        sharded:
                          type: boolean
                          description: >-
                            Whether or not the keyspace modified by the deploy
                            operation summary is sharded
                        operations:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: string
                                description: The ID for the deploy operation
                              shard:
                                type: string
                                description: >-
                                  The shard the deploy operation is being
                                  performed on
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
                              progress_percentage:
                                type: number
                                description: >-
                                  The percent completion for the deploy
                                  operation
                              eta_seconds:
                                type: integer
                                description: >-
                                  The estimated seconds until completion for the
                                  deploy operation
                            additionalProperties: false
                            required:
                              - id
                              - shard
                              - state
                              - progress_percentage
                              - eta_seconds
                      additionalProperties: false
                      required:
                        - id
                        - created_at
                        - deploy_errors
                        - ddl_statement
                        - eta_seconds
                        - keyspace_name
                        - operation_name
                        - progress_percentage
                        - state
                        - syntax_highlighted_ddl
                        - table_name
                        - table_recently_used_at
                        - throttled_at
                        - removed_foreign_key_names
                        - shard_count
                        - shard_names
                        - can_drop_data
                        - table_recently_used
                        - sharded
                        - operations
                  lint_errors:
                    items:
                      type: object
                      additionalProperties: true
                    type: array
                    description: >-
                      Schema lint errors preventing the deployment from
                      completing
                  sequential_diff_dependencies:
                    items:
                      type: object
                      additionalProperties: true
                    type: array
                    description: The schema dependencies that must be satisfied
                  lookup_vindex_operations:
                    items:
                      type: object
                      additionalProperties: true
                    type: array
                    description: Lookup Vitess index operations
                  throttler_configurations:
                    items:
                      type: object
                      additionalProperties: true
                    type: array
                    description: Deployment throttling configurations
                  deployment_revert_request:
                    type: object
                    additionalProperties: true
                    description: >-
                      The request to revert the schema operations in this
                      deployment
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
                  cutover_actor:
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
                  cancelled_actor:
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
                  schema_last_updated_at:
                    type: string
                    description: When the schema was last updated for the deployment
                  table_locked:
                    type: boolean
                    description: Whether or not the deployment has a table locked
                  locked_table_name:
                    type: string
                    description: The name of he table that is locked by the deployment
                  instant_ddl:
                    type: boolean
                    description: Whether or not the deployment is an instant DDL deployment
                  instant_ddl_eligible:
                    type: boolean
                    description: Whether or not the deployment is eligible for instant DDL
                additionalProperties: false
                required:
                  - id
                  - auto_cutover
                  - auto_delete_branch
                  - created_at
                  - cutover_at
                  - cutover_expiring
                  - deploy_check_errors
                  - finished_at
                  - queued_at
                  - ready_to_cutover_at
                  - started_at
                  - state
                  - submitted_at
                  - updated_at
                  - into_branch
                  - deploy_request_number
                  - deployable
                  - preceding_deployments
                  - deploy_operations
                  - deploy_operation_summaries
                  - lint_errors
                  - sequential_diff_dependencies
                  - lookup_vindex_operations
                  - throttler_configurations
                  - deployment_revert_request
                  - actor
                  - cutover_actor
                  - cancelled_actor
                  - schema_last_updated_at
                  - table_locked
                  - locked_table_name
                  - instant_ddl
                  - instant_ddl_eligible
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