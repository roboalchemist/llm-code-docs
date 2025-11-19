# Source: https://polar.sh/docs/api-reference/oauth2/connect/get-user-info.md

# Get User Info

> Get information about the authenticated user.

## OpenAPI

````yaml get /v1/oauth2/userinfo
paths:
  path: /v1/oauth2/userinfo
  method: get
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: access token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                You can generate an **Organization Access Token** from your
                organization's settings.
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Oauth2.Userinfo(ctx)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseOauth2Userinfo != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.oauth2.userinfo()

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            const result = await polar.oauth2.userinfo();

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();



          $response = $sdk->oauth2->userinfo(

          );

          if ($response->responseOauth2Userinfo !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              sub:
                allOf:
                  - type: string
                    title: Sub
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Name
              email:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Email
              email_verified:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Email Verified
            title: UserInfoUser
            refIdentifier: '#/components/schemas/UserInfoUser'
            requiredProperties:
              - sub
          - type: object
            properties:
              sub:
                allOf:
                  - type: string
                    title: Sub
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Name
            title: UserInfoOrganization
            refIdentifier: '#/components/schemas/UserInfoOrganization'
            requiredProperties:
              - sub
        examples:
          example:
            value:
              sub: <string>
              name: <string>
              email: <string>
              email_verified: true
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas: {}

````