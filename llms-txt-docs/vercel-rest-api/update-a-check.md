# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/update-a-check.md

# Update a check

> Update an existing check. This endpoint must be called with an OAuth2 or it will produce a 400 error.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/checks/{checkId}
paths:
  path: /v1/deployments/{deploymentId}/checks/{checkId}
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
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to update the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
        checkId:
          schema:
            - type: string
              required: true
              description: The check being updated
              example: check_2qn7PZrx89yxY34vEZPD31Y9XVj6
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
              status:
                allOf:
                  - description: The current status of the check
                    enum:
                      - running
                      - completed
              conclusion:
                allOf:
                  - description: The result of the check being run
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
              detailsUrl:
                allOf:
                  - description: >-
                      A URL a user may visit to see more information about the
                      check
                    type: string
                    example: https://example.com/check/run/1234abc
              output:
                allOf:
                  - description: The results of the check Run
                    type: object
                    properties:
                      metrics:
                        type: object
                        description: Metrics about the page
                        required:
                          - FCP
                          - LCP
                          - CLS
                          - TBT
                        additionalProperties: false
                        properties:
                          FCP:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 1200
                                description: First Contentful Paint value
                                nullable: true
                              previousValue:
                                type: number
                                example: 900
                                description: >-
                                  Previous First Contentful Paint value to
                                  display a delta
                              source:
                                type: string
                                enum:
                                  - web-vitals
                          LCP:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 1200
                                description: Largest Contentful Paint value
                                nullable: true
                              previousValue:
                                type: number
                                example: 1000
                                description: >-
                                  Previous Largest Contentful Paint value to
                                  display a delta
                              source:
                                type: string
                                enum:
                                  - web-vitals
                          CLS:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 4
                                description: Cumulative Layout Shift value
                                nullable: true
                              previousValue:
                                type: number
                                example: 2
                                description: >-
                                  Previous Cumulative Layout Shift value to
                                  display a delta
                              source:
                                type: string
                                enum:
                                  - web-vitals
                          TBT:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 3000
                                description: Total Blocking Time value
                                nullable: true
                              previousValue:
                                type: number
                                example: 3500
                                description: >-
                                  Previous Total Blocking Time value to display
                                  a delta
                              source:
                                enum:
                                  - web-vitals
                          virtualExperienceScore:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: integer
                                maximum: 100
                                minimum: 0
                                example: 30
                                description: >-
                                  The calculated Virtual Experience Score value,
                                  between 0 and 100
                                nullable: true
                              previousValue:
                                type: integer
                                maximum: 100
                                minimum: 0
                                example: 35
                                description: >-
                                  A previous Virtual Experience Score value to
                                  display a delta, between 0 and 100
                              source:
                                enum:
                                  - web-vitals
              externalId:
                allOf:
                  - description: An identifier that can be used as an external reference
                    type: string
                    example: 1234abc
            required: true
        examples:
          example:
            value:
              name: Performance Check
              path: /
              status: running
              conclusion: canceled
              detailsUrl: https://example.com/check/run/1234abc
              output:
                metrics:
                  FCP:
                    value: 1200
                    previousValue: 900
                    source: web-vitals
                  LCP:
                    value: 1200
                    previousValue: 1000
                    source: web-vitals
                  CLS:
                    value: 4
                    previousValue: 2
                    source: web-vitals
                  TBT:
                    value: 3000
                    previousValue: 3500
                    source: web-vitals
                  virtualExperienceScore:
                    value: 30
                    previousValue: 35
                    source: web-vitals
              externalId: 1234abc
    codeSamples:
      - label: updateCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.UpdateCheck(ctx, operations.UpdateCheckRequest{\n        DeploymentID: \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\",\n        CheckID: \"check_2qn7PZrx89yxY34vEZPD31Y9XVj6\",\n        RequestBody: &operations.UpdateCheckRequestBody{\n            Name: vercel.String(\"Performance Check\"),\n            Path: vercel.String(\"/\"),\n            DetailsURL: vercel.String(\"https://example.com/check/run/1234abc\"),\n            Output: &operations.Output{\n                Metrics: &operations.Metrics{\n                    Fcp: operations.Fcp{\n                        Value: vercel.Float64(1200),\n                        PreviousValue: vercel.Float64(900),\n                        Source: operations.UpdateCheckSourceWebVitals,\n                    },\n                    Lcp: operations.Lcp{\n                        Value: vercel.Float64(1200),\n                        PreviousValue: vercel.Float64(1000),\n                        Source: operations.UpdateCheckChecksSourceWebVitals,\n                    },\n                    Cls: operations.Cls{\n                        Value: vercel.Float64(4),\n                        PreviousValue: vercel.Float64(2),\n                        Source: operations.UpdateCheckChecksRequestSourceWebVitals,\n                    },\n                    Tbt: operations.Tbt{\n                        Value: vercel.Float64(3000),\n                        PreviousValue: vercel.Float64(3500),\n                        Source: operations.UpdateCheckChecksRequestRequestBodySourceWebVitals,\n                    },\n                    VirtualExperienceScore: &operations.VirtualExperienceScore{\n                        Value: vercel.Int64(30),\n                        PreviousValue: vercel.Int64(35),\n                        Source: operations.UpdateCheckChecksRequestRequestBodyOutputSourceWebVitals,\n                    },\n                },\n            },\n            ExternalID: vercel.String(\"1234abc\"),\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.updateCheck({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              checkId: "check_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "Performance Check",
                path: "/",
                detailsUrl: "https://example.com/check/run/1234abc",
                output: {
                  metrics: {
                    fcp: {
                      value: 1200,
                      previousValue: 900,
                      source: "web-vitals",
                    },
                    lcp: {
                      value: 1200,
                      previousValue: 1000,
                      source: "web-vitals",
                    },
                    cls: {
                      value: 4,
                      previousValue: 2,
                      source: "web-vitals",
                    },
                    tbt: {
                      value: 3000,
                      previousValue: 3500,
                      source: "web-vitals",
                    },
                    virtualExperienceScore: {
                      value: 30,
                      previousValue: 35,
                      source: "web-vitals",
                    },
                  },
                },
                externalId: "1234abc",
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
              name:
                allOf:
                  - type: string
              path:
                allOf:
                  - type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - registered
                      - running
                      - completed
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
              id: <string>
              name: <string>
              path: <string>
              status: registered
              conclusion: canceled
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
              The provided token is not from an OAuth2 Client
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
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
            description: |-
              Check was not found
              The deployment was not found
        examples: {}
        description: |-
          Check was not found
          The deployment was not found
    '413':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The output provided is too large
        examples: {}
        description: The output provided is too large
  deprecated: false
  type: path
components:
  schemas: {}

````