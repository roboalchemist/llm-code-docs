# Source: https://planetscale.com/docs/api/reference/update_keyspace_vschema.md

# Update the VSchema for the keyspace

> 
### Authorization
A service token   must have at least one of the following access   in order to use this API endpoint:

**Service Token Accesses**
 `write_production_branch_vschema`, `write_branch_vschema`





## OpenAPI

````yaml patch /organizations/{organization}/databases/{database}/branches/{branch}/keyspaces/{keyspace}/vschema
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
  /organizations/{organization}/databases/{database}/branches/{branch}/keyspaces/{keyspace}/vschema:
    patch:
      tags:
        - Keyspace VSchemas
      summary: Update the VSchema for the keyspace
      description: >+

        ### Authorization

        A service token   must have at least one of the following access   in
        order to use this API endpoint:


        **Service Token Accesses**
         `write_production_branch_vschema`, `write_branch_vschema`

      operationId: update_keyspace_vschema
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
        - name: keyspace
          in: path
          required: true
          description: The name of the keyspace
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                vschema:
                  type: string
                  description: The new VSchema for the keyspace
              additionalProperties: false
              required:
                - vschema
      responses:
        '200':
          description: Returns the VSchema for the keyspace
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  raw:
                    type: string
                    description: The keyspace's VSchema
                additionalProperties: false
                required:
                  - raw
        '401':
          description: Unauthorized
        '403':
          description: Forbidden
        '404':
          description: Not Found
        '422':
          description: Unprocessable Content
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