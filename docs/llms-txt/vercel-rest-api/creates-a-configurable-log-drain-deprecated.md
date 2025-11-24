# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/creates-a-configurable-log-drain-deprecated.md

# Creates a Configurable Log Drain (deprecated)

> Creates a configurable log drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed)

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/log-drains
paths:
  path: /v1/log-drains
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
              deliveryFormat:
                allOf:
                  - description: The delivery log format
                    example: json
                    enum:
                      - json
                      - ndjson
              url:
                allOf:
                  - description: The log drain url
                    format: uri
                    pattern: ^(http|https)?://
                    type: string
              headers:
                allOf:
                  - description: Headers to be sent together with the request
                    type: object
                    additionalProperties:
                      type: string
              projectIds:
                allOf:
                  - minItems: 1
                    maxItems: 50
                    type: array
                    items:
                      pattern: ^[a-zA-z0-9_]+$
                      type: string
              sources:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - static
                        - lambda
                        - build
                        - edge
                        - external
                        - firewall
                    minItems: 1
              environments:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - preview
                        - production
                    minItems: 1
              secret:
                allOf:
                  - description: Custom secret of log drain
                    type: string
              samplingRate:
                allOf:
                  - type: number
                    description: >-
                      The sampling rate for this log drain. It should be a
                      percentage rate between 0 and 100. With max 2 decimal
                      points
                    minimum: 0.01
                    maximum: 1
                    multipleOf: 0.01
              name:
                allOf:
                  - type: string
                    description: The custom name of this log drain.
            required: true
            requiredProperties:
              - deliveryFormat
              - url
              - sources
            additionalProperties: false
        examples:
          example:
            value:
              deliveryFormat: json
              url: <string>
              headers: {}
              projectIds:
                - <string>
              sources:
                - static
              environments:
                - preview
              secret: <string>
              samplingRate: 0.505
              name: <string>
    codeSamples:
      - label: createConfigurableLogDrain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.CreateConfigurableLogDrain(ctx, nil, nil, &operations.CreateConfigurableLogDrainRequestBody{\n        DeliveryFormat: operations.CreateConfigurableLogDrainDeliveryFormatJSON,\n        URL: \"https://sugary-technician.name\",\n        Sources: []operations.CreateConfigurableLogDrainSources{\n            operations.CreateConfigurableLogDrainSourcesExternal,\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createConfigurableLogDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.createConfigurableLogDrain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                deliveryFormat: "json",
                url: "https://wavy-meander.net",
                sources: [],
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
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````