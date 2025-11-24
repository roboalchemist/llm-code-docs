# Source: https://docs.turso.tech/api-reference/organizations/members/remove.md

# Remove Member

> Remove a user from the organization by username.

## OpenAPI

````yaml DELETE /v1/organizations/{organizationSlug}/members/{username}
paths:
  path: /v1/organizations/{organizationSlug}/members/{username}
  method: delete
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
        username:
          schema:
            - type: string
              required: true
              description: The username of a Turso user or organization member.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              member:
                allOf:
                  - $ref: '#/components/schemas/Member/properties/username'
        examples:
          example:
            value:
              member: iku
        description: Successful response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: user [username] is not a member of org [organizationSlug]
        examples:
          example:
            value:
              error: user [username] is not a member of org [organizationSlug]
        description: Member not found
  deprecated: false
  type: path
components:
  schemas: {}

````