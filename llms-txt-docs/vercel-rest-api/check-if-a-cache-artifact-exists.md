# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/check-if-a-cache-artifact-exists.md

# Check if a cache artifact exists

> Check that a cache artifact with the given `hash` exists. This request returns response headers only and is equivalent to a `GET` request to this endpoint where the response contains no body.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples head /v8/artifacts/{hash}
paths:
  path: /v8/artifacts/{hash}
  method: head
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
        hash:
          schema:
            - type: string
              required: true
              description: The artifact hash
              example: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
      - label: artifactExists
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.ArtifactExists(ctx, \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: artifactExists
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.artifacts.artifactExists({
              hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The artifact was found and headers are returned
        examples: {}
        description: The artifact was found and headers are returned
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The artifact was not found
        examples: {}
        description: The artifact was not found
  deprecated: false
  type: path
components:
  schemas: {}

````