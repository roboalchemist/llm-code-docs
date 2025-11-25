# Source: https://getlago.com/docs/api-reference/webhook-endpoints/get-specific.md

# Source: https://getlago.com/docs/api-reference/wallets/get-specific.md

# Source: https://getlago.com/docs/api-reference/taxes/get-specific.md

# Source: https://getlago.com/docs/api-reference/subscriptions/get-specific.md

# Source: https://getlago.com/docs/api-reference/plans/get-specific.md

# Source: https://getlago.com/docs/api-reference/payments/get-specific.md

# Source: https://getlago.com/docs/api-reference/payment-receipts/get-specific.md

# Source: https://getlago.com/docs/api-reference/invoices/get-specific.md

# Source: https://getlago.com/docs/api-reference/events/get-specific.md

# Source: https://getlago.com/docs/api-reference/customers/get-specific.md

# Source: https://getlago.com/docs/api-reference/credit-notes/get-specific.md

# Source: https://getlago.com/docs/api-reference/coupons/get-specific.md

# Source: https://getlago.com/docs/api-reference/billing-entities/get-specific.md

# Source: https://getlago.com/docs/api-reference/billable-metrics/get-specific.md

# Source: https://getlago.com/docs/api-reference/alerts/get-specific.md

# Source: https://getlago.com/docs/api-reference/add-ons/get-specific.md

# Source: https://getlago.com/docs/api-reference/invoices/get-specific.md

# Source: https://getlago.com/docs/api-reference/events/get-specific.md

# Source: https://getlago.com/docs/api-reference/customers/get-specific.md

# Source: https://getlago.com/docs/api-reference/credit-notes/get-specific.md

# Source: https://getlago.com/docs/api-reference/coupons/get-specific.md

# Source: https://getlago.com/docs/api-reference/billing-entities/get-specific.md

# Source: https://getlago.com/docs/api-reference/billable-metrics/get-specific.md

# Source: https://getlago.com/docs/api-reference/alerts/get-specific.md

# Source: https://getlago.com/docs/api-reference/add-ons/get-specific.md

# Retrieve an add-on

> This endpoint is used to retrieve a specific add-on.

## OpenAPI

````yaml GET /add_ons/{code}
paths:
  path: /add_ons/{code}
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
      path:
        code:
          schema:
            - type: string
              required: true
              description: Unique code used to identify the add-on.
              example: setup_fee
      query: {}
      header: {}
      cookie: {}
    body: {}
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
        description: Add-on
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
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 404
              error:
                allOf:
                  - type: string
                    example: Not Found
              code:
                allOf:
                  - type: string
                    example: object_not_found
            refIdentifier: '#/components/schemas/ApiErrorNotFound'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 404
              error: Not Found
              code: object_not_found
        description: Not Found error
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

````