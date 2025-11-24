# Source: https://polar.sh/docs/api-reference/oauth2/connect/revoke-token.md

# Revoke Token

> Revoke an access token or a refresh token.

## OpenAPI

````yaml post /v1/oauth2/revoke
paths:
  path: /v1/oauth2/revoke
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
              token:
                allOf:
                  - title: Token
                    type: string
              token_type_hint:
                allOf:
                  - anyOf:
                      - enum:
                          - access_token
                          - refresh_token
                        type: string
                      - type: 'null'
                    default: null
                    title: Token Type Hint
              client_id:
                allOf:
                  - title: Client Id
                    type: string
              client_secret:
                allOf:
                  - title: Client Secret
                    type: string
            required: true
            title: RevokeTokenRequest
            refIdentifier: '#/components/schemas/RevokeTokenRequest'
            requiredProperties:
              - token
              - client_id
              - client_secret
        examples:
          example:
            value:
              token: <string>
              token_type_hint: access_token
              client_id: <string>
              client_secret: <string>
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.Oauth2.Revoke(ctx, components.RevokeTokenRequest{\n        Token: \"<value>\",\n        ClientID: \"<id>\",\n        ClientSecret: \"<value>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.RevokeTokenResponse != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.oauth2.revoke(request={
                  "token": "<value>",
                  "client_id": "<id>",
                  "client_secret": "<value>",
              })

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.oauth2.revoke({
              token: "<value>",
              clientId: "<id>",
              clientSecret: "<value>",
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

          $request = new Components\RevokeTokenRequest(
              token: '<value>',
              clientId: '<id>',
              clientSecret: '<value>',
          );

          $response = $sdk->oauth2->revoke(
              request: $request
          );

          if ($response->revokeTokenResponse !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            title: RevokeTokenResponse
            refIdentifier: '#/components/schemas/RevokeTokenResponse'
        examples:
          example:
            value: {}
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas: {}

````