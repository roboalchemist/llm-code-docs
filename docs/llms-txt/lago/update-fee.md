# Source: https://getlago.com/docs/api-reference/fees/update-fee.md

# Update a fee

> This endpoint is used for updating a specific fee that has been issued.

## OpenAPI

````yaml PUT /fees/{lago_id}
paths:
  path: /fees/{lago_id}
  method: put
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
        lago_id:
          schema:
            - type: string
              required: true
              description: >-
                Unique identifier assigned to the fee within the Lago
                application. This ID is exclusively created by Lago and serves
                as a unique identifier for the fee's record within the Lago
                system.
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              fee:
                allOf:
                  - type: object
                    required:
                      - payment_status
                    properties:
                      payment_status:
                        type: string
                        enum:
                          - pending
                          - succeeded
                          - failed
                          - refunded
                        description: >-
                          The payment status of the fee. Possible values are
                          `pending`, `succeeded`, `failed` or `refunded`.
                        example: succeeded
            refIdentifier: '#/components/schemas/FeeUpdateInput'
            requiredProperties:
              - fee
        examples:
          example:
            value:
              fee:
                payment_status: succeeded
        description: Fee payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              fee:
                allOf:
                  - $ref: '#/components/schemas/FeeObject'
            refIdentifier: '#/components/schemas/Fee'
            requiredProperties:
              - fee
        examples:
          example:
            value:
              fee:
                lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_charge_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_charge_filter_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_invoice_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_true_up_fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_true_up_parent_fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_subscription_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_customer_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                external_customer_id: external_id
                external_subscription_id: external_id
                amount_cents: 100
                precise_amount: '1.0001'
                precise_total_amount: '1.0212'
                amount_currency: EUR
                taxes_amount_cents: 20
                taxes_precise_amount: '0.20123'
                taxes_rate: 20
                units: '0.32'
                precise_unit_amount: '312.5'
                total_aggregated_units: '0.32'
                total_amount_cents: 120
                total_amount_currency: EUR
                events_count: 23
                pay_in_advance: true
                invoiceable: true
                from_date: '2022-04-29T08:59:51Z'
                to_date: '2022-05-29T08:59:51Z'
                payment_status: pending
                created_at: '2022-08-24T14:58:59Z'
                succeeded_at: '2022-08-24T14:58:59Z'
                failed_at: '2022-08-24T14:58:59Z'
                refunded_at: '2022-08-24T14:58:59Z'
                event_transaction_id: transaction_1234567890
                description: Fee description
                precise_coupons_amount_cents: '0.0'
                amount_details:
                  plan_amount_cents: 10000
                  graduated_ranges:
                    - units: '10.0'
                      from_value: 0
                      to_value: 10
                      flat_unit_amount: '1.0'
                      per_unit_amount: '1.0'
                      per_unit_total_amount: '10.0'
                      total_with_flat_amount: '11.0'
                  graduated_percentage_ranges:
                    - units: '10.0'
                      from_value: 0
                      to_value: 10
                      flat_unit_amount: '1.0'
                      rate: '1.0'
                      per_unit_total_amount: '10.0'
                      total_with_flat_amount: '11.0'
                  free_units: '10.0'
                  paid_units: '40.0'
                  per_package_size: 1000
                  per_package_unit_amount: '0.5'
                  per_unit_total_amount: '10.0'
                  units: '20.0'
                  free_events: 10
                  rate: '1.0'
                  paid_events: 20
                  fixed_fee_unit_amount: '1.0'
                  fixed_fee_total_amount: '20.0'
                  min_max_adjustment_total_amount: '20.0'
                  per_unit_amount: '0.5'
                  flat_unit_amount: '10.0'
                self_billed: false
                item:
                  type: subscription
                  code: startup
                  name: Startup
                  description: Startup
                  invoice_display_name: Setup Fee (SF1)
                  filter_invoice_display_name: AWS eu-east-1
                  filters: {}
                  lago_item_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  item_type: Subscription
                  grouped_by: {}
                applied_taxes:
                  - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                    lago_tax_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                    tax_name: TVA
                    tax_code: french_standard_vat
                    tax_rate: 20
                    tax_description: French standard VAT
                    amount_cents: 2000
                    amount_currency: USD
                    created_at: '2022-09-14T16:35:31Z'
                    lago_fee_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                pricing_unit_details:
                  lago_pricing_unit_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  pricing_unit_code: credits
                  short_name: CR
                  amount_cents: 200
                  precise_amount_cents: '200.0'
                  unit_amount_cents: 100
                  precise_unit_amount: '100.0'
                  conversion_rate: '0.5'
        description: Fee updated
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
    '405':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 405
              error:
                allOf:
                  - type: string
                    example: Method Not Allowed
              code:
                allOf:
                  - type: string
                    example: not_allowed
            refIdentifier: '#/components/schemas/ApiErrorNotAllowed'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 405
              error: Method Not Allowed
              code: not_allowed
        description: Not Allowed error
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
    FeeAmountDetails:
      type: object
      properties:
        plan_amount_cents:
          type: integer
          description: >-
            The base cost of the plan, excluding any applicable taxes, that is
            billed on a recurring basis. This value is defined at 0 if your plan
            is a pay-as-you-go plan.
          example: 10000
        graduated_ranges:
          type: array
          description: Graduated ranges, used for a `graduated` charge model.
          items:
            type: object
            required:
              - units
              - from_value
              - to_value
              - flat_unit_amount
              - per_unit_amount
              - per_unit_total_amount
              - total_with_flat_amount
            properties:
              units:
                type: string
                pattern: ^[0-9]+.?[0-9]*$
                example: '10.0'
                description: Total units received in Lago.
              from_value:
                type: integer
                description: >-
                  Lower value of a tier. It is either 0 or the previous range's
                  `to_value + 1`.
                example: 0
              to_value:
                type:
                  - integer
                  - 'null'
                description: |-
                  Highest value of a tier.
                  - This value is higher than the from_value of the same tier.
                  - This value is null for the last tier.
                example: 10
              flat_unit_amount:
                type: string
                description: Flat unit amount within a specified tier.
                example: '1.0'
              per_unit_amount:
                type: string
                description: Amount per unit within a specified tier.
                example: '1.0'
              per_unit_total_amount:
                type: string
                description: >-
                  Total amount of received units to be charged within a
                  specified tier.
                example: '10.0'
              total_with_flat_amount:
                type: string
                description: >-
                  Total amount to be charged for a specific tier, taking into
                  account the flat_unit_amount and the per_unit_total_amount.
                example: '11.0'
        graduated_percentage_ranges:
          type: array
          description: >-
            Graduated percentage ranges, used for a `graduated_percentage`
            charge model.
          items:
            type: object
            required:
              - units
              - from_value
              - to_value
              - flat_unit_amount
              - rate
              - per_unit_total_amount
              - total_with_flat_amount
            properties:
              units:
                type: string
                pattern: ^[0-9]+.?[0-9]*$
                example: '10.0'
                description: Total units received in Lago.
              from_value:
                type: integer
                description: >-
                  Lower value of a tier. It is either 0 or the previous range's
                  `to_value + 1`.
                example: 0
              to_value:
                type:
                  - integer
                  - 'null'
                description: |-
                  Highest value of a tier.
                  - This value is higher than the from_value of the same tier.
                  - This value is null for the last tier.
                example: 10
              flat_unit_amount:
                type: string
                description: Flat unit amount within a specified tier.
                example: '1.0'
              rate:
                type: string
                format: ^[0-9]+.?[0-9]*$
                description: Percentage rate applied within a specified tier.
                example: '1.0'
              per_unit_total_amount:
                type: string
                description: >-
                  Total amount of received units to be charged within a
                  specified tier.
                example: '10.0'
              total_with_flat_amount:
                type: string
                description: >-
                  Total amount to be charged for a specific tier, taking into
                  account the flat_unit_amount and the per_unit_total_amount.
                example: '11.0'
        free_units:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          example: '10.0'
          description: >-
            The quantity of units that are provided free of charge for each
            billing period in a `package` charge model.
        paid_units:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          example: '40.0'
          description: >-
            The quantity of units that are not provided free of charge for each
            billing period in a `package` charge model.
        per_package_size:
          type: integer
          description: >-
            The quantity of units included, defined for Package or Percentage
            charge model.
          example: 1000
        per_package_unit_amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            Total amount to charge for received paid_units, defined for Package
            or Percentage charge model.
          example: '0.5'
        per_unit_total_amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            Total amount of received units to be charged for the Volume or
            Percentage charge model.
          example: '10.0'
        units:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          example: '20.0'
          description: The total units received in Lago for the Percentage charge model.
        free_events:
          type: integer
          example: 10
          description: Total number of free events allowed for the Percentage charge model.
        rate:
          type: string
          format: ^[0-9]+.?[0-9]*$
          description: Percentage rate applied for the Percentage charge model.
          example: '1.0'
        paid_events:
          type: integer
          example: 20
          description: Total number of paid events for the Percentage charge model.
        fixed_fee_unit_amount:
          type: string
          description: >-
            Fixed fee unit price per received paid_event for the Percentage
            charge model.
          example: '1.0'
        fixed_fee_total_amount:
          type: string
          description: >-
            Total amount to charge for received paid_events for the Percentage
            charge model.
          example: '20.0'
        min_max_adjustment_total_amount:
          type: string
          description: >-
            Total adjustment amount linked to minimum and maximum spending per
            transaction for the Percentage charge model.
          example: '20.0'
        per_unit_amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            The flat amount for a whole tier, excluding tax, for a `volume`
            charge model.
          example: '0.5'
        flat_unit_amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            The unit price, excluding tax, for a specific tier of a `volume`
            charge model.
          example: '10.0'
    BaseAppliedTax:
      type: object
      required:
        - lago_id
        - lago_tax_id
        - tax_name
        - tax_code
        - tax_rate
        - tax_description
        - amount_cents
        - amount_currency
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the applied tax, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_tax_id:
          type:
            - string
            - 'null'
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
            Unique code used to identify the tax associated with the API
            request.
          example: french_standard_vat
        tax_rate:
          type: number
          description: The percentage rate of the tax
          example: 20
        tax_description:
          type:
            - string
            - 'null'
          description: Internal description of the tax
          example: French standard VAT
        amount_cents:
          type: integer
          description: Amount of the tax
          example: 2000
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: Currency of the tax
          example: USD
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the applied tax was created. It is expressed
            in UTC format according to the ISO 8601 datetime standard. This
            field provides the timestamp for the exact moment when the applied
            tax was initially created.
          example: '2022-09-14T16:35:31Z'
    FeeAppliedTaxObject:
      allOf:
        - $ref: '#/components/schemas/BaseAppliedTax'
      type: object
      properties:
        lago_fee_id:
          type: string
          format: uuid
          description: Unique identifier of the fee, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
    PricingUnitDetailsObject:
      type: object
      required:
        - lago_pricing_unit_id
        - pricing_unit_code
        - short_name
        - amount_cents
        - precise_amount_cents
        - unit_amount_cents
        - precise_unit_amount
        - conversion_rate
      properties:
        lago_pricing_unit_id:
          type: string
          format: uuid
          description: Unique identifier of the pricing unit, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        pricing_unit_code:
          type: string
          description: The code of the pricing unit.
          example: credits
        short_name:
          type: string
          description: >-
            The short name of the pricing unit. Will be used as currency name in
            the UI and PDFs.
          example: CR
        amount_cents:
          type: integer
          description: The amount in cents in the pricing unit.
          example: 200
        precise_amount_cents:
          type: string
          description: The precise amount in cents in the pricing unit.
          example: '200.0'
        unit_amount_cents:
          type: integer
          description: The unit amount in cents in the pricing unit.
          example: 100
        precise_unit_amount:
          type: string
          description: The precise unit amount in the pricing unit.
          example: '100.0'
        conversion_rate:
          type: string
          description: The conversion rate from pricing units to the plan's currency.
          example: '0.5'
    FeeObject:
      type: object
      required:
        - item
        - amount_cents
        - amount_currency
        - taxes_amount_cents
        - taxes_rate
        - total_amount_cents
        - total_amount_currency
        - pay_in_advance
        - invoiceable
        - units
        - total_aggregated_units
        - precise_unit_amount
        - payment_status
      properties:
        lago_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the fee within the Lago application.
            This ID is exclusively created by Lago and serves as a unique
            identifier for the fee's record within the Lago system.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_charge_id:
          type:
            - string
            - 'null'
          format: uuid
          description: Unique identifier assigned to the charge that the fee belongs to
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_charge_filter_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the charge filter that the fee belongs
            to
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_invoice_id:
          type:
            - string
            - 'null'
          format: uuid
          description: Unique identifier assigned to the invoice that the fee belongs to
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_true_up_fee_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the true-up fee when a minimum has
            been set to the charge. This identifier helps to distinguish and
            manage the true-up fee associated with the charge, which may be
            applicable when a minimum threshold or limit is set for the charge
            amount.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_true_up_parent_fee_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the parent fee on which the true-up
            fee is assigned. This identifier establishes the relationship
            between the parent fee and the associated true-up fee.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_subscription_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the subscription, created by Lago.
            This field is specifically displayed when the fee type is charge or
            subscription.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_customer_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the customer, created by Lago. This
            field is specifically displayed when the fee type is charge or
            subscription.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        external_customer_id:
          type:
            - string
            - 'null'
          description: >-
            Unique identifier assigned to the customer in your application. This
            field is specifically displayed when the fee type is charge or
            subscription.
          example: external_id
        external_subscription_id:
          type:
            - string
            - 'null'
          description: >-
            Unique identifier assigned to the subscription in your application.
            This field is specifically displayed when the fee type is charge or
            subscription.
          example: external_id
        amount_cents:
          type: integer
          description: The cost of this specific fee, excluding any applicable taxes.
          example: 100
        precise_amount:
          type: string
          description: >-
            The cost of this specific fee, excluding any applicable taxes, with
            precision.
          example: '1.0001'
        precise_total_amount:
          type: string
          description: >-
            The cost of this specific fee, including any applicable taxes, with
            precision.
          example: '1.0212'
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: >-
            The currency of this specific fee. It indicates the monetary unit in
            which the fee's cost is expressed.
          example: EUR
        taxes_amount_cents:
          type: integer
          description: The cost of the tax associated with this specific fee.
          example: 20
        taxes_precise_amount:
          type: string
          description: >-
            The cost of the tax associated with this specific fee, with
            precision.
          example: '0.20123'
        taxes_rate:
          type: number
          description: The tax rate associated with this specific fee.
          example: 20
        units:
          type: string
          description: >-
            The number of units used to charge the customer. This field
            indicates the quantity or count of units consumed or utilized in the
            context of the charge. It helps in determining the basis for
            calculating the fee or cost associated with the usage of the service
            or product provided to the customer.
          example: '0.32'
        precise_unit_amount:
          type: string
          description: The unit amount of the fee per unit, with precision.
          example: '312.5'
        total_aggregated_units:
          type: string
          description: >-
            The total number of units that have been aggregated for this
            specific fee.
          example: '0.32'
        total_amount_cents:
          type: integer
          description: The cost of this specific fee, including any applicable taxes.
          example: 120
        total_amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of this specific fee, including any applicable taxes.
          example: EUR
        events_count:
          type:
            - integer
            - 'null'
          description: >-
            The number of events that have been sent and used to charge the
            customer. This field indicates the count or quantity of events that
            have been processed and considered in the charging process.
          example: 23
        pay_in_advance:
          type: boolean
          description: >-
            Flag that indicates whether the fee was paid in advance. It serves
            as a boolean value, where `true` represents that the fee was paid in
            advance (straightaway), and `false` indicates that the fee was not
            paid in arrears (at the end of the period).
          example: true
        invoiceable:
          type: boolean
          description: >-
            Flag that indicates whether the fee was included on the invoice. It
            serves as a boolean value, where `true` represents that the fee was
            included on the invoice, and `false` indicates that the fee was not
            included on the invoice.
          example: true
        from_date:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The beginning date of the period that the fee covers. It is
            applicable only to `subscription` and `charge` fees. This field
            indicates the start date of the billing period or subscription
            period associated with the fee.
          example: '2022-04-29T08:59:51Z'
        to_date:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The ending date of the period that the fee covers. It is applicable
            only to `subscription` and `charge` fees. This field indicates the
            end date of the billing period or subscription period associated
            with the fee.
          example: '2022-05-29T08:59:51Z'
        payment_status:
          type: string
          enum:
            - pending
            - succeeded
            - failed
            - refunded
          description: >-
            Indicates the payment status of the fee. It represents the current
            status of the payment associated with the fee. The possible values
            for this field are `pending`, `succeeded`, `failed` and `refunded`.
          example: pending
        created_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time when the fee was created. It is provided in
            Coordinated Universal Time (UTC) format.
          example: '2022-08-24T14:58:59Z'
        succeeded_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time when the payment for the fee was successfully
            processed. It is provided in Coordinated Universal Time (UTC)
            format.
          example: '2022-08-24T14:58:59Z'
        failed_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time when the payment for the fee failed to process. It
            is provided in Coordinated Universal Time (UTC) format.
          example: '2022-08-24T14:58:59Z'
        refunded_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time when the payment for the fee was refunded. It is
            provided in Coordinated Universal Time (UTC) format
          example: '2022-08-24T14:58:59Z'
        event_transaction_id:
          type:
            - string
            - 'null'
          description: >-
            Unique identifier assigned to the transaction. This field is
            specifically displayed when the fee type is `charge` and the payment
            for the fee is made in advance (`pay_in_advance` is set to `true`).
          example: transaction_1234567890
        description:
          type:
            - string
            - 'null'
          description: The description of the fee.
          example: Fee description
        precise_coupons_amount_cents:
          type: string
          description: The coupon amount applied to the fee, with precision.
          example: '0.0'
        amount_details:
          $ref: '#/components/schemas/FeeAmountDetails'
          description: List of all unit amount details for calculating the fee.
        self_billed:
          type: boolean
          example: false
          description: >-
            Indicates if the fee belongs to self-billed invoice. Self-billing is
            a process where an organization creates the invoice on behalf of the
            partner.
        item:
          type: object
          description: Item attached to the fee
          required:
            - type
            - code
            - name
            - lago_item_id
            - item_type
          properties:
            type:
              type: string
              enum:
                - charge
                - add_on
                - subscription
                - credit
                - commitment
              description: >-
                The fee type. Possible values are `add-on`, `charge`, `credit`,
                `subscription` or `commitment`.
              example: subscription
            code:
              type: string
              description: >-
                The code of the fee item. It can be the code of the `add-on`,
                the code of the `charge`, the code of the `credit` or the code
                of the `subscription`.
              example: startup
            name:
              type: string
              description: >
                The name of the fee item. The value depends on the type of the
                fee item:


                - If the fee item is a `charge`, it is the billable metric name.

                - If the fee item is a `add-on`, it is the add-on name.

                - If the fee item is a `credit`, it is the wallet transaction
                name if set, or `"credit"` if not.

                - If the fee item is a `fixed_charge`, it is the fixed charge
                add-on name.

                - For all the other fee items, it is the subscription plan name.
              example: Startup
            description:
              type:
                - string
                - 'null'
              description: >
                The description of the fee item. The value depends on the type
                of the fee item:


                - If the fee item is a `charge`, it is the billable metric
                description.

                - If the fee item is a `add-on`, it is the add-on description.

                - If the fee item is a `credit`, it is always `"credit"`.

                - If the fee item is a `fixed_charge`, it is the fixed charge
                add-on description.

                - For all the other fee items, it is the subscription plan
                description.
              example: Startup
            invoice_display_name:
              type: string
              description: >
                Specifies the name that will be displayed on an invoice. If no
                value is set for this field, we'll fallback to a value that
                depends on the type of the fee items:


                - If the fee item is a `charge`, we'll fallback to the
                `invoice_display_name` of the `charge` or the billable metric
                name if no `invoice_display_name` is set.

                - If the fee item is a `add-on`, we'll fallback to the
                `invoice_name` of the `add-on` or the `name` of the `add-on`.

                - If the fee item is a `credit`, we'll fallback to the wallet
                transaction name if set, or `credit` if not.

                - If the fee item is a `fixed_charge`, we'll fallback to the
                `invoice_display_name` of the `fixed_charge` or the
                `invoice_name` of the `fixed_charge_add_on` if no
                `invoice_display_name` is set.

                - For all the other fee items, we'll fallback to the
                `invoice_display_name` of the subscription plan.
              example: Setup Fee (SF1)
            filter_invoice_display_name:
              type:
                - string
                - 'null'
              description: >-
                Specifies the name that will be displayed on an invoice. If no
                value is set for this field, the actual charge filter values
                will be used as the default display name.
              example: AWS eu-east-1
            filters:
              type:
                - object
                - 'null'
              description: Key value list of event properties
              additionalProperties:
                type: array
                items:
                  type: string
            lago_item_id:
              type: string
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              description: >-
                Unique identifier of the fee item, created by Lago. It can be
                the identifier of the `add-on`, the `charge`, the `credit`, the
                `subscription` or the `commitment`.
              format: uuid
            item_type:
              type: string
              enum:
                - AddOn
                - BillableMetric
                - Subscription
                - WalletTransaction
              description: >-
                The type of the fee item. Possible values are `AddOn`,
                `BillableMetric`, `WalletTransaction`, `Subscription`.
              example: Subscription
            grouped_by:
              type: object
              description: >-
                Key value list of event properties aggregated by the charge
                model
              additionalProperties:
                type: string
        applied_taxes:
          type: array
          description: List of fee applied taxes
          items:
            $ref: '#/components/schemas/FeeAppliedTaxObject'
        pricing_unit_details:
          type:
            - object
            - 'null'
          description: Details about the pricing unit used and amounts for this fee.
          $ref: '#/components/schemas/PricingUnitDetailsObject'

````