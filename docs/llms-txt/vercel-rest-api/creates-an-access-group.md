# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/creates-an-access-group.md

# Creates an access group

> Allows to create an access group

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups
paths:
  path: /v1/access-groups
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
            required: true
            requiredProperties:
              - name
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
    codeSamples:
      - label: createAccessGroup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.CreateAccessGroup(ctx, nil, nil, &operations.CreateAccessGroupRequestBody{\n        Name: \"My access group\",\n        Projects: []operations.CreateAccessGroupProjects{\n            operations.CreateAccessGroupProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.CreateAccessGroupRoleAdmin.ToPointer(),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createAccessGroup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.createAccessGroup({
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
              membersCount:
                allOf:
                  - type: number
              projectsCount:
                allOf:
                  - type: number
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
              - membersCount
              - projectsCount
              - name
              - createdAt
              - teamId
              - updatedAt
              - accessGroupId
        examples:
          example:
            value:
              entitlements:
                - v0
              membersCount: 123
              projectsCount: 123
              name: my-access-group
              createdAt: 1588720733602
              teamId: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt: 1588720733602
              accessGroupId: ag_123a6c5209bc3778245d011443644c8d27dc2c50
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