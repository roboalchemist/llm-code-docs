# Source: https://getlago.com/docs/guide/subscriptions/assign-plan.md

# Source: https://getlago.com/docs/api-reference/subscriptions/assign-plan.md

# Create a subscription

> This endpoint assigns a plan to a customer, creating or modifying a subscription. Ideal for initial subscriptions or plan changes (upgrades/downgrades).

## OpenAPI

````yaml POST /subscriptions
paths:
  path: /subscriptions
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
              authorization:
                allOf:
                  - type: object
                    description: >
                      Optionally, you can create a pre-authorization on the
                      customer's card before creating a subscription. This
                      process places a temporary hold (capture) for a specified
                      amount on the customer's account, but does not actually
                      withdraw the funds.


                      Important notes:
                        - The final amount due for the subscription is not known at the time of creation; it is determined only after the invoice is finalized.
                        - The payment intent generated for pre-authorization cannot be reused, as the final invoice amount may exceed the authorized amount.
                        - The payment intent is canceled immediately after creation, but this cancellation occurs asynchronously.
                        - For these reasons, it is recommended to use a small amount (such as $1) for pre-authorization. While this does not guarantee sufficient funds for the final payment, it helps reduce the likelihood of payment errors.
                    required:
                      - amount_cents
                      - amount_currency
                    properties:
                      amount_cents:
                        type: integer
                        example: 1000
                        description: The amount of the authorization in cents.
                      amount_currency:
                        type: string
                        example: USD
                        description: The currency of the authorization.
              subscription:
                allOf:
                  - type: object
                    required:
                      - external_customer_id
                      - plan_code
                      - external_id
                    properties:
                      billing_entity_code:
                        type: string
                        example: default
                        description: >-
                          The code of the billing entity to be used for the
                          subscription. If not provided, the default billing
                          entity will be used.
                      external_customer_id:
                        type: string
                        example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                        description: >-
                          The customer external unique identifier (provided by
                          your own application)
                      plan_code:
                        type: string
                        example: premium
                        description: >-
                          The unique code representing the plan to be attached
                          to the customer. This code must correspond to the
                          `code` property of one of the active plans.
                      name:
                        type: string
                        example: Repository A
                        description: >-
                          The display name of the subscription on an invoice.
                          This field allows for customization of the
                          subscription's name for billing purposes, especially
                          useful when a single customer has multiple
                          subscriptions using the same plan.
                      external_id:
                        type: string
                        example: my_sub_1234567890
                        description: >-
                          The unique external identifier for the subscription.
                          This identifier serves as an idempotency key, ensuring
                          that each subscription is unique.
                      billing_time:
                        type: string
                        description: >-
                          The billing time for the subscription, which can be
                          set as either `anniversary` or `calendar`. If not
                          explicitly provided, it will default to `calendar`.
                          The billing time determines the timing of recurring
                          billing cycles for the subscription. By specifying
                          `anniversary`, the billing cycle will be based on the
                          specific date the subscription started (billed fully),
                          while `calendar` sets the billing cycle at the first
                          day of the week/month/year (billed with proration).
                        example: anniversary
                        enum:
                          - calendar
                          - anniversary
                      ending_at:
                        type: string
                        format: date-time
                        example: '2022-10-08T00:00:00Z'
                        description: >-
                          The effective end date of the subscription. If this
                          field is set to null, the subscription will
                          automatically renew. This date should be provided in
                          ISO 8601 datetime format, and use Coordinated
                          Universal Time (UTC).
                      subscription_at:
                        type: string
                        format: date-time
                        example: '2022-08-08T00:00:00Z'
                        description: >-
                          The start date for the subscription, allowing for the
                          creation of subscriptions that can begin in the past
                          or future. Please note that it cannot be used to
                          update the start date of a pending subscription or
                          schedule an upgrade/downgrade. The start_date should
                          be provided in ISO 8601 datetime format and expressed
                          in Coordinated Universal Time (UTC).
                      plan_overrides:
                        $ref: '#/components/schemas/PlanOverridesObject'
            required: true
            refIdentifier: '#/components/schemas/SubscriptionCreateInput'
            requiredProperties:
              - subscription
        examples:
          example:
            value:
              authorization:
                amount_cents: 1000
                amount_currency: USD
              subscription:
                billing_entity_code: default
                external_customer_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                plan_code: premium
                name: Repository A
                external_id: my_sub_1234567890
                billing_time: anniversary
                ending_at: '2022-10-08T00:00:00Z'
                subscription_at: '2022-08-08T00:00:00Z'
                plan_overrides:
                  amount_cents: 10000
                  amount_currency: USD
                  description: Plan for early stage startups.
                  invoice_display_name: Startup plan
                  name: Startup
                  tax_codes: &ref_0
                    - french_standard_vat
                  trial_period: 5
                  minimum_commitment:
                    amount_cents: 100000
                    invoice_display_name: Minimum Commitment (C1)
                    tax_codes: *ref_0
                  charges:
                    - id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      charge_model: dynamic
                      invoice_display_name: Setup
                      min_amount_cents: 0
                      properties:
                        grouped_by: &ref_1
                          - agent_name
                        pricing_group_keys: &ref_2
                          - agent_name
                        graduated_ranges:
                          - {}
                        graduated_percentage_ranges:
                          - {}
                        amount: '30'
                        free_units: 100
                        package_size: 1000
                        rate: '1'
                        fixed_amount: '0.5'
                        free_units_per_events: 5
                        free_units_per_total_aggregation: '500'
                        per_transaction_max_amount: '3.75'
                        per_transaction_min_amount: '1.75'
                        volume_ranges:
                          - {}
                      filters:
                        - invoice_display_name: AWS
                          properties:
                            grouped_by: *ref_1
                            pricing_group_keys: *ref_2
                            graduated_ranges:
                              - {}
                            graduated_percentage_ranges:
                              - {}
                            amount: '30'
                            free_units: 100
                            package_size: 1000
                            rate: '1'
                            fixed_amount: '0.5'
                            free_units_per_events: 5
                            free_units_per_total_aggregation: '500'
                            per_transaction_max_amount: '3.75'
                            per_transaction_min_amount: '1.75'
                            volume_ranges:
                              - {}
                          values:
                            region:
                              - us-east-1
                      tax_codes: *ref_0
                      applied_pricing_unit:
                        conversion_rate: '0.5'
                  usage_thresholds:
                    - threshold_display_name: Threshold 1
                      amount_cents: 10000
                      recurring: true
        description: Subscription payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              subscription:
                allOf:
                  - $ref: '#/components/schemas/SubscriptionObjectExtended'
            refIdentifier: '#/components/schemas/Subscription'
            requiredProperties:
              - subscription
        examples:
          example:
            value:
              subscription:
                lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                external_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                lago_customer_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                external_customer_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                billing_time: anniversary
                name: Repository A
                plan_code: premium
                status: active
                created_at: '2022-08-08T00:00:00Z'
                canceled_at: '2022-09-14T16:35:31Z'
                started_at: '2022-08-08T00:00:00Z'
                ending_at: '2022-10-08T00:00:00Z'
                subscription_at: '2022-08-08T00:00:00Z'
                terminated_at: '2022-09-14T16:35:31Z'
                previous_plan_code: null
                next_plan_code: null
                downgrade_plan_date: '2022-04-30'
                trial_ended_at: '2022-08-08T00:00:00Z'
                current_billing_period_started_at: '2022-08-08T00:00:00Z'
                current_billing_period_ending_at: '2022-09-08T00:00:00Z'
                on_termination_credit_note: credit
                on_termination_invoice: generate
                plan:
                  lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  name: Startup
                  invoice_display_name: Startup plan
                  created_at: '2023-06-27T19:43:42Z'
                  code: startup
                  interval: monthly
                  description: ''
                  amount_cents: 10000
                  amount_currency: USD
                  trial_period: 5
                  pay_in_advance: true
                  bill_charges_monthly: null
                  minimum_commitment:
                    lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                    plan_code: premium
                    amount_cents: 100000
                    invoice_display_name: Minimum Commitment (C1)
                    interval: monthly
                    created_at: '2022-04-29T08:59:51Z'
                    updated_at: '2022-04-29T08:59:51Z'
                    taxes:
                      - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                        name: TVA
                        code: french_standard_vat
                        description: French standard VAT
                        rate: 20
                        applied_to_organization: true
                        created_at: '2023-07-06T14:35:58Z'
                  charges:
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a91
                      lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a91
                      billable_metric_code: requests
                      created_at: '2023-06-27T19:43:42Z'
                      charge_model: package
                      invoiceable: true
                      invoice_display_name: Setup
                      pay_in_advance: false
                      regroup_paid_fees: null
                      prorated: false
                      min_amount_cents: 3000
                      properties:
                        amount: '30'
                        free_units: 100
                        package_size: 1000
                      filters: []
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a92
                      lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a92
                      billable_metric_code: cpu
                      created_at: '2023-06-27T19:43:42Z'
                      charge_model: graduated
                      invoiceable: true
                      invoice_display_name: Setup
                      pay_in_advance: false
                      regroup_paid_fees: null
                      prorated: false
                      min_amount_cents: 0
                      properties:
                        graduated_ranges:
                          - from_value: 0
                            to_value: 10
                            flat_amount: '10'
                            per_unit_amount: '0.5'
                          - from_value: 11
                            to_value: null
                            flat_amount: '0'
                            per_unit_amount: '0.4'
                      filters: []
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a93
                      lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a93
                      billable_metric_code: seats
                      created_at: '2023-06-27T19:43:42Z'
                      charge_model: standard
                      invoiceable: true
                      invoice_display_name: Setup
                      pay_in_advance: true
                      regroup_paid_fees: null
                      prorated: false
                      min_amount_cents: 0
                      properties: {}
                      filters:
                        - invoice_display_name: Europe
                          properties:
                            amount: '10'
                          values:
                            region:
                              - Europe
                        - invoice_display_name: USA
                          properties:
                            amount: '5'
                          values:
                            region:
                              - USA
                        - invoice_display_name: Africa
                          properties:
                            amount: '8'
                          values:
                            region:
                              - Africa
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a94
                      lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a94
                      billable_metric_code: storage
                      created_at: '2023-06-27T19:43:42Z'
                      charge_model: volume
                      invoiceable: true
                      invoice_display_name: Setup
                      pay_in_advance: false
                      regroup_paid_fees: null
                      prorated: false
                      min_amount_cents: 0
                      properties:
                        volume_ranges:
                          - from_value: 0
                            to_value: 100
                            flat_amount: '0'
                            per_unit_amount: '0'
                          - from_value: 101
                            to_value: null
                            flat_amount: '0'
                            per_unit_amount: '0.5'
                      filters: []
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a95
                      lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a95
                      billable_metric_code: payments
                      created_at: '2023-06-27T19:43:42Z'
                      charge_model: percentage
                      invoiceable: false
                      invoice_display_name: Setup
                      pay_in_advance: true
                      regroup_paid_fees: invoice
                      prorated: false
                      min_amount_cents: 0
                      properties:
                        rate: '1'
                        fixed_amount: '0.5'
                        free_units_per_events: 5
                        free_units_per_total_aggregation: '500'
                      filters: []
                  taxes:
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      name: TVA
                      code: french_standard_vat
                      description: French standard VAT
                      rate: 20
                      applied_to_organization: true
                      created_at: '2023-07-06T14:35:58Z'
                  usage_thresholds:
                    - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      threshold_display_name: Threshold 1
                      amount_cents: 10000
                      recurring: true
                      created_at: '2023-06-27T19:43:42Z'
                      updated_at: '2023-06-27T19:43:42Z'
                  entitlements:
                    - entitlement:
                        code: seats
                        name: Number of seats
                        description: Number of users of the account
                        privileges:
                          - code: max
                            name: Maximum
                            value_type: integer
                            config: {}
                            value: 10
                          - code: max_admins
                            name: Max Admins
                            value_type: integer
                            config: {}
                            value: 5
                          - code: root
                            name: Allow root user
                            value_type: boolean
                            config: {}
                            value: true
                          - code: provider
                            name: SSO Provider
                            value_type: select
                            value: google
                            config:
                              select_options:
                                - google
                                - okta
        description: Subscription created
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
    FeaturePrivilegeObject:
      type: object
      required:
        - code
        - name
        - value_type
        - config
      properties:
        code:
          type: string
          example: max
          description: Unique code for the privilege.
        name:
          type:
            - string
            - 'null'
          example: Maximum
          description: Display name for the privilege.
        value_type:
          type: string
          enum:
            - integer
            - boolean
            - string
            - select
          example: integer
          description: 'Data type of the privilege value. Default: string'
        config:
          type: object
          properties:
            select_options:
              type: array
              items:
                type: string
              example:
                - google
                - okta
              description: Array of string, required only when value_type is `select`.
    UsageThresholdObject:
      type: object
      required:
        - lago_id
        - threshold_display_name
        - amount_cents
        - recurring
        - created_at
        - updated_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the usage threshold created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        threshold_display_name:
          type:
            - string
            - 'null'
          description: The display name of the usage threshold.
          example: Threshold 1
        amount_cents:
          type: integer
          description: The amount to reach to trigger a `progressive_billing` invoice.
          example: 10000
        recurring:
          type: boolean
          description: >-
            This field when set to `true` indicates that a `progressive_billing`
            invoice will be created every time the lifetime usage increases by
            the specified amount.
          example: true
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the usage threshold was created. It is
            expressed in UTC format according to the ISO 8601 datetime standard.
          example: '2023-06-27T19:43:42Z'
        updated_at:
          type: string
          format: date-time
          description: >-
            The date and time when the usage threshold was last updated. It is
            expressed in UTC format according to the ISO 8601 datetime standard.
          example: '2023-06-27T19:43:42Z'
    SubscriptionObject:
      type: object
      required:
        - billing_time
        - canceled_at
        - created_at
        - current_billing_period_ending_at
        - current_billing_period_started_at
        - downgrade_plan_date
        - ending_at
        - external_customer_id
        - external_id
        - lago_customer_id
        - lago_id
        - name
        - next_plan_code
        - on_termination_credit_note
        - on_termination_invoice
        - plan_code
        - previous_plan_code
        - started_at
        - status
        - subscription_at
        - terminated_at
        - trial_ended_at
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the subscription within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the subscription's record within the Lago
            system
        external_id:
          type: string
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          description: >-
            The subscription external unique identifier (provided by your own
            application).
        lago_customer_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the customer within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the customer's record within the Lago system
        external_customer_id:
          type: string
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          description: >-
            The customer external unique identifier (provided by your own
            application).
        billing_time:
          type: string
          description: >-
            The billing time for the subscription, which can be set as either
            `anniversary` or `calendar`. If not explicitly provided, it will
            default to `calendar`. The billing time determines the timing of
            recurring billing cycles for the subscription. By specifying
            `anniversary`, the billing cycle will be based on the specific date
            the subscription started (billed fully), while `calendar` sets the
            billing cycle at the first day of the week/month/year (billed with
            proration).
          example: anniversary
          enum:
            - calendar
            - anniversary
        name:
          type:
            - string
            - 'null'
          example: Repository A
          description: >-
            The display name of the subscription on an invoice. This field
            allows for customization of the subscription's name for billing
            purposes, especially useful when a single customer has multiple
            subscriptions using the same plan.
        plan_code:
          type: string
          example: premium
          description: >-
            The unique code representing the plan to be attached to the
            customer. This code must correspond to the `code` property of one of
            the active plans.
        status:
          type: string
          description: >-
            The status of the subscription, which can have the following values:

            - `active`: the subscription is currently active and applied to the
            customer.

            - `canceled`: the subscription has been stopped before its
            activation. This can occur when two consecutive downgrades have been
            applied to a customer or when a subscription with a pending status
            is terminated.

            - `pending`: a previous subscription has been downgraded, and the
            current one is awaiting automatic activation at the end of the
            billing period.

            - `terminated`: the subscription is no longer active.
          example: active
          enum:
            - active
            - canceled
            - pending
            - terminated
        created_at:
          type: string
          format: date-time
          example: '2022-08-08T00:00:00Z'
          description: >-
            The creation date of the subscription, represented in ISO 8601
            datetime format and expressed in Coordinated Universal Time (UTC).
            This date provides a timestamp indicating when the subscription was
            initially created.
        canceled_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-09-14T16:35:31Z'
          description: >-
            The cancellation date of the subscription. This field is not null
            when the subscription is `canceled`. This date should be provided in
            ISO 8601 datetime format and expressed in Coordinated Universal Time
            (UTC).
        started_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-08-08T00:00:00Z'
          description: >-
            The effective start date of the subscription. This field can be null
            if the subscription is `pending` or `canceled`. This date should be
            provided in ISO 8601 datetime format and expressed in Coordinated
            Universal Time (UTC).
        ending_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-10-08T00:00:00Z'
          description: >-
            The effective end date of the subscription. If this field is set to
            null, the subscription will automatically renew. This date should be
            provided in ISO 8601 datetime format, and use Coordinated Universal
            Time (UTC).
        subscription_at:
          type: string
          format: date-time
          example: '2022-08-08T00:00:00Z'
          description: >-
            The anniversary date and time of the initial subscription. This date
            serves as the basis for billing subscriptions with `anniversary`
            billing time. The `anniversary_date` should be provided in ISO 8601
            datetime format and expressed in Coordinated Universal Time (UTC).
        terminated_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-09-14T16:35:31Z'
          description: >-
            The termination date of the subscription. This field is not null
            when the subscription is `terminated`. This date should be provided
            in ISO 8601 datetime format and expressed in Coordinated Universal
            Time (UTC)
        previous_plan_code:
          type:
            - string
            - 'null'
          example: null
          description: >-
            The code identifying the previous plan associated with this
            subscription.
        next_plan_code:
          type:
            - string
            - 'null'
          example: null
          description: The code identifying the next plan in the case of a downgrade.
        downgrade_plan_date:
          type:
            - string
            - 'null'
          format: date
          example: '2022-04-30'
          description: >-
            The date when the plan will be downgraded, represented in ISO 8601
            date format.
        trial_ended_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-08-08T00:00:00Z'
          description: >-
            The date when the free trial is ended, represented in ISO 8601 date
            format.
        current_billing_period_started_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-08-08T00:00:00Z'
          description: >-
            The date and time when the current billing period started,
            represented in ISO 8601 date format.
        current_billing_period_ending_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-09-08T00:00:00Z'
          description: >-
            The date and time when the current billing period ends, represented
            in ISO 8601 date format.
        on_termination_credit_note:
          type:
            - string
            - 'null'
          description: >
            When a pay-in-advance subscription is terminated before the end of
            its billing period, we generate a credit note for the unused
            subscription time by default.

            This field allows you to control the behavior of the credit note
            generation:


            - `credit`: A credit note is generated for the unused subscription
            time. The unused amount is credited back to the customer.

            - `refund`: A credit note is generated for the unused subscription
            time. If the invoice is paid or partially paid, the unused paid
            amount is refunded; any unpaid unused amount is credited back to the
            customer.

            - `skip`: No credit note is generated for the unused subscription
            time.


            _Note: This field is only applicable to pay-in-advance plans and
            will be `null` for pay-in-arrears plans._
          example: credit
          enum:
            - credit
            - refund
            - skip
        on_termination_invoice:
          type:
            - string
          example: generate
          enum:
            - generate
            - skip
          default: generate
          description: >
            When a subscription is terminated before the end of its billing
            period, we generate an invoice for the unbilled usage.

            This field allows you to control the behavior of the invoice
            generation:


            - `generate`: An invoice is generated for the unbilled usage.

            - `skip`: No invoice is generated for the unbilled usage.
    MinimumCommitmentObject:
      type:
        - object
        - 'null'
      required:
        - lago_id
        - amount_cents
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the minimum commitment, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        plan_code:
          type: string
          example: premium
          description: >-
            The unique code representing the plan to be attached to the
            customer.
        amount_cents:
          type: integer
          description: The amount of the minimum commitment in cents.
          example: 100000
        invoice_display_name:
          type: string
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the default name will be used as the display
            name.
          example: Minimum Commitment (C1)
        interval:
          type: string
          description: >-
            The interval used for recurring billing. It represents the frequency
            at which subscription billing occurs. The interval can be one of the
            following values: `yearly`, `semiannual`, `quarterly`, `monthly` or
            `weekly`.
          enum:
            - weekly
            - monthly
            - quarterly
            - semiannual
            - yearly
          example: monthly
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the minimum commitment was created. It is
            expressed in UTC format according to the ISO 8601 datetime standard.
            This field provides the timestamp for the exact moment when the
            minimum commitment was initially created.
          example: '2022-04-29T08:59:51Z'
        updated_at:
          type: string
          format: date-time
          description: >-
            The date and time when the minimum commitment was updated. It is
            expressed in UTC format according to the ISO 8601 datetime standard.
            This field provides the timestamp for the exact moment when the
            minimum commitment was initially created.
          example: '2022-04-29T08:59:51Z'
        taxes:
          type: array
          description: All taxes applied to the minimum commitment.
          items:
            $ref: '#/components/schemas/TaxObject'
    ChargeModelEnum:
      type: string
      description: >
        Specifies the pricing model used for the calculation of the final fee.
        It can be any of the following values:
          - [`dynamic`](https://docs.getlago.com/guide/plans/charges/charge-models/dynamic)
          - [`graduated_percentage`](https://docs.getlago.com/guide/plans/charges/charge-models/graduated-percentage)
          - [`graduated`](https://docs.getlago.com/guide/plans/charges/charge-models/graduated)
          - [`package`](https://docs.getlago.com/guide/plans/charges/charge-models/package)
          - [`percentage`](https://docs.getlago.com/guide/plans/charges/charge-models/percentage)
          - [`standard`](https://docs.getlago.com/guide/plans/charges/charge-models/standard)
          - [`volume`](https://docs.getlago.com/guide/plans/charges/charge-models/volume)
      enum:
        - dynamic
        - graduated
        - graduated_percentage
        - package
        - percentage
        - standard
        - volume
    ChargeProperties:
      type: object
      properties:
        grouped_by:
          type: array
          description: >-
            The list of event properties that are used to group the events on
            the invoice for a `standard` charge model.

            **DEPRECATED** Replaced by `pricing_group_keys`.
          items:
            type: string
          example:
            - agent_name
          deprecated: true
        pricing_group_keys:
          type: array
          description: >-
            The list of event properties that are used to group the events on
            the invoice.
          items:
            type: string
          example:
            - agent_name
        graduated_ranges:
          type: array
          description: >-
            Graduated ranges, sorted from bottom to top tiers, used for a
            `graduated` charge model.
          items:
            type: object
            required:
              - from_value
              - to_value
              - flat_amount
              - per_unit_amount
            properties:
              from_value:
                type: integer
                description: >-
                  Specifies the lower value of a tier for a `graduated` charge
                  model. It must be either 0 or the previous range's `to_value +
                  1` to maintain the proper sequence of values.
                example: 0
              to_value:
                type:
                  - integer
                  - 'null'
                description: >-
                  Specifies the highest value of a tier for a `graduated` charge
                  model.

                  - This value must be higher than the from_value of the same
                  tier.

                  - This value must be null for the last tier.
                example: 10
              flat_amount:
                type: string
                pattern: ^[0-9]+.?[0-9]*$
                description: >-
                  The flat amount for a whole tier, excluding tax, for a
                  `graduated` charge model. It is expressed as a decimal value.
                example: '10'
              per_unit_amount:
                type: string
                pattern: ^[0-9]+.?[0-9]*$
                description: >-
                  The unit price, excluding tax, for a specific tier of a
                  `graduated` charge model. It is expressed as a decimal value.
                example: '0.5'
        graduated_percentage_ranges:
          type: array
          description: >-
            Graduated percentage ranges, sorted from bottom to top tiers, used
            for a `graduated_percentage` charge model.
          items:
            type: object
            required:
              - from_value
              - to_value
              - rate
              - flat_amount
            properties:
              from_value:
                type: integer
                description: >-
                  Specifies the lower value of a tier for a
                  `graduated_percentage` charge model. It must be either 0 or
                  the previous range's `to_value + 1` to maintain the proper
                  sequence of values.
                example: 0
              to_value:
                type:
                  - integer
                  - 'null'
                description: >-
                  Specifies the highest value of a tier for a
                  `graduated_percentage` charge model.

                  - This value must be higher than the from_value of the same
                  tier.

                  - This value must be null for the last tier.
                example: 10
              rate:
                type: string
                format: ^[0-9]+.?[0-9]*$
                description: >-
                  The percentage rate that is applied to the amount of each
                  transaction in the tier for a `graduated_percentage` charge
                  model. It is expressed as a decimal value.
                example: '1'
              flat_amount:
                type: string
                format: ^[0-9]+.?[0-9]*$
                description: >-
                  The flat amount for a whole tier, excluding tax, for a
                  `graduated_percentage` charge model. It is expressed as a
                  decimal value.
                example: '10'
        amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            - The unit price, excluding tax, for a `standard` charge model. It
            is expressed as a decimal value.

            - The amount, excluding tax, for a complete set of units in a
            `package` charge model. It is expressed as a decimal value.
          example: '30'
        free_units:
          type: integer
          description: >-
            The quantity of units that are provided free of charge for each
            billing period in a `package` charge model. This field specifies the
            number of units that customers can use without incurring any
            additional cost during each billing cycle.
          example: 100
        package_size:
          type: integer
          description: >-
            The quantity of units included in each pack or set for a `package`
            charge model. It indicates the number of units that are bundled
            together as a single package or set within the pricing structure.
          example: 1000
        rate:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            The percentage rate that is applied to the amount of each
            transaction for a `percentage` charge model. It is expressed as a
            decimal value.
          example: '1'
        fixed_amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            The fixed fee that is applied to each transaction for a `percentage`
            charge model. It is expressed as a decimal value.
          example: '0.5'
        free_units_per_events:
          type:
            - integer
            - 'null'
          description: >-
            The count of transactions that are not impacted by the `percentage`
            rate and fixed fee in a percentage charge model. This field
            indicates the number of transactions that are exempt from the
            calculation of charges based on the specified percentage rate and
            fixed fee.
          example: 5
        free_units_per_total_aggregation:
          type:
            - string
            - 'null'
          pattern: ^[0-9]+.?[0-9]*$
          description: >-
            The transaction amount that is not impacted by the `percentage` rate
            and fixed fee in a percentage charge model. This field indicates the
            portion of the transaction amount that is exempt from the
            calculation of charges based on the specified percentage rate and
            fixed fee.
          example: '500'
        per_transaction_max_amount:
          type:
            - string
            - 'null'
          format: ^[0-9]+.?[0-9]*$
          description: >-
            Specifies the maximum allowable spending for a single transaction.
            Working as a transaction cap.
          example: '3.75'
        per_transaction_min_amount:
          type:
            - string
            - 'null'
          format: ^[0-9]+.?[0-9]*$
          description: >-
            Specifies the minimum allowable spending for a single transaction.
            Working as a transaction floor.
          example: '1.75'
        volume_ranges:
          type: array
          description: >-
            Volume ranges, sorted from bottom to top tiers, used for a `volume`
            charge model.
          items:
            type: object
            required:
              - from_value
              - to_value
              - flat_amount
              - per_unit_amount
            properties:
              from_value:
                type: integer
                description: >-
                  Specifies the lower value of a tier for a `volume` charge
                  model. It must be either 0 or the previous range's `to_value +
                  1` to maintain the proper sequence of values.
                example: 0
              to_value:
                type:
                  - integer
                  - 'null'
                description: >-
                  Specifies the highest value of a tier for a `volume` charge
                  model.

                  - This value must be higher than the `from_value` of the same
                  tier.

                  - This value must be `null` for the last tier.
                example: 10
              flat_amount:
                type: string
                pattern: ^[0-9]+.?[0-9]*$
                description: >-
                  The flat amount for a whole tier, excluding tax, for a
                  `volume` charge model. It is expressed as a decimal value.
                example: '10'
              per_unit_amount:
                type: string
                pattern: ^[0-9]+.?[0-9]*$
                description: >-
                  The unit price, excluding tax, for a specific tier of a
                  `volume` charge model. It is expressed as a decimal value.
                example: '0.5'
    ChargeFilterObject:
      type: object
      description: >-
        Values used to apply differentiated pricing based on additional event
        properties.
      required:
        - invoice_display_name
        - properties
        - values
      properties:
        invoice_display_name:
          type:
            - string
            - 'null'
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the values of the filter will be used as the
            default display name.
          example: AWS
        properties:
          $ref: '#/components/schemas/ChargeProperties'
          description: List of all thresholds utilized for calculating the charge.
        values:
          type: object
          description: >-
            List of possible filter values. The key and values must match one of
            the billable metric filters.
          additionalProperties:
            type: array
            items:
              type: string
          example:
            region:
              - us-east-1
    ChargeObject:
      type: object
      required:
        - lago_id
        - lago_billable_metric_id
        - invoice_display_name
        - billable_metric_code
        - created_at
        - charge_model
        - invoiceable
        - regroup_paid_fees
        - pay_in_advance
        - prorated
        - min_amount_cents
        - properties
        - filters
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of charge, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_billable_metric_id:
          type: string
          format: uuid
          description: Unique identifier of the billable metric created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        billable_metric_code:
          type: string
          description: Unique code identifying a billable metric.
          example: requests
        invoice_display_name:
          type:
            - string
            - 'null'
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the name of the actual charge will be used as
            the default display name.
          example: Setup
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the charge was created. It is expressed in
            UTC format according to the ISO 8601 datetime standard.
          example: '2022-09-14T16:35:31Z'
        charge_model:
          $ref: '#/components/schemas/ChargeModelEnum'
        pay_in_advance:
          type: boolean
          description: >-
            This field determines the billing timing for this specific
            usage-based charge. When set to `true`, the charge is due and
            invoiced immediately. Conversely, when set to `false`, the charge is
            due and invoiced at the end of each billing period.
          example: true
        invoiceable:
          type: boolean
          description: >-
            This field specifies whether the charge should be included in a
            proper invoice. If set to `false`, no invoice will be issued for
            this charge. You can only set it to `false` when `pay_in_advance` is
            `true`.
          example: true
        regroup_paid_fees:
          type:
            - string
            - 'null'
          enum:
            - null
            - invoice
          description: >-
            This setting can only be configured if `pay_in_advance` is `true`
            and `invoiceable` is `false`.

            This field determines whether and when the charge fee should be
            included in

            the invoice. If `null`, no invoice will be issued for this charge
            fee.

            If `invoice`, an invoice will be generated at the end of the period,

            consolidating all charge fees with a succeeded payment status.
          example: invoice
        prorated:
          type: boolean
          example: false
          description: >-
            Specifies whether a charge is prorated based on the remaining number
            of days in the billing period or billed fully.


            - If set to `true`, the charge is prorated based on the remaining
            days in the current billing period.

            - If set to `false`, the charge is billed in full.

            - If not defined in the request, default value is `false`.
        min_amount_cents:
          type: integer
          description: >-
            The minimum spending amount required for the charge, measured in
            cents and excluding any applicable taxes. It indicates the minimum
            amount that needs to be charged for each billing period.
          example: 1200
        properties:
          $ref: '#/components/schemas/ChargeProperties'
          description: List of all thresholds utilized for calculating the charge.
        filters:
          type: array
          description: >-
            List of filters used to apply differentiated pricing based on
            additional event properties.
          items:
            $ref: '#/components/schemas/ChargeFilterObject'
        taxes:
          type: array
          description: All taxes applied to the charge.
          items:
            $ref: '#/components/schemas/TaxObject'
        applied_pricing_unit:
          type:
            - object
            - 'null'
          required:
            - code
            - conversion_rate
          description: The pricing unit applied to the charge.
          properties:
            code:
              type: string
              description: The code of the pricing unit.
              example: unit_code
            conversion_rate:
              type: string
              description: The conversion rate from pricing units to the plan's currency.
              example: '0.5'
    PlanEntitlementPrivilegeObject:
      allOf:
        - $ref: '#/components/schemas/FeaturePrivilegeObject'
        - type: object
          required:
            - value
          properties:
            value:
              oneOf:
                - type: integer
                  description: Value for integer type privileges
                - type: boolean
                  description: Value for boolean type privileges
                - type: string
                  description: Value for string or select type privileges
              example: 10
              description: >-
                Value assigned to this privilege in the entitlement. Type
                depends on the privilege's value_type.
    PlanEntitlementObject:
      type: object
      required:
        - code
        - name
        - description
        - privileges
      properties:
        code:
          type: string
          example: seats
          description: Unique code used to identify the feature. Max 255 characters.
        name:
          type:
            - string
            - 'null'
          example: Number of seats
          description: Name of the feature. Max 255 characters.
        description:
          type:
            - string
            - 'null'
          example: Number of users of the account
          description: Description of the feature. Max 600 characters.
        privileges:
          type: array
          items:
            $ref: '#/components/schemas/PlanEntitlementPrivilegeObject'
          example:
            - code: max
              name: Maximum
              value_type: integer
              config: {}
              value: 10
            - code: max_admins
              name: Max Admins
              value_type: integer
              config: {}
              value: 5
            - code: root
              name: Allow root user
              value_type: boolean
              config: {}
              value: true
            - code: provider
              name: SSO Provider
              value_type: select
              value: google
              config:
                select_options:
                  - google
                  - okta
          description: >-
            Privileges associated with this feature. Each privilege must have a
            value assigned.
    PlanEntitlement:
      type: object
      required:
        - entitlement
      properties:
        entitlement:
          $ref: '#/components/schemas/PlanEntitlementObject'
    PlanObject:
      type: object
      required:
        - lago_id
        - name
        - created_at
        - code
        - interval
        - amount_cents
        - amount_currency
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the plan created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        name:
          type: string
          description: The name of the plan.
          example: Startup
        invoice_display_name:
          type: string
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the name of the plan will be used as the
            default display name.
          example: Startup plan
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the plan was created. It is expressed in UTC
            format according to the ISO 8601 datetime standard. This field
            provides the timestamp for the exact moment when the plan was
            initially created.
          example: '2023-06-27T19:43:42Z'
        code:
          type: string
          description: >-
            The code of the plan. It serves as a unique identifier associated
            with a particular plan. The code is typically used for internal or
            system-level identification purposes, like assigning a subscription,
            for instance.
          example: startup
        interval:
          type: string
          description: >-
            The interval used for recurring billing. It represents the frequency
            at which subscription billing occurs. The interval can be one of the
            following values: `yearly`, `semiannual`, `quarterly`, `monthly` or
            `weekly`.
          enum:
            - weekly
            - monthly
            - quarterly
            - semiannual
            - yearly
          example: monthly
        description:
          type: string
          description: The description on the plan.
          example: ''
        amount_cents:
          type: integer
          description: >-
            The base cost of the plan, excluding any applicable taxes, that is
            billed on a recurring basis. This value is defined at 0 if your plan
            is a pay-as-you-go plan.
          example: 10000
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: >-
            The currency of the plan. It indicates the monetary unit in which
            the plan's cost, including taxes and usage-based charges, is
            expressed.
          example: USD
        trial_period:
          type: number
          description: >-
            The duration in days during which the base cost of the plan is
            offered for free.
          example: 5
        pay_in_advance:
          type: boolean
          description: >-
            This field determines the billing timing for the plan. When set to
            `true`, the base cost of the plan is due at the beginning of each
            billing period. Conversely, when set to `false`, the base cost of
            the plan is due at the end of each billing period.
          example: true
        bill_charges_monthly:
          type:
            - boolean
            - 'null'
          description: >-
            This field, when set to `true`, enables to invoice usage-based
            charges on monthly basis, even if the cadence of the plan is yearly
            or semiannual. This allows customers to pay charges overage on a
            monthly basis. This can be set to true only if the plan's interval
            is `yearly` or `semiannual`.
          example: null
        minimum_commitment:
          $ref: '#/components/schemas/MinimumCommitmentObject'
        charges:
          type: array
          items:
            $ref: '#/components/schemas/ChargeObject'
          description: Additional usage-based charges for this plan.
          example:
            - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a91
              lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a91
              billable_metric_code: requests
              created_at: '2023-06-27T19:43:42Z'
              charge_model: package
              invoiceable: true
              invoice_display_name: Setup
              pay_in_advance: false
              regroup_paid_fees: null
              prorated: false
              min_amount_cents: 3000
              properties:
                amount: '30'
                free_units: 100
                package_size: 1000
              filters: []
            - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a92
              lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a92
              billable_metric_code: cpu
              created_at: '2023-06-27T19:43:42Z'
              charge_model: graduated
              invoiceable: true
              invoice_display_name: Setup
              pay_in_advance: false
              regroup_paid_fees: null
              prorated: false
              min_amount_cents: 0
              properties:
                graduated_ranges:
                  - from_value: 0
                    to_value: 10
                    flat_amount: '10'
                    per_unit_amount: '0.5'
                  - from_value: 11
                    to_value: null
                    flat_amount: '0'
                    per_unit_amount: '0.4'
              filters: []
            - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a93
              lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a93
              billable_metric_code: seats
              created_at: '2023-06-27T19:43:42Z'
              charge_model: standard
              invoiceable: true
              invoice_display_name: Setup
              pay_in_advance: true
              regroup_paid_fees: null
              prorated: false
              min_amount_cents: 0
              properties: {}
              filters:
                - invoice_display_name: Europe
                  properties:
                    amount: '10'
                  values:
                    region:
                      - Europe
                - invoice_display_name: USA
                  properties:
                    amount: '5'
                  values:
                    region:
                      - USA
                - invoice_display_name: Africa
                  properties:
                    amount: '8'
                  values:
                    region:
                      - Africa
            - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a94
              lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a94
              billable_metric_code: storage
              created_at: '2023-06-27T19:43:42Z'
              charge_model: volume
              invoiceable: true
              invoice_display_name: Setup
              pay_in_advance: false
              regroup_paid_fees: null
              prorated: false
              min_amount_cents: 0
              properties:
                volume_ranges:
                  - from_value: 0
                    to_value: 100
                    flat_amount: '0'
                    per_unit_amount: '0'
                  - from_value: 101
                    to_value: null
                    flat_amount: '0'
                    per_unit_amount: '0.5'
              filters: []
            - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a95
              lago_billable_metric_id: 1a901a90-1a90-1a90-1a90-1a901a901a95
              billable_metric_code: payments
              created_at: '2023-06-27T19:43:42Z'
              charge_model: percentage
              invoiceable: false
              invoice_display_name: Setup
              pay_in_advance: true
              regroup_paid_fees: invoice
              prorated: false
              min_amount_cents: 0
              properties:
                rate: '1'
                fixed_amount: '0.5'
                free_units_per_events: 5
                free_units_per_total_aggregation: '500'
              filters: []
        taxes:
          type: array
          description: All taxes applied to the plan.
          items:
            $ref: '#/components/schemas/TaxObject'
        usage_thresholds:
          type: array
          description: List of usage thresholds applied to the plan.
          items:
            $ref: '#/components/schemas/UsageThresholdObject'
        entitlements:
          type: array
          description: >-
            List of all feature entitlements and their privileges available for
            this plan.
          items:
            $ref: '#/components/schemas/PlanEntitlement'
    MinimumCommitmentInput:
      type:
        - object
        - 'null'
      description: Minimum commitment for this plan.
      required:
        - amount_cents
      properties:
        amount_cents:
          type: integer
          description: The amount of the minimum commitment in cents.
          example: 100000
        invoice_display_name:
          type: string
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the default name will be used as the display
            name.
          example: Minimum Commitment (C1)
        tax_codes:
          $ref: '#/components/schemas/TaxCodes'
    ChargeFilterInput:
      type: object
      description: >-
        Values used to apply differentiated pricing based on additional event
        properties.
      required:
        - properties
        - values
      properties:
        invoice_display_name:
          type:
            - string
            - 'null'
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the values of the filter will be used as the
            default display name.
          example: AWS
        properties:
          $ref: '#/components/schemas/ChargeProperties'
          description: List of all thresholds utilized for calculating the charge.
        values:
          type: object
          description: >-
            List of possible filter values. The key and values must match one of
            the billable metric filters.
          additionalProperties:
            type: array
            items:
              type: string
          example:
            region:
              - us-east-1
    UsageThresholdInput:
      type: object
      required:
        - amount_cents
      properties:
        threshold_display_name:
          type:
            - string
            - 'null'
          description: The display name of the usage threshold.
          example: Threshold 1
        amount_cents:
          type: integer
          description: The amount to reach to trigger a `progressive_billing` invoice.
          example: 10000
        recurring:
          type: boolean
          description: >-
            This field when set to `true` indicates that a `progressive_billing`
            invoice will be created every time the lifetime usage increases by
            the specified amount.
          example: true
          default: false
    PlanOverridesObject:
      type: object
      description: Based plan overrides.
      properties:
        amount_cents:
          type: integer
          description: >-
            The base cost of the plan, excluding any applicable taxes, that is
            billed on a recurring basis. This value is defined at 0 if your plan
            is a pay-as-you-go plan.
          example: 10000
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: >-
            The currency of the plan. It indicates the monetary unit in which
            the plan's cost, including taxes and usage-based charges, is
            expressed.
          example: USD
        description:
          type: string
          description: The description on the plan.
          example: Plan for early stage startups.
        invoice_display_name:
          type: string
          example: Startup plan
          description: >-
            Specifies the name that will be displayed on an invoice. If no value
            is set for this field, the name of the plan will be used as the
            default display name.
        name:
          type: string
          example: Startup
          description: The name of the plan.
        tax_codes:
          $ref: '#/components/schemas/TaxCodes'
        trial_period:
          type: number
          description: >-
            The duration in days during which the base cost of the plan is
            offered for free.
          example: 5
        minimum_commitment:
          $ref: '#/components/schemas/MinimumCommitmentInput'
        charges:
          type: array
          description: Additional usage-based charges for this plan.
          items:
            type: object
            properties:
              id:
                type: string
                format: uuid
                description: Unique identifier of the charge created by Lago.
                example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              billable_metric_id:
                type: string
                format: uuid
                description: Unique identifier of the billable metric created by Lago.
                example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              charge_model:
                $ref: '#/components/schemas/ChargeModelEnum'
              invoice_display_name:
                type: string
                description: >-
                  Specifies the name that will be displayed on an invoice. If no
                  value is set for this field, the name of the actual charge
                  will be used as the default display name.
                example: Setup
              min_amount_cents:
                type: integer
                description: >-
                  The minimum spending amount required for the charge, measured
                  in cents and excluding any applicable taxes. It indicates the
                  minimum amount that needs to be charged for each billing
                  period.
                example: 0
              properties:
                $ref: '#/components/schemas/ChargeProperties'
                description: List of all thresholds utilized for calculating the charge.
              filters:
                type: array
                description: >-
                  List of filters used to apply differentiated pricing based on
                  additional event properties.
                items:
                  $ref: '#/components/schemas/ChargeFilterInput'
              tax_codes:
                $ref: '#/components/schemas/TaxCodes'
              applied_pricing_unit:
                type: object
                description: >-
                  Updates the pricing unit conversion rate for this charge. Only
                  applies if the charge has applied pricing unit.
                properties:
                  conversion_rate:
                    type: string
                    description: >-
                      The conversion rate from pricing units to the plan's
                      currency.

                      This rate determines how many currency units (in the
                      plan's base currency) equal one pricing unit.

                      For example, if the plan uses USD and the conversion rate
                      is 0.5, then 1 pricing unit = $0.50 USD.
                    example: '0.5'
        usage_thresholds:
          type: array
          description: List of usage thresholds applied to the subscription.
          items:
            $ref: '#/components/schemas/UsageThresholdInput'
    SubscriptionObjectExtended:
      allOf:
        - $ref: '#/components/schemas/SubscriptionObject'
        - type: object
          properties:
            plan:
              $ref: '#/components/schemas/PlanObject'

````