# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/list-team-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List team members

> Get a paginated list of team members for the provided team.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/teams/{teamId}/members
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
  /v3/teams/{teamId}/members:
    get:
      tags:
        - teams
      summary: List team members
      description: Get a paginated list of team members for the provided team.
      operationId: getTeamMembers
      parameters:
        - name: limit
          description: Limit how many teams should be returned
          in: query
          required: false
          schema:
            description: Limit how many teams should be returned
            example: 20
            minimum: 1
            type: number
        - name: since
          description: Timestamp in milliseconds to only include members added since then.
          in: query
          required: false
          schema:
            description: >-
              Timestamp in milliseconds to only include members added since
              then.
            example: 1540095775951
            type: number
        - name: until
          description: Timestamp in milliseconds to only include members added until then.
          in: query
          required: false
          schema:
            description: >-
              Timestamp in milliseconds to only include members added until
              then.
            example: 1540095775951
            type: number
        - name: search
          description: Search team members by their name, username, and email.
          in: query
          required: false
          schema:
            description: Search team members by their name, username, and email.
            type: string
        - name: role
          description: Only return members with the specified team role.
          in: query
          required: false
          schema:
            description: Only return members with the specified team role.
            example: OWNER
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
        - name: excludeProject
          description: Exclude members who belong to the specified project.
          in: query
          required: false
          schema:
            description: Exclude members who belong to the specified project.
            type: string
        - name: eligibleMembersForProjectId
          description: >-
            Include team members who are eligible to be members of the specified
            project.
          in: query
          required: false
          schema:
            description: >-
              Include team members who are eligible to be members of the
              specified project.
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  members:
                    items:
                      properties:
                        avatar:
                          type: string
                          description: ID of the file for the Avatar of this member.
                          example: 123a6c5209bc3778245d011443644c8d27dc2c50
                        confirmed:
                          type: boolean
                          enum:
                            - false
                            - true
                          description: >-
                            Boolean that indicates if this member was confirmed
                            by an owner.
                          example: true
                        email:
                          type: string
                          description: The email of this member.
                          example: jane.doe@example.com
                        github:
                          properties:
                            login:
                              type: string
                          type: object
                          description: Information about the GitHub account for this user.
                        gitlab:
                          properties:
                            login:
                              type: string
                          type: object
                          description: Information about the GitLab account of this user.
                        bitbucket:
                          properties:
                            login:
                              type: string
                          type: object
                          description: >-
                            Information about the Bitbucket account of this
                            user.
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
                          description: Role of this user in the team.
                          example: OWNER
                        uid:
                          type: string
                          description: The ID of this user.
                          example: zTuNVUXEAvvnNN3IaqinkyMw
                        username:
                          type: string
                          description: The unique username of this user.
                          example: jane-doe
                        name:
                          type: string
                          description: The name of this user.
                          example: Jane Doe
                        createdAt:
                          type: number
                          description: >-
                            Timestamp in milliseconds when this member was
                            added.
                          example: 1588720733602
                        accessRequestedAt:
                          type: number
                          description: >-
                            Timestamp in milliseconds for when this team member
                            was accepted by an owner.
                          example: 1588820733602
                        joinedFrom:
                          properties:
                            origin:
                              type: string
                              enum:
                                - teams
                                - link
                                - import
                                - mail
                                - github
                                - gitlab
                                - bitbucket
                                - saml
                                - dsync
                                - feedback
                                - organization-teams
                                - nsnb-auto-approve
                            commitId:
                              type: string
                            repoId:
                              type: string
                            repoPath:
                              type: string
                            gitUserId:
                              oneOf:
                                - type: string
                                - type: number
                            gitUserLogin:
                              type: string
                            ssoUserId:
                              type: string
                            ssoConnectedAt:
                              type: number
                            idpUserId:
                              type: string
                            dsyncUserId:
                              type: string
                            dsyncConnectedAt:
                              type: number
                          required:
                            - origin
                          type: object
                          description: >-
                            Map with information about the members origin if
                            they joined by requesting access.
                        projects:
                          items:
                            properties:
                              name:
                                type: string
                              id:
                                type: string
                              role:
                                type: string
                                enum:
                                  - ADMIN
                                  - PROJECT_DEVELOPER
                                  - PROJECT_VIEWER
                                  - PROJECT_GUEST
                            required:
                              - id
                              - name
                            type: object
                            description: Array of project memberships
                          type: array
                          description: Array of project memberships
                      required:
                        - confirmed
                        - createdAt
                        - email
                        - role
                        - uid
                        - username
                      type: object
                    type: array
                  emailInviteCodes:
                    items:
                      properties:
                        accessGroups:
                          items:
                            type: string
                          type: array
                        id:
                          type: string
                        email:
                          type: string
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
                          type: array
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
                          type: array
                        isDSyncUser:
                          type: boolean
                          enum:
                            - false
                            - true
                        createdAt:
                          type: number
                        expired:
                          type: boolean
                          enum:
                            - true
                        projects:
                          additionalProperties:
                            type: string
                            enum:
                              - ADMIN
                              - PROJECT_DEVELOPER
                              - PROJECT_VIEWER
                              - PROJECT_GUEST
                          type: object
                        entitlements:
                          items:
                            type: string
                          type: array
                      required:
                        - id
                        - isDSyncUser
                      type: object
                    type: array
                  pagination:
                    properties:
                      hasNext:
                        type: boolean
                        enum:
                          - false
                          - true
                      count:
                        type: number
                        description: Amount of items in the current page.
                        example: 20
                      next:
                        nullable: true
                        type: number
                        description: Timestamp that must be used to request the next page.
                        example: 1540095775951
                      prev:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp that must be used to request the previous
                          page.
                        example: 1540095775951
                    required:
                      - count
                      - hasNext
                      - next
                      - prev
                    type: object
                required:
                  - members
                  - pagination
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
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