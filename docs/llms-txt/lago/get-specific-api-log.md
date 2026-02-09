# Source: https://getlago.com/docs/api-reference/audit-logs/get-specific-api-log.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve an API log

> This endpoint retrieves an existing api log that represents a request made to the API. The api log is identified by its unique request_id.



## OpenAPI

````yaml GET /api_logs/{request_id}
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
  /api_logs/{request_id}:
    parameters:
      - name: request_id
        in: path
        description: The Request Id of the existing api log.
        required: true
        schema:
          type: string
          example: bdc0eda6-ea52-4f72-a46a-94f47a89b546
    get:
      tags:
        - api_logs
      summary: Retrieve an api log
      description: >-
        This endpoint retrieves an existing api log that represents a request
        made to the API. The api log is identified by its unique request_id.
      operationId: findApiLog
      responses:
        '200':
          description: Api Log
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiLog'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    ApiLog:
      type: object
      required:
        - api_log
      properties:
        api_log:
          $ref: '#/components/schemas/ApiLogObject'
    ApiLogObject:
      type: object
      required:
        - api_version
        - client
        - http_method
        - http_status
        - logged_at
        - request_body
        - request_origin
        - request_path
        - created_at
        - request_id
      properties:
        api_version:
          type: string
          example: v1
          description: Lago API version used in the request.
        client:
          type: string
          example: Lago Ruby v1.26.0
          description: The client used to make the request to the API.
        http_method:
          type: string
          example: post
          enum:
            - post
            - put
            - delete
          description: This field represents the HTTP method of the request.
        http_status:
          type: integer
          example: 200
          description: This field represents the HTTP status of the requests.
        logged_at:
          type: string
          format: date-time
          example: '2025-03-31T12:31:44Z'
          description: >-
            The logged date of the api log, presented in the ISO 8601 datetime
            format, specifically in Coordinated Universal Time (UTC). It
            provides the precise timestamp of when the event's record was
            created within the Lago application
        request_body:
          type: string
          format: object
          example: '{ "billable_metric": { "name": "Storage", "code": "storage" } }'
        request_origin:
          type: string
          description: This field represents the API origin of the requested URL
          example: https://app.lago.dev/
        request_path:
          type: string
          description: This field represents the API path of the requested URL
          example: /billable_metrics
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The creation date of the api log record in the Lago application,
            presented in the ISO 8601 datetime format, specifically in
            Coordinated Universal Time (UTC). It provides the precise timestamp
            of when the event's record was created within the Lago application
        request_id:
          type: string
          format: uuid
          description: Unique identifier for the api log.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        request_response:
          type: string
          format: object
          example: '{ "lago_id": "b9155544-e261-4e92-b54e-f65d7609294c", ... }'
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
  responses:
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````