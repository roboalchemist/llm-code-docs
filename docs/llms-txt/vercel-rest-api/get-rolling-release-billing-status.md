# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/get-rolling-release-billing-status.md

# Get rolling release billing status

> Get the Rolling Releases billing status for a project. The team level billing status is used to determine if the project can be configured for rolling releases.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release/billing
paths:
  path: /v1/projects/{idOrName}/rolling-release/billing
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
        idOrName:
          schema:
            - type: string
              required: true
              description: Project ID or project name (URL-encoded)
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
      - label: getRollingReleaseBillingStatus
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.rollingRelease.getRollingReleaseBillingStatus({
              idOrName: "<value>",
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
              availableSlots:
                allOf:
                  - type: number
                    enum:
                      - 0
              reason:
                allOf:
                  - type: string
                    enum:
                      - plan_not_supported
              message:
                allOf:
                  - type: string
            requiredProperties:
              - availableSlots
              - reason
              - message
          - type: object
            properties:
              availableSlots:
                allOf:
                  - type: string
                    enum:
                      - unlimited
              reason:
                allOf:
                  - type: string
                    enum:
                      - unlimited_slots
              message:
                allOf:
                  - type: string
            requiredProperties:
              - availableSlots
              - reason
              - message
          - type: object
            properties:
              availableSlots:
                allOf:
                  - type: number
                    enum:
                      - 0
              reason:
                allOf:
                  - type: string
                    enum:
                      - no_available_slots
              message:
                allOf:
                  - type: string
              enabledProjects:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - availableSlots
              - reason
              - message
              - enabledProjects
          - type: object
            properties:
              availableSlots:
                allOf:
                  - type: number
              reason:
                allOf:
                  - type: string
                    enum:
                      - available_slots
              message:
                allOf:
                  - type: string
            requiredProperties:
              - availableSlots
              - reason
              - message
        examples:
          example:
            value:
              availableSlots: 0
              reason: plan_not_supported
              message: <string>
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
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````