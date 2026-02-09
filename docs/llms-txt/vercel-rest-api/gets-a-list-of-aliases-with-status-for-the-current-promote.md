# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/gets-a-list-of-aliases-with-status-for-the-current-promote.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Gets a list of aliases with status for the current promote

> Get a list of aliases related to the last promote request with their mapping status



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{projectId}/promote/aliases
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
  /v1/projects/{projectId}/promote/aliases:
    get:
      tags:
        - projects
      summary: Gets a list of aliases with status for the current promote
      description: >-
        Get a list of aliases related to the last promote request with their
        mapping status
      operationId: listPromoteAliases
      parameters:
        - name: projectId
          in: path
          required: true
          schema:
            type: string
        - name: limit
          description: Maximum number of aliases to list from a request (max 100).
          in: query
          required: false
          schema:
            description: Maximum number of aliases to list from a request (max 100).
            type: number
            example: 20
            maximum: 100
        - name: since
          description: Get aliases created after this epoch timestamp.
          in: query
          required: false
          schema:
            description: Get aliases created after this epoch timestamp.
            type: number
            example: 1609499532000
        - name: until
          description: Get aliases created before this epoch timestamp.
          in: query
          required: false
          schema:
            description: Get aliases created before this epoch timestamp.
            type: number
            example: 1612264332000
        - name: failedOnly
          description: >-
            Filter results down to aliases that failed to map to the requested
            deployment
          in: query
          required: false
          schema:
            description: >-
              Filter results down to aliases that failed to map to the requested
              deployment
            type: boolean
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
                      aliases:
                        items:
                          properties:
                            status:
                              type: string
                            alias:
                              type: string
                            id:
                              type: string
                          required:
                            - alias
                            - id
                            - status
                          type: object
                        type: array
                      pagination:
                        $ref: '#/components/schemas/Pagination'
                    required:
                      - aliases
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
  schemas:
    Pagination:
      properties:
        count:
          type: number
          description: Amount of items in the current page.
          example: 20
        next:
          nullable: true
          type: number
          description: Timestamp that must be used to request the next page.
          example: 1540095775951
        prev:
          nullable: true
          type: number
          description: Timestamp that must be used to request the previous page.
          example: 1540095775951
      required:
        - count
        - next
        - prev
      type: object
      description: >-
        This object contains information related to the pagination of the
        current request, including the necessary parameters to get the next or
        previous page of data.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````