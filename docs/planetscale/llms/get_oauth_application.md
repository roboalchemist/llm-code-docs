# Source: https://planetscale.com/docs/api/reference/get_oauth_application.md

# Get an OAuth application

> 
### Authorization
A service token   must have at least one of the following access   in order to use this API endpoint:

**Service Token Accesses**
 `read_oauth_applications`





## OpenAPI

````yaml get /organizations/{organization}/oauth-applications/{application_id}
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
  /organizations/{organization}/oauth-applications/{application_id}:
    get:
      tags:
        - OAuth applications
      summary: Get an OAuth application
      description: >+

        ### Authorization

        A service token   must have at least one of the following access   in
        order to use this API endpoint:


        **Service Token Accesses**
         `read_oauth_applications`

      operationId: get_oauth_application
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization the OAuth application belongs to
          schema:
            type: string
        - name: application_id
          in: path
          required: true
          description: The ID of the OAuth application
          schema:
            type: string
      responses:
        '200':
          description: Returns information abuot an OAuth application
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the app
                  name:
                    type: string
                    description: The name of the app
                  redirect_uri:
                    type: string
                    description: The redirect URI of the OAuth application
                  domain:
                    type: string
                    description: >-
                      The domain of the OAuth application. Used for verification
                      of a valid redirect uri
                  created_at:
                    type: string
                    description: When the OAuth application was created
                  updated_at:
                    type: string
                    description: When the OAuth application was last updated
                  scopes:
                    items:
                      type: string
                    type: array
                    description: >-
                      The scopes that the OAuth application requires on a user
                      account
                  avatar:
                    type: string
                    description: The image source for the OAuth application's avatar
                  client_id:
                    type: string
                    description: The OAuth application's unique client id
                  tokens:
                    type: integer
                    description: The number of tokens issued by the OAuth application
                additionalProperties: false
                required:
                  - id
                  - name
                  - redirect_uri
                  - domain
                  - created_at
                  - updated_at
                  - scopes
                  - avatar
                  - client_id
                  - tokens
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