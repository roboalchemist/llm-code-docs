# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-account-information.md

# Get Account Information

> Fetches the best account or user’s contact info

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/account
paths:
  path: /v1/installations/{integrationConfigurationId}/account
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
        integrationConfigurationId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-account-info
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getAccountInfo({
              integrationConfigurationId: "<id>",
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
              name:
                allOf:
                  - type: string
                    description: The name of the team the installation is tied to.
              url:
                allOf:
                  - type: string
                    description: A URL linking to the installation in the Vercel Dashboard.
              contact:
                allOf:
                  - nullable: true
                    properties:
                      email:
                        type: string
                      name:
                        type: string
                    required:
                      - email
                    type: object
                    description: >-
                      The best contact for the integration, which can change as
                      team members and their roles change.
            requiredProperties:
              - url
              - contact
        examples:
          example:
            value:
              name: <string>
              url: <string>
              contact:
                email: <string>
                name: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
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
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````