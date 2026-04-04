# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-system-bypass.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Read System Bypass

> Retrieve the system bypass rules configured for the specified project



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/bypass
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
  /v1/security/firewall/bypass:
    get:
      tags:
        - security
      summary: Read System Bypass
      description: Retrieve the system bypass rules configured for the specified project
      operationId: getBypassIp
      parameters:
        - name: projectId
          in: query
          required: true
          schema:
            type: string
        - name: limit
          in: query
          required: false
          schema:
            type: number
            example: 10
            maximum: 256
        - name: sourceIp
          description: Filter by source IP
          in: query
          required: false
          schema:
            description: Filter by source IP
            type: string
            maxLength: 49
        - name: domain
          description: Filter by domain
          in: query
          required: false
          schema:
            description: Filter by domain
            type: string
            pattern: ([a-z]+[a-z.]+)$
            maxLength: 2544
        - name: projectScope
          description: Filter by project scoped rules
          in: query
          required: false
          schema:
            description: Filter by project scoped rules
            type: boolean
        - name: offset
          description: Used for pagination. Retrieves results after the provided id
          in: query
          required: false
          schema:
            description: Used for pagination. Retrieves results after the provided id
            type: string
            maxLength: 2560
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
                properties:
                  result:
                    items:
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
                            - bypass
                            - block
                        ProjectId:
                          type: string
                        IsProjectRule:
                          type: boolean
                          enum:
                            - false
                            - true
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
                        - CreatedAt
                        - Domain
                        - Id
                        - Ip
                        - OwnerId
                        - UpdatedAt
                        - UpdatedAtHour
                      type: object
                    type: array
                  pagination:
                    properties:
                      OwnerId:
                        type: string
                      Id:
                        type: string
                    required:
                      - Id
                      - OwnerId
                    type: object
                required:
                  - result
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '500':
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