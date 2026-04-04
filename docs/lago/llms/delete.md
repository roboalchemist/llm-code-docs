# Source: https://getlago.com/docs/api-reference/customers/delete.md

# Source: https://getlago.com/docs/api-reference/alerts/delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an alert

> This endpoint allows you to delete an existing alert for a subscription.



## OpenAPI

````yaml DELETE /subscriptions/{external_id}/alerts/{code}
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
  /subscriptions/{external_id}/alerts/{code}:
    parameters:
      - name: external_id
        in: path
        description: External ID of the existing subscription
        required: true
        schema:
          type: string
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
      - name: code
        in: path
        description: Unique code of the alert
        required: true
        schema:
          type: string
          example: storage_threshold_alert
    delete:
      tags:
        - subscriptions
      summary: Delete a subscription alert
      description: This endpoint allows you to delete an existing alert for a subscription.
      operationId: deleteSubscriptionAlert
      responses:
        '200':
          description: Subscription alert deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Alert'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    Alert:
      type: object
      required:
        - alert
      properties:
        alert:
          $ref: '#/components/schemas/AlertObject'
    AlertObject:
      type: object
      required:
        - lago_id
        - lago_organization_id
        - external_subscription_id
        - external_customer_id
        - billable_metric
        - alert_type
        - code
        - name
        - previous_value
        - last_processed_at
        - thresholds
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the alert, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_organization_id:
          type: string
          format: uuid
          description: Unique identifier of the organization, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        external_subscription_id:
          type: string
          description: >-
            The subscription external unique identifier (provided by your own
            application).
          example: sub_1234567890
        external_customer_id:
          type: string
          description: >-
            The customer external unique identifier (provided by your own
            application).
          example: cus_0987654321
        billable_metric:
          $ref: '#/components/schemas/BillableMetricObject'
          description: >-
            The billable metric associated with the alert. Only for alerts based
            on a billable metric.
        alert_type:
          type: string
          description: The type of alert.
          enum:
            - current_usage_amount
            - billable_metric_current_usage_amount
            - billable_metric_current_usage_units
            - lifetime_usage_amount
          example: billable_metric_current_usage_amount
        code:
          type: string
          description: Unique code used to identify the alert.
          example: storage_threshold_alert
        name:
          type:
            - string
            - 'null'
          description: The name of the alert.
          example: Storage Usage Alert
        previous_value:
          type: number
          description: >-
            When the system checked if this alert should be triggered, this
            value was retrieved and checked against the thresholds.
          example: 1000
        last_processed_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time in UTC (ISO 8601) when the system checked if this
            alert should be triggered. Null until it's processed for the first
            time.
          example: '2025-05-19T10:04:21Z'
        thresholds:
          type: array
          description: Array of thresholds associated with the alert.
          items:
            $ref: '#/components/schemas/AlertThresholdObject'
        created_at:
          type: string
          format: date-time
          description: The date and time in UTC (ISO 8601) when the alert was created.
          example: '2025-03-20T10:00:00Z'
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
    BillableMetricObject:
      type: object
      required:
        - lago_id
        - name
        - code
        - aggregation_type
        - recurring
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: Unique identifier of the billable metric created by Lago.
        name:
          type: string
          example: Storage
          description: Name of the billable metric.
        code:
          type: string
          example: storage
          description: >-
            Unique code used to identify the billable metric associated with the
            API request. This code associates each event with the correct
            metric.
        description:
          type:
            - string
            - 'null'
          example: GB of storage used in my application
          description: Internal description of the billable metric.
        recurring:
          type: boolean
          example: false
          description: >-
            Defines if the billable metric is persisted billing period over
            billing period.


            - If set to `true`: the accumulated number of units calculated from
            the previous billing period is persisted to the next billing period.

            - If set to `false`: the accumulated number of units is reset to 0
            at the end of the billing period.

            - If not defined in the request, default value is `false`.
        rounding_function:
          type:
            - string
            - 'null'
          enum:
            - ceil
            - floor
            - round
            - null
          example: round
          description: >-
            Refers to the numeric value or mathematical expression that will be
            rounded based on the calculated number of billing units. Possible
            values are `round`, `ceil` and `floor`.
        rounding_precision:
          type:
            - integer
            - 'null'
          example: 2
          description: >-
            Specifies the number of decimal places to which the
            `rounding_function` will be rounded. It can be a positive or
            negative value.
        created_at:
          type: string
          format: date-time
          example: '2022-09-14T16:35:31Z'
          description: Creation date of the billable metric.
        expression:
          type: string
          example: round((ended_at - started_at) * units)
          description: >-
            Expression used to calculate the event units. The expression is
            evalutated for each event and the result is then used to calculate
            the total aggregated units.
        field_name:
          type:
            - string
            - 'null'
          example: gb
          description: >-
            Property of the billable metric used for aggregating usage data.
            This field is not required for `count_agg`.
        aggregation_type:
          type: string
          description: Aggregation method used to compute usage for this billable metric.
          example: sum_agg
          enum:
            - count_agg
            - sum_agg
            - max_agg
            - unique_count_agg
            - weighted_sum_agg
            - latest_agg
        weighted_interval:
          type:
            - string
            - 'null'
          enum:
            - seconds
            - null
          example: seconds
          description: >-
            Parameter exclusively utilized in conjunction with the
            `weighted_sum` aggregation type. It serves to adjust the aggregation
            result by assigning weights and proration to the result based on
            time intervals. When this field is not provided, the default time
            interval is assumed to be in `seconds`.
        filters:
          type: array
          items:
            $ref: '#/components/schemas/BillableMetricFilterObject'
    AlertThresholdObject:
      allOf:
        - $ref: '#/components/schemas/AlertThresholdBaseObject'
        - type: object
          required:
            - code
            - value
            - recurring
          properties:
            value:
              type: string
              pattern: ^[0-9]+.?[0-9]*$
              description: >-
                A value that should trigger this alert, formatted as a
                BigDecimal.
              example: '99.0'
    BillableMetricFilterObject:
      type: object
      description: >-
        Values used to apply differentiated pricing based on additional event
        properties.
      required:
        - key
        - values
      properties:
        key:
          type: string
          example: region
          description: Filter key to add to the event properties payload
        values:
          type: array
          items:
            type: string
            example: us-east-1
          description: List of possible filter values
    AlertThresholdBaseObject:
      type: object
      properties:
        code:
          type:
            - string
            - 'null'
          description: Unique identifier of the usage threshold created by Lago.
          example: warn
        recurring:
          type: boolean
          default: false
          description: >-
            This field when set to `true` indicates that the alert will be
            retrigger when this threshold is reached after the last
            non-recurring threshold. Only one recurring threshold per alert
            allowed.
          example: false
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