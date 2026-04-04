# Source: https://getlago.com/docs/api-reference/invoices/refresh.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Refresh an invoice

> This endpoint is used for refreshing a draft invoice.

<RequestExample>
  ```bash cURL theme={"dark"}
  LAGO_URL="https://api.getlago.com"
  API_KEY="__YOUR_API_KEY__"

  curl --location --request PUT "$LAGO_URL/api/v1/invoices/:lago_invoice_id/refresh" \
    --header "Authorization: Bearer $API_KEY" \
    --header 'Content-Type: application/json' \
    --data-raw '{}'
  ```

  ```python Python theme={"dark"}
  from lago_python_client.client import Client
  from lago_python_client.exceptions import LagoApiError

  client = Client(api_key='__YOUR_API_KEY__')

  try:
      client.invoices.refresh('__INVOICE_ID__')  # Invoice ID
  except LagoApiError as e:
      repair_broken_state(e)  # do something on error or raise your own exception
  ```

  ```ruby Ruby theme={"dark"}
  require 'lago-ruby-client'

  client = Lago::Api::Client.new(api_key: '__YOUR_API_KEY__')

  client.invoices.refresh('__INVOICE_ID__') // Invoice ID
  ```

  ```js Javascript theme={"dark"}
  await client.invoices.refreshInvoice('invoice-id')
  ```

  ```go Go theme={"dark"}
  import "fmt"
  import "github.com/getlago/lago-go-client"

  func main() {
  lagoClient := lago.New().
      SetApiKey("__YOUR_API_KEY__")

  invoice, err := lagoClient.Invoice().Refresh("__INVOICE_ID__")
  if err != nil {
      // Error is *lago.Error
      panic(err)
  }

  // invoice is *lago.Invoice
  fmt.Println(invoice)
  }
  ```
</RequestExample>


## OpenAPI

````yaml PUT /invoices/{lago_id}/refresh
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
  /invoices/{lago_id}/refresh:
    put:
      tags:
        - invoices
      summary: Refresh a draft invoice
      description: This endpoint is used for refreshing a draft invoice.
      operationId: refreshInvoice
      parameters:
        - $ref: '#/components/parameters/lago_invoice_id'
      responses:
        '200':
          description: Invoice refreshed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Invoice'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  parameters:
    lago_invoice_id:
      name: lago_id
      in: path
      description: >-
        Unique identifier assigned to the invoice within the Lago application.
        This ID is exclusively created by Lago and serves as a unique identifier
        for the invoice's record within the Lago system.
      required: true
      schema:
        type: string
        format: uuid
        example: 1a901a90-1a90-1a90-1a90-1a901a901a90
  schemas:
    Invoice:
      type: object
      required:
        - invoice
      properties:
        invoice:
          $ref: '#/components/schemas/InvoiceObjectExtended'
    InvoiceObjectExtended:
      allOf:
        - $ref: '#/components/schemas/InvoiceObject'
        - type: object
          properties:
            credits:
              type: array
              items:
                $ref: '#/components/schemas/CreditObject'
            fees:
              type: array
              items:
                $ref: '#/components/schemas/FeeObject'
            subscriptions:
              type: array
              items:
                $ref: '#/components/schemas/SubscriptionObject'
            error_details:
              type: array
              items:
                $ref: '#/components/schemas/ErrorDetailObject'
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
    InvoiceObject:
      allOf:
        - $ref: '#/components/schemas/InvoiceBaseObject'
        - type: object
          properties:
            customer:
              $ref: '#/components/schemas/CustomerObject'
              description: >-
                The customer on which the invoice applies. It refers to the
                customer account or entity associated with the invoice.
            billing_periods:
              type: array
              items:
                $ref: '#/components/schemas/BillingPeriodObject'
            metadata:
              type: array
              items:
                $ref: '#/components/schemas/InvoiceMetadataObject'
            applied_taxes:
              type: array
              items:
                $ref: '#/components/schemas/InvoiceAppliedTaxObject'
            applied_usage_thresholds:
              type: array
              items:
                $ref: '#/components/schemas/AppliedUsageThresholdObject'
    CreditObject:
      type: object
      required:
        - lago_id
        - item
        - amount_cents
        - amount_currency
        - invoice
        - before_taxes
      properties:
        lago_id:
          type: string
          format: uuid
          description: >-
            Unique identifier assigned to the credit within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the credit's item record within the Lago
            system.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        amount_cents:
          type: integer
          description: >-
            The amount of credit associated with the invoice, expressed in
            cents.
          example: 1200
        amount_currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of the credit.
          example: EUR
        before_taxes:
          type: boolean
          description: >-
            Indicates whether the credit is applied on the amount before taxes
            (coupons) or after taxes (credit notes). This flag helps determine
            the order in which credits are applied to the invoice calculation
          example: false
        item:
          type: object
          description: The item attached to the credit.
          required:
            - lago_item_id
            - type
            - code
            - name
          properties:
            lago_item_id:
              type: string
              format: uuid
              description: >-
                Unique identifier assigned to the credit item within the Lago
                application.
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
            type:
              type: string
              enum:
                - coupon
                - credit_note
                - invoice
              description: >-
                The type of credit applied. Possible values are `coupon`,
                `credit_note` or `invoice` (for `progressive_billing` invoice).
              example: coupon
            code:
              type: string
              description: >-
                The code of the credit applied. It can be the code of the coupon
                attached to the credit, the credit note's number or the
                `progressive_billing` invoice number.
              example: startup_deal
            name:
              type: string
              description: >-
                The name of the credit applied. It can be the name of the coupon
                attached to the credit, the initial invoice's number linked to
                the credit note or the `progressive_billing` invoice number.
              example: Startup Deal
        invoice:
          type: object
          required:
            - lago_id
            - payment_status
          properties:
            lago_id:
              type: string
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
            payment_status:
              type: string
              enum:
                - pending
                - succeeded
                - failed
              example: succeeded
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
        lago_fixed_charge_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the fixed charge that the fee belongs
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
            applicable only to `subscription`, `charge`, `fixed_charge` and
            `commitment` fees. This field indicates the start date of the
            billing period or subscription period associated with the fee.
          example: '2022-04-29T08:59:51Z'
        to_date:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The ending date of the period that the fee covers. It is applicable
            only to `subscription`, `charge`, `fixed_charge` and `commitment`
            fees. This field indicates the end date of the billing period or
            subscription period associated with the fee.
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
                - fixed_charge
                - add_on
                - subscription
                - credit
                - commitment
              description: >-
                The fee type. Possible values are `add-on`, `charge`,
                `fixed_charge`, `credit`, `subscription` or `commitment`.
              example: subscription
            code:
              type: string
              description: >-
                The code of the fee item. It can be the code of the `add-on`,
                the code of the `charge`, the code of the `fixed_charge`, the
                code of the `credit` or the code of the `subscription`.
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
          $ref: '#/components/schemas/PricingUnitDetailsObject'
          type:
            - object
            - 'null'
          description: Details about the pricing unit used and amounts for this fee.
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

            - `offset`: A credit note is generated for the unused subscription
            time. If the invoice is paid or partially paid, the unused paid
            amount is refunded; any unpaid unused amount is applied to the
            invoice reducing its amount due.

            - `skip`: No credit note is generated for the unused subscription
            time.


            _Note: This field is only applicable to pay-in-advance plans and
            will be `null` for pay-in-arrears plans._
          example: credit
          enum:
            - credit
            - refund
            - offset
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
    ErrorDetailObject:
      type: object
      required:
        - lago_id
        - error_code
        - details
      properties:
        lago_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            Unique identifier assigned to the error_detail within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the error's record within the Lago system.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        error_code:
          type: string
          description: >-
            Code that specifies part of the application / connection, where the
            error originally happened
          example: tax_error
        details:
          type: object
          description: >-
            Key value list of more elaborated error detail, where by the key of
            error_code an external service error details are stored
          example:
            tax_error: taxDateTooFarInFuture
    InvoiceBaseObject:
      type: object
      required:
        - lago_id
        - billing_entity_code
        - number
        - issuing_date
        - invoice_type
        - status
        - payment_status
        - currency
        - fees_amount_cents
        - coupons_amount_cents
        - credit_notes_amount_cents
        - sub_total_excluding_taxes_amount_cents
        - taxes_amount_cents
        - sub_total_including_taxes_amount_cents
        - prepaid_credit_amount_cents
        - progressive_billing_credit_amount_cents
        - total_amount_cents
        - version_number
        - created_at
        - updated_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: >-
            Unique identifier assigned to the fee within the Lago application.
            This ID is exclusively created by Lago and serves as a unique
            identifier for the fee's record within the Lago system.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        billing_entity_code:
          type:
            - string
            - 'null'
          example: acme_corp
          description: The unique code of the billing entity associated with the invoice
        sequential_id:
          type: integer
          description: >-
            This ID helps in uniquely identifying and organizing the invoices
            associated with a specific customer. It provides a sequential
            numbering system specific to the customer, allowing for easy
            tracking and management of invoices within the customer's context.
          example: 2
        number:
          type: string
          description: >-
            The unique number assigned to the invoice. This number serves as a
            distinct identifier for the invoice and helps in differentiating it
            from other invoices in the system.
          example: LAG-1234-001-002
        issuing_date:
          type: string
          format: date
          description: >-
            The date when the invoice was issued. It is provided in the ISO 8601
            date format.
          example: '2022-04-30'
        payment_dispute_lost_at:
          type: string
          format: date-time
          description: >-
            The date when the payment dispute was lost. It is expressed in
            Coordinated Universal Time (UTC).
          example: '2022-09-14T16:35:31Z'
        payment_due_date:
          type: string
          format: date
          description: >-
            The payment due date for the invoice, specified in the ISO 8601 date
            format.
          example: '2022-04-30'
        payment_overdue:
          type: boolean
          description: Specifies if the payment is considered as overdue.
          example: true
        net_payment_term:
          type: integer
          example: 30
          description: >-
            The net payment term, expressed in days, specifies the duration
            within which a customer is expected to remit payment after the
            invoice is finalized.
        invoice_type:
          type: string
          enum:
            - subscription
            - add_on
            - credit
            - one_off
            - progressive_billing
          description: >-
            The type of invoice issued. Possible values are `subscription`,
            `one-off`, `credit` or `progressive_billing`.
          example: subscription
        status:
          type: string
          enum:
            - draft
            - finalized
            - voided
            - failed
            - pending
          description: >-
            The status of the invoice. It indicates the current state of the
            invoice and can have following values:

            - `draft`: the invoice is in the draft state, waiting for the end of
            the grace period to be finalized. During this period, events can
            still be ingested and added to the invoice.

            - `finalized`: the invoice has been issued and finalized. In this
            state, events cannot be ingested or added to the invoice anymore.

            - `voided`: the invoice has been issued and subsequently voided. In
            this state, events cannot be ingested or added to the invoice
            anymore.

            - `pending`: the invoice remains pending until the taxes are fetched
            from the external provider.

            - `failed`: during an attempt of finalization of the invoice, an
            error happened. This invoice will have an array of error_details,
            explaining, in which part of the system an error happened and how
            it's possible to fix it. This invoice can't be edited or updated,
            only retried. This action will discard current error_details and
            will create new ones if the finalization failed again.
          example: finalized
        payment_status:
          type: string
          enum:
            - pending
            - succeeded
            - failed
          description: >-
            The status of the payment associated with the invoice. It can have
            one of the following values:

            - `pending`: the payment is pending, waiting for payment processing
            in Stripe or when the invoice is emitted but users have not updated
            the payment status through the endpoint.

            - `succeeded`: the payment of the invoice has been successfully
            processed.

            - `failed`: the payment of the invoice has failed or encountered an
            error during processing.
          example: succeeded
        currency:
          $ref: '#/components/schemas/Currency'
          description: The currency of the invoice issued.
          example: EUR
        fees_amount_cents:
          type: integer
          description: >-
            The total sum of fees amount in cents. It calculates the cumulative
            amount of all the fees associated with the invoice, providing a
            consolidated value.
          example: 100
        coupons_amount_cents:
          type: integer
          description: >-
            The total sum of all coupons discounted on the invoice. It
            calculates the cumulative discount amount applied by coupons,
            expressed in cents.
          example: 10
        credit_notes_amount_cents:
          type: integer
          description: >-
            The total sum of all credit notes discounted on the invoice. It
            calculates the cumulative discount amount applied by credit notes,
            expressed in cents.
          example: 10
        sub_total_excluding_taxes_amount_cents:
          type: integer
          description: >-
            Subtotal amount, excluding taxes, expressed in cents.

            This field depends on the version number. Here are the definitions
            based on the version:

            - Version 1: is equal to the sum of `fees_amount_cents`, minus
            `coupons_amount_cents`, and minus `prepaid_credit_amount_cents`.

            - Version 2: is equal to the `fees_amount_cents`.

            - Version 3 & 4: is equal to the `fees_amount_cents`, minus
            `coupons_amount_cents`
          example: 100
        taxes_amount_cents:
          type: integer
          description: >-
            The sum of tax amount associated with the invoice, expressed in
            cents.
          example: 20
        sub_total_including_taxes_amount_cents:
          type: integer
          description: >-
            Subtotal amount, including taxes, expressed in cents.

            This field depends on the version number. Here are the definitions
            based on the version:

            - Version 1: is equal to the `total_amount_cents`.

            - Version 2: is equal to the sum of `fees_amount_cents` and
            `taxes_amount_cents`.

            - Version 3 & 4: is equal to the sum
            `sub_total_excluding_taxes_amount_cents` and `taxes_amount_cents`
          example: 120
        prepaid_credit_amount_cents:
          type: integer
          description: >-
            The total sum of all prepaid credits discounted on the invoice. It
            calculates the cumulative discount amount applied by prepaid
            credits, expressed in cents.
          example: 0
        progressive_billing_credit_amount_cents:
          type: integer
          description: >-
            The usage already billed in previous invoices. Only apply to
            `progressive_billing` and `subscription` invoices.
          example: 0
        total_amount_cents:
          type: integer
          description: >-
            The sum of the amount and taxes amount on the invoice, expressed in
            cents. It calculates the total financial value of the invoice,
            including both the original amount and any applicable taxes.
          example: 100
        version_number:
          type: integer
          example: 3
        self_billed:
          type: boolean
          example: false
          description: >-
            Indicates if the invoice is self-billed. Self-billing is a process
            where an organization creates the invoice on behalf of the partner.
            This field specifies whether the invoice is self-billed or not.
        file_url:
          type: string
          format: uri
          description: >-
            Contains the URL that provides direct access to the invoice PDF
            file. You can use this URL to download or view the PDF document of
            the invoice
          example: https://getlago.com/invoice/file
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The date of the invoice creation, represented in ISO 8601 datetime
            format and expressed in Coordinated Universal Time (UTC). The
            creation_date provides a standardized and internationally recognized
            timestamp for when the invoice object was created
        updated_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The date of the invoice update, represented in ISO 8601 datetime
            format and expressed in Coordinated Universal Time (UTC). The
            update_date provides a standardized and internationally recognized
            timestamp for when the invoice object was updated
    CustomerObject:
      allOf:
        - $ref: '#/components/schemas/CustomerBaseObject'
        - type: object
          properties:
            integration_customers:
              type: array
              items:
                $ref: '#/components/schemas/IntegrationCustomer'
    BillingPeriodObject:
      type: object
      required:
        - lago_subscription_id
        - external_subscription_id
        - lago_plan_id
        - subscription_from_datetime
        - subscription_to_datetime
        - charges_from_datetime
        - charges_to_datetime
        - invoicing_reason
      properties:
        lago_subscription_id:
          type: string
          format: uuid
          description: Unique identifier assigned to the subscription, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        external_subscription_id:
          type: string
          description: Unique identifier assigned to the subscription in your application.
          example: external_id
        lago_plan_id:
          type: string
          format: uuid
          description: Unique identifier assigned to the plan, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        subscription_from_datetime:
          type: string
          format: date-time
          description: >-
            The beginning date of the subscription billing period. This field
            indicates the start date of the billing period associated with the
            subscription fee.
          example: '2022-04-29T08:59:51Z'
        subscription_to_datetime:
          type: string
          format: date-time
          description: >-
            The ending date of the subscription billing period. This field
            indicates the end date of the billing period associated with the
            subscription fee.
          example: '2022-05-29T08:59:51Z'
        charges_from_datetime:
          type: string
          format: date-time
          description: >-
            The beginning date of the period that covers the charge fees. It is
            applicable only to the `charge` fees attached to the subscription.
            This field indicates the start date of the billing period or
            subscription period associated with the fees.
          example: '2022-04-29T08:59:51Z'
        charges_to_datetime:
          type: string
          format: date-time
          description: >-
            The ending date of the period that covers the charge fees. It is
            applicable only to the `charge` fees attached to the subscription.
            This field indicates the end date of the billing period or
            subscription period associated with the fees.
          example: '2022-05-29T08:59:51Z'
        invoicing_reason:
          type: string
          enum:
            - subscription_starting
            - subscription_periodic
            - subscription_terminating
            - in_advance_charge
            - in_advance_charge_periodic
            - progressive_billing
          description: The reason explaining why this subscription appears on the invoice.
          example: subscription_starting
    InvoiceMetadataObject:
      type: object
      properties:
        lago_id:
          type: string
          format: uuid
          description: >-
            Unique identifier assigned to the invoice metadata within the Lago
            application.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        key:
          type: string
          description: Represents the key of the metadata's key-value pair.
          example: digital_ref_id
        value:
          type: string
          description: Represents the value of the metadata's key-value pair.
          example: INV-0123456-98765
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the metadata object was created. It follows
            the ISO 8601 datetime format and is expressed in Coordinated
            Universal Time (UTC).
          example: '2022-04-29T08:59:51Z'
    InvoiceAppliedTaxObject:
      allOf:
        - $ref: '#/components/schemas/BaseAppliedTax'
      type: object
      properties:
        lago_invoice_id:
          type: string
          format: uuid
          description: Unique identifier of the invoice, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        fees_amount_cents:
          type: integer
          description: Fees total amount on which the tax is applied
          example: 20000
    AppliedUsageThresholdObject:
      type: object
      required:
        - lifetime_usage_amount_cents
        - created_at
        - usage_threshold
      properties:
        lifetime_usage_amount_cents:
          type: integer
          description: >-
            The amount of usage in cents that has been accumulated over the
            lifetime of the subscription.
          example: 2000
        created_at:
          type: string
          format: date-time
          description: >-
            The date and time when the lifetime usage was computed. It is
            expressed in UTC format according to the ISO 8601 datetime standard.
          example: '2025-03-31T12:31:44Z'
        usage_threshold:
          $ref: '#/components/schemas/UsageThresholdObject'
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
    CustomerBaseObject:
      type: object
      required:
        - lago_id
        - sequential_id
        - slug
        - external_id
        - applicable_timezone
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the customer within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the customer's record within the Lago system
        sequential_id:
          type: integer
          example: 1
          description: >-
            The unique identifier assigned to the customer within the
            organization's scope. This identifier is used to track and reference
            the customer's order of creation within the organization's system.
            It ensures that each customer has a distinct `sequential_id``
            associated with them, allowing for easy identification and sorting
            based on the order of creation
        slug:
          type: string
          example: LAG-1234-001
          description: >-
            A concise and unique identifier for the customer, formed by
            combining the Organization's `name`, `id`, and customer's
            `sequential_id`
        external_id:
          type: string
          description: >-
            The customer external unique identifier (provided by your own
            application)
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        billing_entity_code:
          type: string
          example: acme_corp
          description: The unique code of the billing entity associated with the customer.
        address_line1:
          type:
            - string
            - 'null'
          example: 5230 Penfield Ave
          description: The first line of the billing address
        address_line2:
          type:
            - string
            - 'null'
          example: null
          description: The second line of the billing address
        applicable_timezone:
          $ref: '#/components/schemas/Timezone'
          description: >-
            The customer's applicable timezone, used for billing purposes in
            their local time.
        city:
          type:
            - string
            - 'null'
          example: Woodland Hills
          description: The city of the customer's billing address
        country:
          $ref: '#/components/schemas/CountryOrNull'
          description: >-
            Country code of the customer's billing address. Format must be ISO
            3166 (alpha-2)
          example: US
        currency:
          $ref: '#/components/schemas/CurrencyOrNull'
          example: USD
          description: Currency of the customer. Format must be ISO 4217
        email:
          type:
            - string
            - 'null'
          format: email
          example: dinesh@piedpiper.test
          description: The email of the customer
        legal_name:
          type:
            - string
            - 'null'
          example: Coleman-Blair
          description: The legal company name of the customer
        legal_number:
          type:
            - string
            - 'null'
          example: 49-008-2965
          description: The legal company number of the customer
        logo_url:
          type:
            - string
            - 'null'
          example: http://hooli.com/logo.png
          description: The logo URL of the customer
        name:
          type:
            - string
            - 'null'
          example: Gavin Belson
          description: The full name of the customer
        firstname:
          type:
            - string
            - 'null'
          example: Gavin
          description: First name of the customer
        lastname:
          type:
            - string
            - 'null'
          example: Belson
          description: Last name of the customer
        account_type:
          type: string
          enum:
            - customer
            - partner
          example: customer
          description: |-
            The type of the account. It can have one of the following values:
            - `customer`: the account is a customer.
            - `partner`: the account is a partner.
        customer_type:
          type:
            - string
            - 'null'
          enum:
            - company
            - individual
            - null
          description: |-
            The type of the customer. It can have one of the following values:
            - `company`: the customer is a company.
            - `individual`: the customer is an individual.
        phone:
          type:
            - string
            - 'null'
          example: 1-171-883-3711 x245
          description: The phone number of the customer
        state:
          type:
            - string
            - 'null'
          example: CA
          description: The state of the customer's billing address
        tax_identification_number:
          type:
            - string
            - 'null'
          example: EU123456789
          description: The tax identification number of the customer
        timezone:
          $ref: '#/components/schemas/TimezoneOrNull'
          description: >-
            The customer's timezone, used for billing purposes in their local
            time. Overrides the organization's timezone
        url:
          type:
            - string
            - 'null'
          example: http://hooli.com
          description: The custom website URL of the customer
        zipcode:
          type:
            - string
            - 'null'
          example: '91364'
          description: The zipcode of the customer's billing address
        net_payment_term:
          type:
            - integer
            - 'null'
          example: 30
          description: >-
            The net payment term, expressed in days, specifies the duration
            within which a customer is expected to remit payment after the
            invoice is finalized.
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The date of the customer creation, represented in ISO 8601 datetime
            format and expressed in Coordinated Universal Time (UTC). The
            creation_date provides a standardized and internationally recognized
            timestamp for when the customer object was created
        updated_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The date of the customer update, represented in ISO 8601 datetime
            format and expressed in Coordinated Universal Time (UTC). The
            update_date provides a standardized and internationally recognized
            timestamp for when the customer object was updated
        finalize_zero_amount_invoice:
          type: string
          enum:
            - inherit
            - skip
            - finalize
          example: inherit
          description: >-
            Specifies how invoices with a zero total amount should be handled:

            - `inherit`: (Default) Follows the organization-level configuration.

            - `finalize`: Invoices are issued and finalized even if the total
            amount is zero.

            - `skip`: Invoices with a total amount of zero are not finalized.
        skip_invoice_custom_sections:
          type: boolean
          example: false
          description: >-
            Set to true to exclude all invoice custom sections from PDF
            generation for this customer only.
        billing_configuration:
          $ref: '#/components/schemas/CustomerBillingConfiguration'
        shipping_address:
          $ref: '#/components/schemas/Address'
        metadata:
          type: array
          items:
            $ref: '#/components/schemas/CustomerMetadata'
    IntegrationCustomer:
      type: object
      required:
        - lago_id
        - type
        - external_customer_id
        - integration_code
      description: >-
        Configuration specific to the accounting and tax integrations. This
        object contains settings and parameters necessary for syncing documents
        and payments.
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            A unique identifier for the integration customer object in the Lago
            application.
        type:
          type: string
          example: netsuite
          description: |-
            The integration type used for accounting and tax syncs.
            Accepted values: `netsuite, anrok`.
          enum:
            - netsuite
            - anrok
            - xero
            - hubspot
            - salesforce
        integration_code:
          type: string
          example: netsuite-eu-1
          description: Unique code used to identify an integration connection.
        external_customer_id:
          type: string
          example: cus_12345
          description: >-
            The customer ID within the integration's system. If this field is
            not provided, Lago has the option to create a new customer record
            within the integration's system on behalf of the customer.
        sync_with_provider:
          type:
            - boolean
            - 'null'
          example: true
          description: >-
            Set this field to `true` if you want to create a customer record in
            the integration's system. This option is applicable only when the
            `external_customer_id` is null and the `sync_with_provider` field is
            set to `true`. By default, the value is set to `false`
        subsidiary_id:
          type: string
          example: '2'
          description: >-
            This optional field is needed only when working with `netsuite`
            connection.
        targeted_object:
          type:
            - string
            - 'null'
          example: contacts
          description: >-
            This optional field is present only when working with `hubspot`
            connection.
        email:
          type:
            - string
            - 'null'
          example: dinesh@piedpiper.test
          description: >-
            This optional field is present only when working with `hubspot`
            connection.
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
    Timezone:
      type: string
      example: America/Los_Angeles
      enum:
        - UTC
        - Africa/Algiers
        - Africa/Cairo
        - Africa/Casablanca
        - Africa/Harare
        - Africa/Johannesburg
        - Africa/Monrovia
        - Africa/Nairobi
        - America/Argentina/Buenos_Aires
        - America/Bogota
        - America/Caracas
        - America/Chicago
        - America/Chihuahua
        - America/Denver
        - America/Guatemala
        - America/Guyana
        - America/Halifax
        - America/Indiana/Indianapolis
        - America/Juneau
        - America/La_Paz
        - America/Lima
        - America/Los_Angeles
        - America/Mazatlan
        - America/Mexico_City
        - America/Monterrey
        - America/Montevideo
        - America/New_York
        - America/Nuuk
        - America/Phoenix
        - America/Puerto_Rico
        - America/Regina
        - America/Santiago
        - America/Sao_Paulo
        - America/St_Johns
        - America/Tijuana
        - Asia/Almaty
        - Asia/Baghdad
        - Asia/Baku
        - Asia/Bangkok
        - Asia/Chongqing
        - Asia/Colombo
        - Asia/Dhaka
        - Asia/Hong_Kong
        - Asia/Irkutsk
        - Asia/Jakarta
        - Asia/Jerusalem
        - Asia/Kabul
        - Asia/Kamchatka
        - Asia/Karachi
        - Asia/Kathmandu
        - Asia/Kolkata
        - Asia/Krasnoyarsk
        - Asia/Kuala_Lumpur
        - Asia/Kuwait
        - Asia/Magadan
        - Asia/Muscat
        - Asia/Novosibirsk
        - Asia/Riyadh
        - Asia/Seoul
        - Asia/Shanghai
        - Asia/Singapore
        - Asia/Srednekolymsk
        - Asia/Taipei
        - Asia/Tashkent
        - Asia/Tbilisi
        - Asia/Tehran
        - Asia/Tokyo
        - Asia/Ulaanbaatar
        - Asia/Urumqi
        - Asia/Vladivostok
        - Asia/Yakutsk
        - Asia/Yangon
        - Asia/Yekaterinburg
        - Asia/Yerevan
        - Atlantic/Azores
        - Atlantic/Cape_Verde
        - Atlantic/South_Georgia
        - Australia/Adelaide
        - Australia/Brisbane
        - Australia/Darwin
        - Australia/Hobart
        - Australia/Melbourne
        - Australia/Perth
        - Australia/Sydney
        - Europe/Amsterdam
        - Europe/Athens
        - Europe/Belgrade
        - Europe/Berlin
        - Europe/Bratislava
        - Europe/Brussels
        - Europe/Bucharest
        - Europe/Budapest
        - Europe/Copenhagen
        - Europe/Dublin
        - Europe/Helsinki
        - Europe/Istanbul
        - Europe/Kaliningrad
        - Europe/Kyiv
        - Europe/Lisbon
        - Europe/Ljubljana
        - Europe/London
        - Europe/Madrid
        - Europe/Minsk
        - Europe/Moscow
        - Europe/Paris
        - Europe/Prague
        - Europe/Riga
        - Europe/Rome
        - Europe/Samara
        - Europe/Sarajevo
        - Europe/Skopje
        - Europe/Sofia
        - Europe/Stockholm
        - Europe/Tallinn
        - Europe/Vienna
        - Europe/Vilnius
        - Europe/Volgograd
        - Europe/Warsaw
        - Europe/Zagreb
        - Europe/Zurich
        - GMT+12
        - Pacific/Apia
        - Pacific/Auckland
        - Pacific/Chatham
        - Pacific/Fakaofo
        - Pacific/Fiji
        - Pacific/Guadalcanal
        - Pacific/Guam
        - Pacific/Honolulu
        - Pacific/Majuro
        - Pacific/Midway
        - Pacific/Noumea
        - Pacific/Pago_Pago
        - Pacific/Port_Moresby
        - Pacific/Tongatapu
    CountryOrNull:
      type:
        - string
        - 'null'
      example: US
      enum:
        - null
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
    CurrencyOrNull:
      type:
        - string
        - 'null'
      example: USD
      enum:
        - null
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
    TimezoneOrNull:
      type:
        - string
        - 'null'
      example: America/Los_Angeles
      enum:
        - null
        - UTC
        - Africa/Algiers
        - Africa/Cairo
        - Africa/Casablanca
        - Africa/Harare
        - Africa/Johannesburg
        - Africa/Monrovia
        - Africa/Nairobi
        - America/Argentina/Buenos_Aires
        - America/Bogota
        - America/Caracas
        - America/Chicago
        - America/Chihuahua
        - America/Denver
        - America/Godthab
        - America/Guatemala
        - America/Guyana
        - America/Halifax
        - America/Indiana/Indianapolis
        - America/Juneau
        - America/La_Paz
        - America/Lima
        - America/Los_Angeles
        - America/Mazatlan
        - America/Mexico_City
        - America/Monterrey
        - America/Montevideo
        - America/New_York
        - America/Phoenix
        - America/Puerto_Rico
        - America/Regina
        - America/Santiago
        - America/Sao_Paulo
        - America/St_Johns
        - America/Tijuana
        - Asia/Almaty
        - Asia/Baghdad
        - Asia/Baku
        - Asia/Bangkok
        - Asia/Chongqing
        - Asia/Colombo
        - Asia/Dhaka
        - Asia/Hong_Kong
        - Asia/Irkutsk
        - Asia/Jakarta
        - Asia/Jerusalem
        - Asia/Kabul
        - Asia/Kamchatka
        - Asia/Karachi
        - Asia/Kathmandu
        - Asia/Kolkata
        - Asia/Krasnoyarsk
        - Asia/Kuala_Lumpur
        - Asia/Kuwait
        - Asia/Magadan
        - Asia/Muscat
        - Asia/Novosibirsk
        - Asia/Rangoon
        - Asia/Riyadh
        - Asia/Seoul
        - Asia/Shanghai
        - Asia/Singapore
        - Asia/Srednekolymsk
        - Asia/Taipei
        - Asia/Tashkent
        - Asia/Tbilisi
        - Asia/Tehran
        - Asia/Tokyo
        - Asia/Ulaanbaatar
        - Asia/Urumqi
        - Asia/Vladivostok
        - Asia/Yakutsk
        - Asia/Yekaterinburg
        - Asia/Yerevan
        - Atlantic/Azores
        - Atlantic/Cape_Verde
        - Atlantic/South_Georgia
        - Australia/Adelaide
        - Australia/Brisbane
        - Australia/Darwin
        - Australia/Hobart
        - Australia/Melbourne
        - Australia/Perth
        - Australia/Sydney
        - Europe/Amsterdam
        - Europe/Athens
        - Europe/Belgrade
        - Europe/Berlin
        - Europe/Bratislava
        - Europe/Brussels
        - Europe/Bucharest
        - Europe/Budapest
        - Europe/Copenhagen
        - Europe/Dublin
        - Europe/Helsinki
        - Europe/Istanbul
        - Europe/Kaliningrad
        - Europe/Kiev
        - Europe/Lisbon
        - Europe/Ljubljana
        - Europe/London
        - Europe/Madrid
        - Europe/Minsk
        - Europe/Moscow
        - Europe/Paris
        - Europe/Prague
        - Europe/Riga
        - Europe/Rome
        - Europe/Samara
        - Europe/Sarajevo
        - Europe/Skopje
        - Europe/Sofia
        - Europe/Stockholm
        - Europe/Tallinn
        - Europe/Vienna
        - Europe/Vilnius
        - Europe/Volgograd
        - Europe/Warsaw
        - Europe/Zagreb
        - Europe/Zurich
        - GMT+12
        - Pacific/Apia
        - Pacific/Auckland
        - Pacific/Chatham
        - Pacific/Fakaofo
        - Pacific/Fiji
        - Pacific/Guadalcanal
        - Pacific/Guam
        - Pacific/Honolulu
        - Pacific/Majuro
        - Pacific/Midway
        - Pacific/Noumea
        - Pacific/Pago_Pago
        - Pacific/Port_Moresby
        - Pacific/Tongatapu
    CustomerBillingConfiguration:
      type: object
      description: >-
        Configuration specific to the payment provider, utilized for billing the
        customer. This object contains settings and parameters necessary for
        processing payments and invoicing the customer.
      properties:
        invoice_grace_period:
          type: integer
          example: 3
          description: >-
            The grace period, expressed in days, for the invoice. This period
            refers to the additional time granted to the customer beyond the
            invoice due date to adjust usage and line items
        subscription_invoice_issuing_date_anchor:
          type:
            - string
            - 'null'
          example: next_period_start
          description: >-
            Defines whether the issuing date follows the current billing
            period's end date or the next period starting date.
          enum:
            - current_period_end
            - next_period_start
            - null
          default: null
        subscription_invoice_issuing_date_adjustment:
          type:
            - string
            - 'null'
          example: keep_anchor
          description: >-
            The logic applied on top of the
            subscription_invoice_issuing_date_anchor rule. You can opt to use
            the invoice finalization date, that includes any configured grace
            period.
          enum:
            - align_with_finalization_date
            - keep_anchor
            - null
          default: null
        payment_provider:
          type: string
          example: stripe
          description: >-
            The payment provider utilized to initiate payments for invoices
            issued by Lago.

            Accepted values: `stripe`, `adyen`, `gocardless` or null. This field
            is required if you intend to assign a `provider_customer_id`.
          enum:
            - stripe
            - adyen
            - gocardless
        payment_provider_code:
          type: string
          example: stripe-eu-1
          description: Unique code used to identify a payment provider connection.
        provider_customer_id:
          type: string
          example: cus_12345
          description: >-
            The customer ID within the payment provider's system. If this field
            is not provided, Lago has the option to create a new customer record
            within the payment provider's system on behalf of the customer
        sync:
          type: boolean
          example: true
          description: >-
            Set this field to `true` if you want to create the customer in the
            payment provider synchronously with the customer creation process in
            Lago. This option is applicable only when the `provider_customer_id`
            is `null` and the customer is automatically created in the payment
            provider through Lago. By default, the value is set to `false`
        sync_with_provider:
          type: boolean
          example: true
          description: >-
            Set this field to `true` if you want to create a customer record in
            the payment provider's system. This option is applicable only when
            the `provider_customer_id` is null and the `sync_with_provider`
            field is set to `true`. By default, the value is set to `false`
        document_locale:
          type: string
          example: fr
          description: >-
            The document locale, specified in the ISO 639-1 format. This field
            represents the language or locale used for the documents issued by
            Lago
        provider_payment_methods:
          type:
            - array
            - 'null'
          items:
            type: string
          description: >-
            Specifies the available payment methods that can be used for this
            customer when `payment_provider` is set to `stripe`. The
            `provider_payment_methods` field is an array that allows multiple
            payment options to be defined. If this field is not explicitly set,
            the payment methods will be set to `card`. For now, possible values
            are `card`, `sepa_debit`, `us_bank_account`, `bacs_debit`, `boleto`,
            `link`, `crypto` and `customer_balance`. Note that when `link` is
            selected, `card` should also be provided in the array. When
            `customer_balance` is selected, no other payment can be selected.
          example:
            - card
            - sepa_debit
            - us_bank_account
            - bacs_debit
            - link
            - boleto
            - crypto
            - customer_balance
    Address:
      type: object
      description: >-
        Configuration specific to the payment provider, utilized for billing the
        customer. This object contains settings and parameters necessary for
        processing payments and invoicing the customer.
      properties:
        address_line1:
          type:
            - string
            - 'null'
          example: 5230 Penfield Ave
          description: The first line of the billing address
        address_line2:
          type:
            - string
            - 'null'
          example: null
          description: The second line of the billing address
        city:
          type:
            - string
            - 'null'
          example: Woodland Hills
          description: The city of the customer's billing address
        country:
          $ref: '#/components/schemas/CountryOrNull'
          description: >-
            Country code of the customer's billing address. Format must be ISO
            3166 (alpha-2)
          example: US
        state:
          type:
            - string
            - 'null'
          example: CA
          description: The state of the customer's billing address
        zipcode:
          type:
            - string
            - 'null'
          example: '91364'
          description: The zipcode of the customer's billing address
    CustomerMetadata:
      type: object
      description: >-
        Set of key-value pairs that you can attach to a customer. This can be
        useful for storing additional information about the customer in a
        structured format
      required:
        - lago_id
        - key
        - value
        - display_in_invoice
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            A unique identifier for the customer metadata object in the Lago
            application. Can be used to update a key-value pair
        key:
          type: string
          example: Purchase Order
          description: The metadata object key
        value:
          type: string
          example: '123456789'
          description: The metadata object value
        display_in_invoice:
          type: boolean
          example: true
          description: >-
            Determines whether the item or information should be displayed in
            the invoice. If set to true, the item or information will be
            included and visible in the generated invoice. If set to false, the
            item or information will be excluded and not displayed in the
            invoice.
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The date of the metadata object creation, represented in ISO 8601
            datetime format and expressed in Coordinated Universal Time (UTC).
            The creation_date provides a standardized and internationally
            recognized timestamp for when the metadata object was created
  responses:
    Unauthorized:
      description: Unauthorized error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnauthorized'
    NotFound:
      description: Not Found error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorNotFound'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````