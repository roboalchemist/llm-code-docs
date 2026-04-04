# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/upload-a-cache-artifact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a cache artifact

> Uploads a cache artifact identified by the `hash` specified on the path. The cache artifact can then be downloaded with the provided `hash`.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v8/artifacts/{hash}
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
  /v8/artifacts/{hash}:
    put:
      tags:
        - artifacts
      summary: Upload a cache artifact
      description: >-
        Uploads a cache artifact identified by the `hash` specified on the path.
        The cache artifact can then be downloaded with the provided `hash`.
      operationId: uploadArtifact
      parameters:
        - in: header
          description: The artifact size in bytes
          required: true
          schema:
            description: The artifact size in bytes
            type: number
          name: Content-Length
        - in: header
          description: The time taken to generate the uploaded artifact in milliseconds.
          required: false
          schema:
            type: number
            description: The time taken to generate the uploaded artifact in milliseconds.
            example: 400
          name: x-artifact-duration
        - in: header
          description: >-
            The continuous integration or delivery environment where this
            artifact was generated.
          required: false
          schema:
            type: string
            description: >-
              The continuous integration or delivery environment where this
              artifact was generated.
            example: VERCEL
            maxLength: 50
          name: x-artifact-client-ci
        - in: header
          description: 1 if the client is an interactive shell. Otherwise 0
          required: false
          schema:
            type: integer
            description: 1 if the client is an interactive shell. Otherwise 0
            example: 0
            minimum: 0
            maximum: 1
          name: x-artifact-client-interactive
        - in: header
          description: >-
            The base64 encoded tag for this artifact. The value is sent back to
            clients when the artifact is downloaded as the header
            `x-artifact-tag`
          required: false
          schema:
            type: string
            description: >-
              The base64 encoded tag for this artifact. The value is sent back
              to clients when the artifact is downloaded as the header
              `x-artifact-tag`
            example: Tc0BmHvJYMIYJ62/zx87YqO0Flxk+5Ovip25NY825CQ=
            maxLength: 600
          name: x-artifact-tag
        - name: hash
          description: The artifact hash
          in: path
          required: true
          schema:
            type: string
            example: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            description: The artifact hash
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
          application/octet-stream:
            schema:
              type: string
              format: binary
        required: true
      responses:
        '202':
          description: File successfully uploaded
          content:
            application/json:
              schema:
                properties:
                  urls:
                    items:
                      type: string
                    type: array
                    description: Array of URLs where the artifact was updated
                    example:
                      - >-
                        https://api.vercel.com/v2/now/artifact/12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                required:
                  - urls
                type: object
        '400':
          description: |-
            One of the provided values in the request query is invalid.
            One of the provided values in the headers is invalid
            File size is not valid
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