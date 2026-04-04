# Source: https://docs.turso.tech/cli/org/members/add.md

# Source: https://docs.turso.tech/api-reference/organizations/members/add.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Member

> Add an existing Turso user to an organization.

<Info>
  If you want to add someone who is not a registered Turso user, you can [create an invite](/api-reference/organizations/invites/create) instead.
</Info>

<Info>
  You must be an `owner` or `admin` to add other members. **You can only add users to a team and not your personal account.**
</Info>


## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/members
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
  /v1/organizations/{organizationSlug}/members:
    post:
      summary: Add Member
      description: Add an existing Turso user to an organization.
      operationId: addOrganizationMember
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
      requestBody:
        description: The member you want to add.
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                  description: The username of an existing Turso user.
                role:
                  type: string
                  enum:
                    - admin
                    - member
                    - viewer
                  description: The role given to the user.
                  default: member
              required:
                - email
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  member: 98c6fa96-b891-4120-a419-04c0bce4a437
                  role: 53851d0f-d772-48da-abd0-98e806e38616
        '404':
          description: Member not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: could not find user [username]
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: >-
                      user [username] is already a member of organization
                      [organizationSlug]
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.

````