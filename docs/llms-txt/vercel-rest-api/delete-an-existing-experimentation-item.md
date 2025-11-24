# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/delete-an-existing-experimentation-item.md

# Delete an existing experimentation item

> Delete an existing experimentation item

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
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
        itemId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: >-
          delete_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.deleteInstallationIntegrationConfiguration({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
              itemId: "<id>",
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The item was deleted
        examples: {}
        description: The item was deleted
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