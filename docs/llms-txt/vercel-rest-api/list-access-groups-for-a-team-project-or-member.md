# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/list-access-groups-for-a-team-project-or-member.md

# List access groups for a team, project or member

> List access groups

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups
paths:
  path: /v1/access-groups
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
        projectId:
          schema:
            - type: string
              description: Filter access groups by project.
              example: prj_pavWOn1iLObbx3RowVvzmPrTWyTf
        search:
          schema:
            - type: string
              description: Search for access groups by name.
              example: example
        membersLimit:
          schema:
            - type: integer
              description: Number of members to include in the response.
              maximum: 100
              minimum: 1
              example: 20
        projectsLimit:
          schema:
            - type: integer
              description: Number of projects to include in the response.
              maximum: 100
              minimum: 1
              example: 20
        limit:
          schema:
            - type: integer
              description: Limit how many access group should be returned.
              maximum: 100
              minimum: 1
              example: 20
        next:
          schema:
            - type: string
              description: Continuation cursor to retrieve the next page of results.
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
      - label: listAccessGroups
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.ListAccessGroups(ctx, operations.ListAccessGroupsRequest{\n        ProjectID: vercel.String(\"prj_pavWOn1iLObbx3RowVvzmPrTWyTf\"),\n        Search: vercel.String(\"example\"),\n        MembersLimit: vercel.Int64(20),\n        ProjectsLimit: vercel.Int64(20),\n        Limit: vercel.Int64(20),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: listAccessGroups
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.listAccessGroups({
              projectId: "prj_pavWOn1iLObbx3RowVvzmPrTWyTf",
              search: "example",
              membersLimit: 20,
              projectsLimit: 20,
              limit: 20,
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
              accessGroups:
                allOf:
                  - items:
                      properties:
                        members:
                          items:
                            type: string
                          type: array
                        projects:
                          items:
                            type: string
                          type: array
                        entitlements:
                          items:
                            type: string
                          type: array
                        teamPermissions:
                          items:
                            type: string
                          type: array
                        isDsyncManaged:
                          type: boolean
                        name:
                          type: string
                          description: The name of this access group.
                          example: my-access-group
                        createdAt:
                          type: string
                          description: >-
                            Timestamp in milliseconds when the access group was
                            created.
                          example: 1588720733602
                        teamId:
                          type: string
                          description: ID of the team that this access group belongs to.
                          example: team_123a6c5209bc3778245d011443644c8d27dc2c50
                        updatedAt:
                          type: string
                          description: >-
                            Timestamp in milliseconds when the access group was
                            last updated.
                          example: 1588720733602
                        accessGroupId:
                          type: string
                          description: ID of the access group.
                          example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
                        membersCount:
                          type: number
                          description: Number of members in the access group.
                          example: 5
                        projectsCount:
                          type: number
                          description: Number of projects in the access group.
                          example: 2
                        teamRoles:
                          items:
                            type: string
                          type: array
                          description: Roles that the team has in the access group.
                          example:
                            - DEVELOPER
                            - BILLING
                      required:
                        - isDsyncManaged
                        - name
                        - createdAt
                        - teamId
                        - updatedAt
                        - accessGroupId
                        - membersCount
                        - projectsCount
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      count:
                        type: number
                      next:
                        nullable: true
                        type: string
                    required:
                      - count
                      - next
                    type: object
            requiredProperties:
              - accessGroups
              - pagination
        examples:
          example:
            value: {}
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
  deprecated: false
  type: path
components:
  schemas: {}

````