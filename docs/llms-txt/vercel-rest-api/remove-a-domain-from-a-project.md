# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/remove-a-domain-from-a-project.md

# Remove a domain from a project

> Remove a domain from a project by passing the domain name and by specifying the project by either passing the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}/domains/{domain}
paths:
  path: /v9/projects/{idOrName}/domains/{domain}
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
        domain:
          schema:
            - type: string
              required: true
              description: The project domain name
              example: www.example.com
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
              removeRedirects:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to remove all domains from this project that
                      redirect to the domain being removed.
        examples:
          example:
            value:
              removeRedirects: true
    codeSamples:
      - label: removeProjectDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.RemoveProjectDomain(ctx, \"<value>\", \"www.example.com\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: removeProjectDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.removeProjectDomain({
              idOrName: "<value>",
              domain: "www.example.com",
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
        examples:
          example:
            value: {}
        description: The domain was succesfully removed from the project
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
    '404': {}
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The project is currently being transferred
        examples: {}
        description: The project is currently being transferred
  deprecated: false
  type: path
components:
  schemas: {}

````