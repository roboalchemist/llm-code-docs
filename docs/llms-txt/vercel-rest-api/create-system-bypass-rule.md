# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/create-system-bypass-rule.md

# Create System Bypass Rule

> Create new system bypass rules

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/security/firewall/bypass
paths:
  path: /v1/security/firewall/bypass
  method: post
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
                    description: >-
                      If the specified bypass will apply to all domains for a
                      project.
              sourceIp:
                allOf:
                  - &ref_2
                    type: string
              allSources:
                allOf:
                  - &ref_3
                    type: boolean
              ttl:
                allOf:
                  - &ref_4
                    type: number
                    description: Time to live in milliseconds
              note:
                allOf:
                  - &ref_5
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
              ttl:
                allOf:
                  - *ref_4
              note:
                allOf:
                  - *ref_5
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
              ttl: 123
              note: <string>
    codeSamples:
      - label: addBypassIp
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.addBypassIp({
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
              result:
                allOf:
                  - items:
                      properties:
                        OwnerId:
                          type: string
                        Id:
                          type: string
                        Domain:
                          type: string
                        Ip:
                          type: string
                        ProjectId:
                          type: string
                        Note:
                          type: string
                        IsProjectRule:
                          type: boolean
                      required:
                        - OwnerId
                        - Id
                        - Domain
                        - ProjectId
                        - Note
                        - IsProjectRule
                      type: object
                    type: array
              pagination:
                allOf:
                  - nullable: true
            requiredProperties:
              - ok
              - result
              - pagination
          - type: object
            properties:
              ok:
                allOf:
                  - type: boolean
              result:
                allOf:
                  - items:
                      properties:
                        OwnerId:
                          type: string
                        Id:
                          type: string
                        Domain:
                          type: string
                        Ip:
                          type: string
                        Action:
                          type: string
                          enum:
                            - block
                            - bypass
                        ProjectId:
                          type: string
                        IsProjectRule:
                          type: boolean
                        Note:
                          type: string
                        CreatedAt:
                          type: string
                        ActorId:
                          type: string
                        UpdatedAt:
                          type: string
                        UpdatedAtHour:
                          type: string
                        DeletedAt:
                          type: string
                        ExpiresAt:
                          nullable: true
                          type: number
                      required:
                        - OwnerId
                        - Id
                        - Domain
                        - Ip
                        - CreatedAt
                        - UpdatedAt
                        - UpdatedAtHour
                      type: object
                    type: array
            requiredProperties:
              - ok
        examples:
          example:
            value:
              ok: true
              result:
                - OwnerId: <string>
                  Id: <string>
                  Domain: <string>
                  Ip: <string>
                  ProjectId: <string>
                  Note: <string>
                  IsProjectRule: true
              pagination: <any>
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