# Source: https://polar.sh/docs/api-reference/orders/patch.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/patch.md

# Source: https://polar.sh/docs/api-reference/orders/patch.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/patch.md

# Update Order

> Update an order for the authenticated customer.

**Scopes**: `customer_portal:write`

## OpenAPI

````yaml patch /v1/customer-portal/orders/{id}
paths:
  path: /v1/customer-portal/orders/{id}
  method: patch
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: customer session
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Customer session tokens are specific tokens that are used to
                authenticate customers on your organization. You can create
                those sessions programmatically using the [Create Customer
                Session
                endpoint](/api-reference/customer-portal/sessions/create).
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              title: Id
              description: The order ID.
              format: uuid4
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              billing_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Billing Name
                    description: >-
                      The name of the customer that should appear on the
                      invoice. Can't be updated after the invoice is generated.
              billing_address:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AddressInput'
                      - type: 'null'
                    description: >-
                      The address of the customer that should appear on the
                      invoice. Can't be updated after the invoice is generated.
            required: true
            title: CustomerOrderUpdate
            description: Schema to update an order.
            refIdentifier: '#/components/schemas/CustomerOrderUpdate'
            requiredProperties:
              - billing_name
              - billing_address
        examples:
          example:
            value:
              billing_name: <string>
              billing_address:
                line1: <string>
                line2: <string>
                postal_code: <string>
                city: <string>
                state: <string>
                country: US
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"os\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.CustomerPortal.Orders.Update(ctx, operations.CustomerPortalOrdersUpdateSecurity{\n        CustomerSession: os.Getenv(\"POLAR_CUSTOMER_SESSION\"),\n    }, \"<value>\", components.CustomerOrderUpdate{\n        BillingName: polargo.Pointer(\"<value>\"),\n        BillingAddress: &components.AddressInput{\n            Country: components.CountryAlpha2InputUs,\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.CustomerOrder != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          import polar_sdk
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_portal.orders.update(security=polar_sdk.CustomerPortalOrdersUpdateSecurity(
                  customer_session="<YOUR_BEARER_TOKEN_HERE>",
              ), id="<value>", customer_order_update={
                  "billing_name": "<value>",
                  "billing_address": {
                      "country": polar_sdk.CountryAlpha2Input.US,
                  },
              })

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.customerPortal.orders.update({
              customerSession: process.env["POLAR_CUSTOMER_SESSION"] ?? "",
            }, {
              id: "<value>",
              customerOrderUpdate: {
                billingName: "<value>",
                billingAddress: {
                  country: "US",
                },
              },
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;
          use Polar\Models\Components;
          use Polar\Models\Operations;

          $sdk = Polar\Polar::builder()->build();

          $customerOrderUpdate = new Components\CustomerOrderUpdate(
              billingName: '<value>',
              billingAddress: new Components\AddressInput(
                  country: Components\CountryAlpha2Input::Us,
              ),
          );
          $requestSecurity = new Operations\CustomerPortalOrdersUpdateSecurity(
              customerSession: '<YOUR_BEARER_TOKEN_HERE>',
          );

          $response = $sdk->customerPortal->orders->update(
              security: $requestSecurity,
              id: '<value>',
              customerOrderUpdate: $customerOrderUpdate

          );

          if ($response->customerOrder !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the object.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              status:
                allOf:
                  - $ref: '#/components/schemas/OrderStatus'
                    examples:
                      - paid
              paid:
                allOf:
                  - type: boolean
                    title: Paid
                    description: Whether the order has been paid for.
                    examples:
                      - true
              subtotal_amount:
                allOf:
                  - type: integer
                    title: Subtotal Amount
                    description: Amount in cents, before discounts and taxes.
                    examples:
                      - 10000
              discount_amount:
                allOf:
                  - type: integer
                    title: Discount Amount
                    description: Discount amount in cents.
                    examples:
                      - 1000
              net_amount:
                allOf:
                  - type: integer
                    title: Net Amount
                    description: Amount in cents, after discounts but before taxes.
                    examples:
                      - 9000
              tax_amount:
                allOf:
                  - type: integer
                    title: Tax Amount
                    description: Sales tax amount in cents.
                    examples:
                      - 720
              total_amount:
                allOf:
                  - type: integer
                    title: Total Amount
                    description: Amount in cents, after discounts and taxes.
                    examples:
                      - 9720
              applied_balance_amount:
                allOf:
                  - type: integer
                    title: Applied Balance Amount
                    description: >-
                      Customer's balance amount applied to this invoice. Can
                      increase the total amount paid, if the customer has a
                      negative balance,  or decrease it, if the customer has a
                      positive balance.Amount in cents.
                    examples:
                      - 0
              due_amount:
                allOf:
                  - type: integer
                    title: Due Amount
                    description: Amount in cents that is due for this order.
                    examples:
                      - 0
              refunded_amount:
                allOf:
                  - type: integer
                    title: Refunded Amount
                    description: Amount refunded in cents.
                    examples:
                      - 0
              refunded_tax_amount:
                allOf:
                  - type: integer
                    title: Refunded Tax Amount
                    description: Sales tax refunded in cents.
                    examples:
                      - 0
              currency:
                allOf:
                  - type: string
                    title: Currency
                    examples:
                      - usd
              billing_reason:
                allOf:
                  - $ref: '#/components/schemas/OrderBillingReason'
              billing_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Billing Name
                    description: >-
                      The name of the customer that should appear on the
                      invoice. 
              billing_address:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/Address'
                      - type: 'null'
              invoice_number:
                allOf:
                  - type: string
                    title: Invoice Number
                    description: The invoice number associated with this order.
              is_invoice_generated:
                allOf:
                  - type: boolean
                    title: Is Invoice Generated
                    description: Whether an invoice has been generated for this order.
              seats:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Seats
                    description: >-
                      Number of seats purchased (for seat-based one-time
                      orders).
              customer_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Customer Id
              product_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Product Id
              discount_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Discount Id
              subscription_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Subscription Id
              checkout_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Checkout Id
              user_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: User Id
                    deprecated: true
              product:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/CustomerOrderProduct'
                      - type: 'null'
              subscription:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/CustomerOrderSubscription'
                      - type: 'null'
              items:
                allOf:
                  - items:
                      $ref: '#/components/schemas/OrderItemSchema'
                    type: array
                    title: Items
                    description: Line items composing the order.
              description:
                allOf:
                  - type: string
                    title: Description
                    description: A summary description of the order.
                    examples:
                      - Pro Plan
              next_payment_attempt_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Next Payment Attempt At
                    description: When the next payment retry is scheduled
            title: CustomerOrder
            refIdentifier: '#/components/schemas/CustomerOrder'
            requiredProperties:
              - id
              - created_at
              - modified_at
              - status
              - paid
              - subtotal_amount
              - discount_amount
              - net_amount
              - tax_amount
              - total_amount
              - applied_balance_amount
              - due_amount
              - refunded_amount
              - refunded_tax_amount
              - currency
              - billing_reason
              - billing_name
              - billing_address
              - invoice_number
              - is_invoice_generated
              - customer_id
              - product_id
              - discount_id
              - subscription_id
              - checkout_id
              - user_id
              - product
              - subscription
              - items
              - description
        examples:
          example:
            value:
              id: <string>
              created_at: '2023-11-07T05:31:56Z'
              modified_at: '2023-11-07T05:31:56Z'
              status: paid
              paid: true
              subtotal_amount: 10000
              discount_amount: 1000
              net_amount: 9000
              tax_amount: 720
              total_amount: 9720
              applied_balance_amount: 0
              due_amount: 0
              refunded_amount: 0
              refunded_tax_amount: 0
              currency: usd
              billing_reason: purchase
              billing_name: <string>
              billing_address:
                line1: <string>
                line2: <string>
                postal_code: <string>
                city: <string>
                state: <string>
                country: US
              invoice_number: <string>
              is_invoice_generated: true
              seats: 123
              customer_id: <string>
              product_id: <string>
              discount_id: <string>
              subscription_id: <string>
              checkout_id: <string>
              user_id: <string>
              product:
                id: <string>
                created_at: '2023-11-07T05:31:56Z'
                modified_at: '2023-11-07T05:31:56Z'
                trial_interval: day
                trial_interval_count: 123
                name: <string>
                description: <string>
                recurring_interval: day
                recurring_interval_count: 123
                is_recurring: true
                is_archived: true
                organization_id: <string>
                prices:
                  - created_at: '2023-11-07T05:31:56Z'
                    modified_at: '2023-11-07T05:31:56Z'
                    id: <string>
                    amount_type: <string>
                    is_archived: true
                    product_id: <string>
                    type: <string>
                    recurring_interval: day
                    price_currency: <string>
                    price_amount: 123
                    legacy: true
                benefits:
                  - id: <string>
                    created_at: '2023-11-07T05:31:56Z'
                    modified_at: '2023-11-07T05:31:56Z'
                    type: custom
                    description: <string>
                    selectable: true
                    deletable: true
                    organization_id: <string>
                medias:
                  - id: <string>
                    organization_id: <string>
                    name: <string>
                    path: <string>
                    mime_type: <string>
                    size: 123
                    storage_version: <string>
                    checksum_etag: <string>
                    checksum_sha256_base64: <string>
                    checksum_sha256_hex: <string>
                    last_modified_at: '2023-11-07T05:31:56Z'
                    version: <string>
                    service: <string>
                    is_uploaded: true
                    created_at: '2023-11-07T05:31:56Z'
                    size_readable: <string>
                    public_url: <string>
                organization:
                  created_at: '2023-11-07T05:31:56Z'
                  modified_at: '2023-11-07T05:31:56Z'
                  id: 1dbfc517-0bbf-4301-9ba8-555ca42b9737
                  name: <string>
                  slug: <string>
                  avatar_url: <string>
                  email: <string>
                  website: <string>
                  socials:
                    - platform: x
                      url: <string>
                  status: created
                  details_submitted_at: '2023-11-07T05:31:56Z'
                  feature_settings:
                    issue_funding_enabled: false
                    seat_based_pricing_enabled: false
                    revops_enabled: false
                  subscription_settings:
                    allow_multiple_subscriptions: true
                    allow_customer_updates: true
                    proration_behavior: invoice
                  notification_settings:
                    new_order: true
                    new_subscription: true
                  customer_email_settings:
                    order_confirmation: true
                    subscription_cancellation: true
                    subscription_confirmation: true
                    subscription_cycled: true
                    subscription_past_due: true
                    subscription_revoked: true
                    subscription_uncanceled: true
                    subscription_updated: true
              subscription:
                created_at: '2023-11-07T05:31:56Z'
                modified_at: '2023-11-07T05:31:56Z'
                id: <string>
                amount: 10000
                currency: usd
                recurring_interval: month
                recurring_interval_count: 123
                status: active
                current_period_start: '2023-11-07T05:31:56Z'
                current_period_end: '2023-11-07T05:31:56Z'
                trial_start: '2023-11-07T05:31:56Z'
                trial_end: '2023-11-07T05:31:56Z'
                cancel_at_period_end: true
                canceled_at: '2023-11-07T05:31:56Z'
                started_at: '2023-11-07T05:31:56Z'
                ends_at: '2023-11-07T05:31:56Z'
                ended_at: '2023-11-07T05:31:56Z'
                customer_id: <string>
                product_id: <string>
                discount_id: <string>
                checkout_id: <string>
                seats: 123
                customer_cancellation_reason: customer_service
                customer_cancellation_comment: <string>
              items:
                - created_at: '2023-11-07T05:31:56Z'
                  modified_at: '2023-11-07T05:31:56Z'
                  id: <string>
                  label: Pro Plan
                  amount: 10000
                  tax_amount: 720
                  proration: false
                  product_price_id: <string>
              description: Pro Plan
              next_payment_attempt_at: '2023-11-07T05:31:56Z'
        description: Successful Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: ResourceNotFound
                    title: Error
                    examples:
                      - ResourceNotFound
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: ResourceNotFound
            refIdentifier: '#/components/schemas/ResourceNotFound'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: ResourceNotFound
              detail: <string>
        description: Order not found.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    Address:
      properties:
        line1:
          anyOf:
            - type: string
            - type: 'null'
          title: Line1
        line2:
          anyOf:
            - type: string
            - type: 'null'
          title: Line2
        postal_code:
          anyOf:
            - type: string
            - type: 'null'
          title: Postal Code
        city:
          anyOf:
            - type: string
            - type: 'null'
          title: City
        state:
          anyOf:
            - type: string
            - type: 'null'
          title: State
        country:
          type: string
          enum:
            - AD
            - AE
            - AF
            - AG
            - AI
            - AL
            - AM
            - AO
            - AQ
            - AR
            - AS
            - AT
            - AU
            - AW
            - AX
            - AZ
            - BA
            - BB
            - BD
            - BE
            - BF
            - BG
            - BH
            - BI
            - BJ
            - BL
            - BM
            - BN
            - BO
            - BQ
            - BR
            - BS
            - BT
            - BV
            - BW
            - BY
            - BZ
            - CA
            - CC
            - CD
            - CF
            - CG
            - CH
            - CI
            - CK
            - CL
            - CM
            - CN
            - CO
            - CR
            - CU
            - CV
            - CW
            - CX
            - CY
            - CZ
            - DE
            - DJ
            - DK
            - DM
            - DO
            - DZ
            - EC
            - EE
            - EG
            - EH
            - ER
            - ES
            - ET
            - FI
            - FJ
            - FK
            - FM
            - FO
            - FR
            - GA
            - GB
            - GD
            - GE
            - GF
            - GG
            - GH
            - GI
            - GL
            - GM
            - GN
            - GP
            - GQ
            - GR
            - GS
            - GT
            - GU
            - GW
            - GY
            - HK
            - HM
            - HN
            - HR
            - HT
            - HU
            - ID
            - IE
            - IL
            - IM
            - IN
            - IO
            - IQ
            - IR
            - IS
            - IT
            - JE
            - JM
            - JO
            - JP
            - KE
            - KG
            - KH
            - KI
            - KM
            - KN
            - KP
            - KR
            - KW
            - KY
            - KZ
            - LA
            - LB
            - LC
            - LI
            - LK
            - LR
            - LS
            - LT
            - LU
            - LV
            - LY
            - MA
            - MC
            - MD
            - ME
            - MF
            - MG
            - MH
            - MK
            - ML
            - MM
            - MN
            - MO
            - MP
            - MQ
            - MR
            - MS
            - MT
            - MU
            - MV
            - MW
            - MX
            - MY
            - MZ
            - NA
            - NC
            - NE
            - NF
            - NG
            - NI
            - NL
            - 'NO'
            - NP
            - NR
            - NU
            - NZ
            - OM
            - PA
            - PE
            - PF
            - PG
            - PH
            - PK
            - PL
            - PM
            - PN
            - PR
            - PS
            - PT
            - PW
            - PY
            - QA
            - RE
            - RO
            - RS
            - RU
            - RW
            - SA
            - SB
            - SC
            - SD
            - SE
            - SG
            - SH
            - SI
            - SJ
            - SK
            - SL
            - SM
            - SN
            - SO
            - SR
            - SS
            - ST
            - SV
            - SX
            - SY
            - SZ
            - TC
            - TD
            - TF
            - TG
            - TH
            - TJ
            - TK
            - TL
            - TM
            - TN
            - TO
            - TR
            - TT
            - TV
            - TW
            - TZ
            - UA
            - UG
            - UM
            - US
            - UY
            - UZ
            - VA
            - VC
            - VE
            - VG
            - VI
            - VN
            - VU
            - WF
            - WS
            - YE
            - YT
            - ZA
            - ZM
            - ZW
          title: CountryAlpha2
          examples:
            - US
            - SE
            - FR
          x-speakeasy-enums:
            - AD
            - AE
            - AF
            - AG
            - AI
            - AL
            - AM
            - AO
            - AQ
            - AR
            - AS
            - AT
            - AU
            - AW
            - AX
            - AZ
            - BA
            - BB
            - BD
            - BE
            - BF
            - BG
            - BH
            - BI
            - BJ
            - BL
            - BM
            - BN
            - BO
            - BQ
            - BR
            - BS
            - BT
            - BV
            - BW
            - BY
            - BZ
            - CA
            - CC
            - CD
            - CF
            - CG
            - CH
            - CI
            - CK
            - CL
            - CM
            - CN
            - CO
            - CR
            - CU
            - CV
            - CW
            - CX
            - CY
            - CZ
            - DE
            - DJ
            - DK
            - DM
            - DO
            - DZ
            - EC
            - EE
            - EG
            - EH
            - ER
            - ES
            - ET
            - FI
            - FJ
            - FK
            - FM
            - FO
            - FR
            - GA
            - GB
            - GD
            - GE
            - GF
            - GG
            - GH
            - GI
            - GL
            - GM
            - GN
            - GP
            - GQ
            - GR
            - GS
            - GT
            - GU
            - GW
            - GY
            - HK
            - HM
            - HN
            - HR
            - HT
            - HU
            - ID
            - IE
            - IL
            - IM
            - IN
            - IO
            - IQ
            - IR
            - IS
            - IT
            - JE
            - JM
            - JO
            - JP
            - KE
            - KG
            - KH
            - KI
            - KM
            - KN
            - KP
            - KR
            - KW
            - KY
            - KZ
            - LA
            - LB
            - LC
            - LI
            - LK
            - LR
            - LS
            - LT
            - LU
            - LV
            - LY
            - MA
            - MC
            - MD
            - ME
            - MF
            - MG
            - MH
            - MK
            - ML
            - MM
            - MN
            - MO
            - MP
            - MQ
            - MR
            - MS
            - MT
            - MU
            - MV
            - MW
            - MX
            - MY
            - MZ
            - NA
            - NC
            - NE
            - NF
            - NG
            - NI
            - NL
            - 'NO'
            - NP
            - NR
            - NU
            - NZ
            - OM
            - PA
            - PE
            - PF
            - PG
            - PH
            - PK
            - PL
            - PM
            - PN
            - PR
            - PS
            - PT
            - PW
            - PY
            - QA
            - RE
            - RO
            - RS
            - RU
            - RW
            - SA
            - SB
            - SC
            - SD
            - SE
            - SG
            - SH
            - SI
            - SJ
            - SK
            - SL
            - SM
            - SN
            - SO
            - SR
            - SS
            - ST
            - SV
            - SX
            - SY
            - SZ
            - TC
            - TD
            - TF
            - TG
            - TH
            - TJ
            - TK
            - TL
            - TM
            - TN
            - TO
            - TR
            - TT
            - TV
            - TW
            - TZ
            - UA
            - UG
            - UM
            - US
            - UY
            - UZ
            - VA
            - VC
            - VE
            - VG
            - VI
            - VN
            - VU
            - WF
            - WS
            - YE
            - YT
            - ZA
            - ZM
            - ZW
      type: object
      required:
        - country
      title: Address
    AddressInput:
      properties:
        line1:
          anyOf:
            - type: string
            - type: 'null'
          title: Line1
        line2:
          anyOf:
            - type: string
            - type: 'null'
          title: Line2
        postal_code:
          anyOf:
            - type: string
            - type: 'null'
          title: Postal Code
        city:
          anyOf:
            - type: string
            - type: 'null'
          title: City
        state:
          anyOf:
            - type: string
            - type: 'null'
          title: State
        country:
          type: string
          enum:
            - AD
            - AE
            - AF
            - AG
            - AI
            - AL
            - AM
            - AO
            - AQ
            - AR
            - AS
            - AT
            - AU
            - AW
            - AX
            - AZ
            - BA
            - BB
            - BD
            - BE
            - BF
            - BG
            - BH
            - BI
            - BJ
            - BL
            - BM
            - BN
            - BO
            - BQ
            - BR
            - BS
            - BT
            - BV
            - BW
            - BY
            - BZ
            - CA
            - CC
            - CD
            - CF
            - CG
            - CH
            - CI
            - CK
            - CL
            - CM
            - CN
            - CO
            - CR
            - CV
            - CW
            - CX
            - CY
            - CZ
            - DE
            - DJ
            - DK
            - DM
            - DO
            - DZ
            - EC
            - EE
            - EG
            - EH
            - ER
            - ES
            - ET
            - FI
            - FJ
            - FK
            - FM
            - FO
            - FR
            - GA
            - GB
            - GD
            - GE
            - GF
            - GG
            - GH
            - GI
            - GL
            - GM
            - GN
            - GP
            - GQ
            - GR
            - GS
            - GT
            - GU
            - GW
            - GY
            - HK
            - HM
            - HN
            - HR
            - HT
            - HU
            - ID
            - IE
            - IL
            - IM
            - IN
            - IO
            - IQ
            - IS
            - IT
            - JE
            - JM
            - JO
            - JP
            - KE
            - KG
            - KH
            - KI
            - KM
            - KN
            - KR
            - KW
            - KY
            - KZ
            - LA
            - LB
            - LC
            - LI
            - LK
            - LR
            - LS
            - LT
            - LU
            - LV
            - LY
            - MA
            - MC
            - MD
            - ME
            - MF
            - MG
            - MH
            - MK
            - ML
            - MM
            - MN
            - MO
            - MP
            - MQ
            - MR
            - MS
            - MT
            - MU
            - MV
            - MW
            - MX
            - MY
            - MZ
            - NA
            - NC
            - NE
            - NF
            - NG
            - NI
            - NL
            - 'NO'
            - NP
            - NR
            - NU
            - NZ
            - OM
            - PA
            - PE
            - PF
            - PG
            - PH
            - PK
            - PL
            - PM
            - PN
            - PR
            - PS
            - PT
            - PW
            - PY
            - QA
            - RE
            - RO
            - RS
            - RW
            - SA
            - SB
            - SC
            - SD
            - SE
            - SG
            - SH
            - SI
            - SJ
            - SK
            - SL
            - SM
            - SN
            - SO
            - SR
            - SS
            - ST
            - SV
            - SX
            - SZ
            - TC
            - TD
            - TF
            - TG
            - TH
            - TJ
            - TK
            - TL
            - TM
            - TN
            - TO
            - TR
            - TT
            - TV
            - TW
            - TZ
            - UA
            - UG
            - UM
            - US
            - UY
            - UZ
            - VA
            - VC
            - VE
            - VG
            - VI
            - VN
            - VU
            - WF
            - WS
            - YE
            - YT
            - ZA
            - ZM
            - ZW
          title: CountryAlpha2Input
          examples:
            - US
            - SE
            - FR
          x-speakeasy-enums:
            - AD
            - AE
            - AF
            - AG
            - AI
            - AL
            - AM
            - AO
            - AQ
            - AR
            - AS
            - AT
            - AU
            - AW
            - AX
            - AZ
            - BA
            - BB
            - BD
            - BE
            - BF
            - BG
            - BH
            - BI
            - BJ
            - BL
            - BM
            - BN
            - BO
            - BQ
            - BR
            - BS
            - BT
            - BV
            - BW
            - BY
            - BZ
            - CA
            - CC
            - CD
            - CF
            - CG
            - CH
            - CI
            - CK
            - CL
            - CM
            - CN
            - CO
            - CR
            - CV
            - CW
            - CX
            - CY
            - CZ
            - DE
            - DJ
            - DK
            - DM
            - DO
            - DZ
            - EC
            - EE
            - EG
            - EH
            - ER
            - ES
            - ET
            - FI
            - FJ
            - FK
            - FM
            - FO
            - FR
            - GA
            - GB
            - GD
            - GE
            - GF
            - GG
            - GH
            - GI
            - GL
            - GM
            - GN
            - GP
            - GQ
            - GR
            - GS
            - GT
            - GU
            - GW
            - GY
            - HK
            - HM
            - HN
            - HR
            - HT
            - HU
            - ID
            - IE
            - IL
            - IM
            - IN
            - IO
            - IQ
            - IS
            - IT
            - JE
            - JM
            - JO
            - JP
            - KE
            - KG
            - KH
            - KI
            - KM
            - KN
            - KR
            - KW
            - KY
            - KZ
            - LA
            - LB
            - LC
            - LI
            - LK
            - LR
            - LS
            - LT
            - LU
            - LV
            - LY
            - MA
            - MC
            - MD
            - ME
            - MF
            - MG
            - MH
            - MK
            - ML
            - MM
            - MN
            - MO
            - MP
            - MQ
            - MR
            - MS
            - MT
            - MU
            - MV
            - MW
            - MX
            - MY
            - MZ
            - NA
            - NC
            - NE
            - NF
            - NG
            - NI
            - NL
            - 'NO'
            - NP
            - NR
            - NU
            - NZ
            - OM
            - PA
            - PE
            - PF
            - PG
            - PH
            - PK
            - PL
            - PM
            - PN
            - PR
            - PS
            - PT
            - PW
            - PY
            - QA
            - RE
            - RO
            - RS
            - RW
            - SA
            - SB
            - SC
            - SD
            - SE
            - SG
            - SH
            - SI
            - SJ
            - SK
            - SL
            - SM
            - SN
            - SO
            - SR
            - SS
            - ST
            - SV
            - SX
            - SZ
            - TC
            - TD
            - TF
            - TG
            - TH
            - TJ
            - TK
            - TL
            - TM
            - TN
            - TO
            - TR
            - TT
            - TV
            - TW
            - TZ
            - UA
            - UG
            - UM
            - US
            - UY
            - UZ
            - VA
            - VC
            - VE
            - VG
            - VI
            - VN
            - VU
            - WF
            - WS
            - YE
            - YT
            - ZA
            - ZM
            - ZW
      type: object
      required:
        - country
      title: AddressInput
    BenefitPublic:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          $ref: '#/components/schemas/BenefitType'
          description: The type of the benefit.
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
      title: BenefitPublic
    BenefitType:
      type: string
      enum:
        - custom
        - discord
        - github_repository
        - downloadables
        - license_keys
        - meter_credit
      title: BenefitType
    CustomerCancellationReason:
      type: string
      enum:
        - customer_service
        - low_quality
        - missing_features
        - switched_service
        - too_complex
        - too_expensive
        - unused
        - other
      title: CustomerCancellationReason
    CustomerOrderProduct:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        trial_interval:
          anyOf:
            - $ref: '#/components/schemas/TrialInterval'
            - type: 'null'
          description: The interval unit for the trial period.
        trial_interval_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Trial Interval Count
          description: The number of interval units for the trial period.
        name:
          type: string
          title: Name
          description: The name of the product.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: The description of the product.
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          description: >-
            The recurring interval of the product. If `None`, the product is a
            one-time purchase.
        recurring_interval_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Recurring Interval Count
          description: >-
            Number of interval units of the subscription. If this is set to 1
            the charge will happen every interval (e.g. every month), if set to
            2 it will be every other month, and so on. None for one-time
            products.
        is_recurring:
          type: boolean
          title: Is Recurring
          description: Whether the product is a subscription.
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the product is archived and no longer available.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the product.
        prices:
          items:
            oneOf:
              - $ref: '#/components/schemas/LegacyRecurringProductPrice'
              - $ref: '#/components/schemas/ProductPrice'
          type: array
          title: Prices
          description: List of prices for this product.
        benefits:
          items:
            $ref: '#/components/schemas/BenefitPublic'
          type: array
          title: BenefitPublic
          description: List of benefits granted by the product.
        medias:
          items:
            $ref: '#/components/schemas/ProductMediaFileRead'
          type: array
          title: Medias
          description: List of medias associated to the product.
        organization:
          $ref: '#/components/schemas/Organization'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - trial_interval
        - trial_interval_count
        - name
        - description
        - recurring_interval
        - recurring_interval_count
        - is_recurring
        - is_archived
        - organization_id
        - prices
        - benefits
        - medias
        - organization
      title: CustomerOrderProduct
    CustomerOrderSubscription:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        amount:
          type: integer
          title: Amount
          description: The amount of the subscription.
          examples:
            - 10000
        currency:
          type: string
          title: Currency
          description: The currency of the subscription.
          examples:
            - usd
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The interval at which the subscription recurs.
          examples:
            - month
        recurring_interval_count:
          type: integer
          title: Recurring Interval Count
          description: >-
            Number of interval units of the subscription. If this is set to 1
            the charge will happen every interval (e.g. every month), if set to
            2 it will be every other month, and so on.
        status:
          $ref: '#/components/schemas/SubscriptionStatus'
          description: The status of the subscription.
          examples:
            - active
        current_period_start:
          type: string
          format: date-time
          title: Current Period Start
          description: The start timestamp of the current billing period.
        current_period_end:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Current Period End
          description: The end timestamp of the current billing period.
        trial_start:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trial Start
          description: The start timestamp of the trial period, if any.
        trial_end:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trial End
          description: The end timestamp of the trial period, if any.
        cancel_at_period_end:
          type: boolean
          title: Cancel At Period End
          description: >-
            Whether the subscription will be canceled at the end of the current
            period.
        canceled_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Canceled At
          description: >-
            The timestamp when the subscription was canceled. The subscription
            might still be active if `cancel_at_period_end` is `true`.
        started_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Started At
          description: The timestamp when the subscription started.
        ends_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Ends At
          description: The timestamp when the subscription will end.
        ended_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Ended At
          description: The timestamp when the subscription ended.
        customer_id:
          type: string
          format: uuid4
          title: Customer Id
          description: The ID of the subscribed customer.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the subscribed product.
        discount_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Discount Id
          description: The ID of the applied discount, if any.
        checkout_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Checkout Id
        seats:
          anyOf:
            - type: integer
            - type: 'null'
          title: Seats
          description: >-
            The number of seats for seat-based subscriptions. None for non-seat
            subscriptions.
        customer_cancellation_reason:
          anyOf:
            - $ref: '#/components/schemas/CustomerCancellationReason'
            - type: 'null'
        customer_cancellation_comment:
          anyOf:
            - type: string
            - type: 'null'
          title: Customer Cancellation Comment
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount
        - currency
        - recurring_interval
        - recurring_interval_count
        - status
        - current_period_start
        - current_period_end
        - trial_start
        - trial_end
        - cancel_at_period_end
        - canceled_at
        - started_at
        - ends_at
        - ended_at
        - customer_id
        - product_id
        - discount_id
        - checkout_id
        - customer_cancellation_reason
        - customer_cancellation_comment
      title: CustomerOrderSubscription
    LegacyRecurringProductPrice:
      oneOf:
        - $ref: '#/components/schemas/LegacyRecurringProductPriceFixed'
        - $ref: '#/components/schemas/LegacyRecurringProductPriceCustom'
        - $ref: '#/components/schemas/LegacyRecurringProductPriceFree'
      discriminator:
        propertyName: amount_type
        mapping:
          custom: '#/components/schemas/LegacyRecurringProductPriceCustom'
          fixed: '#/components/schemas/LegacyRecurringProductPriceFixed'
          free: '#/components/schemas/LegacyRecurringProductPriceFree'
    LegacyRecurringProductPriceCustom:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: custom
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          type: string
          const: recurring
          title: Type
          description: The type of the price.
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The recurring interval of the price.
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        minimum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Minimum Amount
          description: The minimum amount the customer can pay.
        maximum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Maximum Amount
          description: The maximum amount the customer can pay.
        preset_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Preset Amount
          description: The initial amount shown to the customer.
        legacy:
          type: boolean
          const: true
          title: Legacy
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - minimum_amount
        - maximum_amount
        - preset_amount
        - legacy
      title: LegacyRecurringProductPriceCustom
      description: >-
        A pay-what-you-want recurring price for a product, i.e. a subscription.


        **Deprecated**: The recurring interval should be set on the product
        itself.
    LegacyRecurringProductPriceFixed:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: fixed
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          type: string
          const: recurring
          title: Type
          description: The type of the price.
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The recurring interval of the price.
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        price_amount:
          type: integer
          title: Price Amount
          description: The price in cents.
        legacy:
          type: boolean
          const: true
          title: Legacy
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - price_amount
        - legacy
      title: LegacyRecurringProductPriceFixed
      description: >-
        A recurring price for a product, i.e. a subscription.


        **Deprecated**: The recurring interval should be set on the product
        itself.
    LegacyRecurringProductPriceFree:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: free
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          type: string
          const: recurring
          title: Type
          description: The type of the price.
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The recurring interval of the price.
        legacy:
          type: boolean
          const: true
          title: Legacy
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - legacy
      title: LegacyRecurringProductPriceFree
      description: >-
        A free recurring price for a product, i.e. a subscription.


        **Deprecated**: The recurring interval should be set on the product
        itself.
    OrderBillingReason:
      type: string
      enum:
        - purchase
        - subscription_create
        - subscription_cycle
        - subscription_update
      title: OrderBillingReason
    OrderItemSchema:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        label:
          type: string
          title: Label
          description: Description of the line item charge.
          examples:
            - Pro Plan
        amount:
          type: integer
          title: Amount
          description: Amount in cents, before discounts and taxes.
          examples:
            - 10000
        tax_amount:
          type: integer
          title: Tax Amount
          description: Sales tax amount in cents.
          examples:
            - 720
        proration:
          type: boolean
          title: Proration
          description: Whether this charge is due to a proration.
          examples:
            - false
        product_price_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Product Price Id
          description: Associated price ID, if any.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - label
        - amount
        - tax_amount
        - proration
        - product_price_id
      title: OrderItemSchema
      description: An order line item.
    OrderStatus:
      type: string
      enum:
        - pending
        - paid
        - refunded
        - partially_refunded
      title: OrderStatus
    Organization:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The organization ID.
          examples:
            - 1dbfc517-0bbf-4301-9ba8-555ca42b9737
          x-polar-selector-widget:
            displayProperty: name
            resourceName: Organization
            resourceRoot: /v1/organizations
        name:
          type: string
          title: Name
          description: Organization name shown in checkout, customer portal, emails etc.
        slug:
          type: string
          title: Slug
          description: >-
            Unique organization slug in checkout, customer portal and credit
            card statements.
        avatar_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Avatar Url
          description: Avatar URL shown in checkout, customer portal, emails etc.
        email:
          anyOf:
            - type: string
            - type: 'null'
          title: Email
          description: Public support email.
        website:
          anyOf:
            - type: string
            - type: 'null'
          title: Website
          description: Official website of the organization.
        socials:
          items:
            $ref: '#/components/schemas/OrganizationSocialLink'
          type: array
          title: Socials
          description: Links to social profiles.
        status:
          $ref: '#/components/schemas/Status'
          description: Current organization status
        details_submitted_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Details Submitted At
          description: When the business details were submitted.
        feature_settings:
          anyOf:
            - $ref: '#/components/schemas/OrganizationFeatureSettings'
            - type: 'null'
          description: Organization feature settings
        subscription_settings:
          $ref: '#/components/schemas/OrganizationSubscriptionSettings'
          description: Settings related to subscriptions management
        notification_settings:
          $ref: '#/components/schemas/OrganizationNotificationSettings'
          description: Settings related to notifications
        customer_email_settings:
          $ref: '#/components/schemas/OrganizationCustomerEmailSettings'
          description: Settings related to customer emails
      type: object
      required:
        - created_at
        - modified_at
        - id
        - name
        - slug
        - avatar_url
        - email
        - website
        - socials
        - status
        - details_submitted_at
        - feature_settings
        - subscription_settings
        - notification_settings
        - customer_email_settings
      title: Organization
    OrganizationCustomerEmailSettings:
      properties:
        order_confirmation:
          type: boolean
          title: Order Confirmation
        subscription_cancellation:
          type: boolean
          title: Subscription Cancellation
        subscription_confirmation:
          type: boolean
          title: Subscription Confirmation
        subscription_cycled:
          type: boolean
          title: Subscription Cycled
        subscription_past_due:
          type: boolean
          title: Subscription Past Due
        subscription_revoked:
          type: boolean
          title: Subscription Revoked
        subscription_uncanceled:
          type: boolean
          title: Subscription Uncanceled
        subscription_updated:
          type: boolean
          title: Subscription Updated
      type: object
      required:
        - order_confirmation
        - subscription_cancellation
        - subscription_confirmation
        - subscription_cycled
        - subscription_past_due
        - subscription_revoked
        - subscription_uncanceled
        - subscription_updated
      title: OrganizationCustomerEmailSettings
    OrganizationFeatureSettings:
      properties:
        issue_funding_enabled:
          type: boolean
          title: Issue Funding Enabled
          description: If this organization has issue funding enabled
          default: false
        seat_based_pricing_enabled:
          type: boolean
          title: Seat Based Pricing Enabled
          description: If this organization has seat-based pricing enabled
          default: false
        revops_enabled:
          type: boolean
          title: Revops Enabled
          description: If this organization has RevOps enabled
          default: false
      type: object
      title: OrganizationFeatureSettings
    OrganizationNotificationSettings:
      properties:
        new_order:
          type: boolean
          title: New Order
        new_subscription:
          type: boolean
          title: New Subscription
      type: object
      required:
        - new_order
        - new_subscription
      title: OrganizationNotificationSettings
    OrganizationSocialLink:
      properties:
        platform:
          $ref: '#/components/schemas/OrganizationSocialPlatforms'
          description: The social platform of the URL
        url:
          type: string
          maxLength: 2083
          minLength: 1
          format: uri
          title: Url
          description: The URL to the organization profile
      type: object
      required:
        - platform
        - url
      title: OrganizationSocialLink
    OrganizationSocialPlatforms:
      type: string
      enum:
        - x
        - github
        - facebook
        - instagram
        - youtube
        - tiktok
        - linkedin
        - other
      title: OrganizationSocialPlatforms
    OrganizationSubscriptionSettings:
      properties:
        allow_multiple_subscriptions:
          type: boolean
          title: Allow Multiple Subscriptions
        allow_customer_updates:
          type: boolean
          title: Allow Customer Updates
        proration_behavior:
          $ref: '#/components/schemas/SubscriptionProrationBehavior'
      type: object
      required:
        - allow_multiple_subscriptions
        - allow_customer_updates
        - proration_behavior
      title: OrganizationSubscriptionSettings
    ProductMediaFileRead:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
        name:
          type: string
          title: Name
        path:
          type: string
          title: Path
        mime_type:
          type: string
          title: Mime Type
        size:
          type: integer
          title: Size
        storage_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Storage Version
        checksum_etag:
          anyOf:
            - type: string
            - type: 'null'
          title: Checksum Etag
        checksum_sha256_base64:
          anyOf:
            - type: string
            - type: 'null'
          title: Checksum Sha256 Base64
        checksum_sha256_hex:
          anyOf:
            - type: string
            - type: 'null'
          title: Checksum Sha256 Hex
        last_modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Modified At
        version:
          anyOf:
            - type: string
            - type: 'null'
          title: Version
        service:
          type: string
          const: product_media
          title: Service
        is_uploaded:
          type: boolean
          title: Is Uploaded
        created_at:
          type: string
          format: date-time
          title: Created At
        size_readable:
          type: string
          title: Size Readable
        public_url:
          type: string
          title: Public Url
      type: object
      required:
        - id
        - organization_id
        - name
        - path
        - mime_type
        - size
        - storage_version
        - checksum_etag
        - checksum_sha256_base64
        - checksum_sha256_hex
        - last_modified_at
        - version
        - service
        - is_uploaded
        - created_at
        - size_readable
        - public_url
      title: ProductMediaFileRead
      description: File to be used as a product media file.
    ProductPrice:
      oneOf:
        - $ref: '#/components/schemas/ProductPriceFixed'
        - $ref: '#/components/schemas/ProductPriceCustom'
        - $ref: '#/components/schemas/ProductPriceFree'
        - $ref: '#/components/schemas/ProductPriceSeatBased'
        - $ref: '#/components/schemas/ProductPriceMeteredUnit'
      discriminator:
        propertyName: amount_type
        mapping:
          custom: '#/components/schemas/ProductPriceCustom'
          fixed: '#/components/schemas/ProductPriceFixed'
          free: '#/components/schemas/ProductPriceFree'
          metered_unit: '#/components/schemas/ProductPriceMeteredUnit'
          seat_based: '#/components/schemas/ProductPriceSeatBased'
    ProductPriceCustom:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: custom
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        minimum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Minimum Amount
          description: The minimum amount the customer can pay.
        maximum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Maximum Amount
          description: The maximum amount the customer can pay.
        preset_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Preset Amount
          description: The initial amount shown to the customer.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - minimum_amount
        - maximum_amount
        - preset_amount
      title: ProductPriceCustom
      description: A pay-what-you-want price for a product.
    ProductPriceFixed:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: fixed
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        price_amount:
          type: integer
          title: Price Amount
          description: The price in cents.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - price_amount
      title: ProductPriceFixed
      description: A fixed price for a product.
    ProductPriceFree:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: free
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
      title: ProductPriceFree
      description: A free price for a product.
    ProductPriceMeter:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        name:
          type: string
          title: Name
          description: The name of the meter.
      type: object
      required:
        - id
        - name
      title: ProductPriceMeter
      description: A meter associated to a metered price.
    ProductPriceMeteredUnit:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: metered_unit
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        unit_amount:
          type: string
          pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
          title: Unit Amount
          description: The price per unit in cents.
        cap_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Cap Amount
          description: >-
            The maximum amount in cents that can be charged, regardless of the
            number of units consumed.
        meter_id:
          type: string
          format: uuid4
          title: Meter Id
          description: The ID of the meter associated to the price.
        meter:
          $ref: '#/components/schemas/ProductPriceMeter'
          description: The meter associated to the price.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - unit_amount
        - cap_amount
        - meter_id
        - meter
      title: ProductPriceMeteredUnit
      description: A metered, usage-based, price for a product, with a fixed unit price.
    ProductPriceSeatBased:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: seat_based
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        seat_tiers:
          $ref: '#/components/schemas/ProductPriceSeatTiers'
          description: Tiered pricing based on seat quantity
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - seat_tiers
      title: ProductPriceSeatBased
      description: A seat-based price for a product.
    ProductPriceSeatTier:
      properties:
        min_seats:
          type: integer
          minimum: 1
          title: Min Seats
          description: Minimum number of seats (inclusive)
        max_seats:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: Max Seats
          description: Maximum number of seats (inclusive). None for unlimited.
        price_per_seat:
          type: integer
          maximum: 99999999
          minimum: 50
          title: Price Per Seat
          description: Price per seat in cents for this tier
      type: object
      required:
        - min_seats
        - price_per_seat
      title: ProductPriceSeatTier
      description: A pricing tier for seat-based pricing.
    ProductPriceSeatTiers:
      properties:
        tiers:
          items:
            $ref: '#/components/schemas/ProductPriceSeatTier'
          type: array
          minItems: 1
          title: Tiers
          description: List of pricing tiers
      type: object
      required:
        - tiers
      title: ProductPriceSeatTiers
      description: List of pricing tiers for seat-based pricing.
    ProductPriceType:
      type: string
      enum:
        - one_time
        - recurring
      title: ProductPriceType
    Status:
      type: string
      enum:
        - created
        - onboarding_started
        - under_review
        - denied
        - active
      title: Status
    SubscriptionProrationBehavior:
      type: string
      enum:
        - invoice
        - prorate
      title: SubscriptionProrationBehavior
    SubscriptionRecurringInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      title: SubscriptionRecurringInterval
    SubscriptionStatus:
      type: string
      enum:
        - incomplete
        - incomplete_expired
        - trialing
        - active
        - past_due
        - canceled
        - unpaid
      title: SubscriptionStatus
    TrialInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      title: TrialInterval
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````