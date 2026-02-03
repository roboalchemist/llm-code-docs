# Source: https://getlago.com/docs/api-reference/wallets/top-up.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Top-up a wallet

> This endpoint is used to top-up an active wallet.

<RequestExample>
  ```bash cURL theme={"dark"}
  LAGO_URL="https://api.getlago.com"
  API_KEY="__YOUR_API_KEY__"

  curl --location --request POST "$LAGO_URL/api/v1/wallet_transactions" \
    --header "Authorization: Bearer $API_KEY" \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "wallet_transaction": {
        "wallet_id": "wallet_1234",
        "paid_credits": "20.0",
        "granted_credits": "10.0"
      }
    }'
  ```

  ```python Python theme={"dark"}
  from lago_python_client.client import Client
  from lago_python_client.exceptions import LagoApiError
  from lago_python_client.models import WalletTransaction

  client = Client(api_key='__YOUR_API_KEY__')

  transaction = WalletTransaction(
    wallet_id='wallet_1234',
    paid_credits='20.0',
    granted_credits='10.0'
  )

  try:
      client.wallet_transactions.create(transaction)
  except LagoApiError as e:
      repair_broken_state(e)  # do something on error or raise your own exception
  ```

  ```ruby Ruby theme={"dark"}
  require 'lago-ruby-client'

  client = Lago::Api::Client.new(api_key: '__YOUR_API_KEY__')

  client.wallet_transactions.create({
      wallet_id: 'wallet_1234',
      paid_credits: '20.0',
      granted_credits: '10.0'
  })
  ```

  ```js Javascript theme={"dark"}
  await client.walletTransactions.createWalletTransaction({
    wallet_transaction: {
      wallet_id: "wallet_1234",
      paid_credits: 20.0,
      granted_credits: 10.0,
    },
  });
  ```

  ```go Go theme={"dark"}
  import "fmt"
  import "github.com/getlago/lago-go-client"

  func main() {
  lagoClient := lago.New().
      SetApiKey("__YOUR_API_KEY__")

  walletTransactionInput := &lago.WalletTransactionInput{
      WalletId:           "wallet_1234",
      PaidCredits:        "20.0"
      GrantedCredits:     "10.0",
  }

  transactions, err := lagoClient.WalletTransaction().Create(walletTransactionInput)
  if err != nil {
      // Error is *lago.Error
      panic(err)
  }

  // wallet is *lago.Wallet
  fmt.Println(transactions)
  }
  ```
</RequestExample>


## OpenAPI

````yaml POST /wallet_transactions
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
  /wallet_transactions:
    post:
      tags:
        - wallets
      summary: Top up a wallet
      description: This endpoint is used to top-up an active wallet.
      operationId: createWalletTransaction
      requestBody:
        description: Wallet transaction payload
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WalletTransactionCreateInput'
        required: true
      responses:
        '200':
          description: Wallet transaction created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WalletTransactions'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
components:
  schemas:
    WalletTransactionCreateInput:
      type: object
      required:
        - wallet_transaction
      properties:
        wallet_transaction:
          type: object
          required:
            - wallet_id
          properties:
            wallet_id:
              type: string
              format: uuid
              description: >-
                Unique identifier assigned to the wallet within the Lago
                application. This ID is exclusively created by Lago and serves
                as a unique identifier for the wallet's record within the Lago
                system.
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
            name:
              type:
                - string
                - 'null'
              description: >
                The name of the wallet transaction. It will appear on the
                invoice as the label for the fee. If not set, the label on the
                invoice will fallback to either `Prepaid credits -
                {{wallet_name}}` if the wallet name is set, or `Prepaid
                credits`.


                Note that this name will apply to all transactions
                (`paid_credits`, `granted_credits` and `voided_credits`) created
                by this action.
              example: Tokens for models 'high-fidelity-boost'
            paid_credits:
              type:
                - string
                - 'null'
              pattern: ^[0-9]+.?[0-9]*$
              description: The number of paid credits.
              example: '20.0'
            granted_credits:
              type:
                - string
                - 'null'
              pattern: ^[0-9]+.?[0-9]*$
              description: The number of free granted credits.
              example: '10.0'
            voided_credits:
              type:
                - string
                - 'null'
              pattern: ^[0-9]+.?[0-9]*$
              description: The number of voided credits.
              example: '5.0'
            invoice_requires_successful_payment:
              type: boolean
              description: >-
                A boolean setting that, when set to true, delays issuing an
                invoice for a wallet top-up until a successful payment is made;
                if false, the invoice is issued immediately upon wallet top-up,
                regardless of the payment status. Default value of false.
              example: false
            ignore_paid_top_up_limits:
              type: boolean
              description: >-
                When true, allows topping up the wallet with transactions that
                exceed the paid top-up limits. Defaults to false.
              example: false
            metadata:
              type:
                - array
                - 'null'
              description: >-
                This optional field allows you to store a list of key-value
                pairs that hold additional information or custom attributes
                related to the data.
              items:
                type: object
                properties:
                  key:
                    type: string
                    description: The unique identifier for the attribute.
                  value:
                    type: string
                    description: The value associated with the key.
              example:
                - key: example key
                  value: example value
                - key: another key
                  value: another value
    WalletTransactions:
      type: object
      required:
        - wallet_transactions
      properties:
        wallet_transactions:
          type: array
          items:
            $ref: '#/components/schemas/WalletTransactionObject'
    WalletTransactionObject:
      type: object
      required:
        - lago_id
        - lago_wallet_id
        - status
        - source
        - transaction_status
        - transaction_type
        - credit_amount
        - amount
        - created_at
        - name
      properties:
        lago_id:
          type: string
          format: uuid
          description: >-
            Unique identifier assigned to the wallet transaction within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the wallet transaction's record within the
            Lago system.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_wallet_id:
          type: string
          format: uuid
          description: >-
            Unique identifier assigned to the wallet within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the wallet's record within the Lago system.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        status:
          type: string
          enum:
            - pending
            - settled
            - failed
          description: >-
            The status of the wallet transaction. Possible values are `pending`,
            `settled` or `failed`.
          example: settled
        source:
          type: string
          enum:
            - manual
            - interval
            - threshold
          description: >-
            The source field represents the origin or trigger of the wallet
            transaction. Possible values are `manual`, `interval`, `threshold`
          example: manual
        transaction_status:
          type: string
          enum:
            - purchased
            - granted
            - voided
            - invoiced
          description: >-
            The transaction status of the wallet transaction. Possible values
            are `purchased` (with pending or settled status), `granted` (without
            invoice_id), `voided` or `invoiced`.
          example: purchased
        transaction_type:
          type: string
          enum:
            - inbound
            - outbound
          description: >-
            The type of transaction. Possible values are `inbound` (increasing
            the balance) or `outbound` (decreasing the balance).
          example: inbound
        amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: The amount of credits based on the rate and the currency.
          example: '10.0'
        credit_amount:
          type: string
          pattern: ^[0-9]+.?[0-9]*$
          description: The number of credits used in the wallet transaction.
          example: '100.0'
        invoice_requires_successful_payment:
          type: boolean
          description: >-
            A boolean setting that, when set to true, delays issuing an invoice
            for a wallet top-up until a successful payment is made; if false,
            the invoice is issued immediately upon wallet top-up, regardless of
            the payment status. Default value of false.
          example: false
        metadata:
          type: array
          description: >-
            This field allows you to store a list of key-value pairs that hold
            additional information or custom attributes related to the data.
          items:
            type: object
            properties:
              key:
                type: string
                description: The unique identifier for the attribute.
              value:
                type: string
                description: The value associated with the key.
          example:
            - key: example key
              value: example value
            - key: another key
              value: another value
        settled_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date when wallet transaction is settled, represented in ISO 8601
            datetime format and expressed in Coordinated Universal Time (UTC).
          example: '2022-04-29T08:59:51Z'
        failed_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date when the wallet transaction failed, represented in ISO 8601
            datetime format and expressed in Coordinated Universal Time (UTC).
          example: '2022-04-29T08:59:51Z'
        created_at:
          type: string
          format: date-time
          description: >-
            The date of the wallet transaction creation, represented in ISO 8601
            datetime format and expressed in Coordinated Universal Time (UTC).
          example: '2022-04-29T08:59:51Z'
        name:
          type:
            - string
            - 'null'
          description: >-
            The name of the wallet transaction. It will appear on the invoice as
            the label for the fee. If not set, the label on the invoice will
            fallback to either `Prepaid credits - {{wallet_name}}` if the wallet
            name is set, or `Prepaid credits`.
          example: Tokens for models 'high-fidelity-boost'
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