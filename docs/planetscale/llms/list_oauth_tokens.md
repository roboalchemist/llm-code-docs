# Source: https://planetscale.com/docs/api/reference/list_oauth_tokens.md

# List OAuth tokens

> List OAuth tokens created by an OAuth application
### Authorization
A service token   must have at least one of the following access   in order to use this API endpoint:

**Service Token Accesses**
 `read_oauth_tokens`





## OpenAPI

````yaml get /organizations/{organization}/oauth-applications/{application_id}/tokens
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
  /organizations/{organization}/oauth-applications/{application_id}/tokens:
    get:
      tags:
        - OAuth applications
      summary: List OAuth tokens
      description: >+
        List OAuth tokens created by an OAuth application

        ### Authorization

        A service token   must have at least one of the following access   in
        order to use this API endpoint:


        **Service Token Accesses**
         `read_oauth_tokens`

      operationId: list_oauth_tokens
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
          description: Returns the OAuth tokens issued on behalf of the OAuth application
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
                          description: The ID of the service token
                        name:
                          type: string
                          description: The name of the service token
                        display_name:
                          type: string
                          description: The display name of the service token
                        token:
                          type: string
                          description: The plaintext token. Available only after create.
                        plain_text_refresh_token:
                          type: string
                          description: >-
                            The plaintext refresh token. Available only after
                            create.
                        avatar_url:
                          type: string
                          description: The image source for the avatar of the service token
                        created_at:
                          type: string
                          description: When the service token was created
                        updated_at:
                          type: string
                          description: When the service token was last updated
                        expires_at:
                          type: string
                          description: When the service token will expire
                        last_used_at:
                          type: string
                          description: When the service token was last used
                        actor_id:
                          type: string
                          description: >-
                            The ID of the actor on whose behalf the service
                            token was created
                        actor_display_name:
                          type: string
                          description: >-
                            The name of the actor on whose behalf the service
                            token was created
                        actor_type:
                          type: string
                          description: >-
                            The type of the actor on whose behalf the service
                            token was created
                        service_token_accesses:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: string
                                description: The ID of the service token access
                              access:
                                type: string
                                description: The name of the service token access
                              description:
                                type: string
                                description: The description of the service token access
                              resource_name:
                                type: string
                                description: >-
                                  The name of the resource the service token
                                  access gives access to
                              resource_id:
                                type: string
                                description: >-
                                  The ID of the resource the service token
                                  access gives access to
                              resource_type:
                                type: string
                                description: >-
                                  The type of the resource the service token
                                  access gives access to
                              resource:
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
                            additionalProperties: false
                            required:
                              - id
                              - access
                              - description
                              - resource_name
                              - resource_id
                              - resource_type
                              - resource
                        oauth_accesses_by_resource:
                          type: object
                          properties:
                            database:
                              type: object
                              properties:
                                databases:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: >-
                                          the name of the database the token has
                                          access to
                                      id:
                                        type: string
                                        description: >-
                                          the id of the database the token has
                                          access to
                                      organization:
                                        type: string
                                        description: the name of the database's organization
                                      url:
                                        type: string
                                        description: the planetscale app url for the database
                                    additionalProperties: false
                                    required:
                                      - name
                                      - id
                                      - organization
                                      - url
                                accesses:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: The name of the access scope
                                      description:
                                        type: string
                                        description: The scope description
                                    additionalProperties: false
                                    required:
                                      - name
                                      - description
                              additionalProperties: false
                              required:
                                - databases
                                - accesses
                            organization:
                              type: object
                              properties:
                                organizations:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: the name of the organization
                                      id:
                                        type: string
                                        description: the id of the organization
                                      url:
                                        type: string
                                        description: >-
                                          the planetscale app url for the
                                          organization
                                    additionalProperties: false
                                    required:
                                      - name
                                      - id
                                      - url
                                accesses:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: The name of the access scope
                                      description:
                                        type: string
                                        description: The scope description
                                    additionalProperties: false
                                    required:
                                      - name
                                      - description
                              additionalProperties: false
                              required:
                                - organizations
                                - accesses
                            branch:
                              type: object
                              properties:
                                branches:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: the name of the branch
                                      id:
                                        type: string
                                        description: the id of the branch
                                      database:
                                        type: string
                                        description: >-
                                          the name of the database the branch
                                          belongs to
                                      organization:
                                        type: string
                                        description: >-
                                          the name of the organization the branch
                                          belongs to
                                      url:
                                        type: string
                                        description: the planetscale app url for the branch
                                    additionalProperties: false
                                    required:
                                      - name
                                      - id
                                      - database
                                      - organization
                                      - url
                                accesses:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: The name of the access scope
                                      description:
                                        type: string
                                        description: The scope description
                                    additionalProperties: false
                                    required:
                                      - name
                                      - description
                              additionalProperties: false
                              required:
                                - branches
                                - accesses
                            user:
                              type: object
                              properties:
                                users:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: the name of the user
                                      id:
                                        type: string
                                        description: the id of the user
                                    additionalProperties: false
                                    required:
                                      - name
                                      - id
                                accesses:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: The name of the access scope
                                      description:
                                        type: string
                                        description: The scope description
                                    additionalProperties: false
                                    required:
                                      - name
                                      - description
                              additionalProperties: false
                              required:
                                - users
                                - accesses
                          additionalProperties: false
                          required:
                            - database
                            - organization
                            - branch
                            - user
                      additionalProperties: false
                      required:
                        - id
                        - name
                        - display_name
                        - token
                        - plain_text_refresh_token
                        - avatar_url
                        - created_at
                        - updated_at
                        - expires_at
                        - last_used_at
                        - actor_id
                        - actor_display_name
                        - actor_type
                        - service_token_accesses
                        - oauth_accesses_by_resource
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