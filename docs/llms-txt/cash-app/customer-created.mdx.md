# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/customer-created.mdx

# Event: customer.created

POST 

**When is this event triggered?**

This event is created whenever a new Cash App Pay customer is created. A new Cash App Pay customer is created when a Cash App user approves a client's Cash App Pay request for the first time. This event allows clients to detect customers who are using a client's Cash App Pay integration for the first time.

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/customer-created

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  customer-created:
    post:
      operationId: customer-created
      summary: 'Event: customer.created'
      description: >-
        **When is this event triggered?**


        This event is created whenever a new Cash App Pay customer is created. A
        new Cash App Pay customer is created when a Cash App user approves a
        client's Cash App Pay request for the first time. This event allows
        clients to detect customers who are using a client's Cash App Pay
        integration for the first time.
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
                    The type of event that occurred. `customer.created` for this
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
                    #/components/schemas/WebhooksCustomerCreatedPayloadContentApplicationJsonSchemaData
                  description: Data about the Customer that was created.
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
    WebhooksCustomerCreatedPayloadContentApplicationJsonSchemaDataObject:
      type: object
      properties:
        customer:
          $ref: '#/components/schemas/Customer'
      required:
        - customer
      description: A snapshot of the customer immediately after the customer was created.
      title: WebhooksCustomerCreatedPayloadContentApplicationJsonSchemaDataObject
    WebhooksCustomerCreatedPayloadContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          description: A unique identifier provided by Cash App for the customer.
        object:
          $ref: >-
            #/components/schemas/WebhooksCustomerCreatedPayloadContentApplicationJsonSchemaDataObject
          description: >-
            A snapshot of the customer immediately after the customer was
            created.
        type:
          type: string
          description: >-
            The resource type contained in the `object` field. For this event,
            it is `customer`.
      required:
        - id
        - object
        - type
      description: Data about the Customer that was created.
      title: WebhooksCustomerCreatedPayloadContentApplicationJsonSchemaData

```