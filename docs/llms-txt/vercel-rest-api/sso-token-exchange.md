# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/sso-token-exchange.md

# SSO Token Exchange

> During the autorization process, Vercel sends the user to the provider [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url), that includes the OAuth authorization `code` parameter. The provider then calls the SSO Token Exchange endpoint with the sent code and receives the OIDC token. They log the user in based on this token and redirects the user back to the Vercel account using deep-link parameters included the redirectLoginUrl. Providers should not persist the returned `id_token` in a database since the token will expire. See [**Authentication with SSO**](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso) for more details.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/integrations/sso/token
paths:
  path: /v1/integrations/sso/token
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: string
                    description: The sensitive code received from Vercel
              state:
                allOf:
                  - type: string
                    description: The state received from the initialization request
              client_id:
                allOf:
                  - type: string
                    description: The integration client id
              client_secret:
                allOf:
                  - type: string
                    description: The integration client secret
              redirect_uri:
                allOf:
                  - type: string
                    description: The integration redirect URI
              grant_type:
                allOf:
                  - type: string
                    description: >-
                      The grant type, when using x-www-form-urlencoded content
                      type
                    enum:
                      - authorization_code
            required: true
            requiredProperties:
              - code
              - client_id
              - client_secret
        examples:
          example:
            value:
              code: <string>
              state: <string>
              client_id: <string>
              client_secret: <string>
              redirect_uri: <string>
              grant_type: authorization_code
    codeSamples:
      - label: exchange-sso-token
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel();

          async function run() {
            const result = await vercel.authentication.exchangeSsoToken({
              code: "<value>",
              clientId: "<id>",
              clientSecret: "<value>",
            });

            console.log(result);
          }

          run();
      - label: exchange-sso-token
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel();

          async function run() {
            const result = await vercel.marketplace.exchangeSsoToken({
              code: "<value>",
              clientId: "<id>",
              clientSecret: "<value>",
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
              id_token:
                allOf:
                  - type: string
              access_token:
                allOf:
                  - nullable: true
                    type: string
              token_type:
                allOf:
                  - nullable: true
                    type: string
              expires_in:
                allOf:
                  - type: number
            requiredProperties:
              - id_token
              - access_token
              - token_type
        examples:
          example:
            value:
              id_token: <string>
              access_token: <string>
              token_type: <string>
              expires_in: 123
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '403': {}
    '404': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````