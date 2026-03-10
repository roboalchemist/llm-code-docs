# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/customer-updated.mdx

# Event: customer.updated

POST 

**When is this event triggered?**

This event is created whenever a Cash App Pay customer is updated. The `customer.updated` event can be triggered when:
  - A customer updates their Cashtag.
  - A customer approves a request with a `customer_metadata.reference_id` attribute. Upon approval of the request, the customer's `reference_id` attribute is updated.

  > **Note:** If the `customer_metadata.reference_id` is the same as the customer's current `reference_id`, the customer will not be updated and the event will not be triggered.

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/customer-updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  customer-updated:
    post:
      operationId: customer-updated
      summary: 'Event: customer.updated'
      description: >-
        **When is this event triggered?**


        This event is created whenever a Cash App Pay customer is updated. The
        `customer.updated` event can be triggered when:
          - A customer updates their Cashtag.
          - A customer approves a request with a `customer_metadata.reference_id` attribute. Upon approval of the request, the customer's `reference_id` attribute is updated.

          > **Note:** If the `customer_metadata.reference_id` is the same as the customer's current `reference_id`, the customer will not be updated and the event will not be triggered.
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
                    The type of event that occurred. `customer.updated` for this
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
                    #/components/schemas/WebhooksCustomerUpdatedPayloadContentApplicationJsonSchemaData
                  description: Data about the Customer that was updated.
              required:
                - type
                - event_id
                - created_at
                - data
components:
  schemas:
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
    WebhooksCustomerUpdatedPayloadContentApplicationJsonSchemaDataObject:
      type: object
      properties:
        customer:
          $ref: '#/components/schemas/Customer'
      required:
        - customer
      description: A snapshot of the customer immediately after the customer was updated.
      title: WebhooksCustomerUpdatedPayloadContentApplicationJsonSchemaDataObject
    WebhooksCustomerUpdatedPayloadContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: A unique identifier provided by Cash App for the customer.
        object:
          $ref: >-
            #/components/schemas/WebhooksCustomerUpdatedPayloadContentApplicationJsonSchemaDataObject
          description: >-
            A snapshot of the customer immediately after the customer was
            updated.
        type:
          type: string
          description: >-
            The resource type contained in the `object` field. For this event,
            it is `customer`.
      required:
        - id
        - object
        - type
      description: Data about the Customer that was updated.
      title: WebhooksCustomerUpdatedPayloadContentApplicationJsonSchemaData

```