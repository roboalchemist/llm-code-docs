# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-invoice.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Invoice

> This endpoint allows the partner to submit an invoice to Vercel. The invoice is created in Vercel's billing system and sent to the customer. Depending on the type of billing plan, the invoice can be sent at a time of signup, at the start of the billing period, or at the end of the billing period.<br/> <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request. <br/> There are several limitations to the invoice submission:<br/> <br/> 1. A resource can only be billed once per the billing period and the billing plan.<br/> 2. The billing plan used to bill the resource must have been active for this resource during the billing period.<br/> 3. The billing plan used must be a subscription plan.<br/> 4. The interim usage data must be sent hourly for all types of subscriptions. See [Send subscription billing and usage data](#send-subscription-billing-and-usage-data) API on how to send interim billing and usage data.<br/>



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices
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
  /v1/installations/{integrationConfigurationId}/billing/invoices:
    post:
      tags:
        - marketplace
      summary: Submit Invoice
      description: >-
        This endpoint allows the partner to submit an invoice to Vercel. The
        invoice is created in Vercel's billing system and sent to the customer.
        Depending on the type of billing plan, the invoice can be sent at a time
        of signup, at the start of the billing period, or at the end of the
        billing period.<br/> <br/> Use the `credentials.access_token` we
        provided in the [Upsert Installation](#upsert-installation) body to
        authorize this request. <br/> There are several limitations to the
        invoice submission:<br/> <br/> 1. A resource can only be billed once per
        the billing period and the billing plan.<br/> 2. The billing plan used
        to bill the resource must have been active for this resource during the
        billing period.<br/> 3. The billing plan used must be a subscription
        plan.<br/> 4. The interim usage data must be sent hourly for all types
        of subscriptions. See [Send subscription billing and usage
        data](#send-subscription-billing-and-usage-data) API on how to send
        interim billing and usage data.<br/>
      operationId: submit-invoice
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                externalId:
                  type: string
                invoiceDate:
                  description: Invoice date. Must be within the period's start and end.
                  type: string
                  format: date-time
                memo:
                  type: string
                  description: Additional memo for the invoice.
                period:
                  type: object
                  description: Subscription period for this billing cycle.
                  properties:
                    start:
                      type: string
                      format: date-time
                    end:
                      type: string
                      format: date-time
                  required:
                    - start
                    - end
                  additionalProperties: false
                items:
                  type: array
                  items:
                    type: object
                    properties:
                      resourceId:
                        type: string
                        description: Partner's resource ID.
                      billingPlanId:
                        type: string
                        description: Partner's billing plan ID.
                      start:
                        description: >-
                          Start and end are only needed if different from the
                          period's start/end.
                        type: string
                        format: date-time
                      end:
                        description: >-
                          Start and end are only needed if different from the
                          period's start/end.
                        type: string
                        format: date-time
                      name:
                        type: string
                      details:
                        type: string
                      price:
                        type: string
                        pattern: ^[0-9]+(\\.[0-9]+)?$
                        description: Currency amount as a decimal string.
                      quantity:
                        type: number
                      units:
                        type: string
                      total:
                        type: string
                        pattern: ^[0-9]+(\\.[0-9]+)?$
                        description: Currency amount as a decimal string.
                    required:
                      - billingPlanId
                      - name
                      - price
                      - quantity
                      - units
                      - total
                    additionalProperties: false
                discounts:
                  type: array
                  items:
                    type: object
                    properties:
                      resourceId:
                        type: string
                        description: Partner's resource ID.
                      billingPlanId:
                        type: string
                        description: Partner's billing plan ID.
                      start:
                        description: >-
                          Start and end are only needed if different from the
                          period's start/end.
                        type: string
                        format: date-time
                      end:
                        description: >-
                          Start and end are only needed if different from the
                          period's start/end.
                        type: string
                        format: date-time
                      name:
                        type: string
                      details:
                        type: string
                      amount:
                        type: string
                        pattern: ^[0-9]+(\\.[0-9]+)?$
                        description: Currency amount as a decimal string.
                    required:
                      - billingPlanId
                      - name
                      - amount
                    additionalProperties: false
                test:
                  type: object
                  description: Test mode
                  properties:
                    validate:
                      type: boolean
                    result:
                      type: string
                      enum:
                        - paid
                        - notpaid
                  additionalProperties: false
              required:
                - invoiceDate
                - period
                - items
              additionalProperties: false
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  invoiceId:
                    type: string
                  test:
                    type: boolean
                    enum:
                      - false
                      - true
                  validationErrors:
                    items:
                      type: string
                    type: array
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '409':
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