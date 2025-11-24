# Source: https://polar.sh/docs/api-reference/customers/state.md

# Get Customer State

> Get a customer state by ID.

The customer state includes information about
the customer's active subscriptions and benefits.

It's the ideal endpoint to use when you need to get a full overview
of a customer's status.

**Scopes**: `customers:read` `customers:write`

## OpenAPI

````yaml get /v1/customers/{id}/state
paths:
  path: /v1/customers/{id}/state
  method: get
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: access token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                You can generate an **Organization Access Token** from your
                organization's settings.
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              title: Id
              description: The customer ID.
              format: uuid4
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Customers.GetState(ctx, \"<value>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.CustomerState != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.customers.get_state(id="<value>")

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            const result = await polar.customers.getState({
              id: "<value>",
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

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();



          $response = $sdk->customers->getState(
              id: '<value>'
          );

          if ($response->customerState !== null) {
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
                    description: The ID of the customer.
                    examples:
                      - 992fae2a-2a17-4b7a-8d9e-e287cf90131b
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
              metadata:
                allOf:
                  - additionalProperties:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                        - type: boolean
                    type: object
                    title: Metadata
              external_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: External Id
                    description: >-
                      The ID of the customer in your system. This must be unique
                      within the organization. Once set, it can't be updated.
                    examples:
                      - usr_1337
              email:
                allOf:
                  - type: string
                    title: Email
                    description: >-
                      The email address of the customer. This must be unique
                      within the organization.
                    examples:
                      - customer@example.com
              email_verified:
                allOf:
                  - type: boolean
                    title: Email Verified
                    description: >-
                      Whether the customer email address is verified. The
                      address is automatically verified when the customer
                      accesses the customer portal using their email address.
                    examples:
                      - true
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Name
                    description: The name of the customer.
                    examples:
                      - John Doe
              billing_address:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/Address'
                      - type: 'null'
              tax_id:
                allOf:
                  - anyOf:
                      - prefixItems:
                          - type: string
                          - $ref: '#/components/schemas/TaxIDFormat'
                        type: array
                        maxItems: 2
                        minItems: 2
                        examples:
                          - - '911144442'
                            - us_ein
                          - - FR61954506077
                            - eu_vat
                      - type: 'null'
                    title: Tax Id
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
                    description: The ID of the organization owning the customer.
                    examples:
                      - 1dbfc517-0bbf-4301-9ba8-555ca42b9737
              deleted_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Deleted At
                    description: Timestamp for when the customer was soft deleted.
              active_subscriptions:
                allOf:
                  - items:
                      $ref: '#/components/schemas/CustomerStateSubscription'
                    type: array
                    title: Active Subscriptions
                    description: The customer's active subscriptions.
              granted_benefits:
                allOf:
                  - items:
                      $ref: '#/components/schemas/CustomerStateBenefitGrant'
                    type: array
                    title: Granted Benefits
                    description: The customer's active benefit grants.
              active_meters:
                allOf:
                  - items:
                      $ref: '#/components/schemas/CustomerStateMeter'
                    type: array
                    title: Active Meters
                    description: The customer's active meters.
              avatar_url:
                allOf:
                  - type: string
                    title: Avatar Url
                    examples:
                      - https://www.gravatar.com/avatar/xxx?d=404
            title: CustomerState
            description: |-
              A customer along with additional state information:

              * Active subscriptions
              * Granted benefits
              * Active meters
            refIdentifier: '#/components/schemas/CustomerState'
            requiredProperties:
              - id
              - created_at
              - modified_at
              - metadata
              - external_id
              - email
              - email_verified
              - name
              - billing_address
              - tax_id
              - organization_id
              - deleted_at
              - active_subscriptions
              - granted_benefits
              - active_meters
              - avatar_url
        examples:
          example:
            value:
              id: 992fae2a-2a17-4b7a-8d9e-e287cf90131b
              created_at: '2023-11-07T05:31:56Z'
              modified_at: '2023-11-07T05:31:56Z'
              metadata: {}
              external_id: usr_1337
              email: customer@example.com
              email_verified: true
              name: John Doe
              billing_address:
                line1: <string>
                line2: <string>
                postal_code: <string>
                city: <string>
                state: <string>
                country: US
              tax_id:
                - '911144442'
                - us_ein
              organization_id: 1dbfc517-0bbf-4301-9ba8-555ca42b9737
              deleted_at: '2023-11-07T05:31:56Z'
              active_subscriptions:
                - id: e5149aae-e521-42b9-b24c-abb3d71eea2e
                  created_at: '2023-11-07T05:31:56Z'
                  modified_at: '2023-11-07T05:31:56Z'
                  custom_field_data: {}
                  metadata: {}
                  status: active
                  amount: 1000
                  currency: usd
                  recurring_interval: day
                  current_period_start: '2025-02-03T13:37:00Z'
                  current_period_end: '2025-03-03T13:37:00Z'
                  trial_start: '2025-02-03T13:37:00Z'
                  trial_end: '2025-03-03T13:37:00Z'
                  cancel_at_period_end: false
                  canceled_at: null
                  started_at: '2025-01-03T13:37:00Z'
                  ends_at: null
                  product_id: d8dd2de1-21b7-4a41-8bc3-ce909c0cfe23
                  discount_id: null
                  meters:
                    - created_at: '2023-11-07T05:31:56Z'
                      modified_at: '2023-11-07T05:31:56Z'
                      id: <string>
                      consumed_units: 25
                      credited_units: 100
                      amount: 0
                      meter_id: d498a884-e2cd-4d3e-8002-f536468a8b22
              granted_benefits:
                - id: d322132c-a9d0-4e0d-b8d3-d81ad021a3a9
                  created_at: '2023-11-07T05:31:56Z'
                  modified_at: '2023-11-07T05:31:56Z'
                  granted_at: '2025-01-03T13:37:00Z'
                  benefit_id: 397a17aa-15cf-4cb4-9333-18040203cf98
                  benefit_type: custom
                  benefit_metadata:
                    key: value
                  properties:
                    account_id: <string>
                    guild_id: <string>
                    role_id: <string>
                    granted_account_id: <string>
              active_meters:
                - id: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  modified_at: '2023-11-07T05:31:56Z'
                  meter_id: d498a884-e2cd-4d3e-8002-f536468a8b22
                  consumed_units: 25
                  credited_units: 100
                  balance: 75
              avatar_url: https://www.gravatar.com/avatar/xxx?d=404
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
        description: Customer not found.
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
    BenefitGrantCustomProperties:
      properties: {}
      type: object
      title: BenefitGrantCustomProperties
    BenefitGrantDiscordProperties:
      properties:
        account_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Account Id
        guild_id:
          type: string
          title: Guild Id
        role_id:
          type: string
          title: Role Id
        granted_account_id:
          type: string
          title: Granted Account Id
      type: object
      title: BenefitGrantDiscordProperties
    BenefitGrantDownloadablesProperties:
      properties:
        files:
          items:
            type: string
          type: array
          title: Files
      type: object
      title: BenefitGrantDownloadablesProperties
    BenefitGrantGitHubRepositoryProperties:
      properties:
        account_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Account Id
        repository_owner:
          type: string
          title: Repository Owner
        repository_name:
          type: string
          title: Repository Name
        permission:
          type: string
          enum:
            - pull
            - triage
            - push
            - maintain
            - admin
          title: Permission
        granted_account_id:
          type: string
          title: Granted Account Id
      type: object
      title: BenefitGrantGitHubRepositoryProperties
    BenefitGrantLicenseKeysProperties:
      properties:
        license_key_id:
          type: string
          title: License Key Id
        display_key:
          type: string
          title: Display Key
      type: object
      title: BenefitGrantLicenseKeysProperties
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
    CustomerStateBenefitGrant:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the grant.
          examples:
            - d322132c-a9d0-4e0d-b8d3-d81ad021a3a9
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
        granted_at:
          type: string
          format: date-time
          title: Granted At
          description: The timestamp when the benefit was granted.
          examples:
            - '2025-01-03T13:37:00Z'
        benefit_id:
          type: string
          format: uuid4
          title: Benefit Id
          description: The ID of the benefit concerned by this grant.
          examples:
            - 397a17aa-15cf-4cb4-9333-18040203cf98
        benefit_type:
          $ref: '#/components/schemas/BenefitType'
          description: The type of the benefit concerned by this grant.
          examples:
            - custom
        benefit_metadata:
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Benefit Metadata
          description: The metadata of the benefit concerned by this grant.
          examples:
            - key: value
        properties:
          anyOf:
            - $ref: '#/components/schemas/BenefitGrantDiscordProperties'
            - $ref: '#/components/schemas/BenefitGrantGitHubRepositoryProperties'
            - $ref: '#/components/schemas/BenefitGrantDownloadablesProperties'
            - $ref: '#/components/schemas/BenefitGrantLicenseKeysProperties'
            - $ref: '#/components/schemas/BenefitGrantCustomProperties'
          title: Properties
      type: object
      required:
        - id
        - created_at
        - modified_at
        - granted_at
        - benefit_id
        - benefit_type
        - benefit_metadata
        - properties
      title: CustomerStateBenefitGrant
      description: An active benefit grant for a customer.
    CustomerStateMeter:
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
        meter_id:
          type: string
          format: uuid4
          title: Meter Id
          description: The ID of the meter.
          examples:
            - d498a884-e2cd-4d3e-8002-f536468a8b22
        consumed_units:
          type: number
          title: Consumed Units
          description: The number of consumed units.
          examples:
            - 25
        credited_units:
          type: integer
          title: Credited Units
          description: The number of credited units.
          examples:
            - 100
        balance:
          type: number
          title: Balance
          description: >-
            The balance of the meter, i.e. the difference between credited and
            consumed units.
          examples:
            - 75
      type: object
      required:
        - id
        - created_at
        - modified_at
        - meter_id
        - consumed_units
        - credited_units
        - balance
      title: CustomerStateMeter
      description: An active meter for a customer, with latest consumed and credited units.
    CustomerStateSubscription:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the subscription.
          examples:
            - e5149aae-e521-42b9-b24c-abb3d71eea2e
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
        custom_field_data:
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: boolean
              - type: string
                format: date-time
              - type: 'null'
          type: object
          title: Custom Field Data
          description: Key-value object storing custom field values.
        metadata:
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Metadata
        status:
          type: string
          enum:
            - active
            - trialing
          title: Status
          examples:
            - active
            - trialing
        amount:
          type: integer
          title: Amount
          description: The amount of the subscription.
          examples:
            - 1000
        currency:
          type: string
          title: Currency
          description: The currency of the subscription.
          examples:
            - usd
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The interval at which the subscription recurs.
        current_period_start:
          type: string
          format: date-time
          title: Current Period Start
          description: The start timestamp of the current billing period.
          examples:
            - '2025-02-03T13:37:00Z'
        current_period_end:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Current Period End
          description: The end timestamp of the current billing period.
          examples:
            - '2025-03-03T13:37:00Z'
        trial_start:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trial Start
          description: The start timestamp of the trial period, if any.
          examples:
            - '2025-02-03T13:37:00Z'
        trial_end:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trial End
          description: The end timestamp of the trial period, if any.
          examples:
            - '2025-03-03T13:37:00Z'
        cancel_at_period_end:
          type: boolean
          title: Cancel At Period End
          description: >-
            Whether the subscription will be canceled at the end of the current
            period.
          examples:
            - false
        canceled_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Canceled At
          description: >-
            The timestamp when the subscription was canceled. The subscription
            might still be active if `cancel_at_period_end` is `true`.
          examples:
            - null
        started_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Started At
          description: The timestamp when the subscription started.
          examples:
            - '2025-01-03T13:37:00Z'
        ends_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Ends At
          description: The timestamp when the subscription will end.
          examples:
            - null
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the subscribed product.
          examples:
            - d8dd2de1-21b7-4a41-8bc3-ce909c0cfe23
        discount_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Discount Id
          description: The ID of the applied discount, if any.
          examples:
            - null
        meters:
          items:
            $ref: '#/components/schemas/CustomerStateSubscriptionMeter'
          type: array
          title: Meters
          description: List of meters associated with the subscription.
      type: object
      required:
        - id
        - created_at
        - modified_at
        - metadata
        - status
        - amount
        - currency
        - recurring_interval
        - current_period_start
        - current_period_end
        - trial_start
        - trial_end
        - cancel_at_period_end
        - canceled_at
        - started_at
        - ends_at
        - product_id
        - discount_id
        - meters
      title: CustomerStateSubscription
      description: An active customer subscription.
    CustomerStateSubscriptionMeter:
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
        consumed_units:
          type: number
          title: Consumed Units
          description: The number of consumed units so far in this billing period.
          examples:
            - 25
        credited_units:
          type: integer
          title: Credited Units
          description: The number of credited units so far in this billing period.
          examples:
            - 100
        amount:
          type: integer
          title: Amount
          description: The amount due in cents so far in this billing period.
          examples:
            - 0
        meter_id:
          type: string
          format: uuid4
          title: Meter Id
          description: The ID of the meter.
          examples:
            - d498a884-e2cd-4d3e-8002-f536468a8b22
      type: object
      required:
        - created_at
        - modified_at
        - id
        - consumed_units
        - credited_units
        - amount
        - meter_id
      title: CustomerStateSubscriptionMeter
      description: Current consumption and spending for a subscription meter.
    SubscriptionRecurringInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      title: SubscriptionRecurringInterval
    TaxIDFormat:
      type: string
      enum:
        - ad_nrt
        - ae_trn
        - ar_cuit
        - au_abn
        - au_arn
        - bg_uic
        - bh_vat
        - bo_tin
        - br_cnpj
        - br_cpf
        - ca_bn
        - ca_gst_hst
        - ca_pst_bc
        - ca_pst_mb
        - ca_pst_sk
        - ca_qst
        - ch_uid
        - ch_vat
        - cl_tin
        - cn_tin
        - co_nit
        - cr_tin
        - de_stn
        - do_rcn
        - ec_ruc
        - eg_tin
        - es_cif
        - eu_oss_vat
        - eu_vat
        - gb_vat
        - ge_vat
        - hk_br
        - hr_oib
        - hu_tin
        - id_npwp
        - il_vat
        - in_gst
        - is_vat
        - jp_cn
        - jp_rn
        - jp_trn
        - ke_pin
        - kr_brn
        - kz_bin
        - li_uid
        - mx_rfc
        - my_frp
        - my_itn
        - my_sst
        - ng_tin
        - no_vat
        - no_voec
        - nz_gst
        - om_vat
        - pe_ruc
        - ph_tin
        - ro_tin
        - rs_pib
        - ru_inn
        - ru_kpp
        - sa_vat
        - sg_gst
        - sg_uen
        - si_tin
        - sv_nit
        - th_vat
        - tr_tin
        - tw_vat
        - ua_vat
        - us_ein
        - uy_ruc
        - ve_rif
        - vn_tin
        - za_vat
      title: TaxIDFormat
      description: |-
        List of supported tax ID formats.

        Ref: https://docs.stripe.com/billing/customer/tax-ids#supported-tax-id
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