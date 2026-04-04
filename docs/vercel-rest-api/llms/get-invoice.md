# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-invoice.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Invoice

> Get Invoice details and status for a given invoice ID.<br/> <br/> See Billing Events with Webhooks documentation on how to receive invoice events. This endpoint is used to retrieve the invoice details.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}:
    get:
      tags:
        - marketplace
      summary: Get Invoice
      description: >-
        Get Invoice details and status for a given invoice ID.<br/> <br/> See
        Billing Events with Webhooks documentation on how to receive invoice
        events. This endpoint is used to retrieve the invoice details.
      operationId: get-invoice
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
        - name: invoiceId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  test:
                    type: boolean
                    enum:
                      - false
                      - true
                    description: >-
                      Whether the invoice is in the testmode (no real
                      transaction created).
                  invoiceId:
                    type: string
                    description: Vercel Marketplace Invoice ID.
                  externalId:
                    type: string
                    description: Partner-supplied Invoice ID, if applicable.
                  state:
                    type: string
                    enum:
                      - pending
                      - paid
                      - notpaid
                      - draft
                      - scheduled
                      - invoiced
                      - refund_requested
                      - refunded
                    description: Invoice state.
                  invoiceNumber:
                    type: string
                    description: User-readable invoice number.
                  invoiceDate:
                    type: string
                    description: Invoice date. ISO 8601 timestamp.
                  period:
                    properties:
                      start:
                        type: string
                      end:
                        type: string
                    required:
                      - end
                      - start
                    type: object
                    description: >-
                      Subscription period for this billing cycle. ISO 8601
                      timestamps.
                  paidAt:
                    type: string
                    description: Moment the invoice was paid. ISO 8601 timestamp.
                  refundedAt:
                    type: string
                    description: >-
                      Most recent moment the invoice was refunded. ISO 8601
                      timestamp.
                  memo:
                    type: string
                    description: Additional memo for the invoice.
                  items:
                    items:
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
                        - total
                        - units
                      type: object
                      description: Invoice items.
                    type: array
                    description: Invoice items.
                  discounts:
                    items:
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
                        - amount
                        - billingPlanId
                        - name
                      type: object
                      description: Invoice discounts.
                    type: array
                    description: Invoice discounts.
                  total:
                    type: string
                    description: Invoice total amount. A dollar-based decimal string.
                  refundReason:
                    type: string
                    description: >-
                      The reason for refund. Only applicable for states
                      "refunded" or "refund_request".
                  refundTotal:
                    type: string
                    description: >-
                      Refund amount. Only applicable for states "refunded" or
                      "refund_request". A dollar-based decimal string.
                  created:
                    type: string
                    description: System creation date. ISO 8601 timestamp.
                  updated:
                    type: string
                    description: System update date. ISO 8601 timestamp.
                required:
                  - created
                  - invoiceDate
                  - invoiceId
                  - items
                  - period
                  - state
                  - total
                  - updated
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````