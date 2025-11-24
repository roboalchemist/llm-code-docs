# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-invoice.md

# Submit Invoice

> This endpoint allows the partner to submit an invoice to Vercel. The invoice is created in Vercel's billing system and sent to the customer. Depending on the type of billing plan, the invoice can be sent at a time of signup, at the start of the billing period, or at the end of the billing period.<br/> <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request. <br/> There are several limitations to the invoice submission:<br/> <br/> 1. A resource can only be billed once per the billing period and the billing plan.<br/> 2. The billing plan used to bill the resource must have been active for this resource during the billing period.<br/> 3. The billing plan used must be a subscription plan.<br/> 4. The interim usage data must be sent hourly for all types of subscriptions. See [Send subscription billing and usage data](#send-subscription-billing-and-usage-data) API on how to send interim billing and usage data.<br/>

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices
paths:
  path: /v1/installations/{integrationConfigurationId}/billing/invoices
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
              externalId:
                allOf:
                  - type: string
              invoiceDate:
                allOf:
                  - description: Invoice date. Must be within the period's start and end.
                    type: string
                    format: date-time
              memo:
                allOf:
                  - type: string
                    description: Additional memo for the invoice.
              period:
                allOf:
                  - type: object
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
                allOf:
                  - type: array
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
                allOf:
                  - type: array
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
                allOf:
                  - type: object
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
            required: true
            requiredProperties:
              - invoiceDate
              - period
              - items
            additionalProperties: false
        examples:
          example:
            value:
              externalId: <string>
              invoiceDate: '2023-11-07T05:31:56Z'
              memo: <string>
              period:
                start: '2023-11-07T05:31:56Z'
                end: '2023-11-07T05:31:56Z'
              items:
                - resourceId: <string>
                  billingPlanId: <string>
                  start: '2023-11-07T05:31:56Z'
                  end: '2023-11-07T05:31:56Z'
                  name: <string>
                  details: <string>
                  price: <string>
                  quantity: 123
                  units: <string>
                  total: <string>
              discounts:
                - resourceId: <string>
                  billingPlanId: <string>
                  start: '2023-11-07T05:31:56Z'
                  end: '2023-11-07T05:31:56Z'
                  name: <string>
                  details: <string>
                  amount: <string>
              test:
                validate: true
                result: paid
    codeSamples:
      - label: submit-invoice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.submitInvoice({
              integrationConfigurationId: "<id>",
              requestBody: {
                invoiceDate: new Date("2023-12-12T13:24:35.882Z"),
                period: {
                  start: new Date("2024-10-20T02:46:19.279Z"),
                  end: new Date("2025-06-06T21:30:28.107Z"),
                },
                items: [
                  {
                    billingPlanId: "<id>",
                    name: "<value>",
                    price: "469.29",
                    quantity: 3808.42,
                    units: "<value>",
                    total: "<value>",
                  },
                ],
              },
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
              invoiceId:
                allOf:
                  - type: string
              test:
                allOf:
                  - type: boolean
              validationErrors:
                allOf:
                  - items:
                      type: string
                    type: array
        examples:
          example:
            value:
              invoiceId: <string>
              test: true
              validationErrors:
                - <string>
        description: ''
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