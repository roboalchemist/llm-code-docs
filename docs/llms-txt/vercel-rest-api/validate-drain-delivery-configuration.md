# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/validate-drain-delivery-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate Drain delivery configuration

> Validate the delivery configuration of a Drain using sample events.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains/test
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
  /v1/drains/test:
    post:
      tags:
        - drains
      summary: Validate Drain delivery configuration
      description: Validate the delivery configuration of a Drain using sample events.
      operationId: testDrain
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
              additionalProperties: false
              required:
                - schemas
                - delivery
              properties:
                schemas:
                  type: object
                  additionalProperties:
                    type: object
                    required:
                      - version
                    properties:
                      version:
                        type: string
                delivery:
                  type: object
                  oneOf:
                    - type: object
                      additionalProperties: false
                      required:
                        - type
                        - endpoint
                        - encoding
                        - headers
                      properties:
                        type:
                          type: string
                        endpoint:
                          type: string
                        compression:
                          type: string
                          enum:
                            - gzip
                            - none
                        encoding:
                          type: string
                          enum:
                            - json
                            - ndjson
                        headers:
                          additionalProperties:
                            type: string
                          type: object
                        secret:
                          type: string
                    - type: object
                      additionalProperties: false
                      required:
                        - type
                        - endpoint
                        - encoding
                        - headers
                      properties:
                        type:
                          type: string
                        endpoint:
                          oneOf:
                            - type: object
                              additionalProperties: false
                              required:
                                - traces
                              properties:
                                traces:
                                  type: string
                        encoding:
                          type: string
                          enum:
                            - proto
                            - json
                        headers:
                          additionalProperties:
                            type: string
                          type: object
                        secret:
                          type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                  - properties:
                      status:
                        type: string
                      error:
                        type: string
                      endpoint:
                        type: string
                    required:
                      - endpoint
                      - error
                      - status
                    type: object
        '400':
          description: One of the provided values in the request body is invalid.
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