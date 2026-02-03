# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/record-an-artifacts-cache-usage-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Record an artifacts cache usage event

> Records an artifacts cache usage event. The body of this request is an array of cache usage events. The supported event types are `HIT` and `MISS`. The source is either `LOCAL` the cache event was on the users filesystem cache or `REMOTE` if the cache event is for a remote cache. When the event is a `HIT` the request also accepts a number `duration` which is the time taken to generate the artifact in the cache.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts/events
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v8/artifacts/events:
    post:
      tags:
        - artifacts
      summary: Record an artifacts cache usage event
      description: >-
        Records an artifacts cache usage event. The body of this request is an
        array of cache usage events. The supported event types are `HIT` and
        `MISS`. The source is either `LOCAL` the cache event was on the users
        filesystem cache or `REMOTE` if the cache event is for a remote cache.
        When the event is a `HIT` the request also accepts a number `duration`
        which is the time taken to generate the artifact in the cache.
      operationId: recordEvents
      parameters:
        - in: header
          description: >-
            The continuous integration or delivery environment where this
            artifact is downloaded.
          schema:
            type: string
            description: >-
              The continuous integration or delivery environment where this
              artifact is downloaded.
            example: VERCEL
            maxLength: 50
          name: x-artifact-client-ci
        - in: header
          description: 1 if the client is an interactive shell. Otherwise 0
          schema:
            type: integer
            description: 1 if the client is an interactive shell. Otherwise 0
            example: 0
            minimum: 0
            maximum: 1
          name: x-artifact-client-interactive
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
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
                      A UUID (universally unique identifer) for the session that
                      generated this event.
                  source:
                    type: string
                    enum:
                      - LOCAL
                      - REMOTE
                    description: >-
                      One of `LOCAL` or `REMOTE`. `LOCAL` specifies that the
                      cache event was from the user's filesystem cache. `REMOTE`
                      specifies that the cache event is from a remote cache.
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
      responses:
        '200':
          description: Success. Event recorded.
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the headers is invalid
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: >-
            The customer has reached their spend cap limit and has been paused.
            An owner can disable the cap or raise the limit in settings.

            The Remote Caching usage limit has been reached for this account for
            this billing cycle.

            Remote Caching has been disabled for this team or user. An owner can
            enable it in the billing settings.

            You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````