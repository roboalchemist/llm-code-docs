# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/dispute-status-updated.mdx

# Event: dispute.status.updated

POST 

**When is this event triggered?**

This event is created whenever a dispute's state is updated. This can be caused by a variety of things:
  - An API client-driven change where the dispute is accepted or challenged
  - Cash App Pay making a final decision on a dispute

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/dispute-status-updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  dispute-status-updated:
    post:
      operationId: dispute-status-updated
      summary: 'Event: dispute.status.updated'
      description: >-
        **When is this event triggered?**


        This event is created whenever a dispute's state is updated. This can be
        caused by a variety of things:
          - An API client-driven change where the dispute is accepted or challenged
          - Cash App Pay making a final decision on a dispute
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
                    The type of event that occurred. `dispute.status.updated`
                    for this event.
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
                    #/components/schemas/WebhooksDisputeStatusUpdatedPayloadContentApplicationJsonSchemaData
                  description: Data about the dispute that was updated.
              required:
                - type
                - event_id
                - created_at
                - data
components:
  schemas:
    DisputeReason:
      type: string
      enum:
        - FR10
        - FR11
        - PE10
        - PE11
        - PE12
        - CD10
        - CD11
        - CD13
      description: >-
        4-digit code consisting of 2 letters followed by 2 numbers that
        indicates why the dispute was created, at a high level.


        Current values:


        - `FR10`: Customer has no knowledge of the payment.

        - `FR11`: Customer has no knowledge of the payment and liability has
        shifted to the merchant due to collusion, fraud monitoring program
        thresholds, or any other reason.

        - `PE10`: Payment was processed twice.

        - `PE11`: Payment amount differs from agreed amount.

        - `PE12`: Payment was paid for by another means.

        - `CD10`: Cancelled services.

        - `CD11`: Goods or services differ from what was agreed upon for the
        payment.

        - `CD12`: The goods or services were not received.

        - `CD13`: The purchase was cancelled or returned, but the refund has not
        been processed.
      title: DisputeReason
    DisputeSettlementWithholding:
      type: string
      enum:
        - NOT_WITHHELD
        - WITHHELD_ALREADY
      description: >-
        Indicates if the disputed amount has already been withheld from a
        settlement or not.


        Current values:


        - `NOT_WITHHELD`: The disputed amount has not yet been withheld in a
        settlement. It may impact future settlements if the dispute is "lost" by
        the merchant.


        - `WITHHELD_ALREADY`: The disputed amount was withheld in a prior
        settlement. This dispute will not impact future settlements.
      title: DisputeSettlementWithholding
    DisputeState:
      type: string
      enum:
        - RESPONSE_REQUIRED
        - NO_RESPONSE_REQUIRED
        - PROCESSING
        - ACCEPTED
        - WON
        - PARTIALLY_WON
        - LOST
      description: |-
        The step in the dispute lifecycle that this dispute is currently at:

        - `RESPONSE_REQUIRED`
        - `NO_RESPONSE_REQUIRED`
        - `PROCESSING`
        - `ACCEPTED`
        - `WON`
        - `PARTIALLY_WON`
        - `LOST`
      title: DisputeState
    Dispute:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the dispute issued by Cash App.

            Min length: `1`
            Max length: `128`
        payment_id:
          type: string
          description: |-
            ID of the disputed payment.

            Min length: `1`
            Max length: `128`
        amount:
          type: integer
          description: >-
            Amount of disputed money, in the lowest denomination of currency on
            the associated payment.


            Min value: `1`
        customer_credited_amount:
          type:
            - integer
            - 'null'
          description: >-
            The amount credited to the Customer after resolving the dispute. 


            Note: The amount will be in the lowest denomination of the currency
            used on the associated payment.


            Min value: `0`
        reason:
          $ref: '#/components/schemas/DisputeReason'
          description: >-
            4-digit code consisting of 2 letters followed by 2 numbers that
            indicates why the dispute was created, at a high level.


            Current values:


            - `FR10`: Customer has no knowledge of the payment.

            - `FR11`: Customer has no knowledge of the payment and liability has
            shifted to the merchant due to collusion, fraud monitoring program
            thresholds, or any other reason.

            - `PE10`: Payment was processed twice.

            - `PE11`: Payment amount differs from agreed amount.

            - `PE12`: Payment was paid for by another means.

            - `CD10`: Cancelled services.

            - `CD11`: Goods or services differ from what was agreed upon for the
            payment.

            - `CD12`: The goods or services were not received.

            - `CD13`: The purchase was cancelled or returned, but the refund has
            not been processed.
        settlement_withholding:
          $ref: '#/components/schemas/DisputeSettlementWithholding'
          description: >-
            Indicates if the disputed amount has already been withheld from a
            settlement or not.


            Current values:


            - `NOT_WITHHELD`: The disputed amount has not yet been withheld in a
            settlement. It may impact future settlements if the dispute is
            "lost" by the merchant.


            - `WITHHELD_ALREADY`: The disputed amount was withheld in a prior
            settlement. This dispute will not impact future settlements.
        state:
          $ref: '#/components/schemas/DisputeState'
          description: |-
            The step in the dispute lifecycle that this dispute is currently at:

            - `RESPONSE_REQUIRED`
            - `NO_RESPONSE_REQUIRED`
            - `PROCESSING`
            - `ACCEPTED`
            - `WON`
            - `PARTIALLY_WON`
            - `LOST`
        created_at:
          type: string
          format: date-time
          description: >-
            When this dispute was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        response_due_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            When the dispute must be challenged by, after which it will be
            automatically accepted, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this dispute was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        merchant_id:
          type: string
          description: |-
            ID of the merchant that collected the disputed payment.

            Min length: `1`
            Max length: `128`
      required:
        - id
        - payment_id
        - amount
        - reason
        - settlement_withholding
        - state
        - created_at
        - updated_at
        - merchant_id
      description: >-
        Represents a dispute initiated by a customer within Cash App or the
        customer's linked bank
      title: Dispute
    WebhooksDisputeStatusUpdatedPayloadContentApplicationJsonSchemaDataObject:
      type: object
      properties:
        dispute:
          $ref: '#/components/schemas/Dispute'
      required:
        - dispute
      description: >-
        A snapshot of the dispute immediately after the dispute's status was
        updated.
      title: >-
        WebhooksDisputeStatusUpdatedPayloadContentApplicationJsonSchemaDataObject
    WebhooksDisputeStatusUpdatedPayloadContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: A unique identifier provided by Cash App for the dispute.
        object:
          $ref: >-
            #/components/schemas/WebhooksDisputeStatusUpdatedPayloadContentApplicationJsonSchemaDataObject
          description: >-
            A snapshot of the dispute immediately after the dispute's status was
            updated.
        type:
          type: string
          description: >-
            The resource type contained in the `object` field. For this event,
            it is `dispute`.
      required:
        - id
        - object
        - type
      description: Data about the dispute that was updated.
      title: WebhooksDisputeStatusUpdatedPayloadContentApplicationJsonSchemaData

```