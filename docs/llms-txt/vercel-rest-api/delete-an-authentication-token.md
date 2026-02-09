# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/delete-an-authentication-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an authentication token

> Invalidate an authentication token, such that it will no longer be valid for future HTTP requests.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v3/user/tokens/{tokenId}
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
  /v3/user/tokens/{tokenId}:
    delete:
      tags:
        - authentication
      summary: Delete an authentication token
      description: >-
        Invalidate an authentication token, such that it will no longer be valid
        for future HTTP requests.
      operationId: deleteAuthToken
      parameters:
        - name: tokenId
          description: >-
            The identifier of the token to invalidate. The special value
            \"current\" may be supplied, which invalidates the token that the
            HTTP request was authenticated with.
          in: path
          required: true
          schema:
            type: string
            description: >-
              The identifier of the token to invalidate. The special value
              \"current\" may be supplied, which invalidates the token that the
              HTTP request was authenticated with.
            example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
      responses:
        '200':
          description: Authentication token successfully deleted.
          content:
            application/json:
              schema:
                properties:
                  tokenId:
                    type: string
                    description: The unique identifier of the token that was deleted.
                    example: >-
                      5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
                required:
                  - tokenId
                type: object
                description: Authentication token successfully deleted.
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: Token not found with the requested `tokenId`.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````