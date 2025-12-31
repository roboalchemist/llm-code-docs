# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-an-edge-config.md

# Get an Edge Config

> Returns an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}
paths:
  path: /v1/edge-config/{edgeConfigId}
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
      - label: getEdgeConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfig(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfig({
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
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
              id:
                allOf:
                  - type: string
              slug:
                allOf:
                  - type: string
                    description: >-
                      Name for the Edge Config Names are not unique. Must start
                      with an alphabetic character and can contain only
                      alphanumeric characters and underscores).
              ownerId:
                allOf:
                  - type: string
              digest:
                allOf:
                  - type: string
              transfer:
                allOf:
                  - properties:
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
                      Keeps track of the current state of the Edge Config while
                      it gets transferred.
              schema:
                allOf:
                  - type: object
              purpose:
                allOf:
                  - oneOf:
                      - properties:
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
                      - properties:
                          type:
                            type: string
                            enum:
                              - experimentation
                          resourceId:
                            type: string
                        required:
                          - type
                          - resourceId
                        type: object
              syncedToDynamoAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp of when the Edge Config was synced to DynamoDB
                      initially. It is only set when syncing the entire Edge
                      Config, not when updating.
              sizeInBytes:
                allOf:
                  - type: number
              itemCount:
                allOf:
                  - type: number
            description: The EdgeConfig.
            requiredProperties:
              - createdAt
              - updatedAt
              - id
              - slug
              - ownerId
              - digest
              - sizeInBytes
              - itemCount
        examples:
          example:
            value:
              createdAt: 123
              updatedAt: 123
              deletedAt: 123
              id: <string>
              slug: <string>
              ownerId: <string>
              digest: <string>
              transfer:
                fromAccountId: <string>
                startedAt: 123
                doneAt: 123
              schema: {}
              purpose:
                type: flags
                projectId: <string>
              syncedToDynamoAt: 123
              sizeInBytes: 123
              itemCount: 123
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
  schemas: {}

````