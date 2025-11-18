# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/update-an-access-group.md

# Update an access group

> Allows to update an access group metadata

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups/{idOrName}
paths:
  path: /v1/access-groups/{idOrName}
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
      path:
        idOrName:
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
              name:
                allOf:
                  - type: string
                    description: The name of the access group
                    maxLength: 50
                    pattern: ^[A-z0-9_ -]+$
                    example: My access group
              projects:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - role
                        - projectId
                      properties:
                        projectId:
                          type: string
                          maxLength: 256
                          example: prj_ndlgr43fadlPyCtREAqxxdyFK
                          description: The ID of the project.
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_VIEWER
                            - PROJECT_DEVELOPER
                            - null
                          example: ADMIN
                          description: >-
                            The project role that will be added to this Access
                            Group. \"null\" will remove this project level role.
                          nullable: true
              membersToAdd:
                allOf:
                  - description: List of members to add to the access group.
                    type: array
                    items:
                      type: string
                    example:
                      - usr_1a2b3c4d5e6f7g8h9i0j
                      - usr_2b3c4d5e6f7g8h9i0j1k
              membersToRemove:
                allOf:
                  - description: List of members to remove from the access group.
                    type: array
                    items:
                      type: string
                    example:
                      - usr_1a2b3c4d5e6f7g8h9i0j
                      - usr_2b3c4d5e6f7g8h9i0j1k
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              name: My access group
              projects:
                - projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
                  role: ADMIN
              membersToAdd:
                - usr_1a2b3c4d5e6f7g8h9i0j
                - usr_2b3c4d5e6f7g8h9i0j1k
              membersToRemove:
                - usr_1a2b3c4d5e6f7g8h9i0j
                - usr_2b3c4d5e6f7g8h9i0j1k
    codeSamples:
      - label: updateAccessGroup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.UpdateAccessGroup(ctx, \"<value>\", nil, nil, &operations.UpdateAccessGroupRequestBody{\n        Name: vercel.String(\"My access group\"),\n        Projects: []operations.Projects{\n            operations.Projects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.RoleAdmin.ToPointer(),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateAccessGroup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.updateAccessGroup({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "My access group",
                projects: [
                  {
                    projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
                    role: "ADMIN",
                  },
                ],
                membersToAdd: [
                  "usr_1a2b3c4d5e6f7g8h9i0j",
                  "usr_2b3c4d5e6f7g8h9i0j1k",
                ],
                membersToRemove: [
                  "usr_1a2b3c4d5e6f7g8h9i0j",
                  "usr_2b3c4d5e6f7g8h9i0j1k",
                ],
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
            properties:
              entitlements:
                allOf:
                  - items:
                      type: string
                      enum:
                        - v0
                    type: array
              name:
                allOf:
                  - type: string
                    description: The name of this access group.
                    example: my-access-group
              createdAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was
                      created.
                    example: 1588720733602
              teamId:
                allOf:
                  - type: string
                    description: ID of the team that this access group belongs to.
                    example: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was last
                      updated.
                    example: 1588720733602
              accessGroupId:
                allOf:
                  - type: string
                    description: ID of the access group.
                    example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              membersCount:
                allOf:
                  - type: number
                    description: Number of members in the access group.
                    example: 5
              projectsCount:
                allOf:
                  - type: number
                    description: Number of projects in the access group.
                    example: 2
              teamRoles:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Roles that the team has in the access group.
                    example:
                      - DEVELOPER
                      - BILLING
              teamPermissions:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Permissions that the team has in the access group.
                    example:
                      - CreateProject
            requiredProperties:
              - entitlements
              - name
              - createdAt
              - teamId
              - updatedAt
              - accessGroupId
              - membersCount
              - projectsCount
        examples:
          example:
            value:
              entitlements:
                - v0
              name: my-access-group
              createdAt: 1588720733602
              teamId: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt: 1588720733602
              accessGroupId: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              membersCount: 5
              projectsCount: 2
              teamRoles:
                - DEVELOPER
                - BILLING
              teamPermissions:
                - CreateProject
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