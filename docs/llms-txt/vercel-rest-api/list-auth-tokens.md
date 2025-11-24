# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/list-auth-tokens.md

# List Auth Tokens

> Retrieve a list of the current User's authentication tokens.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/user/tokens
paths:
  path: /v5/user/tokens
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listAuthTokens
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Authentication.ListAuthTokens(ctx)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listAuthTokens
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.authentication.listAuthTokens();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              tokens:
                allOf:
                  - items:
                      $ref: '#/components/schemas/AuthToken'
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - tokens
              - pagination
        examples:
          example:
            value:
              tokens:
                - id: >-
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
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
        description: ''
    '400': {}
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas:
    Pagination:
      properties:
        count:
          type: number
          description: Amount of items in the current page.
          example: 20
        next:
          nullable: true
          type: number
          description: Timestamp that must be used to request the next page.
          example: 1540095775951
        prev:
          nullable: true
          type: number
          description: Timestamp that must be used to request the previous page.
          example: 1540095775951
      required:
        - count
        - next
        - prev
      type: object
      description: >-
        This object contains information related to the pagination of the
        current request, including the necessary parameters to get the next or
        previous page of data.
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