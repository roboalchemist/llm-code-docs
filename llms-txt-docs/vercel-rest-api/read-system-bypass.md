# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-system-bypass.md

# Read System Bypass

> Retrieve the system bypass rules configured for the specified project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/bypass
paths:
  path: /v1/security/firewall/bypass
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
              required: true
        limit:
          schema:
            - type: number
              required: false
              maximum: 256
              example: 10
        sourceIp:
          schema:
            - type: string
              required: false
              description: Filter by source IP
              maxLength: 49
        domain:
          schema:
            - type: string
              required: false
              description: Filter by domain
              maxLength: 2544
        projectScope:
          schema:
            - type: boolean
              required: false
              description: Filter by project scoped rules
        offset:
          schema:
            - type: string
              required: false
              description: Used for pagination. Retrieves results after the provided id
              maxLength: 2560
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
      - label: getBypassIp
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.getBypassIp({
              projectId: "<id>",
              limit: 10,
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
              pagination:
                allOf:
                  - properties:
                      OwnerId:
                        type: string
                      Id:
                        type: string
                    required:
                      - OwnerId
                      - Id
                    type: object
            requiredProperties:
              - result
        examples:
          example:
            value:
              result:
                - OwnerId: <string>
                  Id: <string>
                  Domain: <string>
                  Ip: <string>
                  Action: block
                  ProjectId: <string>
                  IsProjectRule: true
                  Note: <string>
                  CreatedAt: <string>
                  ActorId: <string>
                  UpdatedAt: <string>
                  UpdatedAtHour: <string>
                  DeletedAt: <string>
                  ExpiresAt: 123
              pagination:
                OwnerId: <string>
                Id: <string>
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
    '404': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````