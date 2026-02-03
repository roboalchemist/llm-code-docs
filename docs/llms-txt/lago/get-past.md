# Source: https://getlago.com/docs/api-reference/customer-usage/get-past.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve past usage

> Fetch historical customer usage data for closed billing periods.

<RequestExample>
  ```bash cURL theme={"dark"}
  LAGO_URL="https://api.getlago.com"
  API_KEY="__YOUR_API_KEY__"
  EXTERNAL_CUSTOMER_ID="__EXTERNAL_CUSTOMER_ID__"
  EXTERNAL_SUBSCRIPTION_ID="__EXTERNAL_SUBSCRIPTION_ID__"

  curl --location --request GET "$LAGO_URL/api/v1/customers/$EXTERNAL_CUSTOMER_ID/past_usage?external_subscription_id=$EXTERNAL_SUBSCRIPTION_ID" \
  --header "Authorization: Bearer $API_KEY" \
  --header 'Content-Type: application/json'
  ```

  ```python Python theme={"dark"}
  from lago_python_client.client import Client
  from lago_python_client.exceptions import LagoApiError

  client = Client(api_key='__YOUR_API_KEY__')

  customer_usage = None
  try:
      customer_usage = client.customers.past_usage('external_customer_id', 'external_subscription_id')
  except LagoApiError as e:
      repair_broken_state(e)  # do something on error or raise your own exception
  ```

  ```ruby Ruby theme={"dark"}
  require 'lago-ruby-client'

  client = Lago::Api::Client.new(api_key: '__YOUR_API_KEY__')
  customer_usage = client.customer.past_usage(
    'external_customer_id', 'external_subscription_id'
  )
  ```

  ```js Javascript theme={"dark"}
  await client.customers.findCustomerPastUsage(
    "customer_external_id",
    { external_subscription_id: "external_subscription_id" }
  );
  ```

  ```go Go theme={"dark"}
    import "fmt"
    import "github.com/getlago/lago-go-client"

    func main() {
      lagoClient := lago.New().
        SetApiKey("__YOUR_API_KEY__")

      customerUsage, err := lagoClient.Customer().PastUsage("__YOUR_CUSTOMER_ID__")
      if err != nil {
        // Error is *lago.Error
        panic(err)
      }

      // customerUsage is *lago.CustomerUsage
      fmt.Println(customerUsage)
    }
  ```
</RequestExample>


## OpenAPI

````yaml GET /customers/{external_customer_id}/past_usage
openapi: 3.1.0
info:
  title: Lago API documentation
  description: >-
    Lago API allows your application to push customer information and metrics
    (events) from your application to the billing application.
  version: 1.41.0
  license:
    name: AGPLv3
    identifier: AGPLv3
  contact:
    email: tech@getlago.com
servers:
  - url: https://api.getlago.com/api/v1
    description: US Lago cluster
  - url: https://api.eu.getlago.com/api/v1
    description: EU Lago cluster
security:
  - bearerAuth: []
tags:
  - name: activity_logs
    description: Everything about Activity logs
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/audit-logs/activity-logs-object
  - name: analytics
    description: Everything about Analytics
  - name: api_logs
    description: Everything about API logs
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/audit-logs/api-logs-object
  - name: billable_metrics
    description: Everything about Billable metric collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/billable-metrics/object
  - name: features
    description: Everything about Feature collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/features/object
  - name: entitlements
    description: Everything about Entitlement collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/entitlements/object
  - name: billing_entities
    description: Everything about Billing Entities
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/billing-entities/object
  - name: customers
    description: Everything about Customer collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/customers/object
  - name: plans
    description: Everything about Plan collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/plans/object
  - name: subscriptions
    description: Everything about Subscription collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/subscriptions/subscription-object
  - name: events
    description: Everything about Event collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/events/event-object
  - name: organizations
    description: Everything about Organization collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/organizations/organization-object
  - name: taxes
    description: Everything about Tax collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/taxes/tax-object
  - name: coupons
    description: Everything about Coupon collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/coupons/coupon-object
  - name: add_ons
    description: Everything about Add-on collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/add-ons/add-on-object
  - name: fees
    description: Everything about Fees
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/invoices/invoice-object#fee-object
  - name: invoices
    description: Everything about Invoice collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/invoices/invoice-object
  - name: wallets
    description: Everything about Wallet collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/wallets/wallet-object
  - name: credit_notes
    description: Everything about Credit notes collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/credit-notes/credit-note-object
  - name: webhooks
    description: Everything about Webhooks
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/webhooks/format---signature#1-retrieve-the-public-key
  - name: webhook_endpoints
    description: Everything about Webhook Endpoints
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/webhook-endpoints/webhook-endpoint-object
  - name: payment_receipts
    description: Everything about Payment receipts
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/payment-receipts/payment-receipt-object
  - name: payment_requests
    description: Everything about PaymentRequests
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/payment-requests/payment-request-object
  - name: payments
    description: Everything about Payments
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/payments/payment-object
externalDocs:
  description: Lago Github
  url: https://github.com/getlago
paths:
  /customers/{external_customer_id}/past_usage:
    get:
      tags:
        - customers
      summary: Retrieve customer past usage
      description: >-
        This endpoint enables the retrieval of the usage-based billing data for
        a customer within past periods.
      operationId: findAllCustomerPastUsage
      parameters:
        - $ref: '#/components/parameters/page'
        - $ref: '#/components/parameters/per_page'
        - name: external_customer_id
          in: path
          description: >-
            The customer external unique identifier (provided by your own
            application).
          required: true
          schema:
            type: string
            example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        - name: external_subscription_id
          in: query
          description: The unique identifier of the subscription within your application.
          required: true
          explode: true
          schema:
            type: string
            example: sub_1234567890
        - name: billable_metric_code
          in: query
          description: Billable metric code filter to apply to the charge usage
          required: false
          explode: true
          schema:
            type: string
            example: cpu
        - name: periods_count
          in: query
          description: Number of past billing period to returns in the result
          required: false
          explode: true
          schema:
            type: integer
            example: 5
      responses:
        '200':
          description: Customer past usage
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomerPastUsage'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
components:
  parameters:
    page:
      name: page
      in: query
      description: Page number.
      required: false
      explode: true
      schema:
        type: integer
        example: 1
    per_page:
      name: per_page
      in: query
      description: Number of records per page.
      required: false
      explode: true
      schema:
        type: integer
        example: 20
  schemas:
    CustomerPastUsage:
      type: object
      required:
        - usage_periods
        - meta
      properties:
        usage_periods:
          type: array
          items:
            $ref: '#/components/schemas/CustomerUsage'
        meta:
          $ref: '#/components/schemas/PaginationMeta'
    CustomerUsage:
      type: object
      required:
        - customer_usage
      properties:
        customer_usage:
          $ref: '#/components/schemas/CustomerUsageObject'
    PaginationMeta:
      type: object
      required:
        - current_page
        - total_pages
        - total_count
      properties:
        current_page:
          type: integer
          description: Current page.
          example: 2
        next_page:
          type:
            - integer
            - 'null'
          description: Next page.
          example: 3
        prev_page:
          type:
            - integer
            - 'null'
          description: Previous page.
          example: 1
        total_pages:
          type: integer
          description: Total number of pages.
          example: 4
        total_count:
          type: integer
          description: Total number of records.
          example: 70
    ApiErrorUnauthorized:
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: integer
          format: int32
          example: 401
        error:
          type: string
          example: Unauthorized
    ApiErrorNotFound:
      type: object
      required:
        - status
        - error
        - code
      properties:
        status:
          type: integer
          format: int32
          example: 404
        error:
          type: string
          example: Not Found
        code:
          type: string
          example: object_not_found
    ApiErrorUnprocessableEntity:
      type: object
      required:
        - status
        - error
        - code
        - error_details
      properties:
        status:
          type: integer
          format: int32
          example: 422
        error:
          type: string
          example: Unprocessable entity
        code:
          type: string
          example: validation_errors
        error_details:
          type: object
    CustomerUsageObject:
      type: object
      required:
        - from_datetime
        - to_datetime
        - issuing_date
        - amount_cents
        - taxes_amount_cents
        - total_amount_cents
        - charges_usage
      properties:
        from_datetime:
          type: string
          format: date-time
          description: >-
            The lower bound of the billing period, expressed in the ISO 8601
            datetime format in Coordinated Universal Time (UTC).
          example: '2022-07-01T00:00:00Z'
        to_datetime:
          type: string
          format: date-time
          description: >-
            The upper bound of the billing period, expressed in the ISO 8601
            datetime format in Coordinated Universal Time (UTC).
          example: '2022-07-31T23:59:59Z'
        issuing_date:
          type: string
          format: date
          description: The date of creation of the invoice.
          example: '2022-08-01'
        lago_invoice_id:
          type:
            - string
            - 'null'
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            A unique identifier associated with the invoice related to this
            particular usage record.
        currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of the customer's current usage.
          example: EUR
        amount_cents:
          type: integer
          description: The amount in cents, tax excluded.
          example: 123
        taxes_amount_cents:
          type: integer
          description: The tax amount in cents.
          example: 200
        total_amount_cents:
          type: integer
          description: The total amount in cents, tax included.
          example: 123
        charges_usage:
          type: array
          description: >-
            Array of charges that comprise the current usage. It contains
            detailed information about individual charge items associated with
            the usage.
          items:
            $ref: '#/components/schemas/CustomerChargeUsageObject'
    Currency:
      type: string
      example: USD
      enum:
        - AED
        - AFN
        - ALL
        - AMD
        - ANG
        - AOA
        - ARS
        - AUD
        - AWG
        - AZN
        - BAM
        - BBD
        - BDT
        - BGN
        - BIF
        - BMD
        - BND
        - BOB
        - BRL
        - BSD
        - BWP
        - BYN
        - BZD
        - CAD
        - CDF
        - CHF
        - CLF
        - CLP
        - CNY
        - COP
        - CRC
        - CVE
        - CZK
        - DJF
        - DKK
        - DOP
        - DZD
        - EGP
        - ETB
        - EUR
        - FJD
        - FKP
        - GBP
        - GEL
        - GHS
        - GIP
        - GMD
        - GNF
        - GTQ
        - GYD
        - HKD
        - HNL
        - HRK
        - HTG
        - HUF
        - IDR
        - ILS
        - INR
        - ISK
        - JMD
        - JPY
        - KES
        - KGS
        - KHR
        - KMF
        - KRW
        - KYD
        - KZT
        - LAK
        - LBP
        - LKR
        - LRD
        - LSL
        - MAD
        - MDL
        - MGA
        - MKD
        - MMK
        - MNT
        - MOP
        - MRO
        - MUR
        - MVR
        - MWK
        - MXN
        - MYR
        - MZN
        - NAD
        - NGN
        - NIO
        - NOK
        - NPR
        - NZD
        - PAB
        - PEN
        - PGK
        - PHP
        - PKR
        - PLN
        - PYG
        - QAR
        - RON
        - RSD
        - RUB
        - RWF
        - SAR
        - SBD
        - SCR
        - SEK
        - SGD
        - SHP
        - SLL
        - SOS
        - SRD
        - STD
        - SZL
        - THB
        - TJS
        - TOP
        - TRY
        - TTD
        - TWD
        - TZS
        - UAH
        - UGX
        - USD
        - UYU
        - UZS
        - VND
        - VUV
        - WST
        - XAF
        - XCD
        - XOF
        - XPF
        - YER
        - ZAR
        - ZMW
    CustomerChargeUsageObject:
      type: object
      required:
        - units
        - total_aggregated_units
        - events_count
        - amount_cents
        - amount_currency
        - charge
        - billable_metric
        - groups
      properties:
        units:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          example: '1.0'
          description: >-
            The number of units consumed by the customer for a specific charge
            item.
        total_aggregated_units:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          example: '1.0'
          description: >-
            The total number of units consumed by the customer for a specific
            charge item, aggregated across all usage events.
        events_count:
          type: integer
          example: 10
          description: >-
            The quantity of usage events that have been recorded for a
            particular charge during the specified time period. These events may
            also be referred to as the number of transactions in some contexts.
        amount_cents:
          type: integer
          example: 123
          description: >-
            The amount in cents, tax excluded, consumed by the customer for a
            specific charge item.
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of a usage item consumed by the customer.
          example: EUR
        pricing_unit_details:
          $ref: '#/components/schemas/UsagePricingUnitDetailsObject'
        charge:
          type: object
          description: Object listing all the properties for a specific charge item.
          required:
            - lago_id
            - charge_model
          properties:
            lago_id:
              type: string
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              description: >-
                Unique identifier assigned to the charge within the Lago
                application. This ID is exclusively created by Lago and serves
                as a unique identifier for the charge's record within the Lago
                system.
            charge_model:
              type: string
              description: >-
                The pricing model applied to this charge. Possible values are
                standard, `graduated`, `percentage`, `package` or `volume`.
              enum:
                - standard
                - graduated
                - package
                - percentage
                - volume
              example: graduated
            invoice_display_name:
              type: string
              description: >-
                Specifies the name that will be displayed on an invoice. If no
                value is set for this field, the name of the actual charge will
                be used as the default display name.
              example: Setup
        billable_metric:
          type: object
          description: The related billable metric object.
          required:
            - lago_id
            - name
            - code
            - aggregation_type
          properties:
            lago_id:
              type: string
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              description: >-
                Unique identifier assigned to the billable metric within the
                Lago application. This ID is exclusively created by Lago and
                serves as a unique identifier for the billable metric's record
                within the Lago system.
            name:
              type: string
              example: Storage
              description: The name of the billable metric used for this charge.
            code:
              type: string
              example: storage
              description: The code of the billable metric used for this charge.
            aggregation_type:
              type: string
              description: >-
                The aggregation type of the billable metric used for this
                charge. Possible values are `count_agg`, `sum_agg`, `max_agg` or
                `unique_count_agg`.
              enum:
                - count_agg
                - sum_agg
                - max_agg
                - unique_count_agg
                - weighted_sum_agg
                - latest_agg
              example: sum_agg
        filters:
          $ref: '#/components/schemas/CustomerChargeFiltersUsageObject'
        grouped_usage:
          $ref: '#/components/schemas/CustomerChargeGroupedUsageObject'
    UsagePricingUnitDetailsObject:
      type:
        - object
        - 'null'
      required:
        - amount_cents
        - short_name
        - conversion_rate
      description: Details about the pricing unit used for charge usage.
      properties:
        amount_cents:
          type: integer
          description: The amount in cents in the pricing unit.
          example: 200
        short_name:
          type: string
          example: CR
          description: The short name of the pricing unit.
        conversion_rate:
          type: string
          description: The conversion rate from pricing units to the plan's currency.
          example: '0.5'
    CustomerChargeFiltersUsageObject:
      type: array
      description: >-
        Array of filter object, representing multiple dimensions for a charge
        item.
      required:
        - values
        - units
        - total_aggregated_units
        - events_count
        - amount_cents
      items:
        type: object
        properties:
          units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '0.9'
            description: >-
              The number of units consumed for a specific charge filter related
              to a charge item.
          total_aggregated_units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '1.0'
            description: >-
              The total number of units consumed by the customer for a specific
              charge item, aggregated across all usage events.
          amount_cents:
            type: integer
            example: 1000
            description: >-
              The amount in cents, tax excluded, consumed for a specific charge
              filter related to a charge item.
          events_count:
            type: integer
            example: 10
            description: >-
              The quantity of usage events that have been recorded for a
              particular charge filter during the specified time period. These
              events may also be referred to as the number of transactions in
              some contexts.
          invoice_display_name:
            type: string
            description: Specifies the name that will be displayed on an invoice.
            example: AWS eu-east-1
          pricing_unit_details:
            $ref: '#/components/schemas/UsagePricingUnitDetailsObject'
          values:
            type: object
            description: List of filter values applied to the usage.
            additionalProperties:
              type: array
              items:
                type: string
            example:
              region:
                - us-east-1
    CustomerChargeGroupedUsageObject:
      type: array
      description: >-
        Array of aggregated fees, grouped by the event properties defined in a
        `standard` charge model.
      required:
        - amount_cents
        - events_count
        - units
        - total_aggregated_units
        - grouped_by
        - groups
      items:
        type: object
        properties:
          amount_cents:
            type: integer
            example: 1000
            description: >-
              The amount in cents, tax excluded, consumed for a specific group
              related to a charge item.
          events_count:
            type: integer
            example: 10
            description: >-
              The quantity of usage events that have been recorded for a
              particular charge during the specified time period. These events
              may also be referred to as the number of transactions in some
              contexts.
          units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '0.9'
            description: >-
              The number of units consumed for a specific group related to a
              charge item.
          total_aggregated_units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '1.0'
            description: >-
              The total number of units consumed by the customer for a specific
              charge item, aggregated across all usage events.
          pricing_unit_details:
            $ref: '#/components/schemas/UsagePricingUnitDetailsObject'
          grouped_by:
            type: object
            description: Key value list of event properties aggregated by the charge model
            additionalProperties:
              type: string
          filters:
            $ref: '#/components/schemas/CustomerChargeFiltersUsageObject'
  responses:
    Unauthorized:
      description: Unauthorized error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnauthorized'
    NotFound:
      description: Not Found error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorNotFound'
    UnprocessableEntity:
      description: Unprocessable entity error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnprocessableEntity'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````