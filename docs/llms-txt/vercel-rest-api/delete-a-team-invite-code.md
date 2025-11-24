# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/delete-a-team-invite-code.md

# Delete a Team invite code

> Delete an active Team invite code.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/invites/{inviteId}
paths:
  path: /v1/teams/{teamId}/invites/{inviteId}
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
        inviteId:
          schema:
            - type: string
              required: true
              description: The Team invite code ID.
              example: 2wn2hudbr4chb1ecywo9dvzo7g9sscs6mzcz8htdde0txyom4l
        teamId:
          schema:
            - type: string
              required: true
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteTeamInviteCode
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.DeleteTeamInviteCode(ctx, \"2wn2hudbr4chb1ecywo9dvzo7g9sscs6mzcz8htdde0txyom4l\", \"team_LLHUOMOoDlqOp8wPE4kFo9pE\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteTeamInviteCode
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.deleteTeamInviteCode({
              inviteId: "2wn2hudbr4chb1ecywo9dvzo7g9sscs6mzcz8htdde0txyom4l",
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
        description: Successfully deleted Team invite code.
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
              Invite managed by directory sync
              Not authorized to access this team.
        examples: {}
        description: |-
          You do not have permission to access this resource.
          Invite managed by directory sync
          Not authorized to access this team.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Team invite code not found.
        examples: {}
        description: Team invite code not found.
  deprecated: false
  type: path
components:
  schemas: {}

````