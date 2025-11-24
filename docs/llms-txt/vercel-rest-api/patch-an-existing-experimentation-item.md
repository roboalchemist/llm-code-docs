# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/patch-an-existing-experimentation-item.md

# Patch an existing experimentation item

> Patch an existing experimentation item

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
  method: patch
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              slug:
                allOf:
                  - type: string
                    maxLength: 1024
              origin:
                allOf:
                  - type: string
                    maxLength: 2048
              name:
                allOf:
                  - type: string
                    maxLength: 1024
              category:
                allOf:
                  - type: string
                    enum:
                      - experiment
                      - flag
              description:
                allOf:
                  - type: string
                    maxLength: 1024
              isArchived:
                allOf:
                  - type: boolean
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
            requiredProperties:
              - slug
              - origin
            additionalProperties: false
        examples:
          example:
            value:
              slug: <string>
              origin: <string>
              name: <string>
              category: experiment
              description: <string>
              isArchived: true
              createdAt: 123
              updatedAt: 123
    codeSamples:
      - label: >-
          patch_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateInstallationIntegrationConfiguration({
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
            description: The item was updated
        examples: {}
        description: The item was updated
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
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