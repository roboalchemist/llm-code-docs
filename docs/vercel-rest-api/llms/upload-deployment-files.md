# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/upload-deployment-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload Deployment Files

> Before you create a deployment you need to upload the required files for that deployment. To do it, you need to first upload each file to this endpoint. Once that's completed, you can create a new deployment with the uploaded files. The file content must be placed inside the body of the request. In the case of a successful response you'll receive a status code 200 with an empty body.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/files
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
  /v2/files:
    post:
      tags:
        - deployments
      summary: Upload Deployment Files
      description: >-
        Before you create a deployment you need to upload the required files for
        that deployment. To do it, you need to first upload each file to this
        endpoint. Once that's completed, you can create a new deployment with
        the uploaded files. The file content must be placed inside the body of
        the request. In the case of a successful response you'll receive a
        status code 200 with an empty body.
      operationId: uploadFile
      parameters:
        - in: header
          description: The file size in bytes
          schema:
            description: The file size in bytes
            type: number
          name: Content-Length
        - in: header
          description: The file SHA1 used to check the integrity
          schema:
            type: string
            description: The file SHA1 used to check the integrity
            maxLength: 40
          name: x-vercel-digest
        - in: header
          description: The file SHA1 used to check the integrity
          schema:
            deprecated: true
            type: string
            description: The file SHA1 used to check the integrity
            maxLength: 40
          name: x-now-digest
        - in: header
          description: The file size as an alternative to `Content-Length`
          schema:
            type: number
            deprecated: true
            description: The file size as an alternative to `Content-Length`
          name: x-now-size
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
          application/octet-stream:
            schema:
              type: string
              format: binary
      responses:
        '200':
          description: |-
            File already uploaded
            File successfully uploaded
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      urls:
                        items:
                          type: string
                        type: array
                        description: Array of URLs where the file was updated
                        example:
                          - example-upload.aws.com
                    required:
                      - urls
                    type: object
                  - type: object
        '400':
          description: |-
            One of the provided values in the headers is invalid
            Digest is not valid
            File size is not valid
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