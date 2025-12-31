# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-configs.md

# Get Edge Configs

> Returns all Edge Configs.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config
paths:
  path: /v1/edge-config
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
    body: {}
    codeSamples:
      - label: getEdgeConfigs
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigs(ctx, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseBodies != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigs
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigs({
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
                - properties:
                    id:
                      type: string
                    createdAt:
                      type: number
                    ownerId:
                      type: string
                    slug:
                      type: string
                      description: >-
                        Name for the Edge Config Names are not unique. Must
                        start with an alphabetic character and can contain only
                        alphanumeric characters and underscores).
                    updatedAt:
                      type: number
                    digest:
                      type: string
                    transfer:
                      properties:
                        fromAccountId:
                          type: string
                        startedAt:
                          type: number
                        doneAt:
                          nullable: true
                          type: number
                      required:
                        - fromAccountId
                        - startedAt
                        - doneAt
                      type: object
                      description: >-
                        Keeps track of the current state of the Edge Config
                        while it gets transferred.
                    schema:
                      type: object
                    purpose:
                      properties:
                        type:
                          type: string
                          enum:
                            - flags
                        projectId:
                          type: string
                      required:
                        - type
                        - projectId
                      type: object
                    sizeInBytes:
                      type: number
                    itemCount:
                      type: number
                  required:
                    - sizeInBytes
                    - itemCount
            description: List of all edge configs.
        examples:
          example:
            value:
              - id: <string>
                createdAt: 123
                ownerId: <string>
                slug: <string>
                updatedAt: 123
                digest: <string>
                transfer:
                  fromAccountId: <string>
                  startedAt: 123
                  doneAt: 123
                schema: {}
                purpose:
                  type: flags
                  projectId: <string>
                sizeInBytes: 123
                itemCount: 123
        description: List of all edge configs.
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
  deprecated: false
  type: path
components:
  schemas: {}

````