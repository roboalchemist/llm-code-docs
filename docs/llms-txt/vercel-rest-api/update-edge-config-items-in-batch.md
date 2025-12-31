# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/update-edge-config-items-in-batch.md

# Update Edge Config items in batch

> Update multiple Edge Config Items in batch.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/edge-config/{edgeConfigId}/items
paths:
  path: /v1/edge-config/{edgeConfigId}/items
  method: patch
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
        edgeConfigId:
          schema:
            - type: string
              required: true
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
              items:
                allOf:
                  - type: array
                    items:
                      oneOf:
                        - type: object
                          properties:
                            operation:
                              enum:
                                - create
                                - update
                                - upsert
                                - delete
                            key:
                              maxLength: 256
                              pattern: ^[\\w-]+$
                              type: string
                            value:
                              nullable: true
                            description:
                              oneOf:
                                - type: string
                                  maxLength: 512
                                - {}
                              nullable: true
                          anyOf:
                            - properties:
                                operation:
                                  type: string
                                  enum:
                                    - create
                              required:
                                - operation
                                - key
                                - value
                            - properties:
                                operation:
                                  enum:
                                    - update
                                    - upsert
                              required:
                                - operation
                                - key
                                - value
                            - properties:
                                operation:
                                  enum:
                                    - update
                                    - upsert
                              required:
                                - operation
                                - key
                                - description
            requiredProperties:
              - items
            additionalProperties: false
        examples:
          example:
            value:
              items:
                - operation: create
                  key: <string>
                  value: <any>
                  description: <string>
    codeSamples:
      - label: patchEdgeConfigItems
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.patchEdgeConfigItems({
              edgeConfigId: "<id>",
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
              status:
                allOf:
                  - type: string
            requiredProperties:
              - status
        examples:
          example:
            value:
              status: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '409': {}
    '412': {}
  deprecated: false
  type: path
components:
  schemas: {}

````