# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/schemas/grant-status-updated.mdx

# Event: grant.status.updated

POST 

**When is this event triggered?**

This event is triggered when a Cash App Pay grant status has been updated.

Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/schemas/grant-status-updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  grant-status-updated:
    post:
      operationId: grant-status-updated
      summary: 'Event: grant.status.updated'
      description: >-
        **When is this event triggered?**


        This event is triggered when a Cash App Pay grant status has been
        updated.
      parameters:
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
                    The type of event that occurred. `grant.status.updated` for
                    this event.
                eventId:
                  type: string
                  description: A unique identifier provided by Cash App for the event.
                grant:
                  $ref: '#/components/schemas/CashGrant'
                timestamp:
                  type: string
                  description: When the webhook event was created
              required:
                - type
                - eventId
                - grant
                - timestamp
components:
  schemas:
    CashGrantIntent:
      type: string
      enum:
        - ON_FILE
        - ONE_TIME
      description: Either ON_FILE or ONE_TIME
      title: CashGrantIntent
    CashGrantType:
      type: string
      enum:
        - CASHAPP
      description: CASHAPP for all Cash App Pay transactions
      title: CashGrantType
    CashGrantDetailsStatus:
      type: string
      enum:
        - ACTIVE
        - EXPIRED
        - CONSUMED
        - REVOKED
      description: >
        Describes whether or not this grant can be used to perform the action
        associated with it.


        If `ACTIVE`, it can be used to perform the action.


        If `EXPIRED`, it may no longer be used to perform the action due to the
        current time being past the "expires_at" time.


        If `CONSUMED`, it was already redeemed to perform the action and cannot
        be used again.


        If `REVOKED`, the customer or merchant explicitly unauthorized the
        grant, preventing it from being used to perform the action.
      title: CashGrantDetailsStatus
    CashGrantDetailsCashapp:
      type: object
      properties:
        customerId:
          type: string
        cashtag:
          type: string
          description: >-
            A publicly-accessible, unique identifier (username) for individuals
            and businesses using Cash App.
      required:
        - customerId
        - cashtag
      title: CashGrantDetailsCashapp
    CashGrantDetails:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/CashGrantDetailsStatus'
          description: >
            Describes whether or not this grant can be used to perform the
            action associated with it.


            If `ACTIVE`, it can be used to perform the action.


            If `EXPIRED`, it may no longer be used to perform the action due to
            the current time being past the "expires_at" time.


            If `CONSUMED`, it was already redeemed to perform the action and
            cannot be used again.


            If `REVOKED`, the customer or merchant explicitly unauthorized the
            grant, preventing it from being used to perform the action.
        cashapp:
          $ref: '#/components/schemas/CashGrantDetailsCashapp'
        createdAt:
          type: string
          description: >-
            When this grant was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updatedAt:
          type: string
          description: >-
            When this grant was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        expiresAt:
          type: string
          description: >
            If present, indicates when the grant's status will become EXPIRED,
            preventing a client from using it to create payments or refunds.


            The timestamp is in the [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
      required:
        - status
        - cashapp
        - createdAt
        - updatedAt
        - expiresAt
      title: CashGrantDetails
    CashGrant:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for this grant issued by Cash App.
        intent:
          $ref: '#/components/schemas/CashGrantIntent'
          description: Either ON_FILE or ONE_TIME
        type:
          $ref: '#/components/schemas/CashGrantType'
          description: CASHAPP for all Cash App Pay transactions
        details:
          $ref: '#/components/schemas/CashGrantDetails'
      required:
        - id
        - intent
        - type
        - details
      description: Describes a grant provided by Cash App.
      title: CashGrant

```