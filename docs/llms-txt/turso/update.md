# Source: https://docs.turso.tech/cli/group/update.md

# Source: https://docs.turso.tech/api-reference/organizations/update.md

# Source: https://docs.turso.tech/api-reference/organizations/members/update.md

# Source: https://docs.turso.tech/cli/group/update.md

# Source: https://docs.turso.tech/api-reference/organizations/update.md

# Source: https://docs.turso.tech/api-reference/organizations/members/update.md

# Source: https://docs.turso.tech/cli/group/update.md

# Source: https://docs.turso.tech/api-reference/organizations/update.md

# Source: https://docs.turso.tech/api-reference/organizations/members/update.md

# Source: https://docs.turso.tech/cli/group/update.md

# Source: https://docs.turso.tech/api-reference/organizations/update.md

# Source: https://docs.turso.tech/api-reference/organizations/members/update.md

# Update Member Role

> Update the role of an organization member. Only organization admins or owners can perform this action.

## OpenAPI

````yaml PATCH /v1/organizations/{organizationSlug}/members/{username}
paths:
  path: /v1/organizations/{organizationSlug}/members/{username}
  method: patch
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              role:
                allOf:
                  - type: string
                    enum:
                      - admin
                      - member
                      - viewer
                    description: The new role to assign to the member.
            required: true
            requiredProperties:
              - role
        examples:
          example:
            value:
              role: admin
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              member:
                allOf:
                  - type: object
                    properties:
                      username:
                        type: string
                        description: The username of the updated member.
                      email:
                        type: string
                        description: The email of the updated member.
                      role:
                        type: string
                        description: The new role of the updated member.
                        enum:
                          - admin
                          - member
                          - viewer
        examples:
          example:
            value:
              member:
                username: <string>
                email: <string>
                role: admin
        description: Successful response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: invalid role
        examples:
          example:
            value:
              error: invalid role
        description: Bad Request
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: updating member roles is only allowed for admin or owner
        examples:
          example:
            value:
              error: updating member roles is only allowed for admin or owner
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: could not find user [username]
        examples:
          example:
            value:
              error: could not find user [username]
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````