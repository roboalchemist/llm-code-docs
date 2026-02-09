# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/update-or-move-apex-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update or move apex domain

> Update or move apex domain. Note: This endpoint is no longer used for updating auto-renew or nameservers. For this, please use the endpoints [Update auto-renew for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain) and [Update nameservers for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain).



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v3/domains/{domain}
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
  /v3/domains/{domain}:
    patch:
      tags:
        - domains
      summary: Update or move apex domain
      description: >-
        Update or move apex domain. Note: This endpoint is no longer used for
        updating auto-renew or nameservers. For this, please use the endpoints
        [Update auto-renew for a
        domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain)
        and [Update nameservers for a
        domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain).
      operationId: patchDomain
      parameters:
        - name: domain
          in: path
          schema:
            type: string
          required: true
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
              oneOf:
                - type: object
                  description: update
                  additionalProperties: false
                  properties:
                    op:
                      example: update
                      type: string
                    renew:
                      description: >-
                        This field is deprecated. Please use PATCH
                        /v1/registrar/domains/{domainName}/auto-renew instead.
                      type: boolean
                      deprecated: true
                    customNameservers:
                      description: >-
                        This field is deprecated. Please use PATCH
                        /v1/registrar/domains/{domainName}/nameservers instead.
                      items:
                        type: string
                      maxItems: 4
                      minItems: 0
                      type: array
                      uniqueItems: true
                      deprecated: true
                    zone:
                      description: >-
                        Specifies whether this is a DNS zone that intends to use
                        Vercel's nameservers.
                      type: boolean
                - type: object
                  description: move-out
                  additionalProperties: false
                  properties:
                    op:
                      example: move-out
                      type: string
                    destination:
                      description: User or team to move domain to
                      type: string
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      moved:
                        type: boolean
                        enum:
                          - false
                          - true
                    required:
                      - moved
                    type: object
                  - properties:
                      moved:
                        type: boolean
                        enum:
                          - false
                          - true
                      token:
                        type: string
                    required:
                      - moved
                      - token
                    type: object
                  - properties:
                      renew:
                        type: boolean
                        enum:
                          - false
                          - true
                      customNameservers:
                        items:
                          type: string
                        type: array
                      zone:
                        type: boolean
                        enum:
                          - false
                          - true
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
        '500':
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