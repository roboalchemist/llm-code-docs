# Source: https://getlago.com/docs/api-reference/analytics/overdue-balance.md

# Retrieve overdue balance

> Overdue balance is the total amount associated with overdue invoices (invoices with pending or failed payments which are past their due dates).

## OpenAPI

````yaml GET /analytics/overdue_balance
paths:
  path: /analytics/overdue_balance
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
        currency:
          schema:
            - type: enum<string>
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
              required: false
              description: Currency of revenue analytics. Format must be ISO 4217.
              refIdentifier: '#/components/schemas/Currency'
              example: USD
          explode: true
        external_customer_id:
          schema:
            - type: string
              required: false
              description: >-
                The customer external unique identifier (provided by your own
                application). Use it to filter revenue analytics at the customer
                level.
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          explode: true
        months:
          schema:
            - type: integer
              required: false
              description: Show data only for given number of months.
              example: 12
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
              overdue_balances:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/OverdueBalanceObject'
            refIdentifier: '#/components/schemas/OverdueBalances'
            requiredProperties:
              - overdue_balances
        examples:
          example:
            value:
              overdue_balances:
                - month: '2023-11-01T00:00:00.000Z'
                  amount_cents: 50000
                  currency: USD
                  lago_invoice_ids:
                    - 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        description: Overdue balance
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
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 403
              error:
                allOf:
                  - type: string
                    example: Forbidden
              code:
                allOf:
                  - type: string
                    example: feature_unavailable
            refIdentifier: '#/components/schemas/ApiErrorForbidden'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 403
              error: Forbidden
              code: feature_unavailable
        description: Forbidden
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
    OverdueBalanceObject:
      type: object
      required:
        - month
        - amount_cents
        - currency
        - lago_invoice_ids
      properties:
        month:
          type: string
          description: Identifies the month to analyze revenue.
          example: '2023-11-01T00:00:00.000Z'
        amount_cents:
          type: integer
          description: The total amount of revenue for a period, expressed in cents.
          example: 50000
        currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of revenue analytics. Format must be ISO 4217.
          example: USD
        lago_invoice_ids:
          type: array
          items:
            type: string
            format: uuid
          description: The Lago invoice IDs associated with the revenue.
          example:
            - 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba

````