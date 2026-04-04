# Source: https://getlago.com/docs/api-reference/subscriptions/update-lifetime-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update subscription lifetime usage

> This endpoint allows you to update the total lifetime usage of a subscription for migration purposes.



## OpenAPI

````yaml PUT /subscriptions/{external_id}/lifetime_usage
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
  /subscriptions/{external_id}/lifetime_usage:
    parameters:
      - name: external_id
        in: path
        description: External ID of the existing subscription
        required: true
        schema:
          type: string
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
    put:
      tags:
        - subscriptions
      summary: Update a subscription lifetime usage
      description: This endpoint allows you to update the lifetime usage of a subscription.
      operationId: updateSubscriptionLifetimeUsage
      requestBody:
        description: Update the lifetime usage of a subscription
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LifetimeUsageInput'
        required: true
      responses:
        '200':
          description: Subscription lifetime usage updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LifetimeUsage'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
components:
  schemas:
    LifetimeUsageInput:
      type: object
      required:
        - lifetime_usage
      properties:
        lifetime_usage:
          type: object
          required:
            - external_historical_usage_amount_cents
          properties:
            external_historical_usage_amount_cents:
              type: integer
              example: 100
              description: >-
                The historical usage amount in cents for the subscription
                (provided by your own application).
    LifetimeUsage:
      type: object
      required:
        - lifetime_usage
      properties:
        lifetime_usage:
          $ref: '#/components/schemas/LifetimeUsageObject'
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
    NotFound:
      description: Not Found error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorNotFound'
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