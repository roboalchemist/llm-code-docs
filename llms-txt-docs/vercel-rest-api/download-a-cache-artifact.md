# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/download-a-cache-artifact.md

# Download a cache artifact

> Downloads a cache artifact indentified by its `hash` specified on the request path. The artifact is downloaded as an octet-stream. The client should verify the content-length header and response body.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/artifacts/{hash}
paths:
  path: /v8/artifacts/{hash}
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
      header:
        x-artifact-client-ci:
          schema:
            - type: string
              description: >-
                The continuous integration or delivery environment where this
                artifact is downloaded.
              maxLength: 50
              example: VERCEL
        x-artifact-client-interactive:
          schema:
            - type: integer
              description: 1 if the client is an interactive shell. Otherwise 0
              maximum: 1
              minimum: 0
              example: 0
      cookie: {}
    body: {}
    codeSamples:
      - label: downloadArtifact
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.DownloadArtifact(ctx, operations.DownloadArtifactRequest{\n        XArtifactClientCi: vercel.String(\"VERCEL\"),\n        XArtifactClientInteractive: vercel.Int64(0),\n        Hash: \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseStream != nil {\n        // handle response\n    }\n}"
      - label: downloadArtifact
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.artifacts.downloadArtifact({
              xArtifactClientCi: "VERCEL",
              xArtifactClientInteractive: 0,
              hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
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
          - type: file
            contentEncoding: binary
            description: >-
              An octet stream response that will be piped to the response
              stream.
        examples:
          example: {}
        description: >-
          The artifact was found and is downloaded as a stream. Content-Length
          should be verified.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request query is invalid.
              One of the provided values in the headers is invalid
        examples: {}
        description: |-
          One of the provided values in the request query is invalid.
          One of the provided values in the headers is invalid
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