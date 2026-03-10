# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/grant-created.mdx

# Event: grant.created

POST 

**When is this event triggered?**

This event is created whenever a grant is created. This is caused by a customer request being approved.

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/grant-created

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  grant-created:
    post:
      operationId: grant-created
      summary: 'Event: grant.created'
      description: >-
        **When is this event triggered?**


        This event is created whenever a grant is created. This is caused by a
        customer request being approved.
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
                    The type of event that occurred. `grant.created` for this
                    event.
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
                    #/components/schemas/WebhooksGrantCreatedPayloadContentApplicationJsonSchemaData
                  description: Data about the grant that was created.
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
    OneTimePaymentActionType:
      type: string
      enum:
        - ONE_TIME_PAYMENT
      description: The type of the action (`ONE_TIME_PAYMENT`).
      title: OneTimePaymentActionType
    OneTimePaymentAction:
      type: object
      properties:
        amount:
          type: integer
          description: >-
            Amount to charge the customer, in the lowest unit of the associated
            currency.


            Min value: `1`
        currency:
          $ref: '#/components/schemas/Currency'
        scope_id:
          type: string
          description: >-
            ID of the client, brand, or merchant that will charge the customer.


            If a client ID is passed, the grant from this action can be used to
            create a payment for any merchant owned by the client.


            If a brand ID is passed, the grant from this action can be used to
            create a payment for any merchant that has a matching brand ID.


            If a merchant ID is passed, the grant from this action can be used
            to create a payment for the merchant with a matching ID.


            Min length: `1`

            Max length: `128`
        type:
          $ref: '#/components/schemas/OneTimePaymentActionType'
          description: The type of the action (`ONE_TIME_PAYMENT`).
      required:
        - scope_id
        - type
      description: >-
        Describes an intent for a client to charge a customer a given amount.


        Note the following restrictions when using this action:


        - If no amount is provided to the action, the payment charged may be
        **any** amount.

        - If `amount` is provided, `currency` must be provided too (and vice
        versa).
      title: OneTimePaymentAction
    OnFilePaymentActionType:
      type: string
      enum:
        - ON_FILE_PAYMENT
      default: ON_FILE_PAYMENT
      description: The type of the action (`ON_FILE_PAYMENT`).
      title: OnFilePaymentActionType
    OnFilePaymentAction:
      type: object
      properties:
        scope_id:
          type: string
          description: >-
            ID of the client or brand that will charge customers.


            If a client ID is passed, the grant from this action can be used to
            create a payment for any merchant owned by the client.


            If a brand ID is passed, the grant from this action can be used to
            create a payment for any merchant that has a matching brand ID.


            Merchant IDs may *not* be passed.


            Min length: `1`

            Max length: `128`
        type:
          $ref: '#/components/schemas/OnFilePaymentActionType'
          description: The type of the action (`ON_FILE_PAYMENT`).
        account_reference_id:
          type: string
          description: >-
            Identifier of the account or customer associated to the on file
            action.
      required:
        - scope_id
        - type
      description: "Describes an\_intent for a client to store a customer's account, allowing a client to create payments or issue refunds for it on a recurring basis."
      title: OnFilePaymentAction
    OnFileDepositActionType:
      type: string
      enum:
        - ON_FILE_DEPOSIT
      description: The type of the action (`ON_FILE_DEPOSIT`).
      title: OnFileDepositActionType
    OnFileDepositAction:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OnFileDepositActionType'
          description: The type of the action (`ON_FILE_DEPOSIT`).
        scope_id:
          type: string
          description: >-
            ID of the client or brand that indicates the set of merchants that
            will deposit to customers.


            If a client ID is passed, the grant from this action can be used to
            create a deposit for any merchant owned by the client.


            If a brand ID is passed, the grant from this action can be used to
            create a deposit for any merchant that has a matching brand ID.

            Min length: `1`

            Max length: `128`
        account_reference_id:
          type: string
          description: >-
            Identifier of the account or customer associated to the on file
            action.
      required:
        - type
        - scope_id
        - account_reference_id
      description: >-
        Describes an intent for a client to deposit funds into the Cash App
        account balances in perpetuity until the Cash App account revokes the
        grant.
      title: OnFileDepositAction
    LinkAccountActionType:
      type: string
      enum:
        - LINK_ACCOUNT
      description: The type of the action (`LINK_ACCOUNT`).
      title: LinkAccountActionType
    LinkAccountAction:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LinkAccountActionType'
          description: The type of the action (`LINK_ACCOUNT`).
      required:
        - type
      description: "Describes an\_intent for a client to manage a customer's merchant profiles in Cash App."
      title: LinkAccountAction
    Action:
      oneOf:
        - $ref: '#/components/schemas/OneTimePaymentAction'
        - $ref: '#/components/schemas/OnFilePaymentAction'
        - $ref: '#/components/schemas/OnFileDepositAction'
        - $ref: '#/components/schemas/LinkAccountAction'
      description: >-
        Represents what the client intends to do to a customer if given
        authorization.
      title: Action
    GrantStatus:
      type: string
      enum:
        - ACTIVE
        - CONSUMED
        - REVOKED
        - EXPIRED
      description: >-
        Describes whether or not this grant can be used to perform the action
        associated with it.


        If `ACTIVE`, it can be used to perform the action.


        If `EXPIRED`, it may no longer be used to perform the action due to the
        current time being past the "expires_at" time.


        If `CONSUMED`, it was already redeemed to perform the action and cannot
        be used again.


        If `REVOKED`, the customer or merchant explicitly unauthorized the
        grant, preventing it from being used to perform the action.
      title: GrantStatus
    GrantType:
      type: string
      enum:
        - ONE_TIME
        - EXTENDED
      description: >-
        Describes whether this grant can be only be used once (`ONE_TIME`) or
        repeatedly (`EXTENDED`).
      title: GrantType
    Channel:
      type: string
      enum:
        - IN_PERSON
        - ONLINE
        - IN_APP
      description: >-
        How the customer is expected to interact with the request.


        - `IN_PERSON`: The customer presents or scans a QR code at a physical
        location to approve the request.

        - `ONLINE`: The customer scans a QR code or is redirected to Cash App
        from a browser context.

        - `IN_APP`: The customer scans a QR code or is redirected to Cash App
        from a native mobile application context.
      title: Channel
    Grant:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this grant issued by Cash App.

            Min length: `1`
            Max length: `256`
        customer_id:
          type: string
          description: |-
            ID of the customer that approved this grant.

            Min length: `1`
            Max length: `128`
        request_id:
          type: string
          description: >-
            A unique identifier issued by Cash App for the customer request that
            resulted in the creation of this grant.


            Min length: `1`

            Max length: `128`
        action:
          $ref: '#/components/schemas/Action'
        status:
          $ref: '#/components/schemas/GrantStatus'
          description: >-
            Describes whether or not this grant can be used to perform the
            action associated with it.


            If `ACTIVE`, it can be used to perform the action.


            If `EXPIRED`, it may no longer be used to perform the action due to
            the current time being past the "expires_at" time.


            If `CONSUMED`, it was already redeemed to perform the action and
            cannot be used again.


            If `REVOKED`, the customer or merchant explicitly unauthorized the
            grant, preventing it from being used to perform the action.
        type:
          $ref: '#/components/schemas/GrantType'
          description: >-
            Describes whether this grant can be only be used once (`ONE_TIME`)
            or repeatedly (`EXTENDED`).
        channel:
          $ref: '#/components/schemas/Channel'
        created_at:
          type: string
          format: date-time
          description: >-
            When this grant was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this grant was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        expires_at:
          type: string
          format: date-time
          description: >-
            If present, indicates when the grant's status will become `EXPIRED`,
            preventing a client from using it to create payments or refunds.


            The timestamp is in the [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
      required:
        - id
        - customer_id
        - request_id
        - action
        - status
        - type
        - channel
        - created_at
        - updated_at
      description: >-
        Describes a grant that can be used to perform actions specified in a
        customer request using the Network API.
      title: Grant
    WebhooksGrantCreatedPayloadContentApplicationJsonSchemaDataObject:
      type: object
      properties:
        grant:
          $ref: '#/components/schemas/Grant'
      required:
        - grant
      description: A snapshot of the grant immediately after the grant was created.
      title: WebhooksGrantCreatedPayloadContentApplicationJsonSchemaDataObject
    WebhooksGrantCreatedPayloadContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: A unique identifier provided by Cash App for the grant.
        object:
          $ref: >-
            #/components/schemas/WebhooksGrantCreatedPayloadContentApplicationJsonSchemaDataObject
          description: A snapshot of the grant immediately after the grant was created.
        type:
          type: string
          description: >-
            The resource type contained in the `object` field. For this event,
            it is `grant`.
      required:
        - id
        - object
        - type
      description: Data about the grant that was created.
      title: WebhooksGrantCreatedPayloadContentApplicationJsonSchemaData

```