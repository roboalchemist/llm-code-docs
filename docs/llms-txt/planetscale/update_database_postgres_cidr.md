# Source: https://planetscale.com/docs/api/reference/update_database_postgres_cidr.md

# Update an IP restriction entry

> 
### Authorization
A   OAuth token must have at least one of the following   scopes in order to use this API endpoint:

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `write_databases` |
| Database | `write_database` |



## OpenAPI

````yaml put /organizations/{organization}/databases/{database}/cidrs/{id}
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
  /organizations/{organization}/databases/{database}/cidrs/{id}:
    put:
      tags:
        - Database Postgres IP restrictions
      summary: Update an IP restriction entry
      description: >-

        ### Authorization

        A   OAuth token must have at least one of the following   scopes in
        order to use this API endpoint:


        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `write_databases` |

        | Database | `write_database` |
      operationId: update_database_postgres_cidr
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization the database belongs to
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the database
          schema:
            type: string
        - name: id
          in: path
          required: true
          description: The ID of the IP restriction entry
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                schema:
                  type: string
                  description: >-
                    The PostgreSQL schema to restrict access to. Leave empty to
                    allow access to all schemas.
                role:
                  type: string
                  description: >-
                    The PostgreSQL role to restrict access to. Leave empty to
                    allow access for all roles.
                cidrs:
                  type: array
                  items:
                    type: string
                  description: >-
                    List of IPv4 CIDR ranges (e.g., ['192.168.1.0/24',
                    '192.168.1.1/32']). Only provided fields will be updated.
              additionalProperties: false
      responses:
        '200':
          description: Returns the updated IP restriction entry
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the IP allowlist entry
                  schema:
                    type: string
                    description: The schema name to restrict access to (optional)
                  role:
                    type: string
                    description: The role to restrict access to (optional)
                  cidrs:
                    items:
                      type: string
                    type: array
                    description: List of CIDR ranges
                  created_at:
                    type: string
                    description: When the entry was created
                  updated_at:
                    type: string
                    description: When the entry was updated
                  deleted_at:
                    type: string
                    description: When the entry was deleted
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
                  - schema
                  - role
                  - cidrs
                  - created_at
                  - updated_at
                  - deleted_at
                  - actor
        '401':
          description: Unauthorized
        '403':
          description: Forbidden
        '404':
          description: Not Found
        '422':
          description: Unprocessable Entity - Invalid parameters or validation errors
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