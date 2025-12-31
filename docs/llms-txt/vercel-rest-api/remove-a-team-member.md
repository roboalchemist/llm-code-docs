# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/remove-a-team-member.md

# Remove a Team Member

> Remove a Team Member from the Team, or dismiss a user that requested access, or leave a team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/members/{uid}
paths:
  path: /v1/teams/{teamId}/members/{uid}
  method: delete
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
              description: The user ID of the member.
              example: ndlgr43fadlPyCtREAqxxdyFK
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query:
        newDefaultTeamId:
          schema:
            - type: string
              required: false
              description: >-
                The ID of the team to set as the new default team for the
                Northstar user.
              example: team_nllPyCtREAqxxdyFKbbMDlxd
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: removeTeamMember
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.RemoveTeamMember(ctx, \"ndlgr43fadlPyCtREAqxxdyFK\", \"<id>\", vercel.String(\"team_nllPyCtREAqxxdyFKbbMDlxd\"))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: removeTeamMember
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.removeTeamMember({
              uid: "ndlgr43fadlPyCtREAqxxdyFK",
              newDefaultTeamId: "team_nllPyCtREAqxxdyFKbbMDlxd",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
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
        description: Successfully removed a member of the team.
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
            description: |-
              You do not have permission to access this resource.
              Not authorized to update the team.
        examples: {}
        description: |-
          You do not have permission to access this resource.
          Not authorized to update the team.
    '404': {}
    '503': {}
  deprecated: false
  type: path
components:
  schemas: {}

````