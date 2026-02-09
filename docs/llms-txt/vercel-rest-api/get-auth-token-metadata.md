# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/get-auth-token-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Auth Token Metadata

> Retrieve metadata about an authentication token belonging to the currently authenticated User.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/user/tokens/{tokenId}
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
  /v5/user/tokens/{tokenId}:
    get:
      tags:
        - authentication
      summary: Get Auth Token Metadata
      description: >-
        Retrieve metadata about an authentication token belonging to the
        currently authenticated User.
      operationId: getAuthToken
      parameters:
        - name: tokenId
          description: >-
            The identifier of the token to retrieve. The special value
            \"current\" may be supplied, which returns the metadata for the
            token that the current HTTP request is authenticated with.
          in: path
          required: true
          schema:
            type: string
            description: >-
              The identifier of the token to retrieve. The special value
              \"current\" may be supplied, which returns the metadata for the
              token that the current HTTP request is authenticated with.
            example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
      responses:
        '200':
          description: Successful response.
          content:
            application/json:
              schema:
                properties:
                  token:
                    $ref: '#/components/schemas/AuthToken'
                required:
                  - token
                type: object
                description: Successful response.
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: Token not found with the requested `tokenId`.
      security:
        - bearerToken: []
components:
  schemas:
    AuthToken:
      properties:
        id:
          type: string
          description: The unique identifier of the token.
          example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
        name:
          type: string
          description: The human-readable name of the token.
        type:
          type: string
          description: The type of the token.
          example: oauth2-token
        origin:
          type: string
          description: The origin of how the token was created.
          example: github
        scopes:
          items:
            oneOf:
              - properties:
                  type:
                    type: string
                    enum:
                      - user
                  sudo:
                    properties:
                      origin:
                        type: string
                        enum:
                          - totp
                          - webauthn
                          - recovery-code
                        description: Possible multi-factor origins
                      expiresAt:
                        type: number
                    required:
                      - expiresAt
                      - origin
                    type: object
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - createdAt
                  - type
                type: object
                description: The access scopes granted to the token.
              - properties:
                  type:
                    type: string
                    enum:
                      - team
                  teamId:
                    type: string
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - createdAt
                  - teamId
                  - type
                type: object
                description: The access scopes granted to the token.
          type: array
          description: The access scopes granted to the token.
        expiresAt:
          type: number
          description: Timestamp (in milliseconds) of when the token expires.
          example: 1632816536002
        activeAt:
          type: number
          description: >-
            Timestamp (in milliseconds) of when the token was most recently
            used.
          example: 1632816536002
        createdAt:
          type: number
          description: Timestamp (in milliseconds) of when the token was created.
          example: 1632816536002
        leakedAt:
          type: number
          description: Timestamp (in milliseconds) of when the token was marked as leaked.
          example: 1632816536002
      required:
        - activeAt
        - createdAt
        - id
        - name
        - type
      type: object
      description: Authentication token metadata.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````