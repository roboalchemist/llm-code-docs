# Source: https://planetscale.com/docs/api/reference/remove_organization_member.md

# Remove a member from an organization

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `write_organization`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `write_organization` |



## OpenAPI

````yaml delete /organizations/{organization}/members/{id}
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
  /organizations/{organization}/members/{id}:
    delete:
      tags:
        - Organization members
      summary: Remove a member from an organization
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `write_organization`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `write_organization` |
      operationId: remove_organization_member
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization
          schema:
            type: string
        - name: id
          in: path
          required: true
          description: The ID of the user
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                delete_passwords:
                  type: boolean
                  description: >-
                    Whether to delete all passwords associated with the member.
                    Only available when removing other members (not yourself).
                delete_service_tokens:
                  type: boolean
                  description: >-
                    Whether to delete all service tokens associated with the
                    member. Only available when removing other members (not
                    yourself).
              additionalProperties: false
      responses:
        '204':
          description: >-
            Member removed successfully. Note: Cannot remove the last admin or
            leave your only organization.
          headers: {}
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