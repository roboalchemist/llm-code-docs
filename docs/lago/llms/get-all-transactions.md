# Source: https://getlago.com/docs/api-reference/wallets/get-all-transactions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all wallet transactions

> This endpoint is used to list all wallet transactions.

<RequestExample>
  ```bash cURL theme={"dark"}
  LAGO_URL="https://api.getlago.com"
  API_KEY="__YOUR_API_KEY__"

  curl --location --request GET "$LAGO_URL/api/v1/wallets/:id/wallet_transactions?per_page=2&page=1" \
    --header "Authorization: Bearer $API_KEY"
  ```

  ```python Python theme={"dark"}
  from lago_python_client.client import Client
  from lago_python_client.exceptions import LagoApiError

  client = Client(api_key='__YOUR_API_KEY__')

  try:
      client.wallet_transactions.find_all({'per_page': 2, 'page': 1})
  except LagoApiError as e:
      repair_broken_state(e)  # do something on error or raise your own exception
  ```

  ```ruby Ruby theme={"dark"}
  require 'lago-ruby-client'

  client = Lago::Api::Client.new(api_key: '__YOUR_API_KEY__')

  client.wallet_transactions.get_all({ per_page: 2, page: 3 })
  ```

  ```js Javascript theme={"dark"}
  await client.wallets.findAllWalletTransactions("wallet-id", {
    per_page: 2,
    page: 3,
  });
  ```

  ```go Go theme={"dark"}
  import "fmt"
  import "github.com/getlago/lago-go-client"

  func main() {
  lagoClient := lago.New().
      SetApiKey("__YOUR_API_KEY__")

  walletTransactionListInput := &lago.WalletTransactionListInput{
      PerPage: 1,
      Page: 1,
      WalletId: 12345,
  }

  walletTransactionResult, err := lagoClient.WalletTransaction().GetList(walletTransactionListInput)
  if err != nil {
      // Error is *lago.Error
      panic(err)
  }

  // walletTransactionResult is *lago.WalletTransactionResult
  fmt.Println(walletTransactionResult)
  }
  ```
</RequestExample>


## OpenAPI

````yaml GET /wallets/{lago_id}/wallet_transactions
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
  /wallets/{lago_id}/wallet_transactions:
    get:
      tags:
        - wallets
      summary: List all wallet transactions
      description: This endpoint is used to list all wallet transactions.
      operationId: findAllWalletTransactions
      parameters:
        - name: lago_id
          in: path
          description: >-
            Unique identifier assigned to the wallet within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the wallet's record within the Lago system.
          required: true
          schema:
            type: string
            format: uuid
            example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        - $ref: '#/components/parameters/page'
        - $ref: '#/components/parameters/per_page'
        - name: status
          in: query
          description: >-
            The status of the wallet transaction. Possible values are `pending`
            or `settled`.
          required: false
          explode: true
          schema:
            type: string
            example: pending
        - name: transaction_status
          in: query
          description: >-
            The transaction status of the wallet transaction. Possible values
            are `purchased` (with pending or settled status), `granted` (without
            invoice_id), `voided` or `invoiced`.
          required: false
          explode: true
          schema:
            type: string
            example: purchased
        - name: transaction_type
          in: query
          description: >-
            The transaction type of the wallet transaction. Possible values are
            `inbound` (increasing the wallet balance) or `outbound` (decreasing
            the wallet balance).
          required: false
          explode: true
          schema:
            type: string
            example: inbound
      responses:
        '200':
          description: Wallet transactions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WalletTransactionsPaginated'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  parameters:
    page:
      name: page
      in: query
      description: Page number.
      required: false
      explode: true
      schema:
        type: integer
        example: 1
    per_page:
      name: per_page
      in: query
      description: Number of records per page.
      required: false
      explode: true
      schema:
        type: integer
        example: 20
  schemas:
    WalletTransactionsPaginated:
      allOf:
        - $ref: '#/components/schemas/WalletTransactions'
        - type: object
          required:
            - meta
          properties:
            meta:
              $ref: '#/components/schemas/PaginationMeta'
    WalletTransactions:
      type: object
      required:
        - wallet_transactions
      properties:
        wallet_transactions:
          type: array
          items:
            $ref: '#/components/schemas/WalletTransactionObject'
    PaginationMeta:
      type: object
      required:
        - current_page
        - total_pages
        - total_count
      properties:
        current_page:
          type: integer
          description: Current page.
          example: 2
        next_page:
          type:
            - integer
            - 'null'
          description: Next page.
          example: 3
        prev_page:
          type:
            - integer
            - 'null'
          description: Previous page.
          example: 1
        total_pages:
          type: integer
          description: Total number of pages.
          example: 4
        total_count:
          type: integer
          description: Total number of records.
          example: 70
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
  responses:
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````