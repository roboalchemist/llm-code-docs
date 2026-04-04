# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/patch-an-existing-experimentation-item.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Patch an existing experimentation item

> Patch an existing experimentation item



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
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
    patch:
      tags:
        - marketplace
      summary: Patch an existing experimentation item
      description: Patch an existing experimentation item
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              required:
                - slug
                - origin
              properties:
                slug:
                  type: string
                  maxLength: 1024
                origin:
                  type: string
                  maxLength: 2048
                name:
                  type: string
                  maxLength: 1024
                category:
                  type: string
                  enum:
                    - experiment
                    - flag
                description:
                  type: string
                  maxLength: 1024
                isArchived:
                  type: boolean
                createdAt:
                  type: number
                updatedAt:
                  type: number
      responses:
        '204':
          description: The item was updated
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
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````