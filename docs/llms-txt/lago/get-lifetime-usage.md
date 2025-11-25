# Source: https://getlago.com/docs/api-reference/subscriptions/get-lifetime-usage.md

# Retrieve subscription lifetime usage

> This endpoint allows you to retrieve the total lifetime usage of a subscription.

## OpenAPI

````yaml GET /subscriptions/{external_id}/lifetime_usage
paths:
  path: /subscriptions/{external_id}/lifetime_usage
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
        external_id:
          schema:
            - type: string
              required: true
              description: External ID of the existing subscription
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
              lifetime_usage:
                allOf:
                  - $ref: '#/components/schemas/LifetimeUsageObject'
            refIdentifier: '#/components/schemas/LifetimeUsage'
            requiredProperties:
              - lifetime_usage
        examples:
          example:
            value:
              lifetime_usage:
                lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_subscription_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                external_subscription_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                external_historical_usage_amount_cents: 100
                invoiced_usage_amount_cents: 100
                current_usage_amount_cents: 100
                from_datetime: '2024-01-01T00:00:00Z'
                to_datetime: '2024-12-31T23:59:59Z'
                usage_thresholds:
                  - amount_cents: 100
                    completion_ratio: 0.5
                    reached_at: '2024-01-01T00:00:00Z'
        description: Subscription lifetime usage
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
  schemas:
    LifetimeUsageThresholdObject:
      type: object
      required:
        - amount_cents
        - completion_ratio
        - reached_at
      properties:
        amount_cents:
          type: integer
          description: The usage threshold amount in cents.
          example: 100
        completion_ratio:
          type: number
          description: The completion ratio of the usage threshold.
          example: 0.5
        reached_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time when the usage threshold was reached. The date and
            time must be in ISO 8601 format.
          example: '2024-01-01T00:00:00Z'
    LifetimeUsageObject:
      type: object
      required:
        - lago_id
        - lago_subscription_id
        - external_subscription_id
        - external_historical_usage_amount_cents
        - invoiced_usage_amount_cents
        - current_usage_amount_cents
        - from_datetime
        - to_datetime
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the lifetime usage record within the
            Lago application. This ID is exclusively created by Lago and serves
            as a unique identifier for the lifetime usage record within the Lago
            system
        lago_subscription_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the subscription record within the
            Lago application. This ID is exclusively created by Lago and serves
            as a unique identifier for the subscription record within the Lago
            system
        external_subscription_id:
          type: string
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          description: >-
            The subscription external unique identifier (provided by your own
            application).
        external_historical_usage_amount_cents:
          type: integer
          example: 100
          description: >-
            The historical usage amount in cents for the subscription (provided
            by your own application).
        invoiced_usage_amount_cents:
          type: integer
          example: 100
          description: The total invoiced usage amount in cents for the subscription.
        current_usage_amount_cents:
          type: integer
          example: 100
          description: >-
            The current usage amount in cents for the subscription on the
            current billing period.
        from_datetime:
          type:
            - string
            - 'null'
          format: date-time
          example: '2024-01-01T00:00:00Z'
          description: >-
            The recording start date and time of the subscription lifetime
            usage. The date and time must be in ISO 8601 format.
        to_datetime:
          type: string
          format: date-time
          example: '2024-12-31T23:59:59Z'
          description: >-
            The recording end date and time of the subscription lifetime usage.
            The date and time must be in ISO 8601 format.
        usage_thresholds:
          type: array
          description: Array of usage thresholds attached to the subscription's plan.
          items:
            $ref: '#/components/schemas/LifetimeUsageThresholdObject'

````