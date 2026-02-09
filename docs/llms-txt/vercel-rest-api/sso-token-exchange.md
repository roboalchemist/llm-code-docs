# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/sso-token-exchange.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# SSO Token Exchange

> During the autorization process, Vercel sends the user to the provider [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url), that includes the OAuth authorization `code` parameter. The provider then calls the SSO Token Exchange endpoint with the sent code and receives the OIDC token. They log the user in based on this token and redirects the user back to the Vercel account using deep-link parameters included the redirectLoginUrl. Providers should not persist the returned `id_token` in a database since the token will expire. See [**Authentication with SSO**](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso) for more details.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/integrations/sso/token
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
  /v1/integrations/sso/token:
    post:
      tags:
        - authentication
        - marketplace
      summary: SSO Token Exchange
      description: >-
        During the autorization process, Vercel sends the user to the provider
        [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url),
        that includes the OAuth authorization `code` parameter. The provider
        then calls the SSO Token Exchange endpoint with the sent code and
        receives the OIDC token. They log the user in based on this token and
        redirects the user back to the Vercel account using deep-link parameters
        included the redirectLoginUrl. Providers should not persist the returned
        `id_token` in a database since the token will expire. See
        [**Authentication with
        SSO**](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso)
        for more details.
      operationId: exchange-sso-token
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - type: object
                  required:
                    - code
                    - client_id
                    - client_secret
                    - grant_type
                  properties:
                    code:
                      type: string
                      description: The sensitive code received from Vercel
                    state:
                      type: string
                      description: The state received from the initialization request
                    client_id:
                      type: string
                      description: The integration client id
                    client_secret:
                      type: string
                      description: The integration client secret
                    redirect_uri:
                      type: string
                      description: The integration redirect URI
                    grant_type:
                      type: string
                      description: >-
                        The grant type, when using x-www-form-urlencoded content
                        type
                      enum:
                        - authorization_code
                - type: object
                  required:
                    - refresh_token
                    - client_id
                    - client_secret
                    - grant_type
                  properties:
                    refresh_token:
                      type: string
                      description: The refresh token received from previous token exchange
                    client_id:
                      type: string
                      description: The integration client id
                    client_secret:
                      type: string
                      description: The integration client secret
                    grant_type:
                      type: string
                      description: >-
                        The grant type, when using x-www-form-urlencoded content
                        type
                      enum:
                        - refresh_token
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      id_token:
                        type: string
                      token_type:
                        nullable: true
                        type: string
                      expires_in:
                        type: number
                      access_token:
                        nullable: true
                        type: string
                      refresh_token:
                        type: string
                    required:
                      - access_token
                      - id_token
                      - token_type
                    type: object
                  - properties:
                      id_token:
                        type: string
                      token_type:
                        type: string
                      access_token:
                        type: string
                      refresh_token:
                        type: string
                      expires_in:
                        type: number
                    required:
                      - access_token
                      - expires_in
                      - id_token
                      - refresh_token
                      - token_type
                    type: object
        '400':
          description: One of the provided values in the request body is invalid.
        '403':
          description: ''
        '500':
          description: ''
      security: []

````