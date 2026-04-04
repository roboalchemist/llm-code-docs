# Source: https://docs.turso.tech/cli/group/update.md

# Source: https://docs.turso.tech/api-reference/organizations/update.md

# Source: https://docs.turso.tech/api-reference/organizations/members/update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Member Role

> Update the role of an organization member. Only organization admins or owners can perform this action.

<RequestExample>
  ```bash  theme={null}
  curl -L -X PATCH https://api.turso.tech/v1/organizations/{organizationSlug}/members/{username} \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
      "role": "member"
    }'
  ```
</RequestExample>


## OpenAPI

````yaml PATCH /v1/organizations/{organizationSlug}/members/{username}
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
  /v1/organizations/{organizationSlug}/members/{username}:
    patch:
      summary: Update Member Role
      description: >-
        Update the role of an organization member. Only organization admins or
        owners can perform this action.
      operationId: updateMemberRole
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/username'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                role:
                  type: string
                  enum:
                    - admin
                    - member
                    - viewer
                  description: The new role to assign to the member.
              required:
                - role
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  member:
                    type: object
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
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: invalid role
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: updating member roles is only allowed for admin or owner
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: could not find user [username]
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.
    username:
      name: username
      in: path
      required: true
      schema:
        type: string
      description: The username of a Turso user or organization member.

````