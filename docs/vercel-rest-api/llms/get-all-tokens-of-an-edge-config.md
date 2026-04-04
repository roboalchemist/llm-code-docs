# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-all-tokens-of-an-edge-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all tokens of an Edge Config

> Returns all tokens of an Edge Config.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/tokens
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
  /v1/edge-config/{edgeConfigId}/tokens:
    get:
      tags:
        - edge-config
      summary: Get all tokens of an Edge Config
      description: Returns all tokens of an Edge Config.
      operationId: getEdgeConfigTokens
      parameters:
        - name: edgeConfigId
          in: path
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
      responses:
        '200':
          description: The EdgeConfig.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EdgeConfigToken'
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
  schemas:
    EdgeConfigToken:
      properties:
        token:
          type: string
        label:
          type: string
        id:
          type: string
          description: >-
            This is not the token itself, but rather an id to identify the token
            by
        edgeConfigId:
          type: string
        createdAt:
          type: number
      required:
        - createdAt
        - edgeConfigId
        - id
        - label
        - token
      type: object
      description: The EdgeConfig.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````