# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-billing-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Billing Data

> Sends the billing and usage data. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing
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
  /v1/installations/{integrationConfigurationId}/billing:
    post:
      tags:
        - marketplace
      summary: Submit Billing Data
      description: >-
        Sends the billing and usage data. The partner should do this at least
        once a day and ideally once per hour. <br/> Use the
        `credentials.access_token` we provided in the [Upsert
        Installation](#upsert-installation) body to authorize this request.
      operationId: submit-billing-data
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
                timestamp:
                  description: >-
                    Server time of your integration, used to determine the most
                    recent data for race conditions & updates. Only the latest
                    usage data for a given day, week, and month will be kept.
                  type: string
                  format: date-time
                eod:
                  description: >-
                    End of Day, the UTC datetime for when the end of the
                    billing/usage day is in UTC time. This tells us which day
                    the usage data is for, and also allows for your \"end of
                    day\" to be different from UTC 00:00:00. eod must be within
                    the period dates, and cannot be older than 24h earlier from
                    our server's current time.
                  type: string
                  format: date-time
                period:
                  type: object
                  description: >-
                    Period for the billing cycle. The period end date cannot be
                    older than 24 hours earlier than our current server's time.
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
                  description: Billing data (interim invoicing data).
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
                  type: array
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
                          queries.\n              - rate: rate of usage, such as
                          queries per second.\n            
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
                          Metric value for the billing period. Could be a final
                          or an interim value for the period.
                      planValue:
                        type: number
                        description: >-
                          The limit value of the metric for a billing period, if
                          a limit is defined by the plan.
                    required:
                      - name
                      - type
                      - units
                      - dayValue
                      - periodValue
                    additionalProperties: false
              required:
                - timestamp
                - eod
                - period
                - billing
                - usage
              additionalProperties: false
        required: true
      responses:
        '201':
          description: ''
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
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````