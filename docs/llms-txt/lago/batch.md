# Source: https://getlago.com/docs/api-reference/events/batch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch usage events

> This endpoint can be used to send a batch of usage records. Each request may include up to 100 events.

<RequestExample>
  ```bash cURL theme={"dark"}
  LAGO_URL="https://api.getlago.com"
  API_KEY="__YOUR_API_KEY__"

  curl --location --request POST "$LAGO_URL/api/v1/events/batch" \
  --header "Authorization: Bearer $API_KEY" \
  --header 'Content-Type: application/json' \
  --data-raw '{
  	"events": [
        {
          "transaction_id": "__UNIQUE_ID__",
          "external_subscription_id": "__YOUR_SUBSCRIPTION_ID__",
          "code": "__BILLABLE_METRIC_CODE__",
          "timestamp": $(date +%s),
          "properties": {
            "custom_field": 12
          }
        }
      ]
    }'
  ```

  ```python Python theme={"dark"}
  from lago_python_client.client import Client
  from lago_python_client.exceptions import LagoApiError
  from lago_python_client.models import BatchEvent

  client = Client(api_key='__YOUR_API_KEY__')

  # Create a list of events
  batch_event = BatchEvent(events=[
      Event(
          transaction_id="__UNIQUE_ID_1__",
          external_subscription_id="__SUBSCRIPTION_ID_1__",
          code="__BILLABLE_METRIC_CODE__",
          timestamp=1650893379,
          properties={"custom_field": "custom"}
      ),
      Event(
          transaction_id="__UNIQUE_ID_2__",
          external_subscription_id="__SUBSCRIPTION_ID_2__",
          code="__BILLABLE_METRIC_CODE__",
          timestamp=1650893380,
          properties={"custom_field": "custom"}
      )
      # Add more events as needed
  ])
  try:
      client.events.batch_create(batch_event)
  except LagoApiError as e:
      repair_broken_state(e)  # do something on error or raise your own exception
  ```

  ```ruby Ruby theme={"dark"}
  require 'lago-ruby-client'

  client = Lago::Api::Client.new(api_key: '__YOUR_API_KEY__')

  # Create an array of event hashes
  events = [
    {
      transaction_id: "__UNIQUE_ID_1__",
      external_subscription_id: "__SUBSCRIPTION_ID_1__",
      code: "__BILLABLE_METRIC_CODE__",
      timestamp: Time.now.to_i,
      properties: {
        custom_field: "custom value 1"
      }
    },
    {
      transaction_id: "__UNIQUE_ID_2__",
      external_subscription_id: "__SUBSCRIPTION_ID_2__",
      code: "__BILLABLE_METRIC_CODE__",
      timestamp: Time.now.to_i,
      properties: {
        custom_field: "custom value 2"
      }
    }
    # Add more events as needed
  ]

  client.events.batch_create(events)
  ```

  ```js Javascript theme={"dark"}
  const batchEvent = [
    {
      transaction_id: "__UNIQUE_TRANSACTION_ID_1__",
      external_subscription_id: "__SUBSCRIPTION_ID_1__",
      code: "__BILLABLE_METRIC_CODE__",
      timestamp: 1650893379,
      properties: { customField: "custom1" },
    },
    {
      transaction_id: "__UNIQUE_TRANSACTION_ID_2__",
      external_subscription_id: "__SUBSCRIPTION_ID_2__",
      code: "__BILLABLE_METRIC_CODE__",
      timestamp: 1650893380,
      properties: { customField: "custom2" },
    },
    // Add more events as needed
  ];

  await client.events.createBatchEvents({ events: batchEvent });

  ```

  ```go Go theme={"dark"}
  import "fmt"
  import "github.com/getlago/lago-go-client"

  func main() {
    ctx := context.Background()
    lagoClient := lago.New().SetApiKey("__YOUR_API_KEY__")

    event := lago.EventInput{
      TransactionID:          "__UNIQUE_TRANSACTION_ID__",
      ExternalSubscriptionID: "__UNIQUE_SUBSCRIPTION_ID__",
      Code:                   "__BILLABLE_METRIC_CODE__",
      Timestamp:              strconv.FormatInt(time.Now().Unix(), 10),
      Properties: map[string]interface{}{
        "nbusers": "12",
      },
    }

    batchInput := make([]lago.EventInput, 1)
    batchInput[0] = event

    res, err := lagoClient.Event().Batch(ctx, &batchInput)
  }
  ```
</RequestExample>


## OpenAPI

````yaml POST /events/batch
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
  /events/batch:
    post:
      tags:
        - events
      summary: Batch multiple events
      description: >-
        This endpoint can be used to send a batch of usage records. Each request
        may include up to 100 events.
      operationId: createBatchEvents
      requestBody:
        description: Batch events payload
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EventBatchInput'
        required: true
      responses:
        '200':
          description: Event received
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventsCreated'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
components:
  schemas:
    EventBatchInput:
      type: object
      required:
        - events
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/EventInputObject'
    EventsCreated:
      type: object
      required:
        - events
      properties:
        events:
          type: array
          items:
            allOf:
              - $ref: '#/components/schemas/EventObject'
              - type: object
                properties:
                  lago_customer_id:
                    type: 'null'
                    description: >-
                      The value will always be null in this response as the
                      event processing is done asynchronously
                    example: null
    EventInputObject:
      type: object
      required:
        - transaction_id
        - external_subscription_id
        - code
      properties:
        transaction_id:
          type: string
          example: transaction_1234567890
          description: >
            This field represents a unique identifier for the event.

            It is crucial for ensuring idempotency, meaning that each event can
            be uniquely identified and processed without causing any unintended
            side effects.


            WARNING: If the Lago organization is configured to use the new
            Clickhouse-based event pipeline (designed for high-volume
            processing), the idempotency logic is handled differently.

            Event uniqueness is maintained with both `transaction_id` and
            `timestamp` fields.

            If a new event arrives with identical values for these two fields as
            an existing event, the new one will overwrite the previous event
            rather than being rejected.
        external_subscription_id:
          type: string
          example: sub_1234567890
          description: >-
            The unique identifier of the subscription in your application. This
            field is mandatory in order to link events to the correct customer
            subscription.
        code:
          type: string
          example: storage
          description: >-
            The code that identifies a targeted billable metric. It is essential
            that this code matches the `code` property of one of your active
            billable metrics. If the provided code does not correspond to any
            active billable metric, it will be ignored during the process.
        timestamp:
          oneOf:
            - type: integer
            - type: string
          example: '1651240791.123'
          description: >
            This field captures the Unix timestamp in seconds indicating the
            occurrence of the event in Coordinated Universal Time (UTC).

            If this timestamp is not provided, the API will automatically set it
            to the time of event reception.

            You can also provide miliseconds precision by appending decimals to
            the timestamp.
        precise_total_amount_cents:
          type:
            - string
            - 'null'
          example: '1234.56'
          description: >-
            The precise total amount in cents with precision used by the
            `dynamic` pricing model to compute the usage amount.
        properties:
          type:
            - object
            - 'null'
          description: >-
            This field represents additional properties associated with the
            event, which are utilized in the calculation of the final fee. This
            object becomes mandatory when the targeted billable metric employs a
            `sum_agg`, `max_agg`, or `unique_count_agg` aggregation method.
            However, when using a simple `count_agg`, this object is not
            required.
          additionalProperties:
            oneOf:
              - type: string
              - type: integer
              - type: number
          example:
            gb: 10
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