# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-backups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Edge Config backups

> Returns backups of an Edge Config.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/backups
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
  /v1/edge-config/{edgeConfigId}/backups:
    get:
      tags:
        - edge-config
      summary: Get Edge Config backups
      description: Returns backups of an Edge Config.
      operationId: getEdgeConfigBackups
      parameters:
        - name: edgeConfigId
          in: path
          required: true
          schema:
            type: string
        - name: next
          in: query
          required: false
          schema:
            type: string
        - name: limit
          in: query
          required: false
          schema:
            type: number
            minimum: 0
            maximum: 50
        - name: metadata
          in: query
          required: false
          schema:
            type: string
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
                  backups:
                    items:
                      properties:
                        metadata:
                          properties:
                            updatedAt:
                              type: string
                            updatedBy:
                              type: string
                            itemsCount:
                              type: number
                            itemsBytes:
                              type: number
                          type: object
                        id:
                          type: string
                        lastModified:
                          type: number
                      required:
                        - id
                        - lastModified
                      type: object
                    type: array
                  pagination:
                    properties:
                      hasNext:
                        type: boolean
                        enum:
                          - false
                          - true
                      next:
                        type: string
                    required:
                      - hasNext
                    type: object
                required:
                  - backups
                  - pagination
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