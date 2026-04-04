# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-cache/dangerously-delete-by-source-image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Dangerously delete by source image

> Marks a source image as deleted, causing cache entries associated with that source image to be revalidated in the foreground on the next request. Use this method with caution because one source image can be associated with many paths and deleting the cache can cause many concurrent requests to the origin leading to cache stampede problem. This method is for advanced use cases and is not recommended; prefer using `invalidateBySrcImage` instead.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-cache/dangerously-delete-by-src-images
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
  /v1/edge-cache/dangerously-delete-by-src-images:
    post:
      tags:
        - edge-cache
      summary: Dangerously delete by source image
      description: >-
        Marks a source image as deleted, causing cache entries associated with
        that source image to be revalidated in the foreground on the next
        request. Use this method with caution because one source image can be
        associated with many paths and deleting the cache can cause many
        concurrent requests to the origin leading to cache stampede problem.
        This method is for advanced use cases and is not recommended; prefer
        using `invalidateBySrcImage` instead.
      operationId: dangerouslyDeleteBySrcImages
      parameters:
        - name: projectIdOrName
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
              additionalProperties: false
              type: object
              required:
                - srcImages
              properties:
                revalidationDeadlineSeconds:
                  minimum: 0
                  type: number
                srcImages:
                  items:
                    maxLength: 8192
                    type: string
                  maxItems: 8
                  minItems: 1
                  type: array
      responses:
        '200':
          description: ''
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: ''
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