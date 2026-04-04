# Source: https://getlago.com/docs/api-reference/audit-logs/get-all-activity-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all activity logs

> This endpoint retrieves all existing activity logs that represent actions performed on application resources.



## OpenAPI

````yaml GET /activity_logs
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
  /activity_logs:
    get:
      tags:
        - activity_logs
      summary: List all activity logs
      description: >-
        This endpoint retrieves all existing activity logs that represent
        actions performed on application resources.
      operationId: findAllActivityLogs
      parameters:
        - $ref: '#/components/parameters/page'
        - $ref: '#/components/parameters/per_page'
        - name: from_date
          in: query
          description: Filter activity logs from a specific date.
          required: false
          explode: true
          schema:
            type: string
            format: date
            example: '2022-08-09'
        - name: to_date
          in: query
          description: Filter activity logs up to a specific date.
          required: false
          explode: true
          schema:
            type: string
            format: date
            example: '2022-08-09'
        - name: activity_types[]
          in: query
          description: Filter results by activity types
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
            example:
              - billing_metric.created
              - billing_metric.updated
        - name: activity_sources[]
          in: query
          description: Filter results by activity sources
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
              enum:
                - api
                - front
                - system
            example:
              - api
              - front
        - name: user_emails[]
          in: query
          description: Filter results by user emails
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
            example:
              - dinesh@piedpiper.test
        - $ref: '#/components/parameters/external_customer_id'
        - $ref: '#/components/parameters/external_subscription_id'
        - name: resource_ids[]
          in: query
          description: Filter results by resources unique identifiers
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
              format: uuid
            example:
              - 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
              - 1a901a90-1a90-1a90-1a90-1a901a901a90
        - name: resource_types[]
          in: query
          description: Filter results by resource class types
          required: false
          explode: true
          schema:
            type: array
            items:
              type: string
            example:
              - BillableMetric
              - Invoice
      responses:
        '200':
          description: List of activity logs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActivityLogsPaginated'
        '401':
          $ref: '#/components/responses/Unauthorized'
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
    external_customer_id:
      name: external_customer_id
      in: query
      description: Unique identifier assigned to the customer in your application.
      required: false
      explode: true
      schema:
        type: string
        example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
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
    ActivityLogsPaginated:
      type: object
      required:
        - activity_logs
        - meta
      properties:
        activity_logs:
          type: array
          items:
            $ref: '#/components/schemas/ActivityLogObject'
        meta:
          $ref: '#/components/schemas/PaginationMeta'
    ActivityLogObject:
      type: object
      required:
        - activity_id
        - activity_source
        - activity_type
        - logged_at
        - resource_id
        - resource_type
        - organization_id
        - created_at
      properties:
        activity_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the activity log within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the activity log record within the Lago system
        user_email:
          type:
            - string
            - 'null'
          format: email
          example: dinesh@piedpiper.test
          description: The email of the user who performed the activity
        activity_type:
          type: string
          example: billing_metric.created
          description: >-
            This field stores the actitivy action that was performed to the
            activity_object.
        activity_source:
          type: string
          example: api
          enum:
            - api
            - front
            - system
          description: >-
            This field represents the source of the activity log, the
            interaction source that triggered the action.
        activity_object:
          type:
            - object
            - 'null'
          format: object
          example:
            lago_id: dad68bc7-c01a-4ad8-a87b-13e78693a5bc
            plan_id: b9155544-e261-4e92-b54e-f65d7609294c
          description: >-
            This field represents the final state of the object that the action
            was applied.
        activity_object_changes:
          type:
            - object
            - 'null'
          format: object
          example:
            plan_id:
              - null
              - b9155544-e261-4e92-b54e-f65d7609294c
        external_customer_id:
          type:
            - string
            - 'null'
          description: >-
            The customer external unique identifier (provided by your own
            application)
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        external_subscription_id:
          type:
            - string
            - 'null'
          description: Unique identifier assigned to the subscription in your application.
          example: external_id
        resource_id:
          type: string
          description: The resource id of the object that the action was applied.
          format: uuid
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        resource_type:
          type: string
          description: The resource type of the resource_id record.
          example: BillableMetric
        organization_id:
          type: string
          format: uuid
          description: >-
            Unique identifier for the organization associated with the activity
            log.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        logged_at:
          type: string
          format: date-time
          example: '2025-03-31T12:31:44Z'
          description: >-
            The logged date of the activity, presented in the ISO 8601 datetime
            format, specifically in Coordinated Universal Time (UTC). It
            provides the precise timestamp of when the event's record was
            created within the Lago application
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The creation date of the activity record in the Lago application,
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
  responses:
    Unauthorized:
      description: Unauthorized error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiErrorUnauthorized'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````