# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projectmembers/list-project-members.md

# List project members

> Lists all members of a project.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/members
paths:
  path: /v1/projects/{idOrName}/members
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The ID or name of the Project.
              example: prj_pavWOn1iLObbXLRiwVvzmPrTWyTf
      query:
        limit:
          schema:
            - type: integer
              required: false
              description: Limit how many project members should be returned
              maximum: 100
              minimum: 1
              example: 20
        since:
          schema:
            - type: integer
              required: false
              description: >-
                Timestamp in milliseconds to only include members added since
                then.
              example: 1540095775951
        until:
          schema:
            - type: integer
              required: false
              description: >-
                Timestamp in milliseconds to only include members added until
                then.
              example: 1540095775951
        search:
          schema:
            - type: string
              required: false
              description: Search project members by their name, username, and email.
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
      - label: getProjectMembers
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.ProjectMembers.GetProjectMembers(ctx, operations.GetProjectMembersRequest{\n        IDOrName: \"prj_pavWOn1iLObbXLRiwVvzmPrTWyTf\",\n        Limit: vercel.Int64(20),\n        Since: vercel.Int64(1540095775951),\n        Until: vercel.Int64(1540095775951),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getProjectMembers
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projectMembers.getProjectMembers({
              idOrName: "prj_pavWOn1iLObbXLRiwVvzmPrTWyTf",
              limit: 20,
              since: 1540095775951,
              until: 1540095775951,
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
            properties: {}
          - type: object
            properties:
              members:
                allOf:
                  - items:
                      properties:
                        avatar:
                          type: string
                          description: ID of the file for the Avatar of this member.
                          example: 123a6c5209bc3778245d011443644c8d27dc2c50
                        email:
                          type: string
                          description: The email of this member.
                          example: jane.doe@example.com
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_DEVELOPER
                            - PROJECT_VIEWER
                          description: Role of this user in the project.
                          example: ADMIN
                        computedProjectRole:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_DEVELOPER
                            - PROJECT_VIEWER
                          description: Role of this user in the project.
                          example: ADMIN
                        uid:
                          type: string
                          description: The ID of this user.
                          example: zTuNVUXEAvvnNN3IaqinkyMw
                        username:
                          type: string
                          description: The unique username of this user.
                          example: jane-doe
                        name:
                          type: string
                          description: The name of this user.
                          example: Jane Doe
                        createdAt:
                          type: number
                          description: >-
                            Timestamp in milliseconds when this member was
                            added.
                          example: 1588720733602
                        teamRole:
                          type: string
                          enum:
                            - OWNER
                            - MEMBER
                            - DEVELOPER
                            - SECURITY
                            - BILLING
                            - VIEWER
                            - VIEWER_FOR_PLUS
                            - CONTRIBUTOR
                          description: The role of this user in the team.
                          example: CONTRIBUTOR
                      required:
                        - email
                        - role
                        - computedProjectRole
                        - uid
                        - username
                        - createdAt
                        - teamRole
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      hasNext:
                        type: boolean
                      count:
                        type: number
                        description: Amount of items in the current page.
                        example: 20
                      next:
                        nullable: true
                        type: number
                        description: Timestamp that must be used to request the next page.
                        example: 1540095775951
                      prev:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp that must be used to request the previous
                          page.
                        example: 1540095775951
                    required:
                      - hasNext
                      - count
                      - next
                      - prev
                    type: object
            description: Paginated list of members for the project.
            requiredProperties:
              - members
              - pagination
        examples:
          example:
            value: {}
        description: Paginated list of members for the project.
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