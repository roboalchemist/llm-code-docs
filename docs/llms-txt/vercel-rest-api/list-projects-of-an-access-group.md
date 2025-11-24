# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/list-projects-of-an-access-group.md

# List projects of an access group

> List projects of an access group

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}/projects
paths:
  path: /v1/access-groups/{idOrName}/projects
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
              description: The ID or name of the Access Group.
              example: ag_pavWOn1iLObbXLRiwVvzmPrTWyTf
      query:
        limit:
          schema:
            - type: integer
              required: false
              description: Limit how many access group projects should be returned.
              maximum: 100
              minimum: 1
              example: 20
        next:
          schema:
            - type: string
              required: false
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
      - label: listAccessGroupProjects
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.ListAccessGroupProjects(ctx, operations.ListAccessGroupProjectsRequest{\n        IDOrName: \"ag_pavWOn1iLObbXLRiwVvzmPrTWyTf\",\n        Limit: vercel.Int64(20),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listAccessGroupProjects
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.listAccessGroupProjects({
              idOrName: "ag_pavWOn1iLObbXLRiwVvzmPrTWyTf",
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
            properties:
              projects:
                allOf:
                  - items:
                      properties:
                        projectId:
                          type: string
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_DEVELOPER
                            - PROJECT_VIEWER
                        createdAt:
                          type: string
                        updatedAt:
                          type: string
                        project:
                          properties:
                            name:
                              type: string
                            framework:
                              nullable: true
                              type: string
                            latestDeploymentId:
                              type: string
                          type: object
                      required:
                        - projectId
                        - role
                        - createdAt
                        - updatedAt
                        - project
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
              - projects
              - pagination
        examples:
          example:
            value:
              projects:
                - projectId: <string>
                  role: ADMIN
                  createdAt: <string>
                  updatedAt: <string>
                  project:
                    name: <string>
                    framework: <string>
                    latestDeploymentId: <string>
              pagination:
                count: 123
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
  deprecated: false
  type: path
components:
  schemas: {}

````