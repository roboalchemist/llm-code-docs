# Source: https://getlago.com/docs/api-reference/events/list-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all events

> This endpoint is used for retrieving all events.



## OpenAPI

````yaml GET /events
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
  /events:
    get:
      tags:
        - events
      summary: List all events
      description: This endpoint is used for retrieving all events.
      operationId: findAllEvents
      parameters:
        - $ref: '#/components/parameters/page'
        - $ref: '#/components/parameters/per_page'
        - $ref: '#/components/parameters/external_subscription_id'
        - name: code
          in: query
          description: Filter events by its code.
          required: false
          explode: true
          schema:
            type: string
            example: event-123
        - name: timestamp_from_started_at
          in: query
          description: >-
            Requires `external_subscription_id` to be set. Filter events by
            timestamp after the subscription started at datetime.
          required: false
          explode: true
          schema:
            type: boolean
            example: true
        - name: timestamp_from
          in: query
          description: Filter events by timestamp starting from a specific date.
          required: false
          explode: true
          schema:
            type: string
            format: date-time
            example: '2022-08-08T00:00:00Z'
        - name: timestamp_to
          in: query
          description: Filter events by timestamp up to a specific date.
          required: false
          explode: true
          schema:
            type: string
            format: date-time
            example: '2022-08-08T00:00:00Z'
      responses:
        '200':
          description: Events
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventsPaginated'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
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
    external_subscription_id:
      name: external_subscription_id
      in: query
      description: External subscription ID
      required: false
      explode: true
      schema:
        type: string
        example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
  schemas:
    EventsPaginated:
      type: object
      required:
        - events
        - meta
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/EventObject'
        meta:
          $ref: '#/components/schemas/PaginationMeta'
    EventObject:
      type: object
      required:
        - transaction_id
        - lago_customer_id
        - code
        - timestamp
        - lago_subscription_id
        - external_subscription_id
      properties:
        lago_id:
          type:
            - string
            - 'null'
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the event within the Lago application.
            This ID is exclusively created by Lago and serves as a unique
            identifier for the event's record within the Lago system
        transaction_id:
          type: string
          example: transaction_1234567890
          description: >-
            This field represents a unique identifier for the event. It is
            crucial for ensuring idempotency, meaning that each event can be
            uniquely identified and processed without causing any unintended
            side effects.
        lago_customer_id:
          type:
            - string
            - 'null'
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the customer within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the customer's record within the Lago system
        code:
          type: string
          example: storage
          description: >-
            The code that identifies a targeted billable metric. It is essential
            that this code matches the `code` property of one of your active
            billable metrics. If the provided code does not correspond to any
            active billable metric, it will be ignored during the process.
        timestamp:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51.123Z'
          description: >-
            This field captures the Unix timestamp in seconds indicating the
            occurrence of the event in Coordinated Universal Time (UTC). If this
            timestamp is not provided, the API will automatically set it to the
            time of event reception.
        precise_total_amount_cents:
          type:
            - string
            - 'null'
          example: '1234.56'
          description: >-
            The precise total amount that was sent in the event payload. This
            filed is used by the `dynamic` pricing model.
        properties:
          type: object
          description: >-
            This field represents additional properties associated with the
            event, which are utilized in the calculation of the final fee. This
            object becomes mandatory when the targeted billable metric employs a
            `sum_agg`, `max_agg`, or `unique_count_agg` aggregation method.
            However, when using a simple `count_agg`, this object is not
            required.
          properties:
            operation_type:
              type:
                - string
                - 'null'
              description: >-
                The `operation_type` field is only necessary when adding or
                removing a specific unit when the targeted billable metric
                adopts a `unique_count_agg` aggregation method. In other cases,
                the `operation_type` field is not required. The valid values for
                the `operation_type` field are `add` or `remove`, which indicate
                whether the unit is being added or removed from the unique count
                aggregation, respectively.
              enum:
                - add
                - remove
          additionalProperties:
            oneOf:
              - type: string
              - type: integer
              - type: number
          example:
            gb: 10
        lago_subscription_id:
          type:
            - string
            - 'null'
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the subscription within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the subscription's record within the Lago
            system
        external_subscription_id:
          type: string
          example: sub_1234567890
          description: >-
            The unique identifier of the subscription within your application.
            It is a mandatory field when the customer possesses multiple
            subscriptions or when the `external_customer_id` is not provided.
        created_at:
          type:
            - string
            - 'null'
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The creation date of the event's record in the Lago application,
            presented in the ISO 8601 datetime format, specifically in
            Coordinated Universal Time (UTC). It provides the precise timestamp
            of when the event's record was created within the Lago application
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