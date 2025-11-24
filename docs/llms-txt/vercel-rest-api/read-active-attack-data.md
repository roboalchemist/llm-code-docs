# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-active-attack-data.md

# Read active attack data

> Retrieve active attack data within the last N days (default: 1 day)

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/attack-status
paths:
  path: /v1/security/firewall/attack-status
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
        since:
          schema:
            - type: number
              required: false
              minimum: 1
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
      - label: getActiveAttackStatus
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.getActiveAttackStatus({
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
            properties: {}
          - type: object
            properties:
              anomalies:
                allOf:
                  - items:
                      properties:
                        projectId:
                          type: string
                        ownerId:
                          type: string
                        startTime:
                          type: number
                        endTime:
                          nullable: true
                          type: number
                        atMinute:
                          type: number
                        state:
                          type: string
                        affectedHostMap:
                          additionalProperties:
                            properties:
                              anomalyAlerts:
                                additionalProperties:
                                  properties:
                                    at_minute:
                                      type: string
                                    zscore:
                                      type: number
                                    total_requests_minute:
                                      type: number
                                    avg_requests:
                                      type: number
                                    stddev_requests:
                                      type: number
                                  required:
                                    - at_minute
                                    - zscore
                                    - total_requests_minute
                                    - avg_requests
                                    - stddev_requests
                                  type: object
                                type: object
                              ddosAlerts:
                                additionalProperties:
                                  properties:
                                    atMinute:
                                      type: string
                                    totalReqs:
                                      type: number
                                  required:
                                    - atMinute
                                    - totalReqs
                                  type: object
                                type: object
                            type: object
                          type: object
                      required:
                        - projectId
                        - ownerId
                        - startTime
                        - endTime
                        - atMinute
                        - affectedHostMap
                      type: object
                    type: array
            requiredProperties:
              - anomalies
        examples:
          example:
            value: {}
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
  deprecated: false
  type: path
components:
  schemas: {}

````