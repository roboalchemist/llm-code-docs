# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/get-a-single-check.md

# Get a single check

> Return a detailed response for a single check.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks/{checkId}
paths:
  path: /v1/deployments/{deploymentId}/checks/{checkId}
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
      path:
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to get the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
        checkId:
          schema:
            - type: string
              required: true
              description: The check to fetch
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
    body: {}
    codeSamples:
      - label: getCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.GetCheck(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", \"check_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.getCheck({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              checkId: "check_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
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
            description: >-
              You do not have permission to access this resource.

              The provided token is not from an OAuth2 Client that created the
              Check
        examples: {}
        description: |-
          You do not have permission to access this resource.
          The provided token is not from an OAuth2 Client that created the Check
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
  deprecated: false
  type: path
components:
  schemas: {}

````