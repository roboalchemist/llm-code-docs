# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projectmembers/adds-a-new-member-to-a-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Adds a new member to a project.

> Adds a new member to the project.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/members
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
  /v1/projects/{idOrName}/members:
    post:
      tags:
        - projectMembers
      summary: Adds a new member to a project.
      description: Adds a new member to the project.
      operationId: addProjectMember
      parameters:
        - name: idOrName
          description: The ID or name of the Project.
          in: path
          required: true
          schema:
            type: string
            description: The ID or name of the Project.
            example: prj_pavWOn1iLObbXLRiwVvzmPrTWyTf
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
              oneOf:
                - required:
                    - uid
                - required:
                    - username
                - required:
                    - email
              properties:
                uid:
                  type: string
                  maxLength: 256
                  example: ndlgr43fadlPyCtREAqxxdyFK
                  description: >-
                    The ID of the team member that should be added to this
                    project.
                username:
                  type: string
                  maxLength: 256
                  example: example
                  description: >-
                    The username of the team member that should be added to this
                    project.
                email:
                  type: string
                  format: email
                  example: entity@example.com
                  description: >-
                    The email of the team member that should be added to this
                    project.
                role:
                  type: string
                  example: ADMIN
                  description: The project role of the member that will be added.
                  enum:
                    - ADMIN
                    - PROJECT_VIEWER
                    - PROJECT_DEVELOPER
        required: true
      responses:
        '200':
          description: Responds with the project ID on success.
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                required:
                  - id
                type: object
                description: Responds with the project ID on success.
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
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