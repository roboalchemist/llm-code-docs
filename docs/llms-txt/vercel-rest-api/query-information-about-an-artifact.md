# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/query-information-about-an-artifact.md

# Query information about an artifact

> Query information about an array of artifacts.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts
paths:
  path: /v8/artifacts
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
              hashes:
                allOf:
                  - items:
                      type: string
                    description: artifact hashes
                    type: array
                    example:
                      - 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                      - 34HKQaOmR5t5Uy6vasdasdasdasd
            required: true
            requiredProperties:
              - hashes
        examples:
          example:
            value:
              hashes:
                - 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                - 34HKQaOmR5t5Uy6vasdasdasdasd
    codeSamples:
      - label: artifactQuery
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.ArtifactQuery(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: artifactQuery
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.artifacts.artifactQuery({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                hashes: [
                  "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
                  "34HKQaOmR5t5Uy6vasdasdasdasd",
                ],
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
            properties: {}
            additionalProperties:
              allOf:
                - nullable: true
                  oneOf:
                    - properties:
                        size:
                          type: number
                        taskDurationMs:
                          type: number
                        tag:
                          type: string
                      required:
                        - size
                        - taskDurationMs
                      type: object
                    - properties:
                        error:
                          properties:
                            message:
                              type: string
                          required:
                            - message
                          type: object
                      required:
                        - error
                      type: object
        examples:
          example:
            value: {}
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '402':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The account was soft-blocked for an unhandled reason.
              The account is missing a payment so payment method must be updated
        examples: {}
        description: |-
          The account was soft-blocked for an unhandled reason.
          The account is missing a payment so payment method must be updated
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The customer has reached their spend cap limit and has been
              paused. An owner can disable the cap or raise the limit in
              settings.

              The Remote Caching usage limit has been reached for this account
              for this billing cycle.

              Remote Caching has been disabled for this team or user. An owner
              can enable it in the billing settings.

              You do not have permission to access this resource.
        examples: {}
        description: >-
          The customer has reached their spend cap limit and has been paused. An
          owner can disable the cap or raise the limit in settings.

          The Remote Caching usage limit has been reached for this account for
          this billing cycle.

          Remote Caching has been disabled for this team or user. An owner can
          enable it in the billing settings.

          You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````