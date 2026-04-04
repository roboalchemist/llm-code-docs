# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/invite-a-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Invite a user

> Invite a user to join the team specified in the URL. The authenticated user needs to be an `OWNER` in order to successfully invoke this endpoint. The user to be invited must be specified by email.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/teams/{teamId}/members
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
  /v2/teams/{teamId}/members:
    post:
      tags:
        - teams
      summary: Invite a user
      description: >-
        Invite a user to join the team specified in the URL. The authenticated
        user needs to be an `OWNER` in order to successfully invoke this
        endpoint. The user to be invited must be specified by email.
      operationId: inviteUserToTeam
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                required:
                  - email
                properties:
                  email:
                    type: string
                    format: email
                    description: The email address of the user to invite
                    example: john@example.com
                  role:
                    type: string
                    enum:
                      - OWNER
                      - MEMBER
                      - DEVELOPER
                      - SECURITY
                      - BILLING
                      - VIEWER
                      - VIEWER_FOR_PLUS
                      - CONTRIBUTOR
                    default: VIEWER
                    description: The role of the user to invite
                    example: VIEWER
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
                          maxLength: 64
                          example: prj_ndlgr43fadlPyCtREAqxxdyFK
                          description: The ID of the project.
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_VIEWER
                            - PROJECT_DEVELOPER
                            - PROJECT_GUEST
                          example: ADMIN
                          description: Sets the project roles for the invited user
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InvitedTeamMember'
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: |-
            You do not have permission to access this resource.
            The authenticated user must be a team owner to perform the action
        '503':
          description: ''
      security:
        - bearerToken: []
components:
  schemas:
    InvitedTeamMember:
      properties:
        uid:
          type: string
          description: The ID of the invited user
          example: kr1PsOIzqEL5Xg6M4VZcZosf
        username:
          type: string
          description: The username of the invited user
          example: john-doe
        email:
          type: string
          description: The email of the invited user.
          example: john@user.co
        role:
          type: string
          enum:
            - OWNER
            - MEMBER
            - DEVELOPER
            - SECURITY
            - BILLING
            - VIEWER
            - VIEWER_FOR_PLUS
            - CONTRIBUTOR
          description: The role used for the invitation
          example: MEMBER
        teamRoles:
          items:
            type: string
            enum:
              - OWNER
              - MEMBER
              - DEVELOPER
              - SECURITY
              - BILLING
              - VIEWER
              - VIEWER_FOR_PLUS
              - CONTRIBUTOR
            description: The team roles of the user
            example:
              - MEMBER
          type: array
          description: The team roles of the user
          example:
            - MEMBER
        teamPermissions:
          items:
            type: string
            enum:
              - IntegrationManager
              - CreateProject
              - FullProductionDeployment
              - UsageViewer
              - EnvVariableManager
              - EnvironmentManager
              - V0Builder
              - V0Chatter
              - V0Viewer
            description: The team permissions of the user
            example:
              - CreateProject
          type: array
          description: The team permissions of the user
          example:
            - CreateProject
      required:
        - email
        - role
        - uid
        - username
      type: object
      description: The member was successfully added to the team.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````