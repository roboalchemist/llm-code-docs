# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/update-protection-bypass-for-automation.md

# Update Protection Bypass for Automation

> Update the deployment protection automation bypass for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/protection-bypass
paths:
  path: /v1/projects/{idOrName}/protection-bypass
  method: patch
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
              revoke:
                allOf:
                  - description: >-
                      Optional instructions for revoking and regenerating a
                      automation bypass
                    type: object
                    properties:
                      secret:
                        description: Automation bypass to revoked
                        type: string
                      regenerate:
                        description: >-
                          Whether or not a new automation bypass should be
                          created after the provided secret is revoked
                        type: boolean
                    required:
                      - secret
                      - regenerate
              generate:
                allOf:
                  - description: >-
                      Generate a new secret. If neither generate or revoke are
                      provided, a new random secret will be generated.
                    type: object
                    properties:
                      secret:
                        description: >-
                          Optional value of the secret to generate, don't send
                          it for oauth2 tokens
                        type: string
                        pattern: ^[a-zA-Z0-9]{32}$
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              revoke:
                secret: <string>
                regenerate: true
              generate:
                secret: <string>
    codeSamples:
      - label: updateProjectProtectionBypass
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.UpdateProjectProtectionBypass(ctx, \"<value>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateProjectProtectionBypass
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.updateProjectProtectionBypass({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {},
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
              protectionBypass:
                allOf:
                  - additionalProperties:
                      oneOf:
                        - properties:
                            createdAt:
                              type: number
                            createdBy:
                              type: string
                            scope:
                              type: string
                              enum:
                                - integration-automation-bypass
                            integrationId:
                              type: string
                            configurationId:
                              type: string
                          required:
                            - createdAt
                            - createdBy
                            - scope
                            - integrationId
                            - configurationId
                          type: object
                        - properties:
                            createdAt:
                              type: number
                            createdBy:
                              type: string
                            scope:
                              type: string
                              enum:
                                - automation-bypass
                          required:
                            - createdAt
                            - createdBy
                            - scope
                          type: object
                    type: object
        examples:
          example:
            value:
              protectionBypass: {}
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
    '404': {}
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````