# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/update-or-move-apex-domain.md

# Update or move apex domain

> Update or move apex domain. Note: This endpoint is no longer used for updating auto-renew or nameservers. For this, please use the endpoints [Update auto-renew for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain) and [Update nameservers for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v3/domains/{domain}
paths:
  path: /v3/domains/{domain}
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
        domain:
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
              op:
                allOf:
                  - example: update
                    type: string
              renew:
                allOf:
                  - description: >-
                      This field is deprecated. Please use PATCH
                      /v1/registrar/domains/{domainName}/auto-renew instead.
                    type: boolean
                    deprecated: true
              customNameservers:
                allOf:
                  - description: >-
                      This field is deprecated. Please use PATCH
                      /v1/registrar/domains/{domainName}/nameservers instead.
                    items:
                      type: string
                    maxItems: 4
                    minItems: 0
                    type: array
                    uniqueItems: true
                    deprecated: true
              zone:
                allOf:
                  - description: >-
                      Specifies whether this is a DNS zone that intends to use
                      Vercel's nameservers.
                    type: boolean
            required: true
            description: update
            additionalProperties: false
          - type: object
            properties:
              op:
                allOf:
                  - example: move-out
                    type: string
              destination:
                allOf:
                  - description: User or team to move domain to
                    type: string
            required: true
            description: move-out
            additionalProperties: false
        examples:
          example:
            value:
              op: update
              renew: true
              customNameservers:
                - <string>
              zone: true
    codeSamples:
      - label: patchDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.PatchDomain(ctx, \"tight-secrecy.info\", nil, nil, vercel.Pointer(operations.CreatePatchDomainRequestBodyPatchDomainRequestBody1(\n        operations.PatchDomainRequestBody1{\n            Op: vercel.String(\"update\"),\n        },\n    )))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: patchDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.patchDomain({
              domain: "flimsy-napkin.com",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                op: "update",
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
              moved:
                allOf:
                  - type: boolean
            requiredProperties:
              - moved
          - type: object
            properties:
              moved:
                allOf:
                  - type: boolean
              token:
                allOf:
                  - type: string
            requiredProperties:
              - moved
              - token
          - type: object
            properties:
              renew:
                allOf:
                  - type: boolean
              customNameservers:
                allOf:
                  - items:
                      type: string
                    type: array
              zone:
                allOf:
                  - type: boolean
        examples:
          example:
            value:
              moved: true
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````