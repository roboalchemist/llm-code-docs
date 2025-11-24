# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/update-the-protection-bypass-for-a-url.md

# Update the protection bypass for a URL

> Update the protection bypass for the alias or deployment URL (used for user access & comment access for deployments). Used as shareable links and user scoped access for Vercel Authentication and also to allow external (logged in) people to comment on previews for Preview Comments (next-live-mode).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /aliases/{id}/protection-bypass
paths:
  path: /aliases/{id}/protection-bypass
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
        id:
          schema:
            - type: string
              required: true
              description: The alias or deployment ID
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
              ttl:
                allOf:
                  - description: >-
                      Optional time the shareable link is valid for in seconds.
                      If not provided, the shareable link will never expire.
                    type: number
                    maximum: 63072000
              revoke:
                allOf:
                  - description: >-
                      Optional instructions for revoking and regenerating a
                      shareable link
                    type: object
                    properties:
                      secret:
                        description: Sharebale link to revoked
                        type: string
                      regenerate:
                        description: >-
                          Whether or not a new shareable link should be created
                          after the provided secret is revoked
                        type: boolean
                    required:
                      - secret
                      - regenerate
            additionalProperties: false
          - type: object
            properties:
              scope:
                allOf:
                  - description: Instructions for creating a user scoped protection bypass
                    type: object
                    properties:
                      userId:
                        type: string
                        description: Specified user id for the scoped bypass.
                      email:
                        type: string
                        format: email
                        description: Specified email for the scoped bypass.
                      access:
                        enum:
                          - denied
                          - granted
                        description: Invitation status for the user scoped bypass.
                    allOf:
                      - anyOf:
                          - required:
                              - userId
                          - required:
                              - email
                      - required:
                          - access
            requiredProperties:
              - scope
            additionalProperties: false
          - type: object
            properties:
              override:
                allOf:
                  - type: object
                    properties:
                      scope:
                        enum:
                          - alias-protection-override
                      action:
                        enum:
                          - create
                          - revoke
                    required:
                      - scope
                      - action
            requiredProperties:
              - override
            additionalProperties: false
        examples:
          example:
            value:
              ttl: 123
              revoke:
                secret: <string>
                regenerate: true
    codeSamples:
      - label: patchUrlProtectionBypass
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.patchUrlProtectionBypass({
              id: "<id>",
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
    '428': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````