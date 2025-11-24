# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/invite-a-user.md

# Invite a user

> Invite a user to join the team specified in the URL. The authenticated user needs to be an `OWNER` in order to successfully invoke this endpoint. The user to be invited must be specified by email.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/members
paths:
  path: /v1/teams/{teamId}/members
  method: post
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
      path:
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              email:
                allOf:
                  - type: string
                    format: email
                    description: The email address of the user to invite
                    example: john@example.com
              role:
                allOf:
                  - type: string
                    enum:
                      - OWNER
                      - MEMBER
                      - DEVELOPER
                      - SECURITY
                      - BILLING
                      - VIEWER
                      - VIEWER_FOR_PLUS
                      - CONTRIBUTOR
                    description: The role of the user to invite
                    example:
                      - OWNER
                      - MEMBER
                      - DEVELOPER
                      - SECURITY
                      - BILLING
                      - VIEWER
                      - VIEWER_FOR_PLUS
                      - CONTRIBUTOR
                    default: MEMBER
              projects:
                allOf:
                  - type: array
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
                          example: ADMIN
                          description: Sets the project roles for the invited user
            required: true
            requiredProperties:
              - email
        examples:
          example:
            value:
              email: john@example.com
              role:
                - OWNER
                - MEMBER
                - DEVELOPER
                - SECURITY
                - BILLING
                - VIEWER
                - VIEWER_FOR_PLUS
                - CONTRIBUTOR
              projects:
                - projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
                  role: ADMIN
    codeSamples:
      - label: inviteUserToTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.InviteUserToTeam(ctx, \"<id>\", &operations.InviteUserToTeamRequestBody{\n        UID: vercel.String(\"kr1PsOIzqEL5Xg6M4VZcZosf\"),\n        Email: vercel.String(\"john@example.com\"),\n        Role: operations.InviteUserToTeamRoleViewer.ToPointer(),\n        Projects: []operations.InviteUserToTeamProjects{\n            operations.InviteUserToTeamProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.InviteUserToTeamTeamsRoleAdmin,\n            },\n            operations.InviteUserToTeamProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.InviteUserToTeamTeamsRoleAdmin,\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: inviteUserToTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.inviteUserToTeam({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                email: "john@example.com",
                role: "DEVELOPER",
                projects: [
                  {
                    projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
                    role: "ADMIN",
                  },
                ],
              },
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
              uid:
                allOf:
                  - type: string
                    description: The ID of the invited user
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              username:
                allOf:
                  - type: string
                    description: The username of the invited user
                    example: john-doe
              email:
                allOf:
                  - type: string
                    description: The email of the invited user.
                    example: john@user.co
              role:
                allOf:
                  - type: string
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
                allOf:
                  - items:
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
                allOf:
                  - items:
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
            description: The member was successfully added to the team
            requiredProperties:
              - uid
              - username
              - email
              - role
        examples:
          example:
            value:
              uid: kr1PsOIzqEL5Xg6M4VZcZosf
              username: john-doe
              email: john@user.co
              role: MEMBER
              teamRoles:
                - MEMBER
              teamPermissions:
                - CreateProject
        description: The member was successfully added to the team
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              The user already requested access to the team
              The team reached the maximum allowed amount of members
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          The user already requested access to the team
          The team reached the maximum allowed amount of members
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
            description: |-
              The authenticated user must be a team owner to perform the action
              You do not have permission to access this resource.
        examples: {}
        description: |-
          The authenticated user must be a team owner to perform the action
          You do not have permission to access this resource.
    '503': {}
  deprecated: false
  type: path
components:
  schemas: {}

````