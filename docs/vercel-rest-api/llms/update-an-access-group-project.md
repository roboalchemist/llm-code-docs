# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/update-an-access-group-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an access group project

> Allows update of an access group project



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
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
  /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}:
    patch:
      tags:
        - access-groups
      summary: Update an access group project
      description: Allows update of an access group project
      operationId: updateAccessGroupProject
      parameters:
        - name: accessGroupIdOrName
          in: path
          required: true
          schema:
            type: string
          examples:
            id:
              summary: Access group ID
              value: ag_1a2b3c4d5e6f7g8h9i0j
            name:
              summary: Access group name
              value: My Access Group
        - name: projectId
          in: path
          required: true
          schema:
            type: string
          example: prj_ndlgr43fadlPyCtREAqxxdyFK
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              required:
                - role
              properties:
                role:
                  type: string
                  example: ADMIN
                  description: The project role that will be added to this Access Group.
                  enum:
                    - ADMIN
                    - PROJECT_VIEWER
                    - PROJECT_DEVELOPER
                    - null
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  teamId:
                    type: string
                  accessGroupId:
                    type: string
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
                required:
                  - accessGroupId
                  - createdAt
                  - projectId
                  - role
                  - teamId
                  - updatedAt
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
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