# Source: https://getlago.com/docs/api-reference/wallets/wallet-transaction-payment-url.md

# Generate a payment URL

> This endpoint generates a checkout link for a specific wallet transaction.

## OpenAPI

````yaml POST /wallet_transactions/{lago_id}/payment_url
paths:
  path: /wallet_transactions/{lago_id}/payment_url
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
      path:
        lago_id:
          schema:
            - type: string
              required: true
              description: ID of the wallet transaction.
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
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
              wallet_transaction_payment_details:
                allOf:
                  - type: object
                    properties:
                      lago_customer_id:
                        type: string
                        example: 1a901a90-1a90-1a90-1a90-1a901a901a90
                        description: >-
                          Unique identifier assigned to the customer within the
                          Lago application. This ID is exclusively created by
                          Lago and serves as a unique identifier for the
                          customer's record within the Lago system
                      lago_wallet_transaction_id:
                        type: string
                        example: 1e501a90-1a90-1a90-1a90-1a901a901a80
                        description: >-
                          Unique identifier assigned to the wallet transaction
                          within the Lago application. This ID is exclusively
                          created by Lago and serves as a unique identifier for
                          the wallet transaction's record within the Lago system
                      external_customer_id:
                        type: string
                        example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                        description: >-
                          The customer external unique identifier (provided by
                          your own application)
                      payment_provider:
                        type: string
                        example: stripe
                        description: The Payment Provider name linked to the Customer.
                      payment_url:
                        type: string
                        example: https://foo.bar
                        description: The generated Payment URL for the Wallet transaction.
            description: .
            refIdentifier: '#/components/schemas/WalletTransactionPaymentUrl'
            requiredProperties:
              - lago_wallet_transaction_id
              - lago_customer_id
              - external_customer_id
              - payment_provider
        examples:
          example:
            value:
              wallet_transaction_payment_details:
                lago_customer_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_wallet_transaction_id: 1e501a90-1a90-1a90-1a90-1a901a901a80
                external_customer_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                payment_provider: stripe
                payment_url: https://foo.bar
        description: Payment URL has been generated
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
  schemas: {}

````