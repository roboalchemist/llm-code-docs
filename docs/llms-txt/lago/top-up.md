# Source: https://getlago.com/docs/api-reference/wallets/top-up.md

# Top-up a wallet

> This endpoint is used to top-up an active wallet.

## OpenAPI

````yaml POST /wallet_transactions
paths:
  path: /wallet_transactions
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
              wallet_transaction:
                allOf:
                  - type: object
                    required:
                      - wallet_id
                    properties:
                      wallet_id:
                        type: string
                        format: uuid
                        description: >-
                          Unique identifier assigned to the wallet within the
                          Lago application. This ID is exclusively created by
                          Lago and serves as a unique identifier for the
                          wallet's record within the Lago system.
                        example: 1a901a90-1a90-1a90-1a90-1a901a901a90
                      name:
                        type:
                          - string
                          - 'null'
                        description: >
                          The name of the wallet transaction. It will appear on
                          the invoice as the label for the fee. If not set, the
                          label on the invoice will fallback to either `Prepaid
                          credits - {{wallet_name}}` if the wallet name is set,
                          or `Prepaid credits`.


                          Note that this name will apply to all transactions
                          (`paid_credits`, `granted_credits` and
                          `voided_credits`) created by this action.
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
                          A boolean setting that, when set to true, delays
                          issuing an invoice for a wallet top-up until a
                          successful payment is made; if false, the invoice is
                          issued immediately upon wallet top-up, regardless of
                          the payment status. Default value of false.
                        example: false
                      ignore_paid_top_up_limits:
                        type: boolean
                        description: >-
                          When true, allows topping up the wallet with
                          transactions that exceed the paid top-up limits.
                          Defaults to false.
                        example: false
                      metadata:
                        type:
                          - array
                          - 'null'
                        description: >-
                          This optional field allows you to store a list of
                          key-value pairs that hold additional information or
                          custom attributes related to the data.
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
            required: true
            refIdentifier: '#/components/schemas/WalletTransactionCreateInput'
            requiredProperties:
              - wallet_transaction
        examples:
          example:
            value:
              wallet_transaction:
                wallet_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                name: Tokens for models 'high-fidelity-boost'
                paid_credits: '20.0'
                granted_credits: '10.0'
                voided_credits: '5.0'
                invoice_requires_successful_payment: false
                ignore_paid_top_up_limits: false
                metadata:
                  - key: example key
                    value: example value
                  - key: another key
                    value: another value
        description: Wallet transaction payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              wallet_transactions:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/WalletTransactionObject'
            refIdentifier: '#/components/schemas/WalletTransactions'
            requiredProperties:
              - wallet_transactions
        examples:
          example:
            value:
              wallet_transactions:
                - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  lago_wallet_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  status: settled
                  source: manual
                  transaction_status: purchased
                  transaction_type: inbound
                  amount: '10.0'
                  credit_amount: '100.0'
                  invoice_requires_successful_payment: false
                  metadata:
                    - key: example key
                      value: example value
                    - key: another key
                      value: another value
                  settled_at: '2022-04-29T08:59:51Z'
                  failed_at: '2022-04-29T08:59:51Z'
                  created_at: '2022-04-29T08:59:51Z'
                  name: Tokens for models 'high-fidelity-boost'
        description: Wallet transaction created
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
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 403
              error:
                allOf:
                  - type: string
                    example: Forbidden
              code:
                allOf:
                  - type: string
                    example: feature_unavailable
            refIdentifier: '#/components/schemas/ApiErrorForbidden'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 403
              error: Forbidden
              code: feature_unavailable
        description: Forbidden
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

````