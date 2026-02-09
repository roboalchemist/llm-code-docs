# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/list-deployment-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List Deployment Files

> Allows to retrieve the file structure of the source code of a deployment by supplying the deployment unique identifier. If the deployment was created with the Vercel CLI or the API directly with the `files` key, it will have a file tree that can be retrievable.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments/{id}/files
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
  /v6/deployments/{id}/files:
    get:
      tags:
        - deployments
      summary: List Deployment Files
      description: >-
        Allows to retrieve the file structure of the source code of a deployment
        by supplying the deployment unique identifier. If the deployment was
        created with the Vercel CLI or the API directly with the `files` key, it
        will have a file tree that can be retrievable.
      operationId: listDeploymentFiles
      parameters:
        - name: id
          description: The unique deployment identifier
          in: path
          required: true
          schema:
            description: The unique deployment identifier
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
          description: Retrieved the file tree successfully
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/FileTree'
                type: array
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: |-
            File tree not found
            Deployment not found
      security:
        - bearerToken: []
components:
  schemas:
    FileTree:
      properties:
        name:
          type: string
          description: The name of the file tree entry
          example: my-file.json
        type:
          type: string
          enum:
            - directory
            - file
            - symlink
            - lambda
            - middleware
            - invalid
          description: String indicating the type of file tree entry.
          example: file
        uid:
          type: string
          description: The unique identifier of the file (only valid for the `file` type)
          example: 2d4aad419917f15b1146e9e03ddc9bb31747e4d0
        children:
          items:
            $ref: '#/components/schemas/FileTree'
          type: array
          description: >-
            The list of children files of the directory (only valid for the
            `directory` type)
        contentType:
          type: string
          description: The content-type of the file (only valid for the `file` type)
          example: application/json
        mode:
          type: number
          description: The file "mode" indicating file type and permissions.
      required:
        - mode
        - name
        - type
      type: object
      description: A deployment file tree entry
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````