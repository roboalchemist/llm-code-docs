# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/record-an-artifacts-cache-usage-event.md

# Record an artifacts cache usage event

> Records an artifacts cache usage event. The body of this request is an array of cache usage events. The supported event types are `HIT` and `MISS`. The source is either `LOCAL` the cache event was on the users filesystem cache or `REMOTE` if the cache event is for a remote cache. When the event is a `HIT` the request also accepts a number `duration` which is the time taken to generate the artifact in the cache.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts/events
paths:
  path: /v8/artifacts/events
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
    body:
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  additionalProperties: false
                  required:
                    - sessionId
                    - source
                    - hash
                    - event
                  properties:
                    sessionId:
                      type: string
                      description: >-
                        A UUID (universally unique identifer) for the session
                        that generated this event.
                    source:
                      type: string
                      enum:
                        - LOCAL
                        - REMOTE
                      description: >-
                        One of `LOCAL` or `REMOTE`. `LOCAL` specifies that the
                        cache event was from the user's filesystem cache.
                        `REMOTE` specifies that the cache event is from a remote
                        cache.
                    event:
                      type: string
                      enum:
                        - HIT
                        - MISS
                      description: >-
                        One of `HIT` or `MISS`. `HIT` specifies that a cached
                        artifact for `hash` was found in the cache. `MISS`
                        specifies that a cached artifact with `hash` was not
                        found.
                    hash:
                      type: string
                      example: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                      description: The artifact hash
                    duration:
                      type: number
                      description: >-
                        The time taken to generate the artifact. This should be
                        sent as a body parameter on `HIT` events.
                      example: 400
            required: true
        examples:
          example:
            value:
              - sessionId: <string>
                source: LOCAL
                event: HIT
                hash: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                duration: 400
    codeSamples:
      - label: recordEvents
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.RecordEvents(ctx, operations.RecordEventsRequest{\n        XArtifactClientCi: vercel.String(\"VERCEL\"),\n        XArtifactClientInteractive: vercel.Int64(0),\n        RequestBody: []operations.RequestBody{\n            operations.RequestBody{\n                SessionID: \"<id>\",\n                Source: operations.SourceLocal,\n                Event: operations.EventHit,\n                Hash: \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\",\n                Duration: vercel.Float64(400),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: recordEvents
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.artifacts.recordEvents({
              xArtifactClientCi: "VERCEL",
              xArtifactClientInteractive: 0,
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: [],
            });


          }

          run();
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Success. Event recorded.
        examples: {}
        description: Success. Event recorded.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the headers is invalid
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
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
  deprecated: false
  type: path
components:
  schemas: {}

````