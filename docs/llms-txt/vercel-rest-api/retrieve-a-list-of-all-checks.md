# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/retrieve-a-list-of-all-checks.md

# Retrieve a list of all checks

> List all of the checks created for a deployment.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks
paths:
  path: /v1/deployments/{deploymentId}/checks
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
              description: The deployment to get all checks for
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
    body: {}
    codeSamples:
      - label: getAllChecks
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.GetAllChecks(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getAllChecks
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.getAllChecks({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
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
              checks:
                allOf:
                  - items:
                      properties:
                        completedAt:
                          type: number
                        conclusion:
                          type: string
                          enum:
                            - canceled
                            - failed
                            - neutral
                            - succeeded
                            - skipped
                            - stale
                        createdAt:
                          type: number
                        detailsUrl:
                          type: string
                        id:
                          type: string
                        integrationId:
                          type: string
                        name:
                          type: string
                        output:
                          properties:
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
                        path:
                          type: string
                        rerequestable:
                          type: boolean
                        blocking:
                          type: boolean
                        startedAt:
                          type: number
                        status:
                          type: string
                          enum:
                            - registered
                            - running
                            - completed
                        updatedAt:
                          type: number
                      required:
                        - createdAt
                        - id
                        - integrationId
                        - name
                        - rerequestable
                        - blocking
                        - status
                        - updatedAt
                      type: object
                    type: array
            requiredProperties:
              - checks
        examples:
          example:
            value:
              checks:
                - completedAt: 123
                  conclusion: canceled
                  createdAt: 123
                  detailsUrl: <string>
                  id: <string>
                  integrationId: <string>
                  name: <string>
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
                  path: <string>
                  rerequestable: true
                  blocking: true
                  startedAt: 123
                  status: registered
                  updatedAt: 123
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