# Source: https://getlago.com/docs/guide/analytics/mrr.md

# Source: https://getlago.com/docs/api-reference/analytics/mrr.md

# Retrieve MRR (monthly recurring revenue)

> This endpoint is used to list MRR.

## OpenAPI

````yaml GET /analytics/mrr
paths:
  path: /analytics/mrr
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
                Quantifies the revenue generated from `subscription` fees on a
                monthly basis. This figure is calculated post-application of
                applicable taxes and deduction of any applicable discounts. The
                method of calculation varies based on the subscription billing
                cycle:


                - Revenue from `monthly` subscription invoices is included in
                the MRR for the month in which the invoice is issued.

                - Revenue from `quarterly` subscription invoices is distributed
                evenly over three months. This distribution applies to fees paid
                in advance (allocated to the next remaining months depending on
                calendar or anniversary billing) as well as to fees paid in
                arrears (allocated to the preceding months depending on calendar
                or anniversary billing).

                - Revenue from `yearly` subscription invoices is distributed
                evenly over twelve months. This allocation is applicable for
                fees paid in advance (spread over the next remaining months
                depending on calendar or anniversary billing) and for fees paid
                in arrears (spread over the previous months depending on
                calendar or anniversary billing).

                - Revenue from `semiannual` subscription invoices is distributed
                evenly over six months. This allocation is applicable for fees
                paid in advance (spread over the next remaining months depending
                on calendar or anniversary billing) and for fees paid in arrears
                (spread over the previous months depending on calendar or
                anniversary billing).

                - Revenue from `weekly` subscription invoices, the total revenue
                from all invoices issued within a month is summed up. This total
                is then divided by the number of invoices issued during that
                month, and the result is multiplied by 4.33, representing the
                average number of weeks in a month.
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
              mrrs:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/MrrObject'
            refIdentifier: '#/components/schemas/Mrrs'
            requiredProperties:
              - mrrs
        examples:
          example:
            value:
              mrrs:
                - month: '2023-11-01T00:00:00.000Z'
                  amount_cents: 50000
                  currency: USD
        description: MRR
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
    MrrObject:
      type: object
      required:
        - month
        - amount_cents
        - currency
      properties:
        month:
          type: string
          description: Identifies the month to analyze MRR.
          example: '2023-11-01T00:00:00.000Z'
        amount_cents:
          type: integer
          description: The total amount of MRR, expressed in cents.
          example: 50000
        currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of MRR analytics. Format must be ISO 4217.
          example: USD

````