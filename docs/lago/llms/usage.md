# Source: https://getlago.com/docs/guide/analytics/usage.md

# Source: https://getlago.com/docs/api-reference/events/usage.md

# Source: https://getlago.com/docs/api-reference/analytics/usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve usage data

> Returns usages.



## OpenAPI

````yaml GET /analytics/usage
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
  /analytics/usage:
    get:
      tags:
        - analytics
      summary: List usage
      description: Returns usages.
      operationId: findAllUsages
      parameters:
        - name: time_granularity
          in: query
          description: >-
            The time granularity of usage analytics. Possible values are
            'daily', 'weekly', 'monthly', 'yearly'.
          required: false
          schema:
            type: string
            enum:
              - daily
              - weekly
              - monthly
            example: monthly
        - name: currency
          in: query
          description: The currency of usage analytics. Format must be ISO 4217.
          required: false
          schema:
            allOf:
              - $ref: '#/components/schemas/Currency'
              - example: USD
        - name: from_date
          in: query
          description: >-
            The start date of the period for which the usage analytics is
            calculated.
          required: false
          schema:
            type: string
            format: date
            example: '2023-11-01'
        - name: to_date
          in: query
          description: >-
            The end date of the period for which the usage analytics is
            calculated.
          required: false
          schema:
            type: string
            format: date
            example: '2023-11-30'
        - name: customer_type
          in: query
          description: >-
            The type of customer for which the usage analytics is calculated.
            Possible values are 'individual', 'company'.
          required: false
          schema:
            type: string
            enum:
              - individual
              - company
            example: individual
        - name: external_customer_id
          in: query
          description: >-
            The external identifier of the customer for which the usage
            analytics is calculated.
          required: false
          schema:
            type: string
            example: ext-customer-123
        - name: customer_country
          in: query
          description: >-
            The country of the customer for which the usage analytics is
            calculated.
          required: false
          schema:
            allOf:
              - $ref: '#/components/schemas/Country'
              - example: US
        - name: external_subscription_id
          in: query
          description: >-
            The external identifier of the subscription for which the usage
            analytics is calculated.
          required: false
          schema:
            type: string
            example: ext-subscription-123
        - name: is_billable_metric_recurring
          in: query
          description: >-
            Indicates whether the billable metric associated with the usage is
            recurring.
          required: false
          schema:
            type: boolean
            example: true
        - name: plan_code
          in: query
          description: The code of the plan for which the usage analytics is calculated.
          required: false
          schema:
            type: string
            example: plan-code-123
        - name: billable_metric_code
          in: query
          description: >-
            The code of the usage-based billable metrics for which the usage
            analytics is calculated.
          required: false
          schema:
            type: string
            example: code1
      responses:
        '200':
          description: Usage
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Usages'
        '401':
          $ref: '#/components/responses/Unauthorized'
components:
  schemas:
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
    Country:
      type: string
      example: US
      enum:
        - AD
        - AE
        - AF
        - AG
        - AI
        - AL
        - AM
        - AO
        - AQ
        - AR
        - AS
        - AT
        - AU
        - AW
        - AX
        - AZ
        - BA
        - BB
        - BD
        - BE
        - BF
        - BG
        - BH
        - BI
        - BJ
        - BL
        - BM
        - BN
        - BO
        - BQ
        - BR
        - BS
        - BT
        - BV
        - BW
        - BY
        - BZ
        - CA
        - CC
        - CD
        - CF
        - CG
        - CH
        - CI
        - CK
        - CL
        - CM
        - CN
        - CO
        - CR
        - CU
        - CV
        - CW
        - CX
        - CY
        - CZ
        - DE
        - DJ
        - DK
        - DM
        - DO
        - DZ
        - EC
        - EE
        - EG
        - EH
        - ER
        - ES
        - ET
        - FI
        - FJ
        - FK
        - FM
        - FO
        - FR
        - GA
        - GB
        - GD
        - GE
        - GF
        - GG
        - GH
        - GI
        - GL
        - GM
        - GN
        - GP
        - GQ
        - GR
        - GS
        - GT
        - GU
        - GW
        - GY
        - HK
        - HM
        - HN
        - HR
        - HT
        - HU
        - ID
        - IE
        - IL
        - IM
        - IN
        - IO
        - IQ
        - IR
        - IS
        - IT
        - JE
        - JM
        - JO
        - JP
        - KE
        - KG
        - KH
        - KI
        - KM
        - KN
        - KP
        - KR
        - KW
        - KY
        - KZ
        - LA
        - LB
        - LC
        - LI
        - LK
        - LR
        - LS
        - LT
        - LU
        - LV
        - LY
        - MA
        - MC
        - MD
        - ME
        - MF
        - MG
        - MH
        - MK
        - ML
        - MM
        - MN
        - MO
        - MP
        - MQ
        - MR
        - MS
        - MT
        - MU
        - MV
        - MW
        - MX
        - MY
        - MZ
        - NA
        - NC
        - NE
        - NF
        - NG
        - NI
        - NL
        - 'NO'
        - NP
        - NR
        - NU
        - NZ
        - OM
        - PA
        - PE
        - PF
        - PG
        - PH
        - PK
        - PL
        - PM
        - PN
        - PR
        - PS
        - PT
        - PW
        - PY
        - QA
        - RE
        - RO
        - RS
        - RU
        - RW
        - SA
        - SB
        - SC
        - SD
        - SE
        - SG
        - SH
        - SI
        - SJ
        - SK
        - SL
        - SM
        - SN
        - SO
        - SR
        - SS
        - ST
        - SV
        - SX
        - SY
        - SZ
        - TC
        - TD
        - TF
        - TG
        - TH
        - TJ
        - TK
        - TL
        - TM
        - TN
        - TO
        - TR
        - TT
        - TV
        - TW
        - TZ
        - UA
        - UG
        - UM
        - US
        - UY
        - UZ
        - VA
        - VC
        - VE
        - VG
        - VI
        - VN
        - VU
        - WF
        - WS
        - YE
        - YT
        - ZA
        - ZM
        - ZW
    Usages:
      type: object
      required:
        - usages
      properties:
        usages:
          type: array
          items:
            $ref: '#/components/schemas/UsageObject'
    UsageObject:
      type: object
      required:
        - organization_id
        - amount_cents
        - amount_currency
      properties:
        organization_id:
          type: string
          format: uuid
          description: >-
            The unique identifier of the organization for which the usage
            analytics is calculated.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        start_of_period_dt:
          type: string
          format: date
          description: >-
            The start date of the period for which the usage analytics is
            calculated.
          example: '2023-11-01'
        end_of_period_dt:
          type: string
          format: date
          description: >-
            The end date of the period for which the usage analytics is
            calculated.
          example: '2023-11-30'
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of usage analytics. Format must be ISO 4217.
          example: USD
        amount_cents:
          type: integer
          description: The total amount for usages for a period, expressed in cents.
          example: 50000
        billable_metric_code:
          type: string
          description: The code of the usage-based billable metrics.
          example: code1
        units:
          type: string
          description: The total number of units for the usage-based billable metrics.
          pattern: ^[0-9]+.?[0-9]*$
          example: '1.0'
        is_billable_metric_deleted:
          type: boolean
          description: >-
            Indicates whether the billable metric associated with the usage is
            deleted.
          example: false
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