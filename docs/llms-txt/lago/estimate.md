# Source: https://getlago.com/docs/api-reference/credit-notes/estimate.md

# Estimate a credit note

> This endpoint allows you to retrieve amounts for a new credit note creation.

## OpenAPI

````yaml POST /credit_notes/estimate
paths:
  path: /credit_notes/estimate
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              credit_note:
                allOf:
                  - type: object
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
                              description: >-
                                The amount of the credit note item, expressed in
                                cents.
                              example: 10
                        description: The list of credit note's items.
                        example:
                          - fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                            amount_cents: 10
                          - fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a91
                            amount_cents: 5
            refIdentifier: '#/components/schemas/CreditNoteEstimateInput'
            requiredProperties:
              - credit_note
        examples:
          example:
            value:
              credit_note:
                invoice_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                items:
                  - fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                    amount_cents: 10
                  - fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a91
                    amount_cents: 5
        description: Credit note estimate payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              estimated_credit_note:
                allOf:
                  - type: object
                    required:
                      - lago_invoice_id
                      - invoice_number
                      - currency
                      - taxes_amount_cents
                      - precise_taxes_amount_cents
                      - sub_total_excluding_taxes_amount_cents
                      - max_creditable_amount_cents
                      - max_refundable_amount_cents
                      - coupons_adjustment_amount_cents
                      - precise_coupons_adjustment_amount_cents
                      - taxes_rate
                      - items
                    properties:
                      lago_invoice_id:
                        type: string
                        format: uuid
                        description: >-
                          Unique identifier assigned to the invoice that the
                          credit note belongs to
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
                          The precise tax amount of the credit note, expressed
                          in cents with decimal precision.
                        example: 20.1
                      taxes_rate:
                        type: number
                        description: >-
                          The tax rate associated with this specific credit
                          note.
                        example: 20
                      sub_total_excluding_taxes_amount_cents:
                        type: integer
                        description: >-
                          The subtotal of the credit note excluding any
                          applicable taxes, expressed in cents.
                        example: 100
                      max_creditable_amount_cents:
                        type: integer
                        description: >-
                          The credited amount of the credit note, expressed in
                          cents.
                        example: 100
                      max_refundable_amount_cents:
                        type: integer
                        description: >-
                          The refunded amount of the credit note, expressed in
                          cents.
                        example: 0
                      coupons_adjustment_amount_cents:
                        type: integer
                        description: >-
                          The pro-rated amount of the coupons applied to the
                          source invoice.
                        example: 20
                      precise_coupons_adjustment_amount_cents:
                        type: number
                        description: >-
                          The precise pro-rated amount with decimal precision of
                          the coupons applied to the source invoice.
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
                              description: >-
                                The credit note's item amount, expressed in
                                cents.
                              example: 100
                            lago_fee_id:
                              type:
                                - string
                                - 'null'
                              format: uuid
                              description: >-
                                Unique identifier assigned to the fee within the
                                Lago application. This ID is exclusively created
                                by Lago and serves as a unique identifier for
                                the fee's record within the Lago system.
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
                                Unique code used to identify the tax associated
                                with the API request.
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
            refIdentifier: '#/components/schemas/CreditNoteEstimated'
            requiredProperties:
              - estimated_credit_note
        examples:
          example:
            value:
              estimated_credit_note:
                lago_invoice_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                invoice_number: LAG-1234
                currency: EUR
                taxes_amount_cents: 20
                precise_taxes_amount_cents: 20.1
                taxes_rate: 20
                sub_total_excluding_taxes_amount_cents: 100
                max_creditable_amount_cents: 100
                max_refundable_amount_cents: 0
                coupons_adjustment_amount_cents: 20
                precise_coupons_adjustment_amount_cents: 20.1
                items:
                  - amount_cents: 100
                    lago_fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                applied_taxes:
                  - lago_tax_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                    tax_name: TVA
                    tax_code: french_standard_vat
                    tax_rate: 20
                    tax_description: French standard VAT
                    base_amount_cents: 100
                    amount_cents: 2000
                    amount_currency: USD
        description: Credit note amounts
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 400
              error:
                allOf:
                  - type: string
                    example: Bad request
            refIdentifier: '#/components/schemas/ApiErrorBadRequest'
            requiredProperties:
              - status
              - error
        examples:
          example:
            value:
              status: 400
              error: Bad request
        description: Bad Request error
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
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 422
              error:
                allOf:
                  - type: string
                    example: Unprocessable entity
              code:
                allOf:
                  - type: string
                    example: validation_errors
              error_details:
                allOf:
                  - type: object
            refIdentifier: '#/components/schemas/ApiErrorUnprocessableEntity'
            requiredProperties:
              - status
              - error
              - code
              - error_details
        examples:
          example:
            value:
              status: 422
              error: Unprocessable entity
              code: validation_errors
              error_details: {}
        description: Unprocessable entity error
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

````