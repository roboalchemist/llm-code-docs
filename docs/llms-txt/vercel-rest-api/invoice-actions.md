# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/invoice-actions.md

# Invoice Actions

> This endpoint allows the partner to request a refund for an invoice to Vercel. The invoice is created using the [Submit Invoice API](#submit-invoice-api).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}/actions
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}/actions
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
        invoiceId:
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
              action:
                allOf:
                  - type: string
                    enum:
                      - refund
              reason:
                allOf:
                  - type: string
                    description: Refund reason.
              total:
                allOf:
                  - description: >-
                      The total amount to be refunded. Must be less than or
                      equal to the total amount of the invoice.
                    type: string
                    pattern: ^[0-9]+(\\.[0-9]+)?$
            required: true
            requiredProperties:
              - action
              - reason
              - total
            additionalProperties: false
        examples:
          example:
            value:
              action: refund
              reason: <string>
              total: <string>
    codeSamples:
      - label: update-invoice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateInvoice({
              integrationConfigurationId: "<id>",
              invoiceId: "<id>",
              requestBody: {
                action: "refund",
                reason: "<value>",
                total: "<value>",
              },
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````