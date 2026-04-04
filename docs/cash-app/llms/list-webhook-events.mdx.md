# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events.mdx

# List webhook events

GET https://api.cash.app/management/v1/webhook-events

Returns a list of all webhook events matching the query parameters provided. Expired events are not included.

Scopes: `WEBHOOK_EVENTS_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /webhook-events:
    get:
      operationId: list-webhook-events
      summary: List webhook events
      description: >-
        Returns a list of all webhook events matching the query parameters
        provided. Expired events are not included.


        Scopes: `WEBHOOK_EVENTS_READ`
      tags:
        - subpackage_webhooks
      parameters:
        - name: webhook_endpoint_id
          in: query
          description: Events delivered to this webhook endpoint ID.
          required: false
          schema:
            type: string
        - name: status
          in: query
          description: >-
            The status of an event that was delivered to a webhook endpoint. The
            status can either be PENDING, SUCCESS, or FAILED.
          required: false
          schema:
            $ref: '#/components/schemas/WebhookEventsGetParametersStatus'
        - name: event_type
          in: query
          description: The type of event that will be sent to the webhook endpoint.
          required: false
          schema:
            $ref: '#/components/schemas/WebhookEventsGetParametersEventType'
        - name: cursor
          in: query
          description: >-
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the
            original query.
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: Maximum number of webhook events to return.
          required: false
          schema:
            type: integer
            default: 100
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
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/webhooks_list-webhook-events_Response_200'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
    WebhookEventsGetParametersStatus:
      type: string
      enum:
        - PENDING
        - SUCCESS
        - FAILED
      title: WebhookEventsGetParametersStatus
    WebhookEventsGetParametersEventType:
      type: string
      enum:
        - customer.created
        - customer.deleted
        - customer.updated
        - customer_request.state.updated
        - dispute.created
        - dispute.state.updated
        - grant.created
        - grant.status.updated
        - merchant.status.updated
        - payment.status.updated
        - refund.status.updated
      title: WebhookEventsGetParametersEventType
    EventType:
      type: string
      enum:
        - customer.created
        - customer.deleted
        - customer.updated
        - customer_request.state.updated
        - dispute.created
        - dispute.state.updated
        - grant.created
        - grant.status.updated
        - merchant.status.updated
        - payment.status.updated
        - refund.status.updated
      description: The type of event that will be sent to the webhook endpoint.
      title: EventType
    EventStatus:
      type: string
      enum:
        - PENDING
        - FAILED
        - SUCCESS
      description: >-
        The status of an event that was delivered to a webhook endpoint. The
        status can either be PENDING, SUCCESS, or FAILED.


        PENDING: The webhook event has been dispatched and is in the process of
        being delivered to the endpoint. If the event has failed and is being
        retried, it will continue to be in the PENDING status.


        SUCCESS: The webhook event has been delivered to the endpoint and we've
        received receipt of the delivery from the client's endpoint (e.g.
        200OK).


        FAILED: The webhook event has failed all delivery attempts for 72 hours.
        No more deliveries will be attempted.
      title: EventStatus
    Customer:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this customer issued by Cash App.

            Min length: `1`
            Max length: `128`
        cashtag:
          type: string
          description: >-
            Public identifier for the customer on Cash App. [Learn
            more](https://cash.app/help/us/en-us/3123-cashtags).


            Min length: `1`

            Max length: `1024`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this customer, typically used to
            associate the customer with a record in an external system. This
            value can be provided via the
            `CustomerRequest.customer_metadata.reference_id` attribute. Upon
            approval of the CustomerRequest, a corresponding customer resource
            is created with the `reference_id` attribute.
      required:
        - id
        - cashtag
      title: Customer
    EventDataDataObject0:
      type: object
      properties:
        customer:
          $ref: '#/components/schemas/Customer'
      title: EventDataDataObject0
    Country:
      type: string
      enum:
        - US
      description: >-
        Indicates the country associated with an entity. Values are from the
        [ISO-3166 Alpha-2](https://www.iso.org/iso-3166-country-codes.html)
        specification.


        Current values:


        - `US`: United States of America
      title: Country
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
    Category:
      type: string
      description: >-
        The merchant category code associated with the entity. Values are from
        the [ISO-18245 specification](https://www.iso.org/standard/33365.html).
      title: Category
    MerchantStatus:
      type: string
      enum:
        - ACTIVE
        - RISK_DISABLED
        - COMPLIANCE_DISABLED
        - CLIENT_DISABLED
        - PENDING
      description: >-
        Whether or not this merchant can be used to accept payments or issue
        refunds.


        - `ACTIVE`: The merchant can accept payments or issue refunds.

        - `RISK_DISABLED`: Cash App Pay blocked this merchant due to them being
        high risk. There is no way to re-enable them programmaticaly.

        - `COMPLIANCE_DISABLED`: Cash App Pay blocked this merchant due to them
        not following the terms of service, Program Rules, or local laws. There
        is no way to re-enable them programmaticaly.

        - `CLIENT_DISABLED`: The client called the
        [UpdateMerchant](Network-API.v1.yaml/paths/~1merchants~1{merchant_id}/patch)
        endpoint and disabled this merchant, preventing it from being able to
        handle payments or refunds. To reverse this, call the endpoint again
        with the status field set to `ACTIVE`.

        - `PENDING`: The merchant is not ready to accept payments or refunds
        yet; the registration process is still running.
      title: MerchantStatus
    Address:
      type: object
      properties:
        address_line_1:
          type: string
          description: >-
            First line of the street address, typically including street number,
            street name, and / or building name.


            Min length: `1`

            Max length: `1024`
        address_line_2:
          type: string
          description: |-
            Second line of the address, if any.

            Min length: `1`
            Max length: `1024`
        locality:
          type: string
          description: |-
            City or township where the entity is located.

            Min length: `1`
            Max length: `1024`
        country:
          $ref: '#/components/schemas/Country'
        postal_code:
          type: string
          description: |-
            ZIP or postal code.

            Min length: `1`
            Max length: `128`
        administrative_district_level_1:
          type: string
          description: |-
            State or province.

            Min length: `1`
            Max length: `1024`
      required:
        - country
      description: Where this entity is located
      title: Address
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
    MerchantFeePlans:
      type: object
      properties:
        in_app_fee_plan_id:
          type: string
          description: >-
            The fee plan ID identifying the fee plan that will be used for all
            in-app payments.
        in_person_fee_plan_id:
          type: string
          description: >-
            The fee plan ID identifying the fee plan that will be used for all
            in-person payments.
        online_fee_plan_id:
          type: string
          description: >-
            The fee plan ID identifying the fee plan that will be used for all
            online payments.
      description: >-
        Merchant fee plans contains the IDs of the different fee plans for a
        merchant. These IDs represent the processing fees that merchants will be
        charged for processing payments for each channel. You can use the Fee
        Plans API to get all the fee information for each fee plan.
      title: MerchantFeePlans
    Merchant:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the merchant issued by Cash App.

            Min length: `1`
            Max length: `128`
        brand_id:
          type: string
          description: |-
            ID of the brand associated with this merchant.

            Min length: `1`
            Max length: `128`
        name:
          type: string
          description: >-
            The name of the individual or business entity associated with the
            merchant.


            Min length: `1`

            Max length: `1024`
        country:
          $ref: '#/components/schemas/Country'
        currency:
          $ref: '#/components/schemas/Currency'
        category:
          $ref: '#/components/schemas/Category'
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this merchant, typically used to
            associate the merchant with a record in an external system.
            Independent from the [brand
            reference_id](https://developers.cash.app/docs/api/network-api/operations/create-a-brand#request-body).


            Min length: `1`

            Max length: `1024`
        status:
          $ref: '#/components/schemas/MerchantStatus'
          description: >-
            Whether or not this merchant can be used to accept payments or issue
            refunds.


            - `ACTIVE`: The merchant can accept payments or issue refunds.

            - `RISK_DISABLED`: Cash App Pay blocked this merchant due to them
            being high risk. There is no way to re-enable them programmaticaly.

            - `COMPLIANCE_DISABLED`: Cash App Pay blocked this merchant due to
            them not following the terms of service, Program Rules, or local
            laws. There is no way to re-enable them programmaticaly.

            - `CLIENT_DISABLED`: The client called the
            [UpdateMerchant](Network-API.v1.yaml/paths/~1merchants~1{merchant_id}/patch)
            endpoint and disabled this merchant, preventing it from being able
            to handle payments or refunds. To reverse this, call the endpoint
            again with the status field set to `ACTIVE`.

            - `PENDING`: The merchant is not ready to accept payments or refunds
            yet; the registration process is still running.
        created_at:
          type: string
          format: date-time
          description: >-
            When this merchant was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this merchant was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        address:
          $ref: '#/components/schemas/Address'
        site_url:
          type: string
          format: uri
          description: |-
            The URL of the website, if this merchant is for an eCommerce site.

            Min length: `8`
            Max length: `8000`
        metadata:
          $ref: '#/components/schemas/Metadata'
        default_fee_plans:
          $ref: '#/components/schemas/MerchantFeePlans'
      required:
        - id
        - brand_id
        - name
        - country
        - currency
        - category
        - reference_id
        - status
        - created_at
        - updated_at
        - address
      description: >-
        A merchant represents a depository account when processing payments from
        Cash App customers. Merchants do not have direct access to Cash App, so
        processed payments are stored in this account until they are ready for
        settlement.
      title: Merchant
    EventDataDataObject1:
      type: object
      properties:
        merchant:
          $ref: '#/components/schemas/Merchant'
      title: EventDataDataObject1
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
    EventDataDataObject2:
      type: object
      properties:
        dispute:
          $ref: '#/components/schemas/Dispute'
      title: EventDataDataObject2
    PaymentStatus:
      type: string
      enum:
        - AUTHORIZED
        - CAPTURED
        - VOIDED
        - DECLINED
      description: >-
        The step of the payment processing lifecycle that this payment is
        currently at.


        - `AUTHORIZED`

        - `CAPTURED`

        - `VOIDED`

        - `DECLINED`
      title: PaymentStatus
    PaymentEnrichmentsInitiationActor:
      type: string
      enum:
        - CUSTOMER
        - MERCHANT
      description: |-
        The party who initiated the payment.

        - `CUSTOMER`
        - `MERCHANT`
      title: PaymentEnrichmentsInitiationActor
    PaymentEnrichmentsInitiation:
      type: object
      properties:
        actor:
          $ref: '#/components/schemas/PaymentEnrichmentsInitiationActor'
          description: |-
            The party who initiated the payment.

            - `CUSTOMER`
            - `MERCHANT`
      required:
        - actor
      description: If present, provides information about transaction initiation.
      title: PaymentEnrichmentsInitiation
    PaymentEnrichmentsRestrictedCategoriesItems:
      type: string
      enum:
        - ALCOHOL
        - FINANCIAL_SERVICES
      title: PaymentEnrichmentsRestrictedCategoriesItems
    PaymentEnrichments:
      type: object
      properties:
        initiation:
          $ref: '#/components/schemas/PaymentEnrichmentsInitiation'
          description: If present, provides information about transaction initiation.
        recurring_series_id:
          type: string
          description: >-
            If present, indicates that this payment is part of a recurring
            series of payments, such as a subscription.


            The value should contain a unique identifier for the recurring
            series that is constant across all of its payments, so it can be
            used to group them together.


            Min length: `1`

            Max length: `1024`
        statement_descriptor:
          type: string
          description: >-
            If present, adds the descriptor as line item on to a customer's
            payment receipt in their in-app Activity page.

            The descriptor will be present under the header "On statement as".


            Statement descriptor requirements vary by platform. If the input for
            this field exceeds the character limit, it will be truncated to the
            limit, then suffixed with an ellipsis (...).


            Min length: `1`

            Max length: `22`
        restricted_categories:
          type: array
          items:
            $ref: '#/components/schemas/PaymentEnrichmentsRestrictedCategoriesItems'
          description: >-
            If present, indicates that this payment is associated with one or
            more restricted categories. Contact the Cash App Pay support team to
            use this field.
      description: >-
        Describes optional fields beyond core payment information to supplement
        payment processing.


        Enrichments provide additional context about a payment, which can
        improve the overall payment experience including, but not limited to: 
          - Increased approval rates
          - Enhanced transaction insights
          - Better payment flows in Cash App
      title: PaymentEnrichments
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
    FeeRate:
      type: object
      properties:
        basis_points:
          type: integer
          description: >-
            The variable fee charged for processing the payment expressed as
            1/100th of a percentage.
        fixed_amount:
          type: integer
          description: >-
            The amount charged for processing the payment, in the lowest
            denomination of currency on the payment.
             **Note: The currency for the fee is found on the fee plan.**
      description: >-
        A fee rate contains the components of a fee charged by Cash App to
        partners for a given payment.
      title: FeeRate
    AuthorizationStatus:
      type: string
      enum:
        - AUTHORIZED
        - DECLINED
      description: >-
        The step of the authorization processing lifecycle that this
        authorization is currently at.


        Allowed values:

        - AUTHORIZED

        - DECLINED
      title: AuthorizationStatus
    Authorization:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this authorization issued by Cash App.

            Min length: 1 character
            Max length: 128 characters
        amount:
          type: integer
          description: >-
            Total authorized amount after this authorization was processed, in
            the lowest denomination of currency on the payment.
        currency:
          $ref: '#/components/schemas/Currency'
        status:
          $ref: '#/components/schemas/AuthorizationStatus'
          description: >-
            The step of the authorization processing lifecycle that this
            authorization is currently at.


            Allowed values:

            - AUTHORIZED

            - DECLINED
        created_at:
          type: string
          format: date-time
          description: When this authorization was created, in RFC 3339 format (UTC).
        payment_id:
          type: string
          description: ID of the payment associated with this authorization
        previous_amount:
          type: integer
          description: Total authorized amount before this authorization was requested
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this authorization, typically used to
            associate the authorization with a record in an external system.


            Min length: 1

            Max length: 1024
        metadata:
          $ref: '#/components/schemas/Metadata'
        decline_errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: >-
            If the authorization was declined, it contains a list of the reasons
            why it was declined.


            Min number of items: 1
      required:
        - id
        - amount
        - currency
        - status
        - created_at
        - payment_id
        - previous_amount
      description: Represents an authorization update for a payment
      title: Authorization
    Payment:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this payment issued by Cash App.

            Min length: `1`
            Max length: `128`
        amount:
          type: integer
          description: >-
            The amount of money to collect, in the lowest denomination of
            currency on the payment. This is the _original_ amount authorized
            when the payment was created.


            Min value: `1`
        net_amount:
          type: integer
          description: >-
            The amount remaining after refunds and voided payments are deducted
            from the amount field. The amount will be in the lowest denomination
            of the currency on the payment.

            This is the amount that will be shown to the customer in their Cash
            App account.



            Min value: `0`
        captured_amount:
          type: integer
          description: >-
            The amount of money on this payment that has been allocated for
            settlement. The amount will be in the lowest denomination of the
            currency on the payment.


            Min value: `0`
        voided_amount:
          type: integer
          description: >-
            The amount of money on this payment that is no longer authorized and
            has been released back to the customer. The amount will be in the
            lowest denomination of the currency on the payment.


            Min value: `0`
        refunded_amount:
          type: integer
          description: >-
            Sum of captured refunds in the lowest denomination of currency on
            the payment.


            Min value: `0`
        currency:
          $ref: '#/components/schemas/Currency'
        customer_id:
          type: string
          description: |-
            ID of the customer that sent this payment.

            Min length: `1`
            Max length: `128`
        merchant_id:
          type: string
          description: |-
            ID of the merchant that received this payment.

            Min length: `1`
            Max length: `128`
        grant_id:
          type: string
          description: |-
            ID of the grant to used to create this payment.

            Min length: `1`
            Max length: `256`
        status:
          $ref: '#/components/schemas/PaymentStatus'
          description: >-
            The step of the payment processing lifecycle that this payment is
            currently at.


            - `AUTHORIZED`

            - `CAPTURED`

            - `VOIDED`

            - `DECLINED`
        created_at:
          type: string
          format: date-time
          description: >-
            When this payment was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this payment was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        capture_before:
          type: string
          format: date-time
          description: >-
            When this payment should be captured by, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        refund_ids:
          type: array
          items:
            type: string
          description: >-
            A list of one or more IDs associated with refunds issued for this
            payment.


            Min array length: `1`

            Min length of IDs: `1`

            Max length of IDs: `128`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this payment, typically used to
            associate the payment with a record in an external system.


            Min length: `1`

            Max length: `1024`
        metadata:
          $ref: '#/components/schemas/Metadata'
        enrichments:
          $ref: '#/components/schemas/PaymentEnrichments'
        decline_errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: >-
            If the payment was declined, contains a list of the reasons why it
            was declined.


            Min number of items: `1`
        fee_amount:
          type: number
          format: double
          description: >-
            The total fee amount that was charged to the merchant for processing
            this payment.
        fee_rate:
          $ref: '#/components/schemas/FeeRate'
          description: >-
            The breakdown of the fee that was charged to the merchant for
            processing this payment.
        authorization_updates:
          type: array
          items:
            $ref: '#/components/schemas/Authorization'
          description: >-
            A list of authorization update attempts associated with this
            payment, sorted in chronological order.


            Note: This field contains only the authorization update attempts, so
            this field will be empty when 

            the payment is first created (even though the amount is authorized
            in this flow, it is not an update).
      required:
        - id
        - amount
        - net_amount
        - captured_amount
        - voided_amount
        - refunded_amount
        - currency
        - customer_id
        - merchant_id
        - grant_id
        - status
        - created_at
        - updated_at
      title: Payment
    EventDataDataObject3:
      type: object
      properties:
        payment:
          $ref: '#/components/schemas/Payment'
      title: EventDataDataObject3
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
    EventDataDataObject4:
      type: object
      properties:
        grant:
          $ref: '#/components/schemas/Grant'
      title: EventDataDataObject4
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
    EventDataDataObject5:
      type: object
      properties:
        refund:
          $ref: '#/components/schemas/Refund'
      title: EventDataDataObject5
    RequestStatus:
      type: string
      enum:
        - APPROVED
        - DECLINED
        - PENDING
        - PROCESSING
      default: PENDING
      description: >-
        Indicates if the state is approved, declined, or pending. Approved
        requests have grants, while pending and declined grants do not.


        Current values:


        - `PENDING`: The request has been created, but not responded to.

        - `PROCESSING`: The Cash App customer is actively responding to the
        request on their mobile device, and will require time to fill out
        information before the request is approved / declined.

        - `APPROVED`: The request was approved by the customer and grants have
        been created for the provided actions.

        - `DECLINED`: The request was denied by the customer. No grants were
        created.
      title: RequestStatus
    RequestAuthFlowTriggers:
      type: object
      properties:
        qr_code_image_url:
          type: string
          format: uri
          description: >-
            Link to a QR code customers can scan with Cash App to authorize the
            given action, encoded as a PNG file.


            Min length: `8`

            Max length: `1024`
        qr_code_svg_url:
          type: string
          format: uri
          description: >-
            Link to a QR code customers can scan with Cash App to authorize the
            given action, encoded as an SVG file.


            Min length: `8`

            Max length: `1024`
        mobile_url:
          type: string
          format: uri
          description: >-
            If on an Android or iOS device, the URL to redirect customers to in
            order to authorize the given action.


            Min length: `8`

            Max length: `1024`
        refreshes_at:
          type: string
          format: date-time
          description: >-
            When the QR code image URL will be rotated. Generally, it will
            rotate every ~20 seconds and become invalid after 30 seconds.
        desktop_url:
          type: string
          format: uri
          description: >-
            If on a desktop browser, the URL to redirect customers to in order
            to authorize the given action.


            Min length: `8`

            Max length: `1024`
      required:
        - qr_code_image_url
        - qr_code_svg_url
        - mobile_url
        - refreshes_at
      description: >-
        While the request is `PENDING`, contains different methods that can be
        used to start

        the authorization flow in the Cash App mobile application. Its contents
        refresh each time

        the `refreshes_at` timestamp passes. When the

        data refreshes, you should update any buttons

        or QR codes referring to it immediately.


        After a request has been scanned (and is no

        longer in the `PENDING` status), this

        field will no longer be returned.
      title: RequestAuthFlowTriggers
    RequestOriginType:
      type: string
      enum:
        - DIRECT
        - REQUEST_INITIATOR
      description: >-
        The method used to create the customer request.


        - `DIRECT` - the client or SDKs created this customer request by calling
        the "CreateCustomerRequest" endpoint

        - `REQUEST_INITIATOR` - a customer interacted with a request initiator
        and caused Cash App to create a customer request.
      title: RequestOriginType
    RequestOrigin:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/RequestOriginType'
          description: >-
            The method used to create the customer request.


            - `DIRECT` - the client or SDKs created this customer request by
            calling the "CreateCustomerRequest" endpoint

            - `REQUEST_INITIATOR` - a customer interacted with a request
            initiator and caused Cash App to create a customer request.
        id:
          type: string
          description: |-
            If present, is the ID of the initiator used to create this request.

            Min length: `1`
            Max length: `128`
      required:
        - type
      description: Metadata describing how the customer request was created.
      title: RequestOrigin
    RequestRequesterProfile:
      type: object
      properties:
        name:
          type: string
          description: |-
            Name of the brand to be shown in Cash App next to payments.

            Min length: `1`
            Max length: `1024`
        logo_url:
          type: string
          format: uri
          description: >-
            URL to the image of the entity (brand or client) that is requesting
            permission to perform the actions on the customer request.


            Formats:

            - `.jpg`

            - `.jpeg`

            - `.png`


            Min length: `8`

            Max length: `8000`
      required:
        - name
        - logo_url
      description: >-
        Details about the brand or client that are requesting permission to
        perform the actions on the customer request.
      title: RequestRequesterProfile
    RequestCustomerProfile:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this customer issued by Cash App.

            Min length: `1`
            Max length: `128`
        cashtag:
          type: string
          description: >-
            Public identifier for the customer on Cash App. [Learn
            more](https://cash.app/help/us/en-us/3123-cashtags).


            Min length: `1`

            Max length: `1024`
      required:
        - id
        - cashtag
      description: >-
        If the customer request was approved, contains the identity of the Cash
        App customer that approved it.
      title: RequestCustomerProfile
    CustomerMetadata:
      type: object
      properties:
        reference_id:
          type: string
          description: >-
            The `reference_id` of the customer approving this request. When a
            customer approves this request, that customer will be associated
            with this `reference_id`.
      description: Metadata to associate with the customer that approves this request.
      title: CustomerMetadata
    Request:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the request issued by Cash App.

            Min length: `1`
            Max length: `128`
        status:
          $ref: '#/components/schemas/RequestStatus'
          description: >-
            Indicates if the state is approved, declined, or pending. Approved
            requests have grants, while pending and declined grants do not.


            Current values:


            - `PENDING`: The request has been created, but not responded to.

            - `PROCESSING`: The Cash App customer is actively responding to the
            request on their mobile device, and will require time to fill out
            information before the request is approved / declined.

            - `APPROVED`: The request was approved by the customer and grants
            have been created for the provided actions.

            - `DECLINED`: The request was denied by the customer. No grants were
            created.
        actions:
          type: array
          items:
            $ref: '#/components/schemas/Action'
          description: >-
            Represents what the client intends to do to a customer if given
            authorization.


            No duplicate action types allowed.


            Min number of items: `1`

            Max number of items: `5`
        auth_flow_triggers:
          $ref: '#/components/schemas/RequestAuthFlowTriggers'
          description: >-
            While the request is `PENDING`, contains different methods that can
            be used to start

            the authorization flow in the Cash App mobile application. Its
            contents refresh each time

            the `refreshes_at` timestamp passes. When the

            data refreshes, you should update any buttons

            or QR codes referring to it immediately.


            After a request has been scanned (and is no

            longer in the `PENDING` status), this

            field will no longer be returned.
        redirect_url:
          type: string
          format: uri
          description: >-
            If this request is responded to via mobile redirect, this field
            specifies the URL that Cash App will open for a customer in the
            mobile device's default browser after the request is approved or
            declined.
        created_at:
          type: string
          format: date-time
          description: >-
            When this customer request was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When the customer request was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        expires_at:
          type: string
          format: date-time
          description: >-
            When this customer request will be automatically declined by Cash
            App, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)
            format (UTC).
        origin:
          $ref: '#/components/schemas/RequestOrigin'
          description: Metadata describing how the customer request was created.
        channel:
          $ref: '#/components/schemas/Channel'
        grants:
          type: array
          items:
            $ref: '#/components/schemas/Grant'
          description: >-
            If present, contains grants that can be used to perform actions
            specified in the request using the Network API.


            Each grant corresponds directly to an action on the request.


            Min number of items: `1`

            Max number of items: `5`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this request, typically used to
            associate the resource with a record in an external system.


            Min length: `1`

            Max length: `1024`
        requester_profile:
          $ref: '#/components/schemas/RequestRequesterProfile'
          description: >-
            Details about the brand or client that are requesting permission to
            perform the actions on the customer request.
        customer_profile:
          $ref: '#/components/schemas/RequestCustomerProfile'
          description: >-
            If the customer request was approved, contains the identity of the
            Cash App customer that approved it.
        metadata:
          $ref: '#/components/schemas/Metadata'
        customer_metadata:
          $ref: '#/components/schemas/CustomerMetadata'
      required:
        - id
        - status
        - actions
        - redirect_url
        - created_at
        - updated_at
        - expires_at
        - origin
        - channel
      description: >-
        Describes a request from a client to perform a given action on a
        customer's account.
      title: Request
    EventDataDataObject6:
      type: object
      properties:
        request:
          $ref: '#/components/schemas/Request'
      title: EventDataDataObject6
    EventDataDataObject:
      oneOf:
        - $ref: '#/components/schemas/EventDataDataObject0'
        - $ref: '#/components/schemas/EventDataDataObject1'
        - $ref: '#/components/schemas/EventDataDataObject2'
        - $ref: '#/components/schemas/EventDataDataObject3'
        - $ref: '#/components/schemas/EventDataDataObject4'
        - $ref: '#/components/schemas/EventDataDataObject5'
        - $ref: '#/components/schemas/EventDataDataObject6'
      description: The snapshot of the resource contained in the event.
      title: EventDataDataObject
    EventDataType:
      type: string
      enum:
        - customer
        - merchant
        - dispute
        - grant
        - payment
        - refund
        - request
      description: The type of the resource contained in the event.
      title: EventDataType
    EventDataData:
      type: object
      properties:
        id:
          type: string
          description: >-
            The unique ID provided by Cash App for the resource contained in the
            event.
        object:
          $ref: '#/components/schemas/EventDataDataObject'
          description: The snapshot of the resource contained in the event.
        type:
          $ref: '#/components/schemas/EventDataType'
      required:
        - id
        - object
        - type
      description: The underlying data encapsulated in the event.
      title: EventDataData
    EventData:
      type: object
      properties:
        event_id:
          type: string
          description: The unique ID of the webhook event.
        type:
          $ref: '#/components/schemas/EventType'
        created_at:
          type: string
          format: date-time
          description: The timestamp of when the event was created.
        data:
          $ref: '#/components/schemas/EventDataData'
          description: The underlying data encapsulated in the event.
      required:
        - event_id
        - type
        - created_at
        - data
      description: This represents the data that is delivered to a webhook endpoint.
      title: EventData
    WebhookEvent:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier for a webhook event issued by Cash App.
        webhook_endpoint_id:
          type: string
          description: This event is delivered to this webhook endpoint ID.
        event_type:
          $ref: '#/components/schemas/EventType'
        status:
          $ref: '#/components/schemas/EventStatus'
        created_at:
          type: string
          format: date-time
          description: The timestamp of when the event was created.
        updated_at:
          type: string
          format: date-time
          description: The timestamp of when the event was last updated.
        expires_at:
          type: string
          format: date-time
          description: >-
            The timestamp of when this event will expire and no longer be
            available in Cash App.
        event_data:
          $ref: '#/components/schemas/EventData'
        api_version:
          type: string
          description: The API version used to serialize the event data.
      required:
        - id
        - webhook_endpoint_id
        - event_type
        - status
        - created_at
        - updated_at
        - expires_at
        - event_data
        - api_version
      description: >-
        The event that is being sent to a particular webhook endpoint. The event
        is either in the process of being delivered (PENDING), has been
        successfully delivered (SUCCESS), or has failed all attempts to deliver
        (FAILED).
      title: WebhookEvent
    webhooks_list-webhook-events_Response_200:
      type: object
      properties:
        webhook_events:
          type: array
          items:
            $ref: '#/components/schemas/WebhookEvent'
        cursor:
          type: string
          description: >-
            The pagination cursor to be used in a subsequent request. If empty,
            this is the final response.
      required:
        - webhook_events
      title: webhooks_list-webhook-events_Response_200
    ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: |-
            A list of errors that occurred while processing the request.

            Min number of items: `1`
      required:
        - errors
      title: ErrorResponse

```

## SDK Code Examples

```python
import requests

url = "https://api.cash.app/management/v1/webhook-events"

headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/management/v1/webhook-events';
const options = {
  method: 'GET',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent'
  }
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/webhook-events"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("X-Region", "X-Region")
	req.Header.Add("X-Signature", "X-Signature")
	req.Header.Add("User-Agent", "User-Agent")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/management/v1/webhook-events")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.cash.app/management/v1/webhook-events")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cash.app/management/v1/webhook-events', [
  'headers' => [
    'Accept' => 'Accept',
    'User-Agent' => 'User-Agent',
    'X-Region' => 'X-Region',
    'X-Signature' => 'X-Signature',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/webhook-events");
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/webhook-events")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```