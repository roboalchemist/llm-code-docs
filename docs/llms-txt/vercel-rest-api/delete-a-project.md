# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/delete-a-project.md

# Delete a Project

> Delete a specific project by passing either the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}
paths:
  path: /v9/projects/{idOrName}
  method: delete
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
              description: The unique project identifier or the project name
              example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
      - label: deleteProject
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.DeleteProject(ctx, \"prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.projects.deleteProject({
              idOrName: "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The project was successfuly removed
        examples: {}
        description: The project was successfuly removed
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````