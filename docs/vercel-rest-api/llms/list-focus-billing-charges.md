# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/billing/list-focus-billing-charges.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List FOCUS billing charges

> Returns the billing charge data in FOCUS v1.3 JSONL format for a specified Vercel team, within a date range specified by `from` and `to` query parameters. Supports 1-day granularity with a maximum date range of 1 year. The response is streamed as newline-delimited JSON (JSONL) and can be optionally compressed with gzip if the `Accept-Encoding: gzip` header is provided.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/billing/charges
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
  /v1/billing/charges:
    get:
      tags:
        - billing
      summary: List FOCUS billing charges
      description: >-
        Returns the billing charge data in FOCUS v1.3 JSONL format for a
        specified Vercel team, within a date range specified by `from` and `to`
        query parameters. Supports 1-day granularity with a maximum date range
        of 1 year. The response is streamed as newline-delimited JSON (JSONL)
        and can be optionally compressed with gzip if the `Accept-Encoding:
        gzip` header is provided.
      operationId: listBillingCharges
      parameters:
        - name: from
          description: >-
            Inclusive start of the date range as an ISO 8601 date-time string in
            UTC.
          in: query
          required: true
          schema:
            type: string
            description: >-
              Inclusive start of the date range as an ISO 8601 date-time string
              in UTC.
            example: '2025-01-01T00:00:00.000Z'
        - name: to
          description: >-
            Exclusive end of the date range as an ISO 8601 date-time string in
            UTC.
          in: query
          required: true
          schema:
            type: string
            description: >-
              Exclusive end of the date range as an ISO 8601 date-time string in
              UTC.
            example: '2025-01-31T00:00:00.000Z'
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
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '500':
          description: ''
        '503':
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