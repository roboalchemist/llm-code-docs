# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/check-if-a-cache-artifact-exists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Check if a cache artifact exists

> Check that a cache artifact with the given `hash` exists. This request returns response headers only and is equivalent to a `GET` request to this endpoint where the response contains no body.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples head /v8/artifacts/{hash}
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
    head:
      tags:
        - artifacts
      summary: Check if a cache artifact exists
      description: >-
        Check that a cache artifact with the given `hash` exists. This request
        returns response headers only and is equivalent to a `GET` request to
        this endpoint where the response contains no body.
      operationId: artifactExists
      parameters:
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
      responses:
        '200':
          description: The artifact was found and headers are returned
        '400':
          description: One of the provided values in the request query is invalid.
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
        '404':
          description: The artifact was not found
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````