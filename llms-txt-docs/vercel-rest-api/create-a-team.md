# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/create-a-team.md

# Create a Team

> Create a new Team under your account. You need to send a POST request with the desired Team slug, and optionally the Team name.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams
paths:
  path: /v1/teams
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              slug:
                allOf:
                  - example: a-random-team
                    description: The desired slug for the Team
                    type: string
                    maxLength: 48
              name:
                allOf:
                  - example: A Random Team
                    description: >-
                      The desired name for the Team. It will be generated from
                      the provided slug if nothing is provided
                    type: string
                    maxLength: 256
              attribution:
                allOf:
                  - type: object
                    description: Attribution information for the session or current page
                    properties:
                      sessionReferrer:
                        type: string
                        description: Session referrer
                      landingPage:
                        type: string
                        description: Session landing page
                      pageBeforeConversionPage:
                        type: string
                        description: Referrer to the signup page
                      utm:
                        type: object
                        properties:
                          utmSource:
                            type: string
                            description: UTM source
                          utmMedium:
                            type: string
                            description: UTM medium
                          utmCampaign:
                            type: string
                            description: UTM campaign
                          utmTerm:
                            type: string
                            description: UTM term
            required: true
            requiredProperties:
              - slug
            additionalProperties: false
        examples:
          example:
            value:
              slug: a-random-team
              name: A Random Team
              attribution:
                sessionReferrer: <string>
                landingPage: <string>
                pageBeforeConversionPage: <string>
                utm:
                  utmSource: <string>
                  utmMedium: <string>
                  utmCampaign: <string>
                  utmTerm: <string>
    codeSamples:
      - label: createTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.CreateTeam(ctx, &operations.CreateTeamRequestBody{\n        Slug: \"a-random-team\",\n        Name: vercel.String(\"A Random Team\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.createTeam({
              slug: "a-random-team",
              name: "A Random Team",
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
                    description: Id of the created team
                    example: team_nLlpyC6RE1qxqglFKbrMxlud
              slug:
                allOf:
                  - type: string
            description: The team was created successfully
            requiredProperties:
              - id
              - slug
        examples:
          example:
            value:
              id: team_nLlpyC6RE1qxqglFKbrMxlud
              slug: <string>
        description: The team was created successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              The slug is already in use
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          The slug is already in use
    '401': {}
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````