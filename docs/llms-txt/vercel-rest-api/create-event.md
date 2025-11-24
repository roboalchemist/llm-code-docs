# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/create-event.md

# Create Event

> Partner notifies Vercel of any changes made to an Installation or a Resource. Vercel is expected to use `list-resources` and other read APIs to get the new state.<br/> <br/> `resource.updated` event should be dispatched when any state of a resource linked to Vercel is modified by the partner.<br/> `installation.updated` event should be dispatched when an installation's billing plan is changed via the provider instead of Vercel.<br/> <br/> Resource update use cases: <br/> <br/> - The user renames a database in the partner’s application. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource in Vercel’s datastores.<br/> - A resource has been suspended due to a lack of use. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource's status in Vercel's datastores.<br/>

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/events
paths:
  path: /v1/installations/{integrationConfigurationId}/events
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              event:
                allOf:
                  - oneOf:
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - installation.updated
                          billingPlanId:
                            type: string
                            description: The installation-level billing plan ID
                        required:
                          - type
                        additionalProperties: false
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - resource.updated
                          productId:
                            type: string
                            description: Partner-provided product slug or id
                          resourceId:
                            type: string
                            description: Partner provided resource ID
                        required:
                          - type
                          - resourceId
                        additionalProperties: false
            required: true
            requiredProperties:
              - event
            additionalProperties: false
        examples:
          example:
            value:
              event:
                type: installation.updated
                billingPlanId: <string>
    codeSamples:
      - label: create-event
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.createEvent({
              integrationConfigurationId: "<id>",
              requestBody: {
                event: {
                  type: "installation.updated",
                },
              },
            });


          }

          run();
  response:
    '201': {}
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