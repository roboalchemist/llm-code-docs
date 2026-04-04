# Source: https://planetscale.com/docs/api/reference/lint_branch_schema.md

# Lint a branch schema

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

````yaml get /organizations/{organization}/databases/{database}/branches/{branch}/schema/lint
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
  /organizations/{organization}/databases/{database}/branches/{branch}/schema/lint:
    get:
      tags:
        - Database branches
      summary: Lint a branch schema
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
      operationId: lint_branch_schema
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
          description: Returns a list of schema errors for a branch
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
                        lint_error:
                          type: string
                          description: Code representing the type of error
                        subject_type:
                          type: string
                          enum:
                            - table
                            - vschema
                            - routing_rules
                          description: The subject for the errors
                        keyspace_name:
                          type: string
                          description: The keyspace of the schema with the error
                        table_name:
                          type: string
                          description: The table with the error
                        error_description:
                          type: string
                          description: A description for the error that occurred
                        docs_url:
                          type: string
                          description: A link to the documentation related to the error
                        column_name:
                          type: string
                          description: The column in a table relevant to the error
                        foreign_key_column_names:
                          items:
                            type: string
                          type: array
                          description: A list of invalid foreign key columns in a table
                        auto_increment_column_names:
                          items:
                            type: string
                          type: array
                          description: A list of invalid auto-incremented columns
                        charset_name:
                          type: string
                          description: The charset of the schema
                        engine_name:
                          type: string
                          description: The engine of the schema
                        vindex_name:
                          type: string
                          description: The name of the vindex for the schema
                        json_path:
                          type: string
                          description: The path for an invalid JSON column
                        check_constraint_name:
                          type: string
                          description: The name of the invalid check constraint
                        enum_value:
                          type: string
                          description: The name of the invalid enum value
                        partitioning_type:
                          type: string
                          description: The name of the invalid partitioning type
                        partition_name:
                          type: string
                          description: The name of the invalid partition in the schema
                      additionalProperties: false
                      required:
                        - lint_error
                        - subject_type
                        - keyspace_name
                        - table_name
                        - error_description
                        - docs_url
                        - column_name
                        - foreign_key_column_names
                        - auto_increment_column_names
                        - charset_name
                        - engine_name
                        - vindex_name
                        - json_path
                        - check_constraint_name
                        - enum_value
                        - partitioning_type
                        - partition_name
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