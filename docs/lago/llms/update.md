# Source: https://getlago.com/docs/api-reference/webhook-endpoints/update.md

# Source: https://getlago.com/docs/api-reference/wallets/update.md

# Source: https://getlago.com/docs/api-reference/taxes/update.md

# Source: https://getlago.com/docs/api-reference/subscriptions/update.md

# Source: https://getlago.com/docs/api-reference/plans/update.md

# Source: https://getlago.com/docs/api-reference/organizations/update.md

# Source: https://getlago.com/docs/api-reference/invoices/update.md

# Source: https://getlago.com/docs/api-reference/customers/update.md

# Source: https://getlago.com/docs/api-reference/credit-notes/update.md

# Source: https://getlago.com/docs/api-reference/coupons/update.md

# Source: https://getlago.com/docs/api-reference/billing-entities/update.md

# Source: https://getlago.com/docs/api-reference/billable-metrics/update.md

# Source: https://getlago.com/docs/api-reference/alerts/update.md

# Source: https://getlago.com/docs/api-reference/add-ons/update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an add-on

> This endpoint is used to update an existing add-on.

<RequestExample>
  ```bash cURL theme={"dark"}
  LAGO_URL="https://api.getlago.com"
  API_KEY="__YOUR_API_KEY__"

  curl --location --request PUT "$LAGO_URL/api/v1/add_ons/:code" \
    --header "Authorization: Bearer $API_KEY" \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "add_on": {
        "name": "Setup Fee",
        "code": "setup_fee",
        "amount_cents": 50000,
        "amount_currency": "USD",
        "description": "Implementation fee for new customers."
      }
    }'
  ```

  ```python Python theme={"dark"}
  from lago_python_client.client import Client
  from lago_python_client.exceptions import LagoApiError
  from lago_python_client.models import AddOn

  client = Client(api_key='__YOUR_API_KEY__')

  update_params = AddOn(name='Setup Fee')

  try:
      client.add_ons.update(update_params, 'setup_fee')
  except LagoApiError as e:
      repair_broken_state(e)  # do something on error or raise your own exception
  ```

  ```ruby Ruby theme={"dark"}
  require 'lago-ruby-client'

  client = Lago::Api::Client.new(api_key: '__YOUR_API_KEY__')

  update_params = {name: 'Setup Fee'}
  client.add_ons.update(update_params, 'setup_fee')
  ```

  ```js Javascript theme={"dark"}
  await client.addOns.updateAddOn("code", {
    add_on: { name: "Setup Fee", code: "setup_fee" },
  });
  ```

  ```go Go theme={"dark"}
  import "fmt"
  import "github.com/getlago/lago-go-client"

  func main() {
  lagoClient := lago.New().
      SetApiKey("__YOUR_API_KEY__")

  addOnInput := &lago.AddOnInput{
          Name:           "Setup Fee",
          Code:           "setup_fee",
          AmountCents:    50000,
          AmountCurrency: lago.USD,
          Description:    "Implementation fee for new customers.",
  }

  addOn, err := lagoClient.AddOn().Update(addOnInput)
  if err != nil {
      // Error is *lago.Error
      panic(err)
  }

  // addOn is *lago.AddOn
  fmt.Println(addOn)
  }
  ```
</RequestExample>


## OpenAPI

````yaml PUT /add_ons/{code}
openapi: 3.1.0
info:
  title: Lago API documentation
  description: >-
    Lago API allows your application to push customer information and metrics
    (events) from your application to the billing application.
  version: 1.41.0
  license:
    name: AGPLv3
    identifier: AGPLv3
  contact:
    email: tech@getlago.com
servers:
  - url: https://api.getlago.com/api/v1
    description: US Lago cluster
  - url: https://api.eu.getlago.com/api/v1
    description: EU Lago cluster
security:
  - bearerAuth: []
tags:
  - name: activity_logs
    description: Everything about Activity logs
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/audit-logs/activity-logs-object
  - name: analytics
    description: Everything about Analytics
  - name: api_logs
    description: Everything about API logs
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/audit-logs/api-logs-object
  - name: billable_metrics
    description: Everything about Billable metric collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/billable-metrics/object
  - name: features
    description: Everything about Feature collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/features/object
  - name: entitlements
    description: Everything about Entitlement collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/entitlements/object
  - name: billing_entities
    description: Everything about Billing Entities
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/billing-entities/object
  - name: customers
    description: Everything about Customer collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/customers/object
  - name: plans
    description: Everything about Plan collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/plans/object
  - name: subscriptions
    description: Everything about Subscription collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/subscriptions/subscription-object
  - name: events
    description: Everything about Event collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/events/event-object
  - name: organizations
    description: Everything about Organization collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/organizations/organization-object
  - name: taxes
    description: Everything about Tax collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/taxes/tax-object
  - name: coupons
    description: Everything about Coupon collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/coupons/coupon-object
  - name: add_ons
    description: Everything about Add-on collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/add-ons/add-on-object
  - name: fees
    description: Everything about Fees
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/invoices/invoice-object#fee-object
  - name: invoices
    description: Everything about Invoice collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/invoices/invoice-object
  - name: wallets
    description: Everything about Wallet collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/wallets/wallet-object
  - name: credit_notes
    description: Everything about Credit notes collection
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/credit-notes/credit-note-object
  - name: webhooks
    description: Everything about Webhooks
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/webhooks/format---signature#1-retrieve-the-public-key
  - name: webhook_endpoints
    description: Everything about Webhook Endpoints
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/webhook-endpoints/webhook-endpoint-object
  - name: payment_receipts
    description: Everything about Payment receipts
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/payment-receipts/payment-receipt-object
  - name: payment_requests
    description: Everything about PaymentRequests
    externalDocs:
      description: Find out more
      url: >-
        https://doc.getlago.com/api-reference/payment-requests/payment-request-object
  - name: payments
    description: Everything about Payments
    externalDocs:
      description: Find out more
      url: https://doc.getlago.com/api-reference/payments/payment-object
externalDocs:
  description: Lago Github
  url: https://github.com/getlago
paths:
  /add_ons/{code}:
    parameters:
      - name: code
        in: path
        description: Unique code used to identify the add-on.
        required: true
        schema:
          type: string
          example: setup_fee
    put:
      tags:
        - add_ons
      summary: Update an add-on
      description: This endpoint is used to update an existing add-on.
      operationId: updateAddOn
      requestBody:
        description: Add-on payload
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddOnUpdateInput'
        required: true
      responses:
        '200':
          description: Add-on updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AddOn'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
components:
  schemas:
    AddOnUpdateInput:
      type: object
      required:
        - add_on
      properties:
        add_on:
          $ref: '#/components/schemas/AddOnBaseInput'
    AddOn:
      type: object
      required:
        - add_on
      properties:
        add_on:
          $ref: '#/components/schemas/AddOnObject'
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
    ApiErrorBadRequest:
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: integer
          format: int32
          example: 400
        error:
          type: string
          example: Bad request
    ApiErrorUnauthorized:
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: integer
          format: int32
          example: 401
        error:
          type: string
          example: Unauthorized
    ApiErrorForbidden:
      type: object
      required:
        - status
        - error
        - code
      properties:
        status:
          type: integer
          format: int32
          example: 403
        error:
          type: string
          example: Forbidden
        code:
          type: string
          example: feature_unavailable
    ApiErrorNotFound:
      type: object
      required:
        - status
        - error
        - code
      properties:
        status:
          type: integer
          format: int32
          example: 404
        error:
          type: string
          example: Not Found
        code:
          type: string
          example: object_not_found
    ApiErrorUnprocessableEntity:
      type: object
      required:
        - status
        - error
        - code
        - error_details
      properties:
        status:
          type: integer
          format: int32
          example: 422
        error:
          type: string
          example: Unprocessable entity
        code:
          type: string
          example: validation_errors
        error_details:
          type: object
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
    TaxCodes:
      type: array
      items:
        type: string
      description: List of unique code used to identify the taxes.
      example:
        - french_standard_vat
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
  responses:
    BadRequest:
      description: Bad Request error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorBadRequest'
    Unauthorized:
      description: Unauthorized error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnauthorized'
    Forbidden:
      description: Forbidden
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorForbidden'
    NotFound:
      description: Not Found error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorNotFound'
    UnprocessableEntity:
      description: Unprocessable entity error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnprocessableEntity'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````