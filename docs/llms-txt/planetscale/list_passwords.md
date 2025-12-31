# Source: https://planetscale.com/docs/api/reference/list_passwords.md

# List passwords

> 
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_branch`, `delete_branch`, `create_branch`, `connect_production_branch`, `connect_branch`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| Organization | `manage_passwords`, `manage_production_branch_passwords` |
| Database | `manage_passwords`, `manage_production_branch_passwords` |
| Branch | `manage_passwords` |



## OpenAPI

````yaml get /organizations/{organization}/databases/{database}/branches/{branch}/passwords
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
  /organizations/{organization}/databases/{database}/branches/{branch}/passwords:
    get:
      tags:
        - Database branch passwords
      summary: List passwords
      description: >-

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_branch`, `delete_branch`, `create_branch`, `connect_production_branch`, `connect_branch`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | Organization | `manage_passwords`,
        `manage_production_branch_passwords` |

        | Database | `manage_passwords`, `manage_production_branch_passwords` |

        | Branch | `manage_passwords` |
      operationId: list_passwords
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization the password belongs to
          schema:
            type: string
        - name: database
          in: path
          required: true
          description: The name of the database the password belongs to
          schema:
            type: string
        - name: branch
          in: path
          required: true
          description: The name of the branch the password belongs to
          schema:
            type: string
        - name: read_only_region_id
          in: query
          description: >-
            A read-only region of the database branch. If present, the password
            results will be filtered to only those in the region
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
          description: Returns passwords for the branch
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
                          description: The ID for the password
                        name:
                          type: string
                          description: The display name for the password
                        role:
                          type: string
                          enum:
                            - reader
                            - writer
                            - admin
                            - readwriter
                          description: The role for the password
                        cidrs:
                          items:
                            type: string
                          type: array
                          description: >-
                            List of IP addresses or CIDR ranges that can use
                            this password
                        created_at:
                          type: string
                          description: When the password was created
                        deleted_at:
                          type: string
                          description: When the password was deleted
                        expires_at:
                          type: string
                          description: When the password will expire
                        last_used_at:
                          type: string
                          description: When the password was last used to execute a query
                        expired:
                          type: boolean
                          description: True if the credentials are expired
                        direct_vtgate:
                          type: boolean
                          description: >-
                            True if the credentials connect directly to a
                            vtgate, bypassing load balancers
                        direct_vtgate_addresses:
                          items:
                            type: string
                          type: array
                          description: >-
                            The list of hosts in each availability zone
                            providing direct access to a vtgate
                        ttl_seconds:
                          type: integer
                          description: >-
                            Time to live (in seconds) for the password. The
                            password will be invalid when TTL has passed
                        access_host_url:
                          type: string
                          description: The host URL for the password
                        access_host_regional_url:
                          type: string
                          description: The regional host URL
                        access_host_regional_urls:
                          items:
                            type: string
                          type: array
                          description: The read-only replica host URLs
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
                        region:
                          type: object
                          properties:
                            id:
                              type: string
                              description: The ID of the region
                            provider:
                              type: string
                              description: Provider for the region (ex. AWS)
                            enabled:
                              type: boolean
                              description: Whether or not the region is currently active
                            public_ip_addresses:
                              items:
                                type: string
                              type: array
                              description: Public IP addresses for the region
                            display_name:
                              type: string
                              description: Name of the region
                            location:
                              type: string
                              description: Location of the region
                            slug:
                              type: string
                              description: The slug of the region
                            current_default:
                              type: boolean
                              description: >-
                                True if the region is the default for new branch
                                creation
                          additionalProperties: false
                          required:
                            - id
                            - provider
                            - enabled
                            - public_ip_addresses
                            - display_name
                            - location
                            - slug
                            - current_default
                        username:
                          type: string
                          description: The username for the password
                        plain_text:
                          type: string
                          description: The plain text password, available only after create
                        replica:
                          type: boolean
                          description: Whether or not the password is for a read replica
                        renewable:
                          type: boolean
                          description: Whether or not the password can be renewed
                        database_branch:
                          type: object
                          properties:
                            name:
                              type: string
                              description: The name for the branch
                            id:
                              type: string
                              description: The ID for the branch
                            production:
                              type: boolean
                              description: Whether or not the branch is a production branch
                            mysql_edge_address:
                              type: string
                              description: The address of the MySQL provider for the branch
                            private_edge_connectivity:
                              type: boolean
                              description: True if private connectivity is enabled
                          additionalProperties: false
                          required:
                            - name
                            - id
                            - production
                            - mysql_edge_address
                            - private_edge_connectivity
                      additionalProperties: false
                      required:
                        - id
                        - name
                        - role
                        - cidrs
                        - created_at
                        - deleted_at
                        - expires_at
                        - last_used_at
                        - expired
                        - direct_vtgate
                        - direct_vtgate_addresses
                        - ttl_seconds
                        - access_host_url
                        - access_host_regional_url
                        - access_host_regional_urls
                        - actor
                        - region
                        - username
                        - plain_text
                        - replica
                        - renewable
                        - database_branch
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