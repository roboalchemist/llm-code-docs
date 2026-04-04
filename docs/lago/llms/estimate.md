# Source: https://getlago.com/docs/api-reference/credit-notes/estimate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Estimate a credit note

> This endpoint allows you to retrieve amounts for a new credit note creation.



## OpenAPI

````yaml POST /credit_notes/estimate
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
  /credit_notes/estimate:
    post:
      tags:
        - credit_notes
      summary: Estimate amounts for a new credit note
      description: >-
        This endpoint allows you to retrieve amounts for a new credit note
        creation.
      operationId: estimateCreditNote
      requestBody:
        description: Credit note estimate payload
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreditNoteEstimateInput'
      responses:
        '200':
          description: Credit note amounts
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreditNoteEstimated'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
components:
  schemas:
    CreditNoteEstimateInput:
      type: object
      required:
        - credit_note
      properties:
        credit_note:
          type: object
          required:
            - invoice_id
            - items
          properties:
            invoice_id:
              type: string
              format: uuid
              description: The invoice unique identifier, created by Lago.
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
            items:
              type: array
              items:
                type: object
                required:
                  - fee_id
                  - amount_cents
                properties:
                  fee_id:
                    type: string
                    format: uuid
                    description: The fee unique identifier, created by Lago.
                    example: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  amount_cents:
                    type: integer
                    description: The amount of the credit note item, expressed in cents.
                    example: 10
              description: The list of credit note's items.
              example:
                - fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  amount_cents: 10
                - fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a91
                  amount_cents: 5
    CreditNoteEstimated:
      type: object
      required:
        - estimated_credit_note
      properties:
        estimated_credit_note:
          type: object
          required:
            - lago_invoice_id
            - invoice_number
            - currency
            - taxes_amount_cents
            - precise_taxes_amount_cents
            - sub_total_excluding_taxes_amount_cents
            - max_creditable_amount_cents
            - max_refundable_amount_cents
            - max_offsettable_amount_cents
            - coupons_adjustment_amount_cents
            - precise_coupons_adjustment_amount_cents
            - taxes_rate
            - items
          properties:
            lago_invoice_id:
              type: string
              format: uuid
              description: >-
                Unique identifier assigned to the invoice that the credit note
                belongs to
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
            invoice_number:
              type: string
              description: The invoice unique number, related to the credit note.
              example: LAG-1234
            currency:
              $ref: '#/components/schemas/Currency'
              description: The currency of the credit note.
              example: EUR
            taxes_amount_cents:
              type: integer
              description: The tax amount of the credit note, expressed in cents.
              example: 20
            precise_taxes_amount_cents:
              type: number
              description: >-
                The precise tax amount of the credit note, expressed in cents
                with decimal precision.
              example: 20.1
            taxes_rate:
              type: number
              description: The tax rate associated with this specific credit note.
              example: 20
            sub_total_excluding_taxes_amount_cents:
              type: integer
              description: >-
                The subtotal of the credit note excluding any applicable taxes,
                expressed in cents.
              example: 100
            max_creditable_amount_cents:
              type: integer
              description: The credited amount of the credit note, expressed in cents.
              example: 100
            max_refundable_amount_cents:
              type: integer
              description: The refunded amount of the credit note, expressed in cents.
              example: 0
            max_offsettable_amount_cents:
              type: integer
              description: The ofsetted amount of the credit note, expressed in cents.
              example: 0
            coupons_adjustment_amount_cents:
              type: integer
              description: >-
                The pro-rated amount of the coupons applied to the source
                invoice.
              example: 20
            precise_coupons_adjustment_amount_cents:
              type: number
              description: >-
                The precise pro-rated amount with decimal precision of the
                coupons applied to the source invoice.
              example: 20.1
            items:
              type: array
              items:
                type: object
                required:
                  - amount_cents
                  - lago_fee_id
                properties:
                  amount_cents:
                    type: integer
                    description: The credit note's item amount, expressed in cents.
                    example: 100
                  lago_fee_id:
                    type:
                      - string
                      - 'null'
                    format: uuid
                    description: >-
                      Unique identifier assigned to the fee within the Lago
                      application. This ID is exclusively created by Lago and
                      serves as a unique identifier for the fee's record within
                      the Lago system.
                    example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              description: Array of credit note's items.
            applied_taxes:
              type: array
              items:
                type: object
                properties:
                  lago_tax_id:
                    type: string
                    format: uuid
                    description: Unique identifier of the tax, created by Lago.
                    example: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  tax_name:
                    type: string
                    description: Name of the tax.
                    example: TVA
                  tax_code:
                    type: string
                    description: >-
                      Unique code used to identify the tax associated with the
                      API request.
                    example: french_standard_vat
                  tax_rate:
                    type: number
                    description: The percentage rate of the tax
                    example: 20
                  tax_description:
                    type: string
                    description: Internal description of the taxe
                    example: French standard VAT
                  base_amount_cents:
                    type: integer
                    example: 100
                  amount_cents:
                    type: integer
                    description: Amount of the tax
                    example: 2000
                  amount_currency:
                    $ref: '#/components/schemas/Currency'
                    description: Currency of the tax
                    example: USD
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
    ApiErrorBadRequest:
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: integer
          format: int32
          example: 400
        error:
          type: string
          example: Bad request
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
  responses:
    BadRequest:
      description: Bad Request error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorBadRequest'
    Unauthorized:
      description: Unauthorized error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnauthorized'
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