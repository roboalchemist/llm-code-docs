# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/create-project-transfer-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create project transfer request

> Initiates a project transfer request from one team to another. <br/> Returns a `code` that remains valid for 24 hours and can be used to accept the transfer request by another team using the `PUT /projects/transfer-request/:code` endpoint. <br/> Users can also accept the project transfer request using the claim URL: `https://vercel.com/claim-deployment?code=<code>&returnUrl=<returnUrl>`. <br/> The `code` parameter specifies the project transfer request code generated using this endpoint. <br/> The `returnUrl` parameter redirects users to a specific page of the application if the claim URL is invalid or expired.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /projects/{idOrName}/transfer-request
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
  /projects/{idOrName}/transfer-request:
    post:
      tags:
        - projects
      summary: Create project transfer request
      description: >-
        Initiates a project transfer request from one team to another. <br/>
        Returns a `code` that remains valid for 24 hours and can be used to
        accept the transfer request by another team using the `PUT
        /projects/transfer-request/:code` endpoint. <br/> Users can also accept
        the project transfer request using the claim URL:
        `https://vercel.com/claim-deployment?code=<code>&returnUrl=<returnUrl>`.
        <br/> The `code` parameter specifies the project transfer request code
        generated using this endpoint. <br/> The `returnUrl` parameter redirects
        users to a specific page of the application if the claim URL is invalid
        or expired.
      operationId: createProjectTransferRequest
      parameters:
        - name: idOrName
          description: The ID or name of the project to transfer.
          in: path
          required: true
          schema:
            type: string
            description: The ID or name of the project to transfer.
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
                callbackUrl:
                  type: string
                  description: The URL to send a webhook to when the transfer is accepted.
                callbackSecret:
                  type: string
                  description: >-
                    The secret to use to sign the webhook payload with
                    HMAC-SHA256.
      responses:
        '200':
          description: The project transfer request has been initiated successfully.
          content:
            application/json:
              schema:
                properties:
                  code:
                    type: string
                    description: >-
                      Code that can be used to accept the project transfer
                      request.
                    example: f99cc49a-602e-4786-a748-762dfb205880
                required:
                  - code
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