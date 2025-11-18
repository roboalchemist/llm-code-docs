# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/list-team-members.md

# List team members

> Get a paginated list of team members for the provided team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/teams/{teamId}/members
paths:
  path: /v3/teams/{teamId}/members
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        limit:
          schema:
            - type: number
              required: false
              description: Limit how many teams should be returned
              minimum: 1
              example: 20
        since:
          schema:
            - type: number
              required: false
              description: >-
                Timestamp in milliseconds to only include members added since
                then.
              example: 1540095775951
        until:
          schema:
            - type: number
              required: false
              description: >-
                Timestamp in milliseconds to only include members added until
                then.
              example: 1540095775951
        search:
          schema:
            - type: string
              required: false
              description: Search team members by their name, username, and email.
        role:
          schema:
            - type: enum<string>
              enum:
                - OWNER
                - MEMBER
                - DEVELOPER
                - SECURITY
                - BILLING
                - VIEWER
                - VIEWER_FOR_PLUS
                - CONTRIBUTOR
              required: false
              description: Only return members with the specified team role.
              example: OWNER
        excludeProject:
          schema:
            - type: string
              required: false
              description: Exclude members who belong to the specified project.
        eligibleMembersForProjectId:
          schema:
            - type: string
              required: false
              description: >-
                Include team members who are eligible to be members of the
                specified project.
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTeamMembers
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.getTeamMembers({
              limit: 20,
              since: 1540095775951,
              until: 1540095775951,
              role: "OWNER",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              members:
                allOf:
                  - items:
                      properties:
                        avatar:
                          type: string
                          description: ID of the file for the Avatar of this member.
                          example: 123a6c5209bc3778245d011443644c8d27dc2c50
                        confirmed:
                          type: boolean
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
                                - mail
                                - import
                                - github
                                - gitlab
                                - bitbucket
                                - saml
                                - dsync
                                - feedback
                                - organization-teams
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
                            required:
                              - name
                              - id
                            type: object
                            description: Array of project memberships
                          type: array
                          description: Array of project memberships
                      required:
                        - confirmed
                        - email
                        - role
                        - uid
                        - username
                        - createdAt
                      type: object
                    type: array
              emailInviteCodes:
                allOf:
                  - items:
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
                        createdAt:
                          type: number
                        expired:
                          type: boolean
                        projects:
                          additionalProperties:
                            type: string
                            enum:
                              - ADMIN
                              - PROJECT_DEVELOPER
                              - PROJECT_VIEWER
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
                allOf:
                  - properties:
                      hasNext:
                        type: boolean
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
                      - hasNext
                      - count
                      - next
                      - prev
                    type: object
            requiredProperties:
              - members
              - pagination
        examples:
          example:
            value:
              members:
                - avatar: 123a6c5209bc3778245d011443644c8d27dc2c50
                  confirmed: true
                  email: jane.doe@example.com
                  github:
                    login: <string>
                  gitlab:
                    login: <string>
                  bitbucket:
                    login: <string>
                  role: OWNER
                  uid: zTuNVUXEAvvnNN3IaqinkyMw
                  username: jane-doe
                  name: Jane Doe
                  createdAt: 1588720733602
                  accessRequestedAt: 1588820733602
                  joinedFrom:
                    origin: teams
                    commitId: <string>
                    repoId: <string>
                    repoPath: <string>
                    gitUserId: <string>
                    gitUserLogin: <string>
                    ssoUserId: <string>
                    ssoConnectedAt: 123
                    idpUserId: <string>
                    dsyncUserId: <string>
                    dsyncConnectedAt: 123
                  projects:
                    - name: <string>
                      id: <string>
                      role: ADMIN
              emailInviteCodes:
                - accessGroups:
                    - <string>
                  id: <string>
                  email: <string>
                  role: OWNER
                  teamRoles:
                    - OWNER
                  teamPermissions:
                    - IntegrationManager
                  isDSyncUser: true
                  createdAt: 123
                  expired: true
                  projects: {}
                  entitlements:
                    - <string>
              pagination:
                hasNext: true
                count: 20
                next: 1540095775951
                prev: 1540095775951
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````