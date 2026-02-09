# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-configs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Edge Configs

> Returns all Edge Configs.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config
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
  /v1/edge-config:
    get:
      tags:
        - edge-config
      summary: Get Edge Configs
      description: Returns all Edge Configs.
      operationId: getEdgeConfigs
      parameters:
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
          description: List of all edge configs.
          content:
            application/json:
              schema:
                type: array
                description: List of all edge configs.
                items:
                  properties:
                    id:
                      type: string
                    createdAt:
                      type: number
                    ownerId:
                      type: string
                    slug:
                      type: string
                      description: >-
                        Name for the Edge Config Names are not unique. Must
                        start with an alphabetic character and can contain only
                        alphanumeric characters and underscores).
                    updatedAt:
                      type: number
                    digest:
                      type: string
                    transfer:
                      properties:
                        fromAccountId:
                          type: string
                        startedAt:
                          type: number
                        doneAt:
                          nullable: true
                          type: number
                      required:
                        - fromAccountId
                        - startedAt
                        - doneAt
                      type: object
                      description: >-
                        Keeps track of the current state of the Edge Config
                        while it gets transferred.
                    schema:
                      type: object
                    purpose:
                      properties:
                        type:
                          type: string
                          enum:
                            - flags
                        projectId:
                          type: string
                      required:
                        - type
                        - projectId
                      type: object
                    sizeInBytes:
                      type: number
                    itemCount:
                      type: number
                  required:
                    - sizeInBytes
                    - itemCount
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````