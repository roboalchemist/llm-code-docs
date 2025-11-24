# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-an-edge-config-item.md

# Get an Edge Config item

> Returns a specific Edge Config Item.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/item/{edgeConfigItemKey}
paths:
  path: /v1/edge-config/{edgeConfigId}/item/{edgeConfigItemKey}
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
        edgeConfigId:
          schema:
            - type: string
              required: true
        edgeConfigItemKey:
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
    body: {}
    codeSamples:
      - label: getEdgeConfigItem
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigItem(ctx, \"<id>\", \"<value>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.EdgeConfigItem != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigItem
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigItem({
              edgeConfigId: "<id>",
              edgeConfigItemKey: "<value>",
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
              key:
                allOf:
                  - type: string
              value:
                allOf:
                  - $ref: '#/components/schemas/EdgeConfigItemValue'
              description:
                allOf:
                  - type: string
              edgeConfigId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
            description: The EdgeConfig.
            refIdentifier: '#/components/schemas/EdgeConfigItem'
            requiredProperties:
              - key
              - value
              - edgeConfigId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              key: <string>
              value: <string>
              description: <string>
              edgeConfigId: <string>
              createdAt: 123
              updatedAt: 123
        description: The EdgeConfig.
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
  schemas:
    EdgeConfigItemValue:
      nullable: true
      oneOf:
        - type: string
        - type: number
        - type: boolean
        - additionalProperties:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: object
        - items:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: array

````