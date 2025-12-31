# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-backups.md

# Get Edge Config backups

> Returns backups of an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/backups
paths:
  path: /v1/edge-config/{edgeConfigId}/backups
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
        next:
          schema:
            - type: string
              required: false
        limit:
          schema:
            - type: number
              required: false
              maximum: 50
              minimum: 0
        metadata:
          schema:
            - type: string
              required: false
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
      - label: getEdgeConfigBackups
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigBackups(ctx, operations.GetEdgeConfigBackupsRequest{\n        EdgeConfigID: \"<id>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigBackups
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigBackups({
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
              backups:
                allOf:
                  - items:
                      properties:
                        metadata:
                          properties:
                            updatedAt:
                              type: string
                            updatedBy:
                              type: string
                            itemsCount:
                              type: number
                            itemsBytes:
                              type: number
                          type: object
                        id:
                          type: string
                        lastModified:
                          type: number
                      required:
                        - id
                        - lastModified
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      hasNext:
                        type: boolean
                      next:
                        type: string
                    required:
                      - hasNext
                    type: object
            requiredProperties:
              - backups
              - pagination
        examples:
          example:
            value:
              backups:
                - metadata:
                    updatedAt: <string>
                    updatedBy: <string>
                    itemsCount: 123
                    itemsBytes: 123
                  id: <string>
                  lastModified: 123
              pagination:
                hasNext: true
                next: <string>
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