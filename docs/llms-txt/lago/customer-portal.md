# Source: https://getlago.com/docs/guide/customers/customer-portal.md

# Source: https://getlago.com/docs/api-reference/customers/customer-portal.md

# Retrieve customer portal URL

> Retrieves an embeddable link for displaying a customer portal.

This endpoint allows you to fetch the URL that can be embedded to provide customers access to a dedicated portal

## OpenAPI

````yaml GET /customers/{external_customer_id}/portal_url
paths:
  path: /customers/{external_customer_id}/portal_url
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
        external_customer_id:
          schema:
            - type: string
              required: true
              description: External ID of the existing customer
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
                      - portal_url
                    properties:
                      portal_url:
                        type: string
                        example: https://app.lago.com/customer-portal/1234567890
                        description: An embeddable link for displaying a customer portal
            requiredProperties:
              - customer
        examples:
          example:
            value:
              customer:
                portal_url: https://app.lago.com/customer-portal/1234567890
        description: Portal URL
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
  deprecated: false
  type: path
components:
  schemas: {}

````