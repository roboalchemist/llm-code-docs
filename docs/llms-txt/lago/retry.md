# Source: https://getlago.com/docs/api-reference/invoices/retry.md

# Retry an invoice payment

> This endpoint resends an invoice for collection and retry a payment.

## OpenAPI

````yaml POST /invoices/{lago_id}/retry_payment
paths:
  path: /invoices/{lago_id}/retry_payment
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
              description: >-
                Unique identifier assigned to the invoice within the Lago
                application. This ID is exclusively created by Lago and serves
                as a unique identifier for the invoice's record within the Lago
                system.
              format: uuid
              example: 1a901a90-1a90-1a90-1a90-1a901a901a90
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Invoice payment retried
        examples: {}
        description: Invoice payment retried
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
    '405':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 405
              error:
                allOf:
                  - type: string
                    example: Method Not Allowed
              code:
                allOf:
                  - type: string
                    example: not_allowed
            refIdentifier: '#/components/schemas/ApiErrorNotAllowed'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 405
              error: Method Not Allowed
              code: not_allowed
        description: Not Allowed error
  deprecated: false
  type: path
components:
  schemas: {}

````