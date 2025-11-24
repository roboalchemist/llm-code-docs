# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/update-a-team-member.md

# Update a Team Member

> Update the membership of a Team Member on the Team specified by `teamId`, such as changing the _role_ of the member, or confirming a request to join the Team for an unconfirmed member. The authenticated user must be an `OWNER` of the Team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/teams/{teamId}/members/{uid}
paths:
  path: /v1/teams/{teamId}/members/{uid}
  method: patch
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
        uid:
          schema:
            - type: string
              required: true
              description: The ID of the member.
              example: ndfasllgPyCtREAqxxdyFKb
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
              confirmed:
                allOf:
                  - type: boolean
                    enum:
                      - true
                    description: Accept a user who requested access to the team.
                    example: true
              role:
                allOf:
                  - type: string
                    description: The role in the team of the member.
                    example:
                      - MEMBER
                      - VIEWER
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
                          maxLength: 256
                          example: prj_ndlgr43fadlPyCtREAqxxdyFK
                          description: The ID of the project.
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_VIEWER
                            - PROJECT_DEVELOPER
                            - null
                          example: ADMIN
                          description: >-
                            The project role of the member that will be added.
                            \"null\" will remove this project level role.
                          nullable: true
              joinedFrom:
                allOf:
                  - additionalProperties: false
                    type: object
                    properties:
                      ssoUserId:
                        nullable: true
            required: true
        examples:
          example:
            value:
              confirmed: true
              role:
                - MEMBER
                - VIEWER
              projects:
                - projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
                  role: ADMIN
              joinedFrom:
                ssoUserId: <any>
    codeSamples:
      - label: updateTeamMember
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.UpdateTeamMember(ctx, \"ndfasllgPyCtREAqxxdyFKb\", \"<id>\", &operations.UpdateTeamMemberRequestBody{\n        Confirmed: vercel.Bool(true),\n        Role: vercel.String(\"[\\\"MEMBER\\\",\\\"VIEWER\\\"]\"),\n        Projects: []operations.UpdateTeamMemberProjects{\n            operations.UpdateTeamMemberProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.UpdateTeamMemberRoleAdmin.ToPointer(),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateTeamMember
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.updateTeamMember({
              uid: "ndfasllgPyCtREAqxxdyFKb",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                confirmed: true,
                role: "[\"MEMBER\",\"VIEWER\"]",
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
              id:
                allOf:
                  - type: string
                    description: ID of the team.
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: <string>
        description: Successfully updated the membership.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request body is invalid.

              One of the provided values in the request query is invalid.

              Cannot disconnect SSO from a Team member that does not have a SSO
              connection.

              Cannot confirm a member that is already confirmed.

              Cannot confirm a member that did not request access.
        examples: {}
        description: >-
          One of the provided values in the request body is invalid.

          One of the provided values in the request query is invalid.

          Cannot disconnect SSO from a Team member that does not have a SSO
          connection.

          Cannot confirm a member that is already confirmed.

          Cannot confirm a member that did not request access.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The request is not authorized.

              Team members can only be updated by an owner, or by the
              authenticated user if they are only disconnecting their SAML
              connection to the Team.
        examples: {}
        description: >-
          The request is not authorized.

          Team members can only be updated by an owner, or by the authenticated
          user if they are only disconnecting their SAML connection to the Team.
    '402': {}
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The provided user is not part of this team.
              A user with the specified ID does not exist.
        examples: {}
        description: |-
          The provided user is not part of this team.
          A user with the specified ID does not exist.
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````