# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/list-deployment-aliases.md

# List Deployment Aliases

> Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/deployments/{id}/aliases
paths:
  path: /v2/deployments/{id}/aliases
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
        id:
          schema:
            - type: string
              required: true
              description: The ID of the deployment the aliases should be listed for
              example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
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
      - label: listDeploymentAliases
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.ListDeploymentAliases(ctx, \"dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listDeploymentAliases
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.listDeploymentAliases({
              id: "dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa",
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
              aliases:
                allOf:
                  - items:
                      properties:
                        uid:
                          type: string
                          description: The unique identifier of the alias
                          example: 2WjyKQmM8ZnGcJsPWMrHRHrE
                        alias:
                          type: string
                          description: >-
                            The alias name, it could be a `.vercel.app`
                            subdomain or a custom domain
                          example: my-alias.vercel.app
                        created:
                          type: string
                          format: date-time
                          description: The date when the alias was created
                          example: '2017-04-26T23:00:34.232Z'
                        redirect:
                          nullable: true
                          type: string
                          description: >-
                            Target destination domain for redirect when the
                            alias is a redirect
                        protectionBypass:
                          additionalProperties:
                            oneOf:
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - shareable-link
                                  expires:
                                    type: number
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  access:
                                    type: string
                                    enum:
                                      - requested
                                      - granted
                                  scope:
                                    type: string
                                    enum:
                                      - user
                                required:
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - access
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - alias-protection-override
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - email_invite
                                required:
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                          type: object
                          description: The protection bypass for the alias
                      required:
                        - uid
                        - alias
                        - created
                      type: object
                      description: A list of the aliases assigned to the deployment
                    type: array
                    description: A list of the aliases assigned to the deployment
            requiredProperties:
              - aliases
        examples:
          example:
            value:
              aliases:
                - uid: 2WjyKQmM8ZnGcJsPWMrHRHrE
                  alias: my-alias.vercel.app
                  created: '2017-04-26T23:00:34.232Z'
                  redirect: <string>
                  protectionBypass: {}
        description: The list of aliases assigned to the deployment
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The deployment was not found
        examples: {}
        description: The deployment was not found
  deprecated: false
  type: path
components:
  schemas: {}

````