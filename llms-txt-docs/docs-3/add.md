# Source: https://docs.turso.tech/cli/org/members/add.md

# Source: https://docs.turso.tech/api-reference/organizations/members/add.md

# Add Member

> Add an existing Turso user to an organization.

## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/members
paths:
  path: /v1/organizations/{organizationSlug}/members
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              username:
                allOf:
                  - type: string
                    description: The username of an existing Turso user.
              role:
                allOf:
                  - type: string
                    enum:
                      - admin
                      - member
                      - viewer
                    description: The role given to the user.
                    default: member
            required: true
            requiredProperties:
              - email
        examples:
          example:
            value:
              username: <string>
              role: member
        description: The member you want to add.
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              member:
                allOf:
                  - $ref: '#/components/schemas/Member/properties/username'
              role:
                allOf:
                  - $ref: '#/components/schemas/Member/properties/role'
        examples:
          example:
            value:
              member: iku
              role: owner
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
                    example: could not find user [username]
        examples:
          example:
            value:
              error: could not find user [username]
        description: Member not found
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: >-
                      user [username] is already a member of organization
                      [organizationSlug]
        examples:
          example:
            value:
              error: >-
                user [username] is already a member of organization
                [organizationSlug]
        description: Conflict
  deprecated: false
  type: path
components:
  schemas: {}

````