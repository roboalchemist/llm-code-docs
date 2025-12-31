# Source: https://getlago.com/docs/api-reference/customers/psp-checkout-url.md

# Regenerate checkout URL

> This endpoint regenerates the Payment Provider Checkout URL of a Customer.

## OpenAPI

````yaml POST /customers/{external_customer_id}/checkout_url
paths:
  path: /customers/{external_customer_id}/checkout_url
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
        external_customer_id:
          schema:
            - type: string
              required: true
              description: >-
                The customer external unique identifier (provided by your own
                application).
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
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
              customer:
                allOf:
                  - type: object
                    required:
                      - lago_customer_id
                      - external_customer_id
                      - payment_provider
                    properties:
                      lago_customer_id:
                        type: string
                        example: 1a901a90-1a90-1a90-1a90-1a901a901a90
                        description: >-
                          Unique identifier assigned to the customer within the
                          Lago application. This ID is exclusively created by
                          Lago and serves as a unique identifier for the
                          customer's record within the Lago system
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
                      payment_provider_code:
                        type: string
                        description: Code of the payment provider
                        example: Stripe Prod
                      checkout_url:
                        type: string
                        example: https://foo.bar
                        description: >-
                          The new generated Payment Provider Checkout URL for
                          the Customer.
            description: .
            refIdentifier: '#/components/schemas/CustomerCheckoutUrl'
        examples:
          example:
            value:
              customer:
                lago_customer_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                external_customer_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                payment_provider: stripe
                payment_provider_code: Stripe Prod
                checkout_url: https://foo.bar
        description: Customer Checkout URL
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