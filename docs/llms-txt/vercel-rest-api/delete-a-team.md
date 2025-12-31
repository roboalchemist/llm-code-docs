# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/delete-a-team.md

# Delete a Team

> Delete a team under your account. You need to send a `DELETE` request with the desired team `id`. An optional array of reasons for deletion may also be sent.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}
paths:
  path: /v1/teams/{teamId}
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
        teamId:
          schema:
            - type: string
              required: true
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query:
        newDefaultTeamId:
          schema:
            - type: string
              required: false
              description: Id of the team to be set as the new default team
              example: team_LLHUOMOoDlqOp8wPE4kFo9pE
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              reasons:
                allOf:
                  - type: array
                    description: >-
                      Optional array of objects that describe the reason why the
                      team is being deleted.
                    items:
                      type: object
                      description: >-
                        An object describing the reason why the team is being
                        deleted.
                      required:
                        - slug
                        - description
                      additionalProperties: false
                      properties:
                        slug:
                          type: string
                          description: >-
                            Idenitifier slug of the reason why the team is being
                            deleted.
                        description:
                          type: string
                          description: >-
                            Description of the reason why the team is being
                            deleted.
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              reasons:
                - slug: <string>
                  description: <string>
    codeSamples:
      - label: deleteTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.DeleteTeam(ctx, \"<id>\", vercel.String(\"team_LLHUOMOoDlqOp8wPE4kFo9pE\"), nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.deleteTeam({
              newDefaultTeamId: "team_LLHUOMOoDlqOp8wPE4kFo9pE",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {},
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
                    description: The ID of the deleted Team
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
              newDefaultTeamIdError:
                allOf:
                  - type: boolean
                    description: >-
                      Signifies whether the default team update has failed, when
                      newDefaultTeamId is provided in request query.
                    example: true
            description: The Team was successfully deleted
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: team_LLHUOMOoDlqOp8wPE4kFo9pE
              newDefaultTeamIdError: true
        description: The Team was successfully deleted
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '402': {}
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              You do not have permission to access this resource.
              The authenticated user can't access the team
        examples: {}
        description: |-
          You do not have permission to access this resource.
          The authenticated user can't access the team
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````