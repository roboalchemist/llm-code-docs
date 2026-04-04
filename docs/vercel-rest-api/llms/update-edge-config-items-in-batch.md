# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/update-edge-config-items-in-batch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Edge Config items in batch

> Update multiple Edge Config Items in batch.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/edge-config/{edgeConfigId}/items
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
  /v1/edge-config/{edgeConfigId}/items:
    patch:
      tags:
        - edge-config
      summary: Update Edge Config items in batch
      description: Update multiple Edge Config Items in batch.
      operationId: patchEdgeConfigItems
      parameters:
        - name: edgeConfigId
          in: path
          required: true
          schema:
            type: string
            pattern: ^ecfg_
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
              additionalProperties: false
              required:
                - items
              properties:
                items:
                  type: array
                  items:
                    oneOf:
                      - type: object
                        properties:
                          operation:
                            enum:
                              - create
                              - update
                              - upsert
                              - delete
                          key:
                            maxLength: 256
                            pattern: ^[\\w-]+$
                            type: string
                          value:
                            nullable: true
                          description:
                            oneOf:
                              - type: string
                                maxLength: 512
                              - {}
                            nullable: true
                        anyOf:
                          - properties:
                              operation:
                                type: string
                                enum:
                                  - create
                            required:
                              - operation
                              - key
                              - value
                          - properties:
                              operation:
                                enum:
                                  - update
                                  - upsert
                            required:
                              - operation
                              - key
                              - value
                          - properties:
                              operation:
                                enum:
                                  - update
                                  - upsert
                            required:
                              - operation
                              - key
                              - description
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  status:
                    type: string
                required:
                  - status
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
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
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````