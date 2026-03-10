# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/refund-status-updated.mdx

# Event: refund.status.updated

POST 

**When is this event triggered?**

This event is created whenever a refund status is changed. The status change can be due to a couple different things:
  - An API client-initiated action to void or capture the refund
  - A refund auto-voiding after 7 days of not being captured

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/refund-status-updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  refund-status-updated:
    post:
      operationId: refund-status-updated
      summary: 'Event: refund.status.updated'
      description: >-
        **When is this event triggered?**


        This event is created whenever a refund status is changed. The status
        change can be due to a couple different things:
          - An API client-initiated action to void or capture the refund
          - A refund auto-voiding after 7 days of not being captured
      parameters:
        - name: Accept
          in: header
          required: true
          schema:
            type: string
        - name: X-Region
          in: header
          required: true
          schema:
            type: string
        - name: X-Signature
          in: header
          required: true
          schema:
            type: string
        - name: User-Agent
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                type:
                  type: string
                  description: >-
                    The type of event that occurred. `refund.status.updated` for
                    this event.
                event_id:
                  type: string
                  description: A unique identifier provided by Cash App for the event.
                created_at:
                  type: string
                  format: date-time
                  description: >-
                    When this event occured in [RFC
                    3339](https://datatracker.ietf.org/doc/html/rfc3339) format
                    (UTC).


                    The time that the event is delivered may be significantly
                    later than this timestamp due to webhooks being retried for
                    up to 72 hours.
                data:
                  $ref: >-
                    #/components/schemas/WebhooksRefundStatusUpdatedPayloadContentApplicationJsonSchemaData
                  description: Data about the refund that had a status change.
              required:
                - type
                - event_id
                - created_at
                - data
components:
  schemas:
    Currency:
      type: string
      enum:
        - USD
      description: >-
        Indicates the country associated with an entity. Values are from the
        [ISO-4217 Alpha-3](https://www.iso.org/iso-4217-currency-codes.html)
        specification.


        Current values:


        - `USD`: United States Dollar
      title: Currency
    RefundStatus:
      type: string
      enum:
        - AUTHORIZED
        - CAPTURED
        - VOIDED
        - DECLINED
      description: >-
        The step of the refund processing lifecycle that this refund is
        currently at.


        - `AUTHORIZED`

        - `CAPTURED`

        - `VOIDED`

        - `DECLINED`
      title: RefundStatus
    Metadata:
      type: object
      additionalProperties:
        type: string
      description: >-
        Freeform key-value pairs of arbitrary data associated with this
        resource.


        Keys and values must be passed as strings and not contain any personally
        identifiable information (PII).


        Min keys: `0`

        Max keys: `50`



        > Note: Nested keys are not supported.
      title: Metadata
    ErrorCategory:
      type: string
      enum:
        - API_ERROR
        - AUTHENTICATION_ERROR
        - BRAND_ERROR
        - DISPUTE_ERROR
        - MERCHANT_ERROR
        - INVALID_REQUEST_ERROR
        - PAYMENT_PROCESSING_ERROR
        - RATE_LIMIT_ERROR
        - WEBHOOK_ERROR
        - API_KEY_ERROR
        - GRANT_ERROR
      description: The high-level reason the error occurred
      title: ErrorCategory
    Error:
      type: object
      properties:
        category:
          $ref: '#/components/schemas/ErrorCategory'
          description: The high-level reason the error occurred
        code:
          type: string
          description: >-
            A unique identifier for the specific type of error that occurred.
            See the Error Code Reference for more information.


            Min length: `1`
        detail:
          type: string
          description: >-
            Human-readable description of why the error occurred and how to
            resolve it.


            Min length: `1`
        field:
          type: string
          description: >-
            The field in the request that caused the error, using array and
            object dot notation.


            Min length: `1`
      required:
        - category
        - code
      description: Represents an error encountered during a request to the API.
      title: Error
    Refund:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this refund issued by Cash App.

            Min length: `1`
            Max length: `128`
        amount:
          type: integer
          description: >-
            Amount of money to refund, in the lowest denomination of currency on
            the refund.


            Min value: `1`
        currency:
          $ref: '#/components/schemas/Currency'
        customer_id:
          type: string
          description: |-
            ID of the customer that received this refund.

            Min length: `1`
            Max length: `128`
        merchant_id:
          type: string
          description: |-
            ID of the merchant that issued this refund.

            Min length: `1`
            Max length: `128`
        status:
          $ref: '#/components/schemas/RefundStatus'
          description: >-
            The step of the refund processing lifecycle that this refund is
            currently at.


            - `AUTHORIZED`

            - `CAPTURED`

            - `VOIDED`

            - `DECLINED`
        created_at:
          type: string
          format: date-time
          description: >-
            When this refund was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this refund was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        grant_id:
          type: string
          description: |-
            This is currently unused and empty.

            Min length: `1`
            Max length: `256`
        payment_id:
          type: string
          description: |-
            This is currently unused and empty.

            Min length: `1`
            Max length: `128`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this refund, typically used to
            associate the refund with a record in an external system.


            Min length: `1`

            Max length: `1024`
        metadata:
          $ref: '#/components/schemas/Metadata'
        decline_errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: >-
            If the refund was declined, contains a list of the reasons why it
            was declined.


            Min number of items: `1`
      required:
        - id
        - amount
        - currency
        - customer_id
        - merchant_id
        - status
        - created_at
        - updated_at
      title: Refund
    WebhooksRefundStatusUpdatedPayloadContentApplicationJsonSchemaDataObject:
      type: object
      properties:
        refund:
          $ref: '#/components/schemas/Refund'
      required:
        - refund
      description: A snapshot of the refund immediately after the refund's status changed.
      title: WebhooksRefundStatusUpdatedPayloadContentApplicationJsonSchemaDataObject
    WebhooksRefundStatusUpdatedPayloadContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: A unique identifier provided by Cash App for the refund.
        object:
          $ref: >-
            #/components/schemas/WebhooksRefundStatusUpdatedPayloadContentApplicationJsonSchemaDataObject
          description: >-
            A snapshot of the refund immediately after the refund's status
            changed.
        type:
          type: string
          description: >-
            The resource type contained in the `object` field. For this event,
            it is `refund`.
      required:
        - id
        - object
        - type
      description: Data about the refund that had a status change.
      title: WebhooksRefundStatusUpdatedPayloadContentApplicationJsonSchemaData

```