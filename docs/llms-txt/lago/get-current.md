# Source: https://getlago.com/docs/api-reference/customer-usage/get-current.md

# Retrieve current usage

> Retrieve real-time customer usage data for the current open billing period.

## OpenAPI

````yaml GET /customers/{external_customer_id}/current_usage
paths:
  path: /customers/{external_customer_id}/current_usage
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
        external_customer_id:
          schema:
            - type: string
              required: true
              description: >-
                The customer external unique identifier (provided by your own
                application).
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
      query:
        external_subscription_id:
          schema:
            - type: string
              required: true
              description: >-
                The unique identifier of the subscription within your
                application.
              example: sub_1234567890
          explode: true
        apply_taxes:
          schema:
            - type: boolean
              required: false
              description: >
                Optional flag to determine if taxes should be applied. Defaults
                to `true` if not provided or if null.
              default: true
              example: true
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              customer_usage:
                allOf:
                  - $ref: '#/components/schemas/CustomerUsageObject'
            refIdentifier: '#/components/schemas/CustomerUsage'
            requiredProperties:
              - customer_usage
        examples:
          example:
            value:
              customer_usage:
                from_datetime: '2022-07-01T00:00:00Z'
                to_datetime: '2022-07-31T23:59:59Z'
                issuing_date: '2022-08-01'
                lago_invoice_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                currency: EUR
                amount_cents: 123
                taxes_amount_cents: 200
                total_amount_cents: 123
                charges_usage:
                  - units: '1.0'
                    total_aggregated_units: '1.0'
                    events_count: 10
                    amount_cents: 123
                    amount_currency: EUR
                    pricing_unit_details:
                      amount_cents: 200
                      short_name: CR
                      conversion_rate: '0.5'
                    charge:
                      lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      charge_model: graduated
                      invoice_display_name: Setup
                    billable_metric:
                      lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      name: Storage
                      code: storage
                      aggregation_type: sum_agg
                    filters:
                      - units: '0.9'
                        total_aggregated_units: '1.0'
                        amount_cents: 1000
                        events_count: 10
                        invoice_display_name: AWS eu-east-1
                        pricing_unit_details:
                          amount_cents: 200
                          short_name: CR
                          conversion_rate: '0.5'
                        values: &ref_0
                          region:
                            - us-east-1
                    grouped_usage:
                      - amount_cents: 1000
                        events_count: 10
                        units: '0.9'
                        total_aggregated_units: '1.0'
                        pricing_unit_details:
                          amount_cents: 200
                          short_name: CR
                          conversion_rate: '0.5'
                        grouped_by: {}
                        filters:
                          - units: '0.9'
                            total_aggregated_units: '1.0'
                            amount_cents: 1000
                            events_count: 10
                            invoice_display_name: AWS eu-east-1
                            pricing_unit_details:
                              amount_cents: 200
                              short_name: CR
                              conversion_rate: '0.5'
                            values: *ref_0
        description: Customer usage
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
    UsagePricingUnitDetailsObject:
      type:
        - object
        - 'null'
      required:
        - amount_cents
        - short_name
        - conversion_rate
      description: Details about the pricing unit used for charge usage.
      properties:
        amount_cents:
          type: integer
          example: 200
          description: The amount in cents in the pricing unit.
        short_name:
          type: string
          example: CR
          description: The short name of the pricing unit.
        conversion_rate:
          type: string
          example: '0.5'
          description: The conversion rate from pricing units to the plan's currency.
    CustomerChargeFiltersUsageObject:
      type: array
      description: >-
        Array of filter object, representing multiple dimensions for a charge
        item.
      required:
        - values
        - units
        - total_aggregated_units
        - events_count
        - amount_cents
      items:
        type: object
        properties:
          units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '0.9'
            description: >-
              The number of units consumed for a specific charge filter related
              to a charge item.
          total_aggregated_units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '1.0'
            description: >-
              The total number of units consumed by the customer for a specific
              charge item, aggregated across all usage events.
          amount_cents:
            type: integer
            example: 1000
            description: >-
              The amount in cents, tax excluded, consumed for a specific charge
              filter related to a charge item.
          events_count:
            type: integer
            example: 10
            description: >-
              The quantity of usage events that have been recorded for a
              particular charge filter during the specified time period. These
              events may also be referred to as the number of transactions in
              some contexts.
          invoice_display_name:
            type: string
            description: Specifies the name that will be displayed on an invoice.
            example: AWS eu-east-1
          pricing_unit_details:
            $ref: '#/components/schemas/UsagePricingUnitDetailsObject'
          values:
            type: object
            description: List of filter values applied to the usage.
            additionalProperties:
              type: array
              items:
                type: string
            example:
              region:
                - us-east-1
    CustomerChargeGroupedUsageObject:
      type: array
      description: >-
        Array of aggregated fees, grouped by the event properties defined in a
        `standard` charge model.
      required:
        - amount_cents
        - events_count
        - units
        - total_aggregated_units
        - grouped_by
        - groups
      items:
        type: object
        properties:
          amount_cents:
            type: integer
            example: 1000
            description: >-
              The amount in cents, tax excluded, consumed for a specific group
              related to a charge item.
          events_count:
            type: integer
            example: 10
            description: >-
              The quantity of usage events that have been recorded for a
              particular charge during the specified time period. These events
              may also be referred to as the number of transactions in some
              contexts.
          units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '0.9'
            description: >-
              The number of units consumed for a specific group related to a
              charge item.
          total_aggregated_units:
            type: string
            pattern: ^[0-9]+.?[0-9]*$
            example: '1.0'
            description: >-
              The total number of units consumed by the customer for a specific
              charge item, aggregated across all usage events.
          pricing_unit_details:
            $ref: '#/components/schemas/UsagePricingUnitDetailsObject'
          grouped_by:
            type: object
            description: Key value list of event properties aggregated by the charge model
            additionalProperties:
              type: string
          filters:
            $ref: '#/components/schemas/CustomerChargeFiltersUsageObject'
    CustomerChargeUsageObject:
      type: object
      required:
        - units
        - total_aggregated_units
        - events_count
        - amount_cents
        - amount_currency
        - charge
        - billable_metric
        - groups
      properties:
        units:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          example: '1.0'
          description: >-
            The number of units consumed by the customer for a specific charge
            item.
        total_aggregated_units:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          example: '1.0'
          description: >-
            The total number of units consumed by the customer for a specific
            charge item, aggregated across all usage events.
        events_count:
          type: integer
          example: 10
          description: >-
            The quantity of usage events that have been recorded for a
            particular charge during the specified time period. These events may
            also be referred to as the number of transactions in some contexts.
        amount_cents:
          type: integer
          example: 123
          description: >-
            The amount in cents, tax excluded, consumed by the customer for a
            specific charge item.
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of a usage item consumed by the customer.
          example: EUR
        pricing_unit_details:
          $ref: '#/components/schemas/UsagePricingUnitDetailsObject'
        charge:
          type: object
          description: Object listing all the properties for a specific charge item.
          required:
            - lago_id
            - charge_model
          properties:
            lago_id:
              type: string
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              description: >-
                Unique identifier assigned to the charge within the Lago
                application. This ID is exclusively created by Lago and serves
                as a unique identifier for the charge's record within the Lago
                system.
            charge_model:
              type: string
              description: >-
                The pricing model applied to this charge. Possible values are
                standard, `graduated`, `percentage`, `package` or `volume`.
              enum:
                - standard
                - graduated
                - package
                - percentage
                - volume
              example: graduated
            invoice_display_name:
              type: string
              description: >-
                Specifies the name that will be displayed on an invoice. If no
                value is set for this field, the name of the actual charge will
                be used as the default display name.
              example: Setup
        billable_metric:
          type: object
          description: The related billable metric object.
          required:
            - lago_id
            - name
            - code
            - aggregation_type
          properties:
            lago_id:
              type: string
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              description: >-
                Unique identifier assigned to the billable metric within the
                Lago application. This ID is exclusively created by Lago and
                serves as a unique identifier for the billable metric's record
                within the Lago system.
            name:
              type: string
              example: Storage
              description: The name of the billable metric used for this charge.
            code:
              type: string
              example: storage
              description: The code of the billable metric used for this charge.
            aggregation_type:
              type: string
              description: >-
                The aggregation type of the billable metric used for this
                charge. Possible values are `count_agg`, `sum_agg`, `max_agg` or
                `unique_count_agg`.
              enum:
                - count_agg
                - sum_agg
                - max_agg
                - unique_count_agg
                - weighted_sum_agg
                - latest_agg
              example: sum_agg
        filters:
          $ref: '#/components/schemas/CustomerChargeFiltersUsageObject'
        grouped_usage:
          $ref: '#/components/schemas/CustomerChargeGroupedUsageObject'
    CustomerUsageObject:
      type: object
      required:
        - from_datetime
        - to_datetime
        - issuing_date
        - amount_cents
        - taxes_amount_cents
        - total_amount_cents
        - charges_usage
      properties:
        from_datetime:
          type: string
          format: date-time
          description: >-
            The lower bound of the billing period, expressed in the ISO 8601
            datetime format in Coordinated Universal Time (UTC).
          example: '2022-07-01T00:00:00Z'
        to_datetime:
          type: string
          format: date-time
          description: >-
            The upper bound of the billing period, expressed in the ISO 8601
            datetime format in Coordinated Universal Time (UTC).
          example: '2022-07-31T23:59:59Z'
        issuing_date:
          type: string
          format: date
          description: The date of creation of the invoice.
          example: '2022-08-01'
        lago_invoice_id:
          type:
            - string
            - 'null'
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            A unique identifier associated with the invoice related to this
            particular usage record.
        currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of the customer's current usage.
          example: EUR
        amount_cents:
          type: integer
          description: The amount in cents, tax excluded.
          example: 123
        taxes_amount_cents:
          type: integer
          description: The tax amount in cents.
          example: 200
        total_amount_cents:
          type: integer
          description: The total amount in cents, tax included.
          example: 123
        charges_usage:
          type: array
          description: >-
            Array of charges that comprise the current usage. It contains
            detailed information about individual charge items associated with
            the usage.
          items:
            $ref: '#/components/schemas/CustomerChargeUsageObject'

````