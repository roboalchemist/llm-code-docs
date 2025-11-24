# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-items.md

# Get Edge Config items

> Returns all items of an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/items
paths:
  path: /v1/edge-config/{edgeConfigId}/items
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
      - label: getEdgeConfigItems
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigItems(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.EdgeConfigItem != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigItems
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigItems({
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
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/EdgeConfigItem'
        examples:
          example:
            value:
              - key: <string>
                value: <string>
                description: <string>
                edgeConfigId: <string>
                createdAt: 123
                updatedAt: 123
        description: List of all Edge Config items.
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
    EdgeConfigItem:
      properties:
        key:
          type: string
        value:
          $ref: '#/components/schemas/EdgeConfigItemValue'
        description:
          type: string
        edgeConfigId:
          type: string
        createdAt:
          type: number
        updatedAt:
          type: number
      required:
        - key
        - value
        - edgeConfigId
        - createdAt
        - updatedAt
      type: object
      description: The EdgeConfig.

````