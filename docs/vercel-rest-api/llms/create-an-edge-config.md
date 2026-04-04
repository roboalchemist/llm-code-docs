# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/create-an-edge-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an Edge Config

> Creates an Edge Config.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config
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
  /v1/edge-config:
    post:
      tags:
        - edge-config
      summary: Create an Edge Config
      description: Creates an Edge Config.
      operationId: createEdgeConfig
      parameters:
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
              required:
                - slug
              properties:
                slug:
                  maxLength: 64
                  pattern: ^[\\w-]+$
                  type: string
                items:
                  type: object
                  additionalProperties: {}
        required: true
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  transfer:
                    properties:
                      fromAccountId:
                        type: string
                      startedAt:
                        type: number
                      doneAt:
                        nullable: true
                        type: number
                    required:
                      - doneAt
                      - fromAccountId
                      - startedAt
                    type: object
                    description: >-
                      Keeps track of the current state of the Edge Config while
                      it gets transferred.
                  id:
                    type: string
                  createdAt:
                    type: number
                  createdBy:
                    type: string
                    description: >-
                      The ID of the user who created the Edge Config, optional
                      because it is not always set.
                  ownerId:
                    type: string
                  slug:
                    type: string
                    description: >-
                      Name for the Edge Config Names are not unique. Must start
                      with an alphabetic character and can contain only
                      alphanumeric characters and underscores).
                  updatedAt:
                    type: number
                  digest:
                    type: string
                  purpose:
                    oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags
                          projectId:
                            type: string
                        required:
                          - projectId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - experimentation
                          resourceId:
                            type: string
                        required:
                          - resourceId
                          - type
                        type: object
                  deletedAt:
                    nullable: true
                    type: number
                  schema:
                    type: object
                  syncedToDynamoAt:
                    type: number
                    description: >-
                      Timestamp of when the Edge Config was synced to DynamoDB
                      initially. It is only set when syncing the entire Edge
                      Config, not when updating.
                  sizeInBytes:
                    type: number
                  itemCount:
                    type: number
                required:
                  - createdAt
                  - digest
                  - id
                  - itemCount
                  - ownerId
                  - sizeInBytes
                  - slug
                  - updatedAt
                type: object
                description: An Edge Config
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
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