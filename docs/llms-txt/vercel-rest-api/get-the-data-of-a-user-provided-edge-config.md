# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-the-data-of-a-user-provided-edge-config.md

# Get the data of a user-provided Edge Config

> When the user enabled Edge Config syncing, then this endpoint can be used by the partner to fetch the contents of the Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples head /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
  method: head
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
      - label: >-
          head_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.createInstallationIntegrationEdgeConfig({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
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
              items:
                allOf:
                  - additionalProperties:
                      $ref: '#/components/schemas/EdgeConfigItemValue'
                    type: object
              updatedAt:
                allOf:
                  - type: number
              digest:
                allOf:
                  - type: string
            requiredProperties:
              - items
              - updatedAt
              - digest
        examples:
          example:
            value:
              items: {}
              updatedAt: 123
              digest: <string>
        description: The Edge Config data
    '304': {}
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
  schemas:
    EdgeConfigItemValue:
      nullable: true
      oneOf:
        - type: string
        - type: number
        - type: boolean
        - additionalProperties:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: object
        - items:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: array

````