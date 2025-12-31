# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/create-one-or-multiple-experimentation-items.md

# Create one or multiple experimentation items

> Create one or multiple experimentation items

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              items:
                allOf:
                  - type: array
                    maxItems: 50
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - id
                        - slug
                        - origin
                      properties:
                        id:
                          type: string
                          maxLength: 1024
                        slug:
                          type: string
                          maxLength: 1024
                        origin:
                          type: string
                          maxLength: 2048
                        category:
                          type: string
                          enum:
                            - experiment
                            - flag
                        name:
                          type: string
                          maxLength: 1024
                        description:
                          type: string
                          maxLength: 1024
                        isArchived:
                          type: boolean
                        createdAt:
                          type: number
                        updatedAt:
                          type: number
            requiredProperties:
              - items
            additionalProperties: false
        examples:
          example:
            value:
              items:
                - id: <string>
                  slug: <string>
                  origin: <string>
                  category: experiment
                  name: <string>
                  description: <string>
                  isArchived: true
                  createdAt: 123
                  updatedAt: 123
    codeSamples:
      - label: >-
          post_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.createInstallationIntegrationConfiguration({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The items were created
        examples: {}
        description: The items were created
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