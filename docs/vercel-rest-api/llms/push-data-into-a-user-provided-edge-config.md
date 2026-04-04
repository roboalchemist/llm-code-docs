# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/push-data-into-a-user-provided-edge-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Push data into a user-provided Edge Config

> When the user enabled Edge Config syncing, then this endpoint can be used by the partner to push their configuration data into the relevant Edge Config.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
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
  /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config:
    put:
      tags:
        - marketplace
      summary: Push data into a user-provided Edge Config
      description: >-
        When the user enabled Edge Config syncing, then this endpoint can be
        used by the partner to push their configuration data into the relevant
        Edge Config.
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
                - data
              properties:
                data:
                  type: object
                  additionalProperties: {}
      responses:
        '200':
          description: The Edge Config was updated
          content:
            application/json:
              schema:
                properties:
                  items:
                    additionalProperties:
                      $ref: '#/components/schemas/EdgeConfigItemValue'
                    type: object
                  updatedAt:
                    type: number
                  digest:
                    type: string
                  purpose:
                    type: string
                    enum:
                      - flags
                      - experimentation
                required:
                  - digest
                  - items
                  - updatedAt
                type: object
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
        '409':
          description: ''
        '412':
          description: ''
      security:
        - bearerToken: []
components:
  schemas:
    EdgeConfigItemValue:
      nullable: true
      oneOf:
        - type: string
        - type: number
        - additionalProperties:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: object
        - items:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: array
        - type: boolean
          enum:
            - false
            - true
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````