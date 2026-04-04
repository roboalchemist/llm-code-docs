# Source: https://planetscale.com/docs/api/reference/get_organization.md

# Get an organization

> 
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

````yaml get /organizations/{organization}
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
  /organizations/{organization}:
    get:
      tags:
        - Organizations
      summary: Get an organization
      description: >-

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
      operationId: get_organization
      parameters:
        - name: organization
          in: path
          required: true
          description: The name of the organization
          schema:
            type: string
      responses:
        '200':
          description: Returns an organization
          headers: {}
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID for the organization
                  name:
                    type: string
                    description: The name of the organization
                  billing_email:
                    type: string
                    description: The billing email of the organization
                  created_at:
                    type: string
                    description: When the organization was created
                  updated_at:
                    type: string
                    description: When the organization was last updated
                  plan:
                    type: string
                    description: The billing plan of the organization
                  valid_billing_info:
                    type: boolean
                    description: >-
                      Whether or not the organization's billing information is
                      valid
                  sso:
                    type: boolean
                    description: Whether or not SSO is enabled on the organization
                  sso_directory:
                    type: boolean
                    description: Whether or not the organization uses an SSO directory
                  single_tenancy:
                    type: boolean
                    description: Whether or not the organization has single tenancy enabled
                  managed_tenancy:
                    type: boolean
                    description: >-
                      Whether or not the organization has managed tenancy
                      enabled
                  has_past_due_invoices:
                    type: boolean
                    description: >-
                      Whether or not the organization has past due billing
                      invoices
                  database_count:
                    type: integer
                    description: The number of databases in the organization
                  sso_portal_url:
                    type: string
                    description: The URL of the organization's SSO portal
                  features:
                    type: object
                    additionalProperties: true
                    description: Features that can be enabled on the organization
                  idp_managed_roles:
                    type: boolean
                    description: >-
                      Whether or not the IdP provider is be responsible for
                      managing roles in PlanetScale
                  invoice_budget_amount:
                    type: number
                    description: The expected monthly budget for the organization
                  keyspace_shard_limit:
                    type: integer
                    description: The keyspace shard limit for the organization
                  has_card:
                    type: boolean
                    description: >-
                      Whether or not the organization has a payment method on
                      file
                  payment_info_required:
                    type: boolean
                    description: >-
                      Whether or not the organization requires payment
                      information
                additionalProperties: false
                required:
                  - id
                  - name
                  - billing_email
                  - created_at
                  - updated_at
                  - plan
                  - valid_billing_info
                  - sso
                  - sso_directory
                  - single_tenancy
                  - managed_tenancy
                  - has_past_due_invoices
                  - database_count
                  - sso_portal_url
                  - features
                  - idp_managed_roles
                  - invoice_budget_amount
                  - keyspace_shard_limit
                  - has_card
                  - payment_info_required
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