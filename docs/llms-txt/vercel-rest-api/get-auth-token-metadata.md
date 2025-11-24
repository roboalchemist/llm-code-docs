# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/get-auth-token-metadata.md

# Get Auth Token Metadata

> Retrieve metadata about an authentication token belonging to the currently authenticated User.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/user/tokens/{tokenId}
paths:
  path: /v5/user/tokens/{tokenId}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        tokenId:
          schema:
            - type: string
              required: true
              description: >-
                The identifier of the token to retrieve. The special value
                \"current\" may be supplied, which returns the metadata for the
                token that the current HTTP request is authenticated with.
              example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getAuthToken
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Authentication.GetAuthToken(ctx, \"5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getAuthToken
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.authentication.getAuthToken({
              tokenId: "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              token:
                allOf:
                  - $ref: '#/components/schemas/AuthToken'
            description: Successful response.
            requiredProperties:
              - token
        examples:
          example:
            value:
              token:
                id: >-
                  5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
                name: <string>
                type: oauth2-token
                origin: github
                scopes:
                  - type: user
                    sudo:
                      origin: totp
                      expiresAt: 123
                    origin: saml
                    createdAt: 123
                    expiresAt: 123
                expiresAt: 1632816536002
                activeAt: 1632816536002
                createdAt: 1632816536002
        description: Successful response.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401': {}
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Token not found with the requested `tokenId`.
        examples: {}
        description: Token not found with the requested `tokenId`.
  deprecated: false
  type: path
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
                      - origin
                      - expiresAt
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
                  - type
                  - createdAt
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
                  - type
                  - teamId
                  - createdAt
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
      required:
        - id
        - name
        - type
        - activeAt
        - createdAt
      type: object
      description: Authentication token metadata.

````