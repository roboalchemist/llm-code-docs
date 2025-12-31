# Source: https://planetscale.com/docs/api/reference/list_extensions.md

# List cluster extensions

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

````yaml get /organizations/{organization}/databases/{database}/branches/{branch}/extensions
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
  /organizations/{organization}/databases/{database}/branches/{branch}/extensions:
    get:
      tags:
        - Cluster extensions
      summary: List cluster extensions
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
      operationId: list_extensions
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
      responses:
        '200':
          description: Returns cluster extensions
          headers: {}
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The ID of the extension
                    name:
                      type: string
                      description: The name of the extension
                    description:
                      type: string
                      description: The description of the extension
                    internal:
                      type: boolean
                      description: The internal state of the extension
                    url:
                      type: string
                      description: The URL of the extension
                    parameters:
                      type: array
                      items:
                        type: object
                        properties:
                          id:
                            type: string
                            description: The ID of the parameter
                          name:
                            type: string
                            description: The name of the parameter
                          display_name:
                            type: string
                            description: The display name of the parameter
                          namespace:
                            type: string
                            enum:
                              - patroni
                              - pgconf
                              - pgbouncer
                            description: The namespace of the parameter
                          category:
                            type: string
                            description: The category of the parameter
                          description:
                            type: string
                            description: The description of the parameter
                          extension:
                            type: boolean
                            description: Configures an extension
                          internal:
                            type: boolean
                            description: The internal state of the parameter
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
                            description: >-
                              True if processes require a server restart on
                              change
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
                          - name
                          - display_name
                          - namespace
                          - category
                          - description
                          - extension
                          - internal
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
                    - description
                    - internal
                    - url
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