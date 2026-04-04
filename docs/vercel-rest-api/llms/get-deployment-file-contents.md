# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/get-deployment-file-contents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Deployment File Contents

> Allows to retrieve the content of a file by supplying the file identifier and the deployment unique identifier. The response body will contain a JSON response containing the contents of the file encoded as base64.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/deployments/{id}/files/{fileId}
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
  /v8/deployments/{id}/files/{fileId}:
    get:
      tags:
        - deployments
      summary: Get Deployment File Contents
      description: >-
        Allows to retrieve the content of a file by supplying the file
        identifier and the deployment unique identifier. The response body will
        contain a JSON response containing the contents of the file encoded as
        base64.
      operationId: getDeploymentFileContents
      parameters:
        - name: id
          description: The unique deployment identifier
          in: path
          required: true
          schema:
            description: The unique deployment identifier
            type: string
        - name: fileId
          description: The unique file identifier
          in: path
          required: true
          schema:
            description: The unique file identifier
            type: string
        - name: path
          description: Path to the file to fetch (only for Git deployments)
          in: query
          required: false
          schema:
            description: Path to the file to fetch (only for Git deployments)
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
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: |-
            File not found
            Deployment not found
        '410':
          description: Invalid API version.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````