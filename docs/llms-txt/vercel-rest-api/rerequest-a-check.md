# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/rerequest-a-check.md

# Rerequest a check

> Rerequest a selected check that has failed.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks/{checkId}/rerequest
paths:
  path: /v1/deployments/{deploymentId}/checks/{checkId}/rerequest
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
              description: The deployment to rerun the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
        checkId:
          schema:
            - type: string
              required: true
              description: The check to rerun
              example: check_2qn7PZrx89yxY34vEZPD31Y9XVj6
      query:
        autoUpdate:
          schema:
            - type: boolean
              required: false
              description: Mark the check as running
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
      - label: rerequestCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.RerequestCheck(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", \"check_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: rerequestCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.rerequestCheck({
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
            properties: {}
        examples:
          example:
            value: {}
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
            description: |-
              The deployment was not found
              Check was not found
        examples: {}
        description: |-
          The deployment was not found
          Check was not found
  deprecated: false
  type: path
components:
  schemas: {}

````