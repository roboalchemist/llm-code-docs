# Source: https://planetscale.com/docs/api/reference/list_webhooks.md

# List webhooks

> List webhooks for a database
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_database`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `read_databases` |
| Database | `read_database` |



## OpenAPI

````yaml get /organizations/{organization}/databases/{database}/webhooks
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
  /organizations/{organization}/databases/{database}/webhooks:
    get:
      tags:
        - Webhooks
      summary: List webhooks
      description: >-
        List webhooks for a database

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_database`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `read_databases` |

        | Database | `read_database` |
      operationId: list_webhooks
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the database
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
          description: Returns a list of webhooks for a database
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
                          description: The ID of the webhook
                        url:
                          type: string
                          description: The URL the webhook will send events to
                        secret:
                          type: string
                          description: The secret used to sign the webhook payloads
                        enabled:
                          type: boolean
                          description: Whether the webhook is enabled
                        last_sent_result:
                          type: string
                          description: The last result sent by the webhook
                        last_sent_success:
                          type: boolean
                          description: Whether the last sent was successful
                        last_sent_at:
                          type: string
                          description: When the last event was sent
                        created_at:
                          type: string
                          description: When the webhook was created
                        updated_at:
                          type: string
                          description: When the webhook was updated
                        events:
                          items:
                            type: string
                            enum:
                              - branch.ready
                              - branch.anomaly
                              - branch.primary_promoted
                              - branch.schema_recommendation
                              - branch.sleeping
                              - branch.start_maintenance
                              - cluster.storage
                              - database.access_request
                              - deploy_request.closed
                              - deploy_request.errored
                              - deploy_request.in_progress
                              - deploy_request.opened
                              - deploy_request.pending_cutover
                              - deploy_request.queued
                              - deploy_request.reverted
                              - deploy_request.schema_applied
                              - keyspace.storage
                              - webhook.test
                          type: array
                          description: The events this webhook subscribes to
                      additionalProperties: false
                      required:
                        - id
                        - url
                        - secret
                        - enabled
                        - last_sent_result
                        - last_sent_success
                        - last_sent_at
                        - created_at
                        - updated_at
                        - events
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