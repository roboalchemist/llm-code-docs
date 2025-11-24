# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/delete-integration-resource.md

# Delete Integration Resource

> Delete a resource owned by the selected installation ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/installations/{integrationConfigurationId}/resources/{resourceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/resources/{resourceId}
  method: delete
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
        resourceId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: delete-integration-resource
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.deleteIntegrationResource({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
            });


          }

          run();
  response:
    '204': {}
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