# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-billing-data.md

# Submit Billing Data

> Sends the billing and usage data. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing
paths:
  path: /v1/installations/{integrationConfigurationId}/billing
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
              timestamp:
                allOf:
                  - description: >-
                      Server time of your integration, used to determine the
                      most recent data for race conditions & updates. Only the
                      latest usage data for a given day, week, and month will be
                      kept.
                    type: string
                    format: date-time
              eod:
                allOf:
                  - description: >-
                      End of Day, the UTC datetime for when the end of the
                      billing/usage day is in UTC time. This tells us which day
                      the usage data is for, and also allows for your \"end of
                      day\" to be different from UTC 00:00:00. eod must be
                      within the period dates, and cannot be older than 24h
                      earlier from our server's current time.
                    type: string
                    format: date-time
              period:
                allOf:
                  - type: object
                    description: >-
                      Period for the billing cycle. The period end date cannot
                      be older than 24 hours earlier than our current server's
                      time.
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
              billing:
                allOf:
                  - description: Billing data (interim invoicing data).
                    oneOf:
                      - type: array
                        items:
                          type: object
                          properties:
                            billingPlanId:
                              type: string
                              description: Partner's billing plan ID.
                            resourceId:
                              type: string
                              description: Partner's resource ID.
                            start:
                              description: >-
                                Start and end are only needed if different from
                                the period's start/end.
                              type: string
                              format: date-time
                            end:
                              description: >-
                                Start and end are only needed if different from
                                the period's start/end.
                              type: string
                              format: date-time
                            name:
                              type: string
                              description: Line item name.
                            details:
                              type: string
                              description: Line item details.
                            price:
                              description: Price per unit.
                              type: string
                              pattern: ^[0-9]+(\\.[0-9]+)?$
                            quantity:
                              type: number
                              description: Quantity of units.
                            units:
                              type: string
                              description: Units of the quantity.
                            total:
                              description: Total amount.
                              type: string
                              pattern: ^[0-9]+(\\.[0-9]+)?$
                          required:
                            - billingPlanId
                            - name
                            - price
                            - quantity
                            - units
                            - total
                          additionalProperties: false
                      - type: object
                        properties:
                          items:
                            type: array
                            items:
                              type: object
                              properties:
                                billingPlanId:
                                  type: string
                                  description: Partner's billing plan ID.
                                resourceId:
                                  type: string
                                  description: Partner's resource ID.
                                start:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                end:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                name:
                                  type: string
                                  description: Line item name.
                                details:
                                  type: string
                                  description: Line item details.
                                price:
                                  description: Price per unit.
                                  type: string
                                  pattern: ^[0-9]+(\\.[0-9]+)?$
                                quantity:
                                  type: number
                                  description: Quantity of units.
                                units:
                                  type: string
                                  description: Units of the quantity.
                                total:
                                  description: Total amount.
                                  type: string
                                  pattern: ^[0-9]+(\\.[0-9]+)?$
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
                                billingPlanId:
                                  type: string
                                  description: Partner's billing plan ID.
                                resourceId:
                                  type: string
                                  description: Partner's resource ID.
                                start:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                end:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                name:
                                  type: string
                                  description: Discount name.
                                details:
                                  type: string
                                  description: Discount details.
                                amount:
                                  description: Discount amount.
                                  type: string
                                  pattern: ^[0-9]+(\\.[0-9]+)?$
                              required:
                                - billingPlanId
                                - name
                                - amount
                              additionalProperties: false
                        required:
                          - items
              usage:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        resourceId:
                          type: string
                          description: Partner's resource ID.
                        name:
                          type: string
                          description: Metric name.
                        type:
                          type: string
                          description: >-
                            \n              Type of the metric.\n              -
                            total: measured total value, such as Database
                            size\n              - interval: usage during the
                            period, such as i/o or number of
                            queries.\n              - rate: rate of usage, such
                            as queries per second.\n            
                          enum:
                            - total
                            - interval
                            - rate
                        units:
                          type: string
                          description: 'Metric units. Example: \"GB\"'
                        dayValue:
                          type: number
                          description: >-
                            Metric value for the day. Could be a final or an
                            interim value for the day.
                        periodValue:
                          type: number
                          description: >-
                            Metric value for the billing period. Could be a
                            final or an interim value for the period.
                        planValue:
                          type: number
                          description: >-
                            The limit value of the metric for a billing period,
                            if a limit is defined by the plan.
                      required:
                        - name
                        - type
                        - units
                        - dayValue
                        - periodValue
                      additionalProperties: false
            required: true
            requiredProperties:
              - timestamp
              - eod
              - period
              - billing
              - usage
            additionalProperties: false
        examples:
          example:
            value:
              timestamp: '2023-11-07T05:31:56Z'
              eod: '2023-11-07T05:31:56Z'
              period:
                start: '2023-11-07T05:31:56Z'
                end: '2023-11-07T05:31:56Z'
              billing:
                - billingPlanId: <string>
                  resourceId: <string>
                  start: '2023-11-07T05:31:56Z'
                  end: '2023-11-07T05:31:56Z'
                  name: <string>
                  details: <string>
                  price: <string>
                  quantity: 123
                  units: <string>
                  total: <string>
              usage:
                - resourceId: <string>
                  name: <string>
                  type: total
                  units: <string>
                  dayValue: 123
                  periodValue: 123
                  planValue: 123
    codeSamples:
      - label: submit-billing-data
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.submitBillingData({
              integrationConfigurationId: "<id>",
              requestBody: {
                timestamp: new Date("2023-11-26T05:03:03.977Z"),
                eod: new Date("2023-04-14T04:58:49.647Z"),
                period: {
                  start: new Date("2023-03-12T13:32:00.895Z"),
                  end: new Date("2023-12-15T15:17:13.187Z"),
                },
                billing: [
                  {
                    billingPlanId: "<id>",
                    name: "<value>",
                    price: "694.00",
                    quantity: 228.64,
                    units: "<value>",
                    total: "<value>",
                  },
                ],
                usage: [
                  {
                    name: "<value>",
                    type: "interval",
                    units: "<value>",
                    dayValue: 5212.43,
                    periodValue: 4147.35,
                  },
                ],
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