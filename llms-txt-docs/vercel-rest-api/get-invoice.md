# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-invoice.md

# Get Invoice

> Get Invoice details and status for a given invoice ID.<br/> <br/> See Billing Events with Webhooks documentation on how to receive invoice events. This endpoint is used to retrieve the invoice details.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}
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
        invoiceId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-invoice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getInvoice({
              integrationConfigurationId: "<id>",
              invoiceId: "<id>",
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
              test:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the invoice is in the testmode (no real
                      transaction created).
              invoiceId:
                allOf:
                  - type: string
                    description: Vercel Marketplace Invoice ID.
              externalId:
                allOf:
                  - type: string
                    description: Partner-supplied Invoice ID, if applicable.
              state:
                allOf:
                  - type: string
                    enum:
                      - draft
                      - pending
                      - scheduled
                      - invoiced
                      - paid
                      - notpaid
                      - refund_requested
                      - refunded
                    description: Invoice state.
              invoiceNumber:
                allOf:
                  - type: string
                    description: User-readable invoice number.
              invoiceDate:
                allOf:
                  - type: string
                    description: Invoice date. ISO 8601 timestamp.
              period:
                allOf:
                  - properties:
                      start:
                        type: string
                      end:
                        type: string
                    required:
                      - start
                      - end
                    type: object
                    description: >-
                      Subscription period for this billing cycle. ISO 8601
                      timestamps.
              memo:
                allOf:
                  - type: string
                    description: Additional memo for the invoice.
              items:
                allOf:
                  - items:
                      properties:
                        billingPlanId:
                          type: string
                          description: Partner's billing plan ID.
                        resourceId:
                          type: string
                          description: >-
                            Partner's resource ID. If not specified, indicates
                            installation-wide item.
                        start:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        end:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        name:
                          type: string
                          description: Invoice item name.
                        details:
                          type: string
                          description: Additional item details.
                        price:
                          type: string
                          description: Item price. A dollar-based decimal string.
                        quantity:
                          type: number
                          description: Item quantity.
                        units:
                          type: string
                          description: Units for item's quantity.
                        total:
                          type: string
                          description: Item total. A dollar-based decimal string.
                      required:
                        - billingPlanId
                        - name
                        - price
                        - quantity
                        - units
                        - total
                      type: object
                      description: Invoice items.
                    type: array
                    description: Invoice items.
              discounts:
                allOf:
                  - items:
                      properties:
                        billingPlanId:
                          type: string
                          description: Partner's billing plan ID.
                        resourceId:
                          type: string
                          description: >-
                            Partner's resource ID. If not specified, indicates
                            installation-wide discount.
                        start:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        end:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        name:
                          type: string
                          description: Discount name.
                        details:
                          type: string
                          description: Additional discount details.
                        amount:
                          type: string
                          description: Discount amount. A dollar-based decimal string.
                      required:
                        - billingPlanId
                        - name
                        - amount
                      type: object
                      description: Invoice discounts.
                    type: array
                    description: Invoice discounts.
              total:
                allOf:
                  - type: string
                    description: Invoice total amount. A dollar-based decimal string.
              refundReason:
                allOf:
                  - type: string
                    description: >-
                      The reason for refund. Only applicable for states
                      "refunded" or "refund_request".
              refundTotal:
                allOf:
                  - type: string
                    description: >-
                      Refund amount. Only applicable for states "refunded" or
                      "refund_request". A dollar-based decimal string.
              created:
                allOf:
                  - type: string
                    description: System creation date. ISO 8601 timestamp.
              updated:
                allOf:
                  - type: string
                    description: System update date. ISO 8601 timestamp.
            requiredProperties:
              - invoiceId
              - state
              - invoiceDate
              - period
              - items
              - total
              - created
              - updated
        examples:
          example:
            value:
              test: true
              invoiceId: <string>
              externalId: <string>
              state: draft
              invoiceNumber: <string>
              invoiceDate: <string>
              period:
                start: <string>
                end: <string>
              memo: <string>
              items:
                - billingPlanId: <string>
                  resourceId: <string>
                  start: <string>
                  end: <string>
                  name: <string>
                  details: <string>
                  price: <string>
                  quantity: 123
                  units: <string>
                  total: <string>
              discounts:
                - billingPlanId: <string>
                  resourceId: <string>
                  start: <string>
                  end: <string>
                  name: <string>
                  details: <string>
                  amount: <string>
              total: <string>
              refundReason: <string>
              refundTotal: <string>
              created: <string>
              updated: <string>
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