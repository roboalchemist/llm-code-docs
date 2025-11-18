# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-integration-resource.md

# Get Integration Resource

> Get a resource by its partner ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/resources/{resourceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/resources/{resourceId}
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
              description: >-
                The ID of the integration configuration (installation) the
                resource belongs to
        resourceId:
          schema:
            - type: string
              required: true
              description: The ID provided by the 3rd party provider for the given resource
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-integration-resource
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getIntegrationResource({
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
              id:
                allOf:
                  - type: string
                    description: >-
                      The ID provided by the 3rd party provider for the given
                      resource
              internalId:
                allOf:
                  - type: string
                    description: The ID assigned by Vercel for the given resource
              name:
                allOf:
                  - type: string
                    description: The name of the resource as it is recorded in Vercel
              status:
                allOf:
                  - type: string
                    enum:
                      - ready
                      - pending
                      - onboarding
                      - suspended
                      - resumed
                      - uninstalled
                      - error
                    description: The current status of the resource
              productId:
                allOf:
                  - type: string
                    description: The ID of the product the resource is derived from
              protocolSettings:
                allOf:
                  - properties:
                      experimentation:
                        properties:
                          edgeConfigSyncingEnabled:
                            type: boolean
                          edgeConfigId:
                            type: string
                          edgeConfigTokenId:
                            type: string
                        type: object
                    type: object
                    description: >-
                      Any settings provided for the resource to support its
                      product's protocols
              notification:
                allOf:
                  - properties:
                      level:
                        type: string
                        enum:
                          - error
                          - info
                          - warn
                      title:
                        type: string
                      message:
                        type: string
                      href:
                        type: string
                    required:
                      - level
                      - title
                    type: object
                    description: >-
                      The notification, if set, displayed to the user when
                      viewing the resource in Vercel
              billingPlanId:
                allOf:
                  - type: string
                    description: >-
                      The ID of the billing plan the resource is subscribed to,
                      if applicable
              metadata:
                allOf:
                  - additionalProperties:
                      oneOf:
                        - type: string
                        - type: number
                        - type: boolean
                        - items:
                            type: string
                          type: array
                          description: >-
                            The configured metadata for the resource as defined
                            by its product's Metadata Schema
                        - items:
                            type: number
                          type: array
                          description: >-
                            The configured metadata for the resource as defined
                            by its product's Metadata Schema
                    type: object
                    description: >-
                      The configured metadata for the resource as defined by its
                      product's Metadata Schema
            requiredProperties:
              - id
              - internalId
              - name
              - productId
        examples:
          example:
            value:
              id: <string>
              internalId: <string>
              name: <string>
              status: ready
              productId: <string>
              protocolSettings:
                experimentation:
                  edgeConfigSyncingEnabled: true
                  edgeConfigId: <string>
                  edgeConfigTokenId: <string>
              notification:
                level: error
                title: <string>
                message: <string>
                href: <string>
              billingPlanId: <string>
              metadata: {}
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