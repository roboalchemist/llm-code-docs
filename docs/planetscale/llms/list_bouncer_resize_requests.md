# Source: https://planetscale.com/docs/api/reference/list_bouncer_resize_requests.md

# Get bouncer resize requests

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_branch`, `delete_branch`, `create_branch`, `connect_production_branch`, `connect_branch`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `read_branches` |
| Database | `read_branches` |
| Branch | `read_branch` |



## OpenAPI

````yaml get /organizations/{organization}/databases/{database}/branches/{branch}/bouncers/{bouncer}/resizes
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
  /organizations/{organization}/databases/{database}/branches/{branch}/bouncers/{bouncer}/resizes:
    get:
      tags:
        - Bouncer resizes
      summary: Get bouncer resize requests
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_branch`, `delete_branch`, `create_branch`, `connect_production_branch`, `connect_branch`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `read_branches` |

        | Database | `read_branches` |

        | Branch | `read_branch` |
      operationId: list_bouncer_resize_requests
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
        - name: bouncer
          in: path
          required: true
          description: The name of the bouncer
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
          description: Returns bouncer resize requests
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
                          description: The ID of the bouncer resize
                        state:
                          type: string
                          enum:
                            - pending
                            - resizing
                            - canceled
                            - completed
                          description: The state of the bouncer resize
                        replicas_per_cell:
                          type: integer
                          description: >-
                            The number of replicas per cell for the bouncer
                            after the resize
                        parameters:
                          type: object
                          additionalProperties: true
                          description: The bouncer parameters
                        previous_replicas_per_cell:
                          type: integer
                          description: >-
                            The number of replicas per cell for the bouncer
                            before the resize
                        previous_parameters:
                          type: object
                          additionalProperties: true
                          description: The previous bouncer parameters
                        started_at:
                          type: string
                          description: The time the bouncer resize started
                        completed_at:
                          type: string
                          description: The time the bouncer resize completed
                        created_at:
                          type: string
                          description: The time the bouncer resize was created
                        updated_at:
                          type: string
                          description: The time the bouncer resize was last updated
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
                        bouncer:
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
                        sku:
                          type: object
                          properties:
                            name:
                              type: string
                              description: The name of the Postgres bouncer SKU
                            display_name:
                              type: string
                              description: The display name
                            cpu:
                              type: string
                              description: The CPU allocation
                            ram:
                              type: integer
                              description: The amount of memory in bytes
                            sort_order:
                              type: integer
                              description: The sort order of the Postgres bouncer SKU
                          additionalProperties: false
                          required:
                            - name
                            - display_name
                            - cpu
                            - ram
                            - sort_order
                        previous_sku:
                          type: object
                          properties:
                            name:
                              type: string
                              description: The name of the Postgres bouncer SKU
                            display_name:
                              type: string
                              description: The display name
                            cpu:
                              type: string
                              description: The CPU allocation
                            ram:
                              type: integer
                              description: The amount of memory in bytes
                            sort_order:
                              type: integer
                              description: The sort order of the Postgres bouncer SKU
                          additionalProperties: false
                          required:
                            - name
                            - display_name
                            - cpu
                            - ram
                            - sort_order
                      additionalProperties: false
                      required:
                        - id
                        - state
                        - replicas_per_cell
                        - parameters
                        - previous_replicas_per_cell
                        - previous_parameters
                        - started_at
                        - completed_at
                        - created_at
                        - updated_at
                        - actor
                        - bouncer
                        - sku
                        - previous_sku
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