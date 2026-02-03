# Source: https://getlago.com/docs/api-reference/coupons/get-all-applied.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all applied coupons

> This endpoint is used to list all applied coupons. You can filter by coupon status and by customer.

<RequestExample>
  ```bash cURL theme={"dark"}
  LAGO_URL="https://api.getlago.com"
  API_KEY="__YOUR_API_KEY__"

  curl --location --request GET "$LAGO_URL/api/v1/applied_coupons?per_page=2&page=1" \
    --header "Authorization: Bearer $API_KEY"
  ```

  ```python Python theme={"dark"}
  from lago_python_client.client import Client
  from lago_python_client.exceptions import LagoApiError

  client = Client(api_key='__YOUR_API_KEY__')

  try:
      client.applied_coupons.find_all({'per_page': 2, 'page': 1})
  except LagoApiError as e:
      repair_broken_state(e)  # do something on error or raise your own exception
  ```

  ```ruby Ruby theme={"dark"}
  require 'lago-ruby-client'

  client = Lago::Api::Client.new(api_key: '__YOUR_API_KEY__')

  client.applied_coupons.get_all({ per_page: 2, page: 3 })
  ```

  ```js Javascript theme={"dark"}
  await client.appliedCoupons.findAllAppliedCoupons({ per_page: 2, page: 3 });
  ```

  ```go Go theme={"dark"}
  import "fmt"
  import "github.com/getlago/lago-go-client"

  func main() {
  lagoClient := lago.New().
      SetApiKey("__YOUR_API_KEY__")

  couponListInput := &lago.AppliedCouponListInput{
      PerPage: 1,
      Page: 1,
  }

  couponResult, err := lagoClient.AppliedCoupon().GetList(couponListInput)
  if err != nil {
      // Error is *lago.Error
      panic(err)
  }

  // couponResult is *lago.CouponResult
  fmt.Println(couponResult)
  }
  ```
</RequestExample>


## OpenAPI

````yaml GET /applied_coupons
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
  /applied_coupons:
    get:
      tags:
        - coupons
      summary: List all applied coupons
      description: >-
        This endpoint is used to list all applied coupons. You can filter by
        coupon status and by customer.
      operationId: findAllAppliedCoupons
      parameters:
        - $ref: '#/components/parameters/page'
        - $ref: '#/components/parameters/per_page'
        - name: status
          in: query
          description: The status of the coupon. Can be either `active` or `terminated`.
          required: false
          explode: true
          schema:
            type: string
            enum:
              - active
              - terminated
            example: active
        - name: external_customer_id
          in: query
          description: >-
            The customer external unique identifier (provided by your own
            application)
          required: false
          explode: true
          schema:
            type: string
            example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        - name: coupon_code[]
          in: query
          description: >-
            The code of the coupon applied to the customer. Use it to filter
            applied coupons by their code.
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
            example:
              - BLACK_FRIDAY_2024
              - CHRISTMAS_2024
      responses:
        '200':
          description: Applied Coupons
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AppliedCouponsPaginated'
        '401':
          $ref: '#/components/responses/Unauthorized'
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
    AppliedCouponsPaginated:
      type: object
      required:
        - applied_coupons
        - meta
      properties:
        applied_coupons:
          type: array
          items:
            $ref: '#/components/schemas/AppliedCouponObjectExtended'
        meta:
          $ref: '#/components/schemas/PaginationMeta'
    AppliedCouponObjectExtended:
      allOf:
        - $ref: '#/components/schemas/AppliedCouponObject'
        - type: object
          required:
            - credits
          properties:
            credits:
              type: array
              items:
                $ref: '#/components/schemas/CreditObject'
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
    AppliedCouponObject:
      type: object
      required:
        - lago_id
        - lago_coupon_id
        - coupon_code
        - coupon_name
        - external_customer_id
        - lago_customer_id
        - status
        - frequency
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the applied coupon, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_coupon_id:
          type: string
          format: uuid
          description: Unique identifier of the coupon, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        coupon_code:
          type: string
          description: Unique code used to identify the coupon.
          example: startup_deal
        coupon_name:
          type: string
          description: The name of the coupon.
          example: Startup Deal
        lago_customer_id:
          type: string
          format: uuid
          description: Unique identifier of the customer, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        external_customer_id:
          type: string
          description: >-
            The customer external unique identifier (provided by your own
            application)
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        status:
          type: string
          enum:
            - active
            - terminated
          description: The status of the coupon. Can be either `active` or `terminated`.
          example: active
        amount_cents:
          type:
            - integer
            - 'null'
          description: >-
            The amount of the coupon in cents. This field is required only for
            coupon with `fixed_amount` type.
          example: 2000
        amount_cents_remaining:
          type:
            - integer
            - 'null'
          description: >-
            The remaining amount in cents for a `fixed_amount` coupon with a
            frequency set to `once`. This field indicates the remaining balance
            or value that can still be utilized from the coupon.
          example: 50
        amount_currency:
          $ref: '#/components/schemas/CurrencyOrNull'
          description: >-
            The currency of the coupon. This field is required only for coupon
            with `fixed_amount` type.
          example: EUR
        percentage_rate:
          type:
            - string
            - 'null'
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            The percentage rate of the coupon. This field is required only for
            coupons with a `percentage` coupon type.
          example: null
        frequency:
          type: string
          enum:
            - once
            - recurring
            - forever
          description: >-
            The type of frequency for the coupon. It can have three possible
            values: `once`, `recurring` or `forever`.


            - If set to `once`, the coupon is applicable only for a single use.

            - If set to `recurring`, the coupon can be used multiple times for
            recurring billing periods.

            - If set to `forever`, the coupon has unlimited usage and can be
            applied indefinitely.
          example: recurring
        frequency_duration:
          type:
            - integer
            - 'null'
          description: >-
            Specifies the number of billing periods to which the coupon applies.
            This field is required only for coupons with a `recurring` frequency
            type
          example: 3
        frequency_duration_remaining:
          type:
            - integer
            - 'null'
          description: >-
            The remaining number of billing periods to which the coupon is
            applicable. This field determines the remaining usage or
            availability of the coupon based on the remaining billing periods.
          example: 1
        expiration_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time after which the coupon will stop applying to
            customer's invoices. Once the expiration date is reached, the coupon
            will no longer be applicable, and any further invoices generated for
            the customer will not include the coupon discount.
          example: '2022-04-29T08:59:51Z'
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the coupon was assigned to a customer. It is
            expressed in UTC format according to the ISO 8601 datetime standard.
          example: '2022-04-29T08:59:51Z'
        terminated_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            This field indicates the specific moment when the coupon amount is
            fully utilized or when the coupon is removed from the customer's
            coupon list. It is expressed in UTC format according to the ISO 8601
            datetime standard.
          example: '2022-04-29T08:59:51Z'
    CreditObject:
      type: object
      required:
        - lago_id
        - item
        - amount_cents
        - amount_currency
        - invoice
        - before_taxes
      properties:
        lago_id:
          type: string
          format: uuid
          description: >-
            Unique identifier assigned to the credit within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the credit's item record within the Lago
            system.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        amount_cents:
          type: integer
          description: >-
            The amount of credit associated with the invoice, expressed in
            cents.
          example: 1200
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of the credit.
          example: EUR
        before_taxes:
          type: boolean
          description: >-
            Indicates whether the credit is applied on the amount before taxes
            (coupons) or after taxes (credit notes). This flag helps determine
            the order in which credits are applied to the invoice calculation
          example: false
        item:
          type: object
          description: The item attached to the credit.
          required:
            - lago_item_id
            - type
            - code
            - name
          properties:
            lago_item_id:
              type: string
              format: uuid
              description: >-
                Unique identifier assigned to the credit item within the Lago
                application.
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
            type:
              type: string
              enum:
                - coupon
                - credit_note
                - invoice
              description: >-
                The type of credit applied. Possible values are `coupon`,
                `credit_note` or `invoice` (for `progressive_billing` invoice).
              example: coupon
            code:
              type: string
              description: >-
                The code of the credit applied. It can be the code of the coupon
                attached to the credit, the credit note's number or the
                `progressive_billing` invoice number.
              example: startup_deal
            name:
              type: string
              description: >-
                The name of the credit applied. It can be the name of the coupon
                attached to the credit, the initial invoice's number linked to
                the credit note or the `progressive_billing` invoice number.
              example: Startup Deal
        invoice:
          type: object
          required:
            - lago_id
            - payment_status
          properties:
            lago_id:
              type: string
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
            payment_status:
              type: string
              enum:
                - pending
                - succeeded
                - failed
              example: succeeded
    CurrencyOrNull:
      type:
        - string
        - 'null'
      example: USD
      enum:
        - null
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
  responses:
    Unauthorized:
      description: Unauthorized error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnauthorized'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````