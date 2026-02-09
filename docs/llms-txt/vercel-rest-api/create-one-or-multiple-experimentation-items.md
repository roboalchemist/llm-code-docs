# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/create-one-or-multiple-experimentation-items.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create one or multiple experimentation items

> Create one or multiple experimentation items



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
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
  /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items:
    post:
      tags:
        - marketplace
      summary: Create one or multiple experimentation items
      description: Create one or multiple experimentation items
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              required:
                - items
              properties:
                items:
                  type: array
                  maxItems: 50
                  items:
                    type: object
                    additionalProperties: false
                    required:
                      - id
                      - slug
                      - origin
                    properties:
                      id:
                        type: string
                        maxLength: 1024
                      slug:
                        type: string
                        maxLength: 1024
                      origin:
                        type: string
                        maxLength: 2048
                      category:
                        type: string
                        enum:
                          - experiment
                          - flag
                      name:
                        type: string
                        maxLength: 1024
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
          description: The items were created
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