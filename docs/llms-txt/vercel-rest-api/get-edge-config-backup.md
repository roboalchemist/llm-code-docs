# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-backup.md

# Get Edge Config backup

> Retrieves a specific version of an Edge Config from backup storage.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/backups/{edgeConfigBackupVersionId}
paths:
  path: /v1/edge-config/{edgeConfigId}/backups/{edgeConfigBackupVersionId}
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
        edgeConfigBackupVersionId:
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
      - label: getEdgeConfigBackup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigBackup(ctx, \"<id>\", \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigBackup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigBackup({
              edgeConfigId: "<id>",
              edgeConfigBackupVersionId: "<id>",
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
              id:
                allOf:
                  - type: string
              lastModified:
                allOf:
                  - type: number
              backup:
                allOf:
                  - properties:
                      digest:
                        type: string
                      items:
                        additionalProperties:
                          properties:
                            updatedAt:
                              type: number
                            value:
                              $ref: '#/components/schemas/EdgeConfigItemValue'
                            description:
                              type: string
                            createdAt:
                              type: number
                          required:
                            - updatedAt
                            - value
                            - createdAt
                          type: object
                        type: object
                      slug:
                        type: string
                        description: >-
                          Name for the Edge Config Names are not unique. Must
                          start with an alphabetic character and can contain
                          only alphanumeric characters and underscores).
                      updatedAt:
                        type: number
                    required:
                      - digest
                      - items
                      - slug
                      - updatedAt
                    type: object
              metadata:
                allOf:
                  - properties:
                      updatedAt:
                        type: string
                      updatedBy:
                        type: string
                      itemsCount:
                        type: number
                      itemsBytes:
                        type: number
                    type: object
              user:
                allOf:
                  - properties:
                      id:
                        type: string
                      username:
                        type: string
                      email:
                        type: string
                      name:
                        type: string
                      avatar:
                        type: string
                    required:
                      - id
                      - username
                      - email
                    type: object
            description: >-
              The object the API responds with when requesting an Edge Config
              backup
            requiredProperties:
              - id
              - lastModified
              - backup
              - metadata
          - type: object
            properties:
              user:
                allOf:
                  - properties:
                      id:
                        type: string
                      username:
                        type: string
                      email:
                        type: string
                      name:
                        type: string
                      avatar:
                        type: string
                    required:
                      - id
                      - username
                      - email
                    type: object
              id:
                allOf:
                  - type: string
              lastModified:
                allOf:
                  - type: number
              backup:
                allOf:
                  - properties:
                      digest:
                        type: string
                      items:
                        additionalProperties:
                          properties:
                            updatedAt:
                              type: number
                            value:
                              $ref: '#/components/schemas/EdgeConfigItemValue'
                            description:
                              type: string
                            createdAt:
                              type: number
                          required:
                            - updatedAt
                            - value
                            - createdAt
                          type: object
                        type: object
                      slug:
                        type: string
                        description: >-
                          Name for the Edge Config Names are not unique. Must
                          start with an alphabetic character and can contain
                          only alphanumeric characters and underscores).
                      updatedAt:
                        type: number
                    required:
                      - digest
                      - items
                      - slug
                      - updatedAt
                    type: object
              metadata:
                allOf:
                  - properties:
                      updatedAt:
                        type: string
                      updatedBy:
                        type: string
                      itemsCount:
                        type: number
                      itemsBytes:
                        type: number
                    type: object
            requiredProperties:
              - user
              - id
              - lastModified
              - backup
              - metadata
        examples:
          example:
            value:
              id: <string>
              lastModified: 123
              backup:
                digest: <string>
                items: {}
                slug: <string>
                updatedAt: 123
              metadata:
                updatedAt: <string>
                updatedBy: <string>
                itemsCount: 123
                itemsBytes: 123
              user:
                id: <string>
                username: <string>
                email: <string>
                name: <string>
                avatar: <string>
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