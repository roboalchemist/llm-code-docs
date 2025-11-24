# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/remove-system-bypass-rule.md

# Remove System Bypass Rule

> Remove system bypass rules

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/security/firewall/bypass
paths:
  path: /v1/security/firewall/bypass
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
      path: {}
      query:
        projectId:
          schema:
            - type: string
              required: true
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
              domain:
                allOf:
                  - &ref_0
                    type: string
                    pattern: ([a-z]+[a-z.]+)$
                    maxLength: 2544
              projectScope:
                allOf:
                  - &ref_1
                    type: boolean
              sourceIp:
                allOf:
                  - &ref_2
                    type: string
              allSources:
                allOf:
                  - &ref_3
                    type: boolean
              note:
                allOf:
                  - &ref_4
                    type: string
                    maxLength: 500
            requiredProperties:
              - domain
            additionalProperties: false
          - type: object
            properties:
              domain:
                allOf:
                  - *ref_0
              projectScope:
                allOf:
                  - *ref_1
              sourceIp:
                allOf:
                  - *ref_2
              allSources:
                allOf:
                  - *ref_3
              note:
                allOf:
                  - *ref_4
            requiredProperties:
              - projectScope
            additionalProperties: false
        examples:
          example:
            value:
              domain: <string>
              projectScope: true
              sourceIp: <string>
              allSources: true
              note: <string>
    codeSamples:
      - label: removeBypassIp
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.removeBypassIp({
              projectId: "<id>",
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
              ok:
                allOf:
                  - type: boolean
            requiredProperties:
              - ok
        examples:
          example:
            value:
              ok: true
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````