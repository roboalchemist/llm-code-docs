# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/creates-a-new-check.md

# Creates a new Check

> Creates a new check. This endpoint must be called with an OAuth2 or it will produce a 400 error.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks
paths:
  path: /v1/deployments/{deploymentId}/checks
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
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to create the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
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
              name:
                allOf:
                  - description: The name of the check being created
                    maxLength: 100
                    example: Performance Check
                    type: string
              path:
                allOf:
                  - description: Path of the page that is being checked
                    type: string
                    maxLength: 255
                    example: /
              blocking:
                allOf:
                  - description: >-
                      Whether the check should block a deployment from
                      succeeding
                    type: boolean
                    example: true
              detailsUrl:
                allOf:
                  - description: URL to display for further details
                    type: string
                    example: http://example.com
              externalId:
                allOf:
                  - description: An identifier that can be used as an external reference
                    type: string
                    example: 1234abc
              rerequestable:
                allOf:
                  - description: >-
                      Whether a user should be able to request for the check to
                      be rerun if it fails
                    type: boolean
                    example: true
            required: true
            requiredProperties:
              - name
              - blocking
        examples:
          example:
            value:
              name: Performance Check
              path: /
              blocking: true
              detailsUrl: http://example.com
              externalId: 1234abc
              rerequestable: true
    codeSamples:
      - label: createCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.CreateCheck(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil, &operations.CreateCheckRequestBody{\n        Name: \"Performance Check\",\n        Path: vercel.String(\"/\"),\n        Blocking: true,\n        DetailsURL: vercel.String(\"http://example.com\"),\n        ExternalID: vercel.String(\"1234abc\"),\n        Rerequestable: vercel.Bool(true),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.createCheck({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "Performance Check",
                path: "/",
                blocking: true,
                detailsUrl: "http://example.com",
                externalId: "1234abc",
                rerequestable: true,
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
                    example: chk_1a2b3c4d5e6f7g8h9i0j
              name:
                allOf:
                  - type: string
                    example: Performance Check
              path:
                allOf:
                  - type: string
                    example: /api/users
              status:
                allOf:
                  - type: string
                    enum:
                      - registered
                      - running
                      - completed
                    example: completed
              conclusion:
                allOf:
                  - type: string
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
                      - stale
                    example: succeeded
              blocking:
                allOf:
                  - type: boolean
              output:
                allOf:
                  - properties:
                      metrics:
                        properties:
                          FCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          LCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          CLS:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          TBT:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          virtualExperienceScore:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                        required:
                          - FCP
                          - LCP
                          - CLS
                          - TBT
                        type: object
                    type: object
              detailsUrl:
                allOf:
                  - type: string
              integrationId:
                allOf:
                  - type: string
              deploymentId:
                allOf:
                  - type: string
              externalId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              startedAt:
                allOf:
                  - type: number
              completedAt:
                allOf:
                  - type: number
              rerequestable:
                allOf:
                  - type: boolean
            requiredProperties:
              - id
              - name
              - status
              - blocking
              - integrationId
              - deploymentId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: chk_1a2b3c4d5e6f7g8h9i0j
              name: Performance Check
              path: /api/users
              status: completed
              conclusion: succeeded
              blocking: true
              output:
                metrics:
                  FCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  LCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  CLS:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  TBT:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  virtualExperienceScore:
                    value: 123
                    previousValue: 123
                    source: web-vitals
              detailsUrl: <string>
              integrationId: <string>
              deploymentId: <string>
              externalId: <string>
              createdAt: 123
              updatedAt: 123
              startedAt: 123
              completedAt: 123
              rerequestable: true
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              Cannot create check for finished deployment
              The provided token is not from an OAuth2 Client
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          Cannot create check for finished deployment
          The provided token is not from an OAuth2 Client
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The deployment was not found
        examples: {}
        description: The deployment was not found
  deprecated: false
  type: path
components:
  schemas: {}

````