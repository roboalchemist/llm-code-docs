# Source: https://getlago.com/docs/guide/analytics/invoice-collection.md

# Source: https://getlago.com/docs/api-reference/analytics/invoice-collection.md

# Source: https://getlago.com/docs/guide/analytics/invoice-collection.md

# Source: https://getlago.com/docs/api-reference/analytics/invoice-collection.md

# Source: https://getlago.com/docs/guide/analytics/invoice-collection.md

# Source: https://getlago.com/docs/api-reference/analytics/invoice-collection.md

# Retrieve invoice collection

> Represents a monthly aggregation, detailing both the total count and the cumulative amount of invoices that have been marked as `finalized`. This report sorts invoices categorically based on their `payment_status`.

## OpenAPI

````yaml GET /analytics/invoice_collection
paths:
  path: /analytics/invoice_collection
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
              description: The currency of revenue analytics. Format must be ISO 4217.
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
              invoice_collections:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/InvoiceCollectionObject'
            refIdentifier: '#/components/schemas/InvoiceCollections'
            requiredProperties:
              - invoice_collections
        examples:
          example:
            value:
              invoice_collections:
                - month: '2023-11-01T00:00:00.000Z'
                  payment_status: succeeded
                  invoices_count: 10
                  amount_cents: 50000
                  currency: USD
        description: Finalized invoice collection
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
    InvoiceCollectionObject:
      type: object
      required:
        - month
        - invoices_count
      properties:
        month:
          type: string
          description: Identifies the month to analyze revenue.
          example: '2023-11-01T00:00:00.000Z'
        payment_status:
          type: string
          enum:
            - pending
            - succeeded
            - failed
          description: The payment status of the invoices.
          example: succeeded
        invoices_count:
          type: integer
          description: Contains invoices count.
          example: 10
        amount_cents:
          type: integer
          description: The total amount of revenue for a period, expressed in cents.
          example: 50000
        currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of revenue analytics. Format must be ISO 4217.
          example: USD

````