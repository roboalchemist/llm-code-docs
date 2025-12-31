# Source: https://getlago.com/docs/api-reference/webhook-endpoints/create.md

# Source: https://getlago.com/docs/api-reference/wallets/create.md

# Source: https://getlago.com/docs/api-reference/taxes/create.md

# Source: https://getlago.com/docs/api-reference/plans/create.md

# Source: https://getlago.com/docs/api-reference/payments/create.md

# Source: https://getlago.com/docs/api-reference/payment-requests/create.md

# Source: https://getlago.com/docs/api-reference/customers/create.md

# Source: https://getlago.com/docs/api-reference/credit-notes/create.md

# Source: https://getlago.com/docs/api-reference/coupons/create.md

# Source: https://getlago.com/docs/api-reference/billing-entities/create.md

# Source: https://getlago.com/docs/api-reference/billable-metrics/create.md

# Source: https://getlago.com/docs/api-reference/alerts/create.md

# Source: https://getlago.com/docs/api-reference/add-ons/create.md

# Source: https://getlago.com/docs/api-reference/webhook-endpoints/create.md

# Source: https://getlago.com/docs/api-reference/wallets/create.md

# Source: https://getlago.com/docs/api-reference/taxes/create.md

# Source: https://getlago.com/docs/api-reference/plans/create.md

# Source: https://getlago.com/docs/api-reference/payments/create.md

# Source: https://getlago.com/docs/api-reference/payment-requests/create.md

# Source: https://getlago.com/docs/api-reference/customers/create.md

# Source: https://getlago.com/docs/api-reference/credit-notes/create.md

# Source: https://getlago.com/docs/api-reference/coupons/create.md

# Source: https://getlago.com/docs/api-reference/billing-entities/create.md

# Source: https://getlago.com/docs/api-reference/billable-metrics/create.md

# Source: https://getlago.com/docs/api-reference/alerts/create.md

# Source: https://getlago.com/docs/api-reference/add-ons/create.md

# Source: https://getlago.com/docs/api-reference/webhook-endpoints/create.md

# Source: https://getlago.com/docs/api-reference/wallets/create.md

# Source: https://getlago.com/docs/api-reference/taxes/create.md

# Source: https://getlago.com/docs/api-reference/plans/create.md

# Source: https://getlago.com/docs/api-reference/payments/create.md

# Source: https://getlago.com/docs/api-reference/payment-requests/create.md

# Source: https://getlago.com/docs/api-reference/customers/create.md

# Source: https://getlago.com/docs/api-reference/credit-notes/create.md

# Source: https://getlago.com/docs/api-reference/coupons/create.md

# Source: https://getlago.com/docs/api-reference/billing-entities/create.md

# Source: https://getlago.com/docs/api-reference/billable-metrics/create.md

# Source: https://getlago.com/docs/api-reference/alerts/create.md

# Source: https://getlago.com/docs/api-reference/add-ons/create.md

# Source: https://getlago.com/docs/api-reference/customers/create.md

# Source: https://getlago.com/docs/api-reference/credit-notes/create.md

# Source: https://getlago.com/docs/api-reference/coupons/create.md

# Source: https://getlago.com/docs/api-reference/billing-entities/create.md

# Source: https://getlago.com/docs/api-reference/billable-metrics/create.md

# Source: https://getlago.com/docs/api-reference/alerts/create.md

# Source: https://getlago.com/docs/api-reference/add-ons/create.md

# Create an add-on

> This endpoint is used to create an add-on that can be then attached to a one-off invoice.

## OpenAPI

````yaml POST /add_ons
paths:
  path: /add_ons
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
              add_on:
                allOf:
                  - $ref: '#/components/schemas/AddOnBaseInput'
                    required:
                      - name
                      - code
                      - amount_cents
                      - amount_currency
            required: true
            refIdentifier: '#/components/schemas/AddOnCreateInput'
            requiredProperties:
              - add_on
        examples:
          example:
            value:
              add_on:
                name: Setup Fee
                invoice_display_name: Setup Fee (SF1)
                code: setup_fee
                amount_cents: 50000
                amount_currency: USD
                description: Implementation fee for new customers.
                tax_codes:
                  - french_standard_vat
        description: Add-on payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              add_on:
                allOf:
                  - $ref: '#/components/schemas/AddOnObject'
            refIdentifier: '#/components/schemas/AddOn'
            requiredProperties:
              - add_on
        examples:
          example:
            value:
              add_on:
                lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                name: Setup Fee
                invoice_display_name: Setup Fee (SF1)
                code: setup_fee
                amount_cents: 50000
                amount_currency: USD
                description: Implementation fee for new customers.
                created_at: '2022-04-29T08:59:51Z'
                taxes:
                  - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                    name: TVA
                    code: french_standard_vat
                    description: French standard VAT
                    rate: 20
                    applied_to_organization: true
                    created_at: '2023-07-06T14:35:58Z'
        description: Add-on created
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
    TaxObject:
      type: object
      required:
        - lago_id
        - name
        - code
        - rate
        - applied_to_organization
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the tax, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        name:
          type: string
          description: Name of the tax.
          example: TVA
        code:
          type: string
          description: >-
            Unique code used to identify the tax associated with the API
            request.
          example: french_standard_vat
        description:
          type:
            - string
            - 'null'
          description: Internal description of the tax
          example: French standard VAT
        rate:
          type: number
          description: The percentage rate of the tax
          example: 20
        applied_to_organization:
          type: boolean
          deprecated: true
          description: >-
            This field is deprecated and will be removed in a future version.
            When set to true, it applies the tax to the organization's default
            billing entity. To apply or remove a tax from any billing entity
            (including the default one), please use the `PUT
            /billing_entities/:code` endpoint instead.
          example: true
        created_at:
          type: string
          format: date-time
          description: Creation date of the tax.
          example: '2023-07-06T14:35:58Z'
    TaxCodes:
      type: array
      items:
        type: string
      description: List of unique code used to identify the taxes.
      example:
        - french_standard_vat
    AddOnObject:
      type: object
      required:
        - lago_id
        - name
        - invoice_display_name
        - code
        - amount_cents
        - amount_currency
        - description
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the add-on, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        name:
          type: string
          description: The name of the add-on.
          example: Setup Fee
        invoice_display_name:
          type:
            - string
            - 'null'
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the name of the actual charge will be used as
            the default display name.
          example: Setup Fee (SF1)
        code:
          type: string
          description: Unique code used to identify the add-on.
          example: setup_fee
        amount_cents:
          type: integer
          description: >-
            The cost of the add-on in cents, excluding any applicable taxes,
            that is billed to a customer. By creating a one-off invoice, you
            will be able to override this value.
          example: 50000
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of the add-on.
          example: USD
        description:
          type:
            - string
            - 'null'
          description: The description of the add-on.
          example: Implementation fee for new customers.
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the add-on was created. It is expressed in
            UTC format according to the ISO 8601 datetime standard. This field
            provides the timestamp for the exact moment when the add-on was
            initially created.
          example: '2022-04-29T08:59:51Z'
        taxes:
          type: array
          description: All taxes applied to the add-on.
          items:
            $ref: '#/components/schemas/TaxObject'
    AddOnBaseInput:
      type: object
      properties:
        name:
          type: string
          description: The name of the add-on.
          example: Setup Fee
        invoice_display_name:
          type:
            - string
            - 'null'
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the name of the actual charge will be used as
            the default display name.
          example: Setup Fee (SF1)
        code:
          type: string
          description: Unique code used to identify the add-on.
          example: setup_fee
        amount_cents:
          type: integer
          description: >-
            The cost of the add-on in cents, excluding any applicable taxes,
            that is billed to a customer. By creating a one-off invoice, you
            will be able to override this value.
          example: 50000
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of the add-on.
          example: USD
        description:
          type:
            - string
            - 'null'
          description: The description of the add-on.
          example: Implementation fee for new customers.
        tax_codes:
          $ref: '#/components/schemas/TaxCodes'

````