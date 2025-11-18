# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/upload-a-cache-artifact.md

# Upload a cache artifact

> Uploads a cache artifact identified by the `hash` specified on the path. The cache artifact can then be downloaded with the provided `hash`.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v8/artifacts/{hash}
paths:
  path: /v8/artifacts/{hash}
  method: put
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
        Content-Length:
          schema:
            - type: number
              required: true
              description: The artifact size in bytes
        x-artifact-duration:
          schema:
            - type: number
              required: false
              description: >-
                The time taken to generate the uploaded artifact in
                milliseconds.
              example: 400
        x-artifact-client-ci:
          schema:
            - type: string
              required: false
              description: >-
                The continuous integration or delivery environment where this
                artifact was generated.
              maxLength: 50
              example: VERCEL
        x-artifact-client-interactive:
          schema:
            - type: integer
              required: false
              description: 1 if the client is an interactive shell. Otherwise 0
              maximum: 1
              minimum: 0
              example: 0
        x-artifact-tag:
          schema:
            - type: string
              required: false
              description: >-
                The base64 encoded tag for this artifact. The value is sent back
                to clients when the artifact is downloaded as the header
                `x-artifact-tag`
              maxLength: 600
              example: Tc0BmHvJYMIYJ62/zx87YqO0Flxk+5Ovip25NY825CQ=
      cookie: {}
    body:
      application/octet-stream:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
    codeSamples:
      - label: uploadArtifact
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.UploadArtifact(ctx, operations.UploadArtifactRequest{\n        ContentLength: 4504.13,\n        XArtifactDuration: vercel.Float64(400),\n        XArtifactClientCi: vercel.String(\"VERCEL\"),\n        XArtifactClientInteractive: vercel.Int64(0),\n        XArtifactTag: vercel.String(\"Tc0BmHvJYMIYJ62/zx87YqO0Flxk+5Ovip25NY825CQ=\"),\n        Hash: \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: uploadArtifact
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";
          import { openAsBlob } from "node:fs";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.artifacts.uploadArtifact({
              contentLength: 3848.22,
              xArtifactDuration: 400,
              xArtifactClientCi: "VERCEL",
              xArtifactClientInteractive: 0,
              xArtifactTag: "Tc0BmHvJYMIYJ62/zx87YqO0Flxk+5Ovip25NY825CQ=",
              hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: await openAsBlob("example.file"),
            });

            console.log(result);
          }

          run();
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              urls:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Array of URLs where the artifact was updated
                    example:
                      - >-
                        https://api.vercel.com/v2/now/artifact/12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            requiredProperties:
              - urls
        examples:
          example:
            value:
              urls:
                - >-
                  https://api.vercel.com/v2/now/artifact/12HKQaOmR5t5Uy6vdcQsNIiZgHGB
        description: File successfully uploaded
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request query is invalid.
              One of the provided values in the headers is invalid
              File size is not valid
        examples: {}
        description: |-
          One of the provided values in the request query is invalid.
          One of the provided values in the headers is invalid
          File size is not valid
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