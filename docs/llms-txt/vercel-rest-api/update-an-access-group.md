# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/update-an-access-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an access group

> Allows to update an access group metadata



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups/{idOrName}
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/access-groups/{idOrName}:
    post:
      tags:
        - access-groups
      summary: Update an access group
      description: Allows to update an access group metadata
      operationId: updateAccessGroup
      parameters:
        - name: idOrName
          in: path
          required: true
          schema:
            type: string
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              properties:
                name:
                  type: string
                  description: The name of the access group
                  maxLength: 50
                  pattern: ^[A-z0-9_ -]+$
                  example: My access group
                projects:
                  type: array
                  items:
                    type: object
                    additionalProperties: false
                    required:
                      - role
                      - projectId
                    properties:
                      projectId:
                        type: string
                        maxLength: 256
                        example: prj_ndlgr43fadlPyCtREAqxxdyFK
                        description: The ID of the project.
                      role:
                        type: string
                        example: ADMIN
                        description: >-
                          The project role that will be added to this Access
                          Group. \"null\" will remove this project level role.
                        nullable: true
                        enum:
                          - ADMIN
                          - PROJECT_VIEWER
                          - PROJECT_DEVELOPER
                          - null
                membersToAdd:
                  description: List of members to add to the access group.
                  type: array
                  items:
                    type: string
                  example:
                    - usr_1a2b3c4d5e6f7g8h9i0j
                    - usr_2b3c4d5e6f7g8h9i0j1k
                membersToRemove:
                  description: List of members to remove from the access group.
                  type: array
                  items:
                    type: string
                  example:
                    - usr_1a2b3c4d5e6f7g8h9i0j
                    - usr_2b3c4d5e6f7g8h9i0j1k
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  entitlements:
                    items:
                      type: string
                      enum:
                        - v0
                    type: array
                  name:
                    type: string
                    description: The name of this access group.
                    example: my-access-group
                  createdAt:
                    type: string
                    description: >-
                      Timestamp in milliseconds when the access group was
                      created.
                    example: 1588720733602
                  teamId:
                    type: string
                    description: ID of the team that this access group belongs to.
                    example: team_123a6c5209bc3778245d011443644c8d27dc2c50
                  updatedAt:
                    type: string
                    description: >-
                      Timestamp in milliseconds when the access group was last
                      updated.
                    example: 1588720733602
                  accessGroupId:
                    type: string
                    description: ID of the access group.
                    example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
                  membersCount:
                    type: number
                    description: Number of members in the access group.
                    example: 5
                  projectsCount:
                    type: number
                    description: Number of projects in the access group.
                    example: 2
                  teamRoles:
                    items:
                      type: string
                    type: array
                    description: Roles that the team has in the access group.
                    example:
                      - DEVELOPER
                      - BILLING
                  teamPermissions:
                    items:
                      type: string
                    type: array
                    description: Permissions that the team has in the access group.
                    example:
                      - CreateProject
                required:
                  - accessGroupId
                  - createdAt
                  - entitlements
                  - membersCount
                  - name
                  - projectsCount
                  - teamId
                  - updatedAt
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````