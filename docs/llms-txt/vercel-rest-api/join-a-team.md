# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/join-a-team.md

# Join a team

> Join a team with a provided invite code or team ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/members/teams/join
paths:
  path: /v1/teams/{teamId}/members/teams/join
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
              inviteCode:
                allOf:
                  - type: string
                    description: The invite code to join the team.
                    example: fisdh38aejkeivn34nslfore9vjtn4ls
            required: true
        examples:
          example:
            value:
              inviteCode: fisdh38aejkeivn34nslfore9vjtn4ls
    codeSamples:
      - label: joinTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.JoinTeam(ctx, \"<id>\", &operations.JoinTeamRequestBody{\n        InviteCode: vercel.String(\"fisdh38aejkeivn34nslfore9vjtn4ls\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: joinTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.joinTeam({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                inviteCode: "fisdh38aejkeivn34nslfore9vjtn4ls",
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
              teamId:
                allOf:
                  - type: string
                    description: The ID of the team the user joined.
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
              slug:
                allOf:
                  - type: string
                    description: The slug of the team the user joined.
                    example: my-team
              name:
                allOf:
                  - type: string
                    description: The name of the team the user joined.
                    example: My Team
              from:
                allOf:
                  - type: string
                    description: The origin of how the user joined.
                    example: email
            description: Successfully joined a team.
            requiredProperties:
              - teamId
              - slug
              - name
              - from
        examples:
          example:
            value:
              teamId: team_LLHUOMOoDlqOp8wPE4kFo9pE
              slug: my-team
              name: My Team
              from: email
        description: Successfully joined a team.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401': {}
    '402': {}
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