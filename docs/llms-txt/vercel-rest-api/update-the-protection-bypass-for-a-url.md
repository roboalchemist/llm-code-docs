# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/update-the-protection-bypass-for-a-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update the protection bypass for a URL

> Update the protection bypass for the alias or deployment URL (used for user access & comment access for deployments). Used as shareable links and user scoped access for Vercel Authentication and also to allow external (logged in) people to comment on previews for Preview Comments (next-live-mode).



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /aliases/{id}/protection-bypass
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
  /aliases/{id}/protection-bypass:
    patch:
      tags:
        - aliases
      summary: Update the protection bypass for a URL
      description: >-
        Update the protection bypass for the alias or deployment URL (used for
        user access & comment access for deployments). Used as shareable links
        and user scoped access for Vercel Authentication and also to allow
        external (logged in) people to comment on previews for Preview Comments
        (next-live-mode).
      operationId: patchUrlProtectionBypass
      parameters:
        - name: id
          description: The alias or deployment ID
          in: path
          required: true
          schema:
            type: string
            description: The alias or deployment ID
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
                  properties:
                    ttl:
                      description: >-
                        Optional time the shareable link is valid for in
                        seconds. If not provided, the shareable link will never
                        expire.
                      type: number
                      maximum: 63072000
                    revoke:
                      description: >-
                        Optional instructions for revoking and regenerating a
                        shareable link
                      type: object
                      properties:
                        secret:
                          description: Sharebale link to revoked
                          type: string
                        regenerate:
                          description: >-
                            Whether or not a new shareable link should be
                            created after the provided secret is revoked
                          type: boolean
                      required:
                        - secret
                        - regenerate
                  additionalProperties: false
                - type: object
                  properties:
                    scope:
                      description: >-
                        Instructions for creating a user scoped protection
                        bypass
                      type: object
                      properties:
                        userId:
                          type: string
                          description: Specified user id for the scoped bypass.
                        email:
                          type: string
                          format: email
                          description: Specified email for the scoped bypass.
                        access:
                          enum:
                            - denied
                            - granted
                          description: Invitation status for the user scoped bypass.
                      allOf:
                        - anyOf:
                            - required:
                                - userId
                            - required:
                                - email
                        - required:
                            - access
                  required:
                    - scope
                  additionalProperties: false
                - type: object
                  properties:
                    override:
                      type: object
                      properties:
                        scope:
                          enum:
                            - alias-protection-override
                        action:
                          enum:
                            - create
                            - revoke
                      required:
                        - scope
                        - action
                  required:
                    - override
                  additionalProperties: false
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                additionalProperties: true
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
        '428':
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