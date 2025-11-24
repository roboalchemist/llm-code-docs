# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/create-an-edge-config.md

# Create an Edge Config

> Creates an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config
paths:
  path: /v1/edge-config
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
              slug:
                allOf:
                  - maxLength: 64
                    pattern: ^[\\w-]+$
                    type: string
              items:
                allOf:
                  - type: object
                    additionalProperties: {}
            required: true
            requiredProperties:
              - slug
        examples:
          example:
            value:
              slug: <string>
              items: {}
    codeSamples:
      - label: createEdgeConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.CreateEdgeConfig(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createEdgeConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.createEdgeConfig({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                slug: "<value>",
              },
            });

            console.log(result);
          }

          run();
  response:
    '201':
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
            description: An Edge Config
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
  deprecated: false
  type: path
components:
  schemas: {}

````