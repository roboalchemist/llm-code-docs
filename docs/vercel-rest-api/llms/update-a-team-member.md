# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/update-a-team-member.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Team Member

> Update the membership of a Team Member on the Team specified by `teamId`, such as changing the _role_ of the member, or confirming a request to join the Team for an unconfirmed member. The authenticated user must be an `OWNER` of the Team.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/teams/{teamId}/members/{uid}
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
  /v1/teams/{teamId}/members/{uid}:
    patch:
      tags:
        - teams
      summary: Update a Team Member
      description: >-
        Update the membership of a Team Member on the Team specified by
        `teamId`, such as changing the _role_ of the member, or confirming a
        request to join the Team for an unconfirmed member. The authenticated
        user must be an `OWNER` of the Team.
      operationId: updateTeamMember
      parameters:
        - name: uid
          description: The ID of the member.
          in: path
          required: true
          schema:
            type: string
            description: The ID of the member.
            example: ndfasllgPyCtREAqxxdyFKb
        - name: teamId
          in: path
          required: true
          schema:
            type: string
            description: The unique team identifier
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                confirmed:
                  type: boolean
                  enum:
                    - true
                  description: Accept a user who requested access to the team.
                  example: true
                role:
                  type: string
                  description: The role in the team of the member.
                  example: VIEWER
                  default: MEMBER
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
                          The project role of the member that will be added.
                          \"null\" will remove this project level role.
                        nullable: true
                        enum:
                          - ADMIN
                          - PROJECT_VIEWER
                          - PROJECT_DEVELOPER
                          - null
                joinedFrom:
                  additionalProperties: false
                  type: object
                  properties:
                    ssoUserId:
                      nullable: true
        required: true
      responses:
        '200':
          description: Successfully updated the membership.
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                    description: ID of the team.
                required:
                  - id
                type: object
        '400':
          description: >-
            One of the provided values in the request body is invalid.

            One of the provided values in the request query is invalid.

            Cannot disconnect SSO from a Team member that does not have a SSO
            connection.

            Cannot confirm a member that is already confirmed.

            Cannot confirm a member that did not request access.
        '401':
          description: >-
            The request is not authorized.

            Team members can only be updated by an owner, or by the
            authenticated user if they are only disconnecting their SAML
            connection to the Team.
        '402':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: |-
            The provided user is not part of this team.
            A user with the specified ID does not exist.
        '409':
          description: ''
        '500':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````