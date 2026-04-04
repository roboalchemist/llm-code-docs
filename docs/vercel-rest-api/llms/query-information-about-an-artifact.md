# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/query-information-about-an-artifact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Query information about an artifact

> Query information about an array of artifacts.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts
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
  /v8/artifacts:
    post:
      tags:
        - artifacts
      summary: Query information about an artifact
      description: Query information about an array of artifacts.
      operationId: artifactQuery
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
                - hashes
              properties:
                hashes:
                  items:
                    type: string
                  description: artifact hashes
                  type: array
                  example:
                    - 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                    - 34HKQaOmR5t5Uy6vasdasdasdasd
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                additionalProperties:
                  nullable: true
                  oneOf:
                    - properties:
                        size:
                          type: number
                        taskDurationMs:
                          type: number
                        tag:
                          type: string
                      required:
                        - size
                        - taskDurationMs
                      type: object
                    - properties:
                        error:
                          properties:
                            message:
                              type: string
                          required:
                            - message
                          type: object
                      required:
                        - error
                      type: object
                type: object
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: >-
            The customer has reached their spend cap limit and has been paused.
            An owner can disable the cap or raise the limit in settings.

            The Remote Caching usage limit has been reached for this account for
            this billing cycle.

            Remote Caching has been disabled for this team or user. An owner can
            enable it in the billing settings.

            You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````