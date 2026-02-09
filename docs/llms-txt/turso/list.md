# Source: https://docs.turso.tech/cli/org/members/list.md

# Source: https://docs.turso.tech/cli/org/list.md

# Source: https://docs.turso.tech/cli/group/list.md

# Source: https://docs.turso.tech/cli/db/list.md

# Source: https://docs.turso.tech/cli/auth/api-tokens/list.md

# Source: https://docs.turso.tech/api-reference/tokens/list.md

# Source: https://docs.turso.tech/api-reference/organizations/members/list.md

# Source: https://docs.turso.tech/api-reference/organizations/list.md

# Source: https://docs.turso.tech/api-reference/organizations/invites/list.md

# Source: https://docs.turso.tech/api-reference/locations/list.md

# Source: https://docs.turso.tech/api-reference/groups/list.md

# Source: https://docs.turso.tech/api-reference/databases/list.md

# Source: https://docs.turso.tech/api-reference/audit-logs/list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# List Audit Logs

> Return the audit logs for the given organization, ordered by the `created_at` field in descending order.

<Warning>Audit Logs are limited to paid plans.</Warning>

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/audit-logs \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/audit-logs
openapi: 3.0.1
info:
  title: Turso Platform API
  description: API description here
  license:
    name: MIT
  version: 0.1.0
servers:
  - url: https://api.turso.tech
    description: Turso's Platform API
security: []
paths:
  /v1/organizations/{organizationSlug}/audit-logs:
    get:
      summary: List Audit Logs
      description: >-
        Return the audit logs for the given organization, ordered by the
        `created_at` field in descending order.
      operationId: listOrganizationAuditLogs
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/page_size'
        - $ref: '#/components/parameters/page'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  audit_logs:
                    type: array
                    items:
                      $ref: '#/components/schemas/AuditLog'
                  pagination:
                    type: object
                    properties:
                      page:
                        type: integer
                        description: The current page number.
                        example: 1
                      page_size:
                        type: integer
                        description: The number of items per page.
                        example: 10
                      total_pages:
                        type: integer
                        description: The total number of pages.
                        example: 1
                      total_rows:
                        type: integer
                        description: The total number of items.
                        example: 1
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.
    page_size:
      in: query
      name: page_size
      required: false
      schema:
        type: integer
      description: The limit of items to return per page. Defaults to 100.
    page:
      in: query
      name: page
      required: false
      schema:
        type: integer
      description: The page number to return. Defaults to 1.
  schemas:
    AuditLog:
      type: object
      properties:
        code:
          type: string
          description: The code associated to the action taken.
          example: db-create
          enum:
            - user-signup
            - db-create
            - db-delete
            - db-protect
            - db-unprotect
            - db-token-create
            - group-token-create
            - user-token-create
            - instance-create
            - instance-delete
            - org-create
            - org-delete
            - org-member-add
            - org-member-rm
            - org-member-leave
            - org-plan-update
            - org-set-overages
            - group-create
            - group-delete
            - group-unarchive
            - group-protect
            - group-unprotect
            - db-aunrchive
            - user-delete
        message:
          type: string
          description: Additional context from the performed action.
          example: ''
        origin:
          type: string
          description: >-
            Where this action was performed. Will be either `cli` or `web`
            depending on the `User-Agent` sent to the API.
          example: cli
        author:
          type: string
          description: The username of the user who performed the action.
          example: iku
        created_at:
          type: string
          description: >-
            A formatted [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            timestamp this action was performed.
          example: '2023-12-20T09:46:08Z'
        data:
          type: object
          description: The payload of the action performed.

````