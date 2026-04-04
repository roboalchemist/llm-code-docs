# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/certs/upload-a-cert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a cert

> Upload a cert



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v8/certs
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
  /v8/certs:
    put:
      tags:
        - certs
      summary: Upload a cert
      description: Upload a cert
      operationId: uploadCert
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
                - ca
                - key
                - cert
              additionalProperties: false
              properties:
                ca:
                  type: string
                  description: The certificate authority
                key:
                  type: string
                  description: The certificate key
                cert:
                  type: string
                  description: The certificate
                skipValidation:
                  type: boolean
                  description: Skip validation of the certificate
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                  autoRenew:
                    type: boolean
                    enum:
                      - false
                      - true
                  cns:
                    items:
                      type: string
                    type: array
                required:
                  - autoRenew
                  - cns
                  - createdAt
                  - expiresAt
                  - id
                type: object
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: This feature is only available for Enterprise customers.
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