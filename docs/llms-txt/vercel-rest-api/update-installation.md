# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-installation.md

# Update Installation

> This endpoint updates an integration installation.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}
paths:
  path: /v1/installations/{integrationConfigurationId}
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              billingPlan:
                allOf:
                  - type: object
                    required:
                      - id
                      - type
                      - name
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                        enum:
                          - prepayment
                          - subscription
                      name:
                        type: string
                      description:
                        type: string
                      paymentMethodRequired:
                        type: boolean
                      cost:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      highlightedDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      effectiveDate:
                        type: string
                    additionalProperties: true
              notification:
                allOf:
                  - oneOf:
                      - type: object
                        required:
                          - level
                          - title
                        properties:
                          level:
                            type: string
                            enum:
                              - info
                              - warn
                              - error
                          title:
                            type: string
                          message:
                            type: string
                          href:
                            type: string
                            format: uri
                      - type: string
                    description: >-
                      A notification to display to your customer. Send `null` to
                      clear the current notification.
            additionalProperties: false
        examples:
          example:
            value:
              billingPlan:
                id: <string>
                type: prepayment
                name: <string>
                description: <string>
                paymentMethodRequired: true
                cost: <string>
                details:
                  - label: <string>
                    value: <string>
                highlightedDetails:
                  - label: <string>
                    value: <string>
                effectiveDate: <string>
              notification:
                level: info
                title: <string>
                message: <string>
                href: <string>
    codeSamples:
      - label: update-installation
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateInstallation({
              integrationConfigurationId: "<id>",
            });


          }

          run();
  response:
    '204': {}
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