# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/list-projects-of-an-access-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List projects of an access group

> List projects of an access group



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}/projects
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
  /v1/access-groups/{idOrName}/projects:
    get:
      tags:
        - access-groups
      summary: List projects of an access group
      description: List projects of an access group
      operationId: listAccessGroupProjects
      parameters:
        - name: idOrName
          description: The ID or name of the Access Group.
          in: path
          required: true
          schema:
            type: string
            description: The ID or name of the Access Group.
            example: ag_pavWOn1iLObbXLRiwVvzmPrTWyTf
        - name: limit
          description: Limit how many access group projects should be returned.
          in: query
          required: false
          schema:
            description: Limit how many access group projects should be returned.
            example: 20
            type: integer
            minimum: 1
            maximum: 100
        - name: next
          description: Continuation cursor to retrieve the next page of results.
          in: query
          required: false
          schema:
            description: Continuation cursor to retrieve the next page of results.
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
                  projects:
                    items:
                      properties:
                        projectId:
                          type: string
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_DEVELOPER
                            - PROJECT_VIEWER
                            - PROJECT_GUEST
                        createdAt:
                          type: string
                        updatedAt:
                          type: string
                        project:
                          properties:
                            name:
                              type: string
                            framework:
                              nullable: true
                              type: string
                            latestDeploymentId:
                              type: string
                          type: object
                      required:
                        - createdAt
                        - project
                        - projectId
                        - role
                        - updatedAt
                      type: object
                    type: array
                  pagination:
                    properties:
                      count:
                        type: number
                      next:
                        nullable: true
                        type: string
                    required:
                      - count
                      - next
                    type: object
                required:
                  - pagination
                  - projects
                type: object
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