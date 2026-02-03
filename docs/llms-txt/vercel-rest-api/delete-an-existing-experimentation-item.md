# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/delete-an-existing-experimentation-item.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an existing experimentation item

> Delete an existing experimentation item



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
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
  /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}:
    delete:
      tags:
        - marketplace
      summary: Delete an existing experimentation item
      description: Delete an existing experimentation item
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
        - name: resourceId
          in: path
          required: true
          schema:
            type: string
        - name: itemId
          in: path
          required: true
          schema:
            type: string
      responses:
        '204':
          description: The item was deleted
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
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