# Source: https://planetscale.com/docs/api/reference/update_database_throttler.md

# Update database throttler configurations

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_deploy_request`, `create_deploy_request`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `deploy_deploy_requests` |
| Database | `deploy_deploy_requests` |



## OpenAPI

````yaml patch /organizations/{organization}/databases/{database}/throttler
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
  /organizations/{organization}/databases/{database}/throttler:
    patch:
      tags:
        - Databases
      summary: Update database throttler configurations
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_deploy_request`, `create_deploy_request`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `deploy_deploy_requests` |

        | Database | `deploy_deploy_requests` |
      operationId: update_database_throttler
      parameters:
        - name: organization
          in: path
          required: true
          description: >-
            The name of the organization that the throttled deploy requests
            belong to
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: >-
            The name of the database that the throttled deploy requests belong
            to
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                ratio:
                  type: integer
                  description: >-
                    A throttler ratio between 0 and 95 that will apply to all
                    keyspaces in the database. 0 effectively disables throttler,
                    while 95 drastically slows down deploy request migrations
                configurations:
                  type: array
                  items:
                    type: string
                  description: >-
                    If specifying throttler ratios per keyspace, an array of {
                    "keyspace_name": "mykeyspace", "ratio": 10 }, one for each
                    eligible keyspace
              additionalProperties: false
      responses:
        '200':
          description: Database throttler configurations
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  keyspaces:
                    items:
                      type: string
                    type: array
                    description: >-
                      Keyspaces that are eligible for throttler configuration in
                      the configurable resource (database or deploy request)
                  configurable:
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
                  configurations:
                    type: array
                    items:
                      type: object
                      properties:
                        keyspace_name:
                          type: string
                          description: Name of keyspace this throttler ratio applies to
                        ratio:
                          type: number
                          description: >-
                            A throttler ratio between 0 and 95 that applies to
                            migrations in this specific keyspace
                      additionalProperties: false
                      required:
                        - keyspace_name
                        - ratio
                additionalProperties: false
                required:
                  - keyspaces
                  - configurable
                  - configurations
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