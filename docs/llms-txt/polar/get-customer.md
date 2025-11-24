# Source: https://polar.sh/docs/api-reference/customer-portal/get-customer.md

# Get Customer

> Get authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

## OpenAPI

````yaml get /v1/customer-portal/customers/me
paths:
  path: /v1/customer-portal/customers/me
  method: get
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"os\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.CustomerPortal.Customers.Get(ctx, operations.CustomerPortalCustomersGetSecurity{\n        CustomerSession: os.Getenv(\"POLAR_CUSTOMER_SESSION\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.CustomerPortalCustomer != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          import polar_sdk
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_portal.customers.get(security=polar_sdk.CustomerPortalCustomersGetSecurity(
                  customer_session="<YOUR_BEARER_TOKEN_HERE>",
              ))

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.customerPortal.customers.get({
              customerSession: process.env["POLAR_CUSTOMER_SESSION"] ?? "",
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
          use Polar\Models\Operations;

          $sdk = Polar\Polar::builder()->build();


          $requestSecurity = new Operations\CustomerPortalCustomersGetSecurity(
              customerSession: '<YOUR_BEARER_TOKEN_HERE>',
          );

          $response = $sdk->customerPortal->customers->get(
              security: $requestSecurity
          );

          if ($response->customerPortalCustomer !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
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
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the object.
              email:
                allOf:
                  - type: string
                    title: Email
              email_verified:
                allOf:
                  - type: boolean
                    title: Email Verified
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Name
              billing_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Billing Name
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
              oauth_accounts:
                allOf:
                  - additionalProperties:
                      $ref: '#/components/schemas/CustomerPortalOAuthAccount'
                    type: object
                    title: Oauth Accounts
              default_payment_method_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Default Payment Method Id
            title: CustomerPortalCustomer
            refIdentifier: '#/components/schemas/CustomerPortalCustomer'
            requiredProperties:
              - created_at
              - modified_at
              - id
              - email
              - email_verified
              - name
              - billing_name
              - billing_address
              - tax_id
              - oauth_accounts
        examples:
          example:
            value:
              created_at: '2023-11-07T05:31:56Z'
              modified_at: '2023-11-07T05:31:56Z'
              id: <string>
              email: <string>
              email_verified: true
              name: <string>
              billing_name: <string>
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
              oauth_accounts: {}
              default_payment_method_id: <string>
        description: Successful Response
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
    CustomerPortalOAuthAccount:
      properties:
        account_id:
          type: string
          title: Account Id
        account_username:
          anyOf:
            - type: string
            - type: 'null'
          title: Account Username
      type: object
      required:
        - account_id
        - account_username
      title: CustomerPortalOAuthAccount
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

````