# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-active-attack-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Read active attack data

> Retrieve active attack data within the last N days (default: 1 day)



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/attack-status
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/security/firewall/attack-status:
    get:
      tags:
        - security
      summary: Read active attack data
      description: 'Retrieve active attack data within the last N days (default: 1 day)'
      operationId: getActiveAttackStatus
      parameters:
        - name: projectId
          in: query
          required: true
          schema:
            type: string
        - name: since
          in: query
          required: false
          schema:
            type: number
            minimum: 1
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                  - properties:
                      anomalies:
                        items:
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
                                        - avg_requests
                                        - stddev_requests
                                        - total_requests_minute
                                        - zscore
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
                            - affectedHostMap
                            - atMinute
                            - endTime
                            - ownerId
                            - projectId
                            - startTime
                          type: object
                        type: array
                    required:
                      - anomalies
                    type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````