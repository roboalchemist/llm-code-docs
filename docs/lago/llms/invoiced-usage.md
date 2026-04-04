# Source: https://getlago.com/docs/api-reference/analytics/invoiced-usage.md

# Retrieve invoiced usage

> Reports a monthly analysis focused on the revenue generated from all usage-based fees. It exclusively accounts for revenue that has been formally invoiced. Importantly, this report does not include revenue related to the usage in the current billing period, limiting its scope to previously invoiced amounts.

## OpenAPI

````yaml GET /analytics/invoiced_usage
paths:
  path: /analytics/invoiced_usage
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
              description: >-
                The currency of invoiced usage analytics. Format must be ISO
                4217.
              refIdentifier: '#/components/schemas/Currency'
              example: USD
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
              invoiced_usages:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/InvoicedUsageObject'
            refIdentifier: '#/components/schemas/InvoicedUsages'
            requiredProperties:
              - invoiced_usages
        examples:
          example:
            value:
              invoiced_usages:
                - month: '2023-11-01T00:00:00.000Z'
                  code: code1
                  amount_cents: 50000
                  currency: USD
        description: Invoiced usage
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
    InvoicedUsageObject:
      type: object
      required:
        - month
        - amount_cents
        - currency
      properties:
        month:
          type: string
          description: Identifies the month to analyze revenue.
          example: '2023-11-01T00:00:00.000Z'
        code:
          type: string
          description: The code of the usage-based billable metrics.
          example: code1
        amount_cents:
          type: integer
          description: The total amount of revenue for a period, expressed in cents.
          example: 50000
        currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of revenue analytics. Format must be ISO 4217.
          example: USD

````