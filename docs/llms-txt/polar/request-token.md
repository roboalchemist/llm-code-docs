# Source: https://polar.sh/docs/api-reference/oauth2/connect/request-token.md

# Request Token

> Request an access token using a valid grant.

## OpenAPI

````yaml post /v1/oauth2/token
paths:
  path: /v1/oauth2/token
  method: post
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/x-www-form-urlencoded:
        schemaArray:
          - type: object
            properties:
              grant_type:
                allOf:
                  - const: authorization_code
                    title: Grant Type
                    type: string
              client_id:
                allOf:
                  - title: Client Id
                    type: string
              client_secret:
                allOf:
                  - title: Client Secret
                    type: string
              code:
                allOf:
                  - title: Code
                    type: string
              redirect_uri:
                allOf:
                  - format: uri
                    maxLength: 2083
                    minLength: 1
                    title: Redirect Uri
                    type: string
            required: true
            title: AuthorizationCodeTokenRequest
            refIdentifier: '#/components/schemas/AuthorizationCodeTokenRequest'
            requiredProperties:
              - grant_type
              - client_id
              - client_secret
              - code
              - redirect_uri
          - type: object
            properties:
              grant_type:
                allOf:
                  - const: refresh_token
                    title: Grant Type
                    type: string
              client_id:
                allOf:
                  - title: Client Id
                    type: string
              client_secret:
                allOf:
                  - title: Client Secret
                    type: string
              refresh_token:
                allOf:
                  - title: Refresh Token
                    type: string
            required: true
            title: RefreshTokenRequest
            refIdentifier: '#/components/schemas/RefreshTokenRequest'
            requiredProperties:
              - grant_type
              - client_id
              - client_secret
              - refresh_token
          - type: object
            properties:
              grant_type:
                allOf:
                  - const: web
                    title: Grant Type
                    type: string
              client_id:
                allOf:
                  - title: Client Id
                    type: string
              client_secret:
                allOf:
                  - title: Client Secret
                    type: string
              session_token:
                allOf:
                  - title: Session Token
                    type: string
              sub_type:
                allOf:
                  - default: user
                    enum:
                      - user
                      - organization
                    title: Sub Type
                    type: string
              sub:
                allOf:
                  - anyOf:
                      - format: uuid4
                        type: string
                      - type: 'null'
                    default: null
                    title: Sub
              scope:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    default: null
                    title: Scope
            required: true
            title: WebTokenRequest
            refIdentifier: '#/components/schemas/WebTokenRequest'
            requiredProperties:
              - grant_type
              - client_id
              - client_secret
              - session_token
        examples:
          example:
            value:
              grant_type: <string>
              client_id: <string>
              client_secret: <string>
              code: <string>
              redirect_uri: <string>
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.Oauth2.Token(ctx, operations.CreateOauth2RequestTokenRequestBodyAuthorizationCodeTokenRequest(\n        components.AuthorizationCodeTokenRequest{\n            ClientID: \"<id>\",\n            ClientSecret: \"<value>\",\n            Code: \"<value>\",\n            RedirectURI: \"https://memorable-season.name\",\n        },\n    ))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.TokenResponse != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.oauth2.token(request={
                  "grant_type": "authorization_code",
                  "client_id": "<id>",
                  "client_secret": "<value>",
                  "code": "<value>",
                  "redirect_uri": "https://memorable-season.name",
              })

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.oauth2.token({
              grantType: "authorization_code",
              clientId: "<id>",
              clientSecret: "<value>",
              code: "<value>",
              redirectUri: "https://memorable-season.name",
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;
          use Polar\Models\Components;

          $sdk = Polar\Polar::builder()->build();

          $request = new Components\AuthorizationCodeTokenRequest(
              clientId: '<id>',
              clientSecret: '<value>',
              code: '<value>',
              redirectUri: 'https://memorable-season.name',
          );

          $response = $sdk->oauth2->token(
              request: $request
          );

          if ($response->tokenResponse !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              access_token:
                allOf:
                  - type: string
                    title: Access Token
              token_type:
                allOf:
                  - type: string
                    const: Bearer
                    title: Token Type
              expires_in:
                allOf:
                  - type: integer
                    title: Expires In
              refresh_token:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Refresh Token
              scope:
                allOf:
                  - type: string
                    title: Scope
              id_token:
                allOf:
                  - type: string
                    title: Id Token
            title: TokenResponse
            refIdentifier: '#/components/schemas/TokenResponse'
            requiredProperties:
              - access_token
              - token_type
              - expires_in
              - refresh_token
              - scope
              - id_token
        examples:
          example:
            value:
              access_token: <string>
              token_type: <string>
              expires_in: 123
              refresh_token: <string>
              scope: <string>
              id_token: <string>
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas: {}

````