# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/merchant-status-updated.mdx

# Event: merchant.status.updated

POST 

**When is this event triggered?**

This event is created whenever a merchant's status is changed. The status change can be due to do many different things:
  - An API client-initiated action to disable / enable the merchant
  - An asynchronous merchant registration process completing, moving the merchant from pending to active
  - A compliance ban on the merchant, moving them to disabled

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/merchant-status-updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  merchant-status-updated:
    post:
      operationId: merchant-status-updated
      summary: 'Event: merchant.status.updated'
      description: >-
        **When is this event triggered?**


        This event is created whenever a merchant's status is changed. The
        status change can be due to do many different things:
          - An API client-initiated action to disable / enable the merchant
          - An asynchronous merchant registration process completing, moving the merchant from pending to active
          - A compliance ban on the merchant, moving them to disabled
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
                    The type of event that occurred. `merchant.status.updated`
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
                    #/components/schemas/WebhooksMerchantStatusUpdatedPayloadContentApplicationJsonSchemaData
                  description: Data about the merchant that had a status change.
              required:
                - type
                - event_id
                - created_at
                - data
components:
  schemas:
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
    WebhooksMerchantStatusUpdatedPayloadContentApplicationJsonSchemaDataObject:
      type: object
      properties:
        merchant:
          $ref: '#/components/schemas/Merchant'
      required:
        - merchant
      description: >-
        A snapshot of the merchant data immediately after the merchant's status
        changed.
      title: >-
        WebhooksMerchantStatusUpdatedPayloadContentApplicationJsonSchemaDataObject
    WebhooksMerchantStatusUpdatedPayloadContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: A unique identifier provided by Cash App for the merchant.
        object:
          $ref: >-
            #/components/schemas/WebhooksMerchantStatusUpdatedPayloadContentApplicationJsonSchemaDataObject
          description: >-
            A snapshot of the merchant data immediately after the merchant's
            status changed.
        type:
          type: string
          description: >-
            The resource type contained in the `object` field. For this event,
            it is `merchant`.
      required:
        - id
        - object
        - type
      description: Data about the merchant that had a status change.
      title: WebhooksMerchantStatusUpdatedPayloadContentApplicationJsonSchemaData

```