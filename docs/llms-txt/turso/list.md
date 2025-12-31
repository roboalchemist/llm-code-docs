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

# List Audit Logs

> Return the audit logs for the given organization, ordered by the `created_at` field in descending order.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/audit-logs
paths:
  path: /v1/organizations/{organizationSlug}/audit-logs
  method: get
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        organizationSlug:
          schema:
            - type: string
              required: true
              description: The slug of the organization or user account.
      query:
        page_size:
          schema:
            - type: integer
              required: false
              description: The limit of items to return per page. Defaults to 100.
        page:
          schema:
            - type: integer
              required: false
              description: The page number to return. Defaults to 1.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              audit_logs:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/AuditLog'
              pagination:
                allOf:
                  - type: object
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
        examples:
          example:
            value:
              audit_logs:
                - code: db-create
                  message: ''
                  origin: cli
                  author: iku
                  created_at: '2023-12-20T09:46:08Z'
                  data: {}
              pagination:
                page: 1
                page_size: 10
                total_pages: 1
                total_rows: 1
        description: Successful response
  deprecated: false
  type: path
components:
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