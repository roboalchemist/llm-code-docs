# Source: https://getlago.com/docs/api-reference/wallets/get-specific-transaction.md

# Retrieve a transaction

> This endpoint is used to retrieve a specific wallet transactions.

## OpenAPI

````yaml GET /wallet_transactions/{lago_id}
paths:
  path: /wallet_transactions/{lago_id}
  method: get
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
      path:
        lago_id:
          schema:
            - type: string
              required: true
              description: >-
                Unique identifier assigned to the wallet transaction within the
                Lago application. This ID is exclusively created by Lago and
                serves as a unique identifier for the wallet's record within the
                Lago system.
              format: uuid
              example: bb0a27be-51f7-4f4f-aad0-2abc80534c0f
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              lago_id:
                allOf:
                  - type: string
                    format: uuid
                    description: >-
                      Unique identifier assigned to the wallet transaction
                      within the Lago application. This ID is exclusively
                      created by Lago and serves as a unique identifier for the
                      wallet transaction's record within the Lago system.
                    example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              lago_wallet_id:
                allOf:
                  - type: string
                    format: uuid
                    description: >-
                      Unique identifier assigned to the wallet within the Lago
                      application. This ID is exclusively created by Lago and
                      serves as a unique identifier for the wallet's record
                      within the Lago system.
                    example: 1a901a90-1a90-1a90-1a90-1a901a901a90
              status:
                allOf:
                  - type: string
                    enum:
                      - pending
                      - settled
                      - failed
                    description: >-
                      The status of the wallet transaction. Possible values are
                      `pending`, `settled` or `failed`.
                    example: settled
              source:
                allOf:
                  - type: string
                    enum:
                      - manual
                      - interval
                      - threshold
                    description: >-
                      The source field represents the origin or trigger of the
                      wallet transaction. Possible values are `manual`,
                      `interval`, `threshold`
                    example: manual
              transaction_status:
                allOf:
                  - type: string
                    enum:
                      - purchased
                      - granted
                      - voided
                      - invoiced
                    description: >-
                      The transaction status of the wallet transaction. Possible
                      values are `purchased` (with pending or settled status),
                      `granted` (without invoice_id), `voided` or `invoiced`.
                    example: purchased
              transaction_type:
                allOf:
                  - type: string
                    enum:
                      - inbound
                      - outbound
                    description: >-
                      The type of transaction. Possible values are `inbound`
                      (increasing the balance) or `outbound` (decreasing the
                      balance).
                    example: inbound
              amount:
                allOf:
                  - type: string
                    pattern: ^[0-9]+.?[0-9]*$
                    description: The amount of credits based on the rate and the currency.
                    example: '10.0'
              credit_amount:
                allOf:
                  - type: string
                    pattern: ^[0-9]+.?[0-9]*$
                    description: The number of credits used in the wallet transaction.
                    example: '100.0'
              invoice_requires_successful_payment:
                allOf:
                  - type: boolean
                    description: >-
                      A boolean setting that, when set to true, delays issuing
                      an invoice for a wallet top-up until a successful payment
                      is made; if false, the invoice is issued immediately upon
                      wallet top-up, regardless of the payment status. Default
                      value of false.
                    example: false
              metadata:
                allOf:
                  - type: array
                    description: >-
                      This field allows you to store a list of key-value pairs
                      that hold additional information or custom attributes
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
              settled_at:
                allOf:
                  - type:
                      - string
                      - 'null'
                    format: date-time
                    description: >-
                      The date when wallet transaction is settled, represented
                      in ISO 8601 datetime format and expressed in Coordinated
                      Universal Time (UTC).
                    example: '2022-04-29T08:59:51Z'
              failed_at:
                allOf:
                  - type:
                      - string
                      - 'null'
                    format: date-time
                    description: >-
                      The date when the wallet transaction failed, represented
                      in ISO 8601 datetime format and expressed in Coordinated
                      Universal Time (UTC).
                    example: '2022-04-29T08:59:51Z'
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: >-
                      The date of the wallet transaction creation, represented
                      in ISO 8601 datetime format and expressed in Coordinated
                      Universal Time (UTC).
                    example: '2022-04-29T08:59:51Z'
              name:
                allOf:
                  - type:
                      - string
                      - 'null'
                    description: >-
                      The name of the wallet transaction. It will appear on the
                      invoice as the label for the fee. If not set, the label on
                      the invoice will fallback to either `Prepaid credits -
                      {{wallet_name}}` if the wallet name is set, or `Prepaid
                      credits`.
                    example: Tokens for models 'high-fidelity-boost'
            refIdentifier: '#/components/schemas/WalletTransactionObject'
            requiredProperties:
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
        examples:
          example:
            value:
              lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
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
        description: Wallet transaction
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
  deprecated: false
  type: path
components:
  schemas: {}

````