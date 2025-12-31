# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/bulk-redirects/delete-project-level-redirects.md

# Delete project-level redirects.

> Deletes the provided redirects from the latest version of the projects' bulk redirects. Stages a new change with the new redirects and returns the alias for the new version in the response.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/bulk-redirects
openapi: 3.0.3
info:
  title: Vercel SDK
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
  /v1/bulk-redirects:
    delete:
      tags:
        - bulk-redirects
      summary: Delete project-level redirects.
      description: >-
        Deletes the provided redirects from the latest version of the projects'
        bulk redirects. Stages a new change with the new redirects and returns
        the alias for the new version in the response.
      operationId: deleteRedirects
      parameters:
        - name: projectId
          in: query
          required: true
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  maxLength: 256
                redirects:
                  description: >-
                    The redirects to delete. The source of the redirect is used
                    to match the redirect to delete.
                  type: array
                  minItems: 1
                  items:
                    type: string
              required:
                - redirects
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  alias:
                    nullable: true
                    type: string
                  version:
                    properties:
                      id:
                        type: string
                        description: The unique identifier for the version.
                      key:
                        type: string
                        description: >-
                          The key of the version. The key may be duplicated
                          across versions if the contents are the same as a
                          different version.
                      lastModified:
                        type: number
                      createdBy:
                        type: string
                      name:
                        type: string
                        description: >-
                          Optional name for the version. If not provided,
                          defaults to an ISO timestamp string.
                      isStaging:
                        type: boolean
                        description: >-
                          Whether this version has not been promoted to
                          production yet and is not serving end users.
                      isLive:
                        type: boolean
                        description: Whether this version is currently live in production.
                      redirectCount:
                        type: number
                        description: The number of redirects in this version.
                      alias:
                        type: string
                        description: >-
                          The staging link for previewing redirects in this
                          version.
                    required:
                      - id
                      - key
                      - lastModified
                      - createdBy
                    type: object
                required:
                  - alias
                  - version
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt