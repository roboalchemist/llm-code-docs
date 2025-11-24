# Source: https://polar.sh/docs/api-reference/oauth2/connect/introspect-token.md

# Introspect Token

> Get information about an access token.

## OpenAPI

````yaml post /v1/oauth2/introspect
paths:
  path: /v1/oauth2/introspect
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
            title: IntrospectTokenRequest
            refIdentifier: '#/components/schemas/IntrospectTokenRequest'
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
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.Oauth2.Introspect(ctx, components.IntrospectTokenRequest{\n        Token: \"<value>\",\n        ClientID: \"<id>\",\n        ClientSecret: \"<value>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.IntrospectTokenResponse != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.oauth2.introspect(request={
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
            const result = await polar.oauth2.introspect({
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

          $request = new Components\IntrospectTokenRequest(
              token: '<value>',
              clientId: '<id>',
              clientSecret: '<value>',
          );

          $response = $sdk->oauth2->introspect(
              request: $request
          );

          if ($response->introspectTokenResponse !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              active:
                allOf:
                  - type: boolean
                    title: Active
              client_id:
                allOf:
                  - type: string
                    title: Client Id
              token_type:
                allOf:
                  - type: string
                    enum:
                      - access_token
                      - refresh_token
                    title: Token Type
              scope:
                allOf:
                  - type: string
                    title: Scope
              sub_type:
                allOf:
                  - $ref: '#/components/schemas/SubType'
              sub:
                allOf:
                  - type: string
                    title: Sub
              aud:
                allOf:
                  - type: string
                    title: Aud
              iss:
                allOf:
                  - type: string
                    title: Iss
              exp:
                allOf:
                  - type: integer
                    title: Exp
              iat:
                allOf:
                  - type: integer
                    title: Iat
            title: IntrospectTokenResponse
            refIdentifier: '#/components/schemas/IntrospectTokenResponse'
            requiredProperties:
              - active
              - client_id
              - token_type
              - scope
              - sub_type
              - sub
              - aud
              - iss
              - exp
              - iat
        examples:
          example:
            value:
              active: true
              client_id: <string>
              token_type: access_token
              scope: <string>
              sub_type: user
              sub: <string>
              aud: <string>
              iss: <string>
              exp: 123
              iat: 123
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas:
    SubType:
      type: string
      enum:
        - user
        - organization
      title: SubType

````