# Source: https://planetscale.com/docs/api/reference/create_bouncer.md

# Create a bouncer

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

````yaml post /organizations/{organization}/databases/{database}/branches/{branch}/bouncers
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
  /organizations/{organization}/databases/{database}/branches/{branch}/bouncers:
    post:
      tags:
        - Bouncers
      summary: Create a bouncer
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
      operationId: create_bouncer
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
                name:
                  type: string
                  description: The bouncer name
                target:
                  type: string
                  description: The type of server the bouncer targets
                bouncer_size:
                  type: string
                  description: The size SKU for the bouncer
                replicas_per_cell:
                  type: integer
                  description: The number of replica servers per cell
              additionalProperties: false
      responses:
        '200':
          description: Returns the new bouncer
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the bouncer
                  name:
                    type: string
                    description: The name of the bouncer
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
                  target:
                    type: string
                    enum:
                      - primary
                      - replica
                      - replica_az_affinity
                    description: The instance type the bouncer targets
                  replicas_per_cell:
                    type: integer
                    description: The count of replicas in each cell
                  created_at:
                    type: string
                    description: When the bouncer was created
                  updated_at:
                    type: string
                    description: When the bouncer was updated
                  deleted_at:
                    type: string
                    description: When the bouncer was deleted
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
                  parameters:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The ID of the parameter
                        namespace:
                          type: string
                          enum:
                            - pgbouncer
                          description: The namespace of the parameter
                        name:
                          type: string
                          description: The name of the parameter
                        display_name:
                          type: string
                          description: The display name of the parameter
                        category:
                          type: string
                          description: The category of the parameter
                        description:
                          type: string
                          description: The description of the parameter
                        parameter_type:
                          type: string
                          enum:
                            - array
                            - boolean
                            - bytes
                            - float
                            - integer
                            - internal
                            - seconds
                            - select
                            - string
                            - time
                          description: The type of the parameter
                        default_value:
                          type: string
                          description: The default value of the parameter
                        value:
                          type: string
                          description: The configured value of the parameter
                        required:
                          type: boolean
                          description: Whether the parameter is required
                        created_at:
                          type: string
                          description: When the parameter was created
                        updated_at:
                          type: string
                          description: When the parameter was last updated
                        restart:
                          type: boolean
                          description: True if processes require a server restart on change
                        max:
                          type: number
                          description: The maximum value of the parameter
                        min:
                          type: number
                          description: The minimum value of the parameter
                        step:
                          type: number
                          description: The step change of the parameter
                        url:
                          type: string
                          description: The URL of the parameter
                        options:
                          items:
                            type: string
                          type: array
                          description: Valid options for the parameter value
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
                        - namespace
                        - name
                        - display_name
                        - category
                        - description
                        - parameter_type
                        - default_value
                        - value
                        - required
                        - created_at
                        - updated_at
                        - restart
                        - max
                        - min
                        - step
                        - url
                        - options
                        - actor
                additionalProperties: false
                required:
                  - id
                  - name
                  - sku
                  - target
                  - replicas_per_cell
                  - created_at
                  - updated_at
                  - deleted_at
                  - actor
                  - branch
                  - parameters
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