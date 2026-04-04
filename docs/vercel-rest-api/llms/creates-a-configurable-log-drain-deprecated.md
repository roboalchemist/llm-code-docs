# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/creates-a-configurable-log-drain-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Creates a Configurable Log Drain (deprecated)

> Creates a configurable log drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed)



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/log-drains
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
  /v1/log-drains:
    post:
      tags:
        - logDrains
      summary: Creates a Configurable Log Drain (deprecated)
      description: >-
        Creates a configurable log drain. This endpoint must be called with a
        team AccessToken (integration OAuth2 clients are not allowed)
      operationId: createConfigurableLogDrain
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
                - deliveryFormat
                - url
                - sources
              properties:
                deliveryFormat:
                  description: The delivery log format
                  example: json
                  enum:
                    - json
                    - ndjson
                url:
                  description: The log drain url
                  format: uri
                  pattern: ^(http|https)?://
                  type: string
                headers:
                  description: Headers to be sent together with the request
                  type: object
                  additionalProperties:
                    type: string
                projectIds:
                  minItems: 1
                  maxItems: 50
                  type: array
                  items:
                    pattern: ^[a-zA-z0-9_]+$
                    type: string
                sources:
                  type: array
                  uniqueItems: true
                  items:
                    type: string
                    enum:
                      - static
                      - lambda
                      - build
                      - edge
                      - external
                      - firewall
                  minItems: 1
                environments:
                  type: array
                  uniqueItems: true
                  items:
                    type: string
                    enum:
                      - preview
                      - production
                  minItems: 1
                secret:
                  description: Custom secret of log drain
                  type: string
                samplingRate:
                  type: number
                  description: >-
                    The sampling rate for this log drain. It should be a
                    percentage rate between 0 and 100. With max 2 decimal points
                  minimum: 0.01
                  maximum: 1
                  multipleOf: 0.01
                name:
                  type: string
                  description: The custom name of this log drain.
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
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