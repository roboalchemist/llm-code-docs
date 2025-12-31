# Source: https://getlago.com/docs/api-reference/coupons/get-all-applied.md

# List all applied coupons

> This endpoint is used to list all applied coupons. You can filter by coupon status and by customer.

## OpenAPI

````yaml GET /applied_coupons
paths:
  path: /applied_coupons
  method: get
  servers:
    - url: https://api.getlago.com/api/v1
      description: US Lago cluster
    - url: https://api.eu.getlago.com/api/v1
      description: EU Lago cluster
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        page:
          schema:
            - type: integer
              required: false
              description: Page number.
              example: 1
          explode: true
        per_page:
          schema:
            - type: integer
              required: false
              description: Number of records per page.
              example: 20
          explode: true
        status:
          schema:
            - type: enum<string>
              enum:
                - active
                - terminated
              required: false
              description: >-
                The status of the coupon. Can be either `active` or
                `terminated`.
              example: active
          explode: true
        external_customer_id:
          schema:
            - type: string
              required: false
              description: >-
                The customer external unique identifier (provided by your own
                application)
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          explode: true
        coupon_code[]:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              required: false
              description: >-
                The code of the coupon applied to the customer. Use it to filter
                applied coupons by their code.
              example:
                - BLACK_FRIDAY_2024
                - CHRISTMAS_2024
          explode: true
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              applied_coupons:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/AppliedCouponObjectExtended'
              meta:
                allOf:
                  - $ref: '#/components/schemas/PaginationMeta'
            refIdentifier: '#/components/schemas/AppliedCouponsPaginated'
            requiredProperties:
              - applied_coupons
              - meta
        examples:
          example:
            value:
              applied_coupons:
                - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  lago_coupon_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  coupon_code: startup_deal
                  coupon_name: Startup Deal
                  lago_customer_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  external_customer_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                  status: active
                  amount_cents: 2000
                  amount_cents_remaining: 50
                  amount_currency: EUR
                  percentage_rate: null
                  frequency: recurring
                  frequency_duration: 3
                  frequency_duration_remaining: 1
                  expiration_at: '2022-04-29T08:59:51Z'
                  created_at: '2022-04-29T08:59:51Z'
                  terminated_at: '2022-04-29T08:59:51Z'
                  credits:
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      amount_cents: 1200
                      amount_currency: EUR
                      before_taxes: false
                      item:
                        lago_item_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                        type: coupon
                        code: startup_deal
                        name: Startup Deal
                      invoice:
                        lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                        payment_status: succeeded
              meta:
                current_page: 2
                next_page: 3
                prev_page: 1
                total_pages: 4
                total_count: 70
        description: Applied Coupons
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 401
              error:
                allOf:
                  - type: string
                    example: Unauthorized
            refIdentifier: '#/components/schemas/ApiErrorUnauthorized'
            requiredProperties:
              - status
              - error
        examples:
          example:
            value:
              status: 401
              error: Unauthorized
        description: Unauthorized error
  deprecated: false
  type: path
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

````