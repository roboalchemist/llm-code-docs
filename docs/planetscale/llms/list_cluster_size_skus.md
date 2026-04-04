# Source: https://planetscale.com/docs/api/reference/list_cluster_size_skus.md

# List available cluster sizes

> List available cluster sizes for an organization
### Authorization
A service token or OAuth token must have at least one of the following access or scopes in order to use this API endpoint:

**Service Token Accesses**
 `read_organization`

**OAuth Scopes**

 | Resource | Scopes |
| :------- | :---------- |
| User | `read_organizations` |
| Organization | `read_organization` |



## OpenAPI

````yaml get /organizations/{organization}/cluster-size-skus
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
  /organizations/{organization}/cluster-size-skus:
    get:
      tags:
        - Organizations
      summary: List available cluster sizes
      description: >-
        List available cluster sizes for an organization

        ### Authorization

        A service token or OAuth token must have at least one of the following
        access or scopes in order to use this API endpoint:


        **Service Token Accesses**
         `read_organization`

        **OAuth Scopes**

         | Resource | Scopes |
        | :------- | :---------- |

        | User | `read_organizations` |

        | Organization | `read_organization` |
      operationId: list_cluster_size_skus
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization
          schema:
            type: string
        - name: engine
          in: query
          description: The database engine to filter by. Defaults to 'mysql'.
          schema:
            type: string
            enum:
              - mysql
              - postgresql
        - name: rates
          in: query
          description: Whether to include pricing rates in the response. Defaults to false.
          schema:
            type: boolean
        - name: region
          in: query
          description: >-
            The region slug to get rates for. If not specified, uses the
            organization's default region.
          schema:
            type: string
      responses:
        '200':
          description: Returns available cluster sizes with optional pricing rates
          headers: {}
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    name:
                      type: string
                      description: The name of the cluster SKU
                    display_name:
                      type: string
                      description: The display name
                    cpu:
                      type: string
                      description: The number of CPUs
                    storage:
                      type: integer
                      description: The amount of storage in bytes
                    ram:
                      type: integer
                      description: The amount of memory in bytes
                    metal:
                      type: boolean
                      description: Whether or not the cluster SKU is Metal
                    enabled:
                      type: boolean
                      description: >-
                        Whether or not the cluster SKU is enabled for the
                        organization
                    provider:
                      type: string
                      description: The provider of the cluster SKU (nil, AWS or GCP)
                    default_vtgate:
                      type: string
                      description: The default vtgate size for the cluster SKU
                    default_vtgate_rate:
                      type: number
                      description: The default vtgate rate for the cluster SKU
                    replica_rate:
                      type: number
                      description: The replica rate for the cluster SKU
                    rate:
                      type: number
                      description: The rate for the cluster SKU
                    sort_order:
                      type: integer
                      description: The sort order of the cluster SKU
                    architecture:
                      type: string
                      description: >-
                        The architecture of the cluster SKU (null, x86_64 or
                        arm64)
                    development:
                      type: boolean
                      description: Whether or not the cluster SKU is a development SKU
                    production:
                      type: boolean
                      description: Whether or not the cluster SKU is a production SKU
                  additionalProperties: false
                  required:
                    - name
                    - display_name
                    - cpu
                    - storage
                    - ram
                    - metal
                    - enabled
                    - provider
                    - default_vtgate
                    - default_vtgate_rate
                    - sort_order
                    - architecture
                    - development
                    - production
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