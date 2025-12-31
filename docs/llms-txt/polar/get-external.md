# Source: https://polar.sh/docs/api-reference/customers/get-external.md

# Get Customer by External ID

> Get a customer by external ID.

**Scopes**: `customers:read` `customers:write`

## OpenAPI

````yaml get /v1/customers/external/{external_id}
paths:
  path: /v1/customers/external/{external_id}
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
        external_id:
          schema:
            - type: string
              required: true
              title: External Id
              description: The customer external ID.
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Customers.GetExternal(ctx, \"<id>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Customer != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.customers.get_external(external_id="<id>")

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
            const result = await polar.customers.getExternal({
              externalId: "<id>",
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



          $response = $sdk->customers->getExternal(
              externalId: '<id>'
          );

          if ($response->customer !== null) {
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
              avatar_url:
                allOf:
                  - type: string
                    title: Avatar Url
                    examples:
                      - https://www.gravatar.com/avatar/xxx?d=404
            title: Customer
            description: A customer in an organization.
            refIdentifier: '#/components/schemas/Customer'
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