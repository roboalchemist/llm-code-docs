# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/create-order.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Order

> Create a new order

Create a new order for processing. Orders are queued and processed asynchronously.

## Request Flow

1. **Submit Order** - Send order details including products and shipping address
2. **Validation** - We validate product URLs and shipping address
3. **Queued** - Order is queued for processing
4. **Processing** - Our system places the order with the retailer
5. **Completed** - You receive confirmation with tracking details

<Frame caption="Order processing flow">
  <img src="https://mintcdn.com/zinc/exQ2EzxrXSSg0dh-/images/orders.png?fit=max&auto=format&n=exQ2EzxrXSSg0dh-&q=85&s=e1dce1f7b158000ba79bad1ecd8fabae" alt="Order flow diagram" width="425" height="539" data-path="images/orders.png" />
</Frame>

## Product URLs

Provide direct product URLs from supported retailers. Each product must include:

* **url** - Direct link to the product page

<Info>
  Make sure product URLs are accessible and lead directly to the product page, not search results or category pages.
</Info>

Optionally, the product can include:

* **quantity** - Number of items to order (integer, default 1)
* **variant** - A list of label, value pairs indicating a variant of a product.
  For example, if you're ordering a shirt. The shirt may come in different colors and different sizes.
  To indicate a red medium shirt, you would do:
  ```
  [
    {
      "label": "Color",
      "value": "Red"
    },
    {
      "label": "Size",
      "value": "Medium"
    }
  ]
  ```
  <Info>
    Make sure the strings used for both the label and value match up to what is
    present on the retailer website. For example, if a `medium` is indicated by the value `M`, use `M`
    for the value.
  </Info>

## Shipping Address

All orders require a valid US shipping address. Addresses are validated using Google's Address Validation API.

Required fields:

* Name
* Street address
* City
* State (2-letter code)
* Postal code
* Phone number
* Country (must be "US")

<Warning>
  We currently only support shipping to addresses in the United States.
</Warning>

## Optional Order Data

You can include additional data with your order for tracking and reference purposes.
This data *will* be used by our system as as input to any fields during checkout that match.

* **po\_number** - Your internal purchase order number for tracking and reconciliation

<Tip>
  If you only need data for internal reference, use the `metadata` field instead.
</Tip>

## Response

A successful order creation returns:

* **id** - Unique order identifier (UUID)
* **status** - Current order status (initially "pending")
* **items** - Array of order items with their details
* **shipping\_address** - Confirmed shipping address
* **created\_at** - Timestamp of order creation

Use the order `id` to retrieve order status and updates.


## OpenAPI

````yaml versions/latest.json post /orders
openapi: 3.1.0
info:
  title: 'Zinc '
  summary: >-
    Zinc lets you search, buy, and return items from top online retailers with a
    single API.
  version: '2026-02-19'
  x-logo:
    url: https://mintlify.s3.us-west-1.amazonaws.com/zinc/logo/light.png
servers:
  - url: https://api.zinc.com
    description: Production
security: []
paths:
  /orders:
    post:
      tags:
        - orders
      summary: Create Order
      description: Posts an order to a queue for processing
      operationId: create_order_orders_post
      parameters:
        - name: authorization
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Authorization
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderCreate'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    OrderCreate:
      properties:
        products:
          items:
            $ref: '#/components/schemas/OrderProduct'
          type: array
          title: Products
        shipping_address:
          $ref: '#/components/schemas/Address'
        max_price:
          type: integer
          title: Max Price
          description: >-
            Maximum price (in cents) allowed for an order before it is
            finalized.
        idempotency_key:
          anyOf:
            - type: string
              maxLength: 36
            - type: 'null'
          title: Idempotency Key
          description: >-
            Optional idempotency key to prevent duplicate orders. If not
            provided, one will be generated.
        retailer_credentials_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Retailer Credentials Id
          description: >-
            Optional short ID (e.g., 'zn_acct_XXXXXXXX') of specific retailer
            credentials to use for this order. If not provided, credentials will
            be selected automatically.
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Metadata
          description: >-
            Optional metadata to attach to the order. Can contain arbitrary
            key-value pairs.
        po_number:
          anyOf:
            - type: string
            - type: 'null'
          title: Po Number
          description: Optional purchase order number for the order.
      type: object
      required:
        - products
        - shipping_address
        - max_price
      title: OrderCreate
      description: Request model for creating a new order.
    OrderResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        status:
          $ref: '#/components/schemas/OrderStatus'
        max_price:
          type: integer
          title: Max Price
        attempts:
          type: integer
          title: Attempts
        items:
          items:
            $ref: '#/components/schemas/OrderItemResponse'
          type: array
          title: Items
        shipping_address:
          additionalProperties: true
          type: object
          title: Shipping Address
        metadata:
          additionalProperties: true
          type: object
          title: Metadata
          default: {}
        po_number:
          anyOf:
            - type: string
            - type: 'null'
          title: Po Number
        retailer_credentials_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Retailer Credentials Id
        tracking_numbers:
          items:
            $ref: '#/components/schemas/TrackingNumberResponse'
          type: array
          title: Tracking Numbers
          default: []
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - id
        - status
        - max_price
        - attempts
        - items
        - shipping_address
        - retailer_credentials_id
        - created_at
        - updated_at
      title: OrderResponse
      description: Response model for order data.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    OrderProduct:
      properties:
        url:
          type: string
          title: Url
          examples:
            - https://www.amazon.com/dp/B07JGBW826
        quantity:
          type: integer
          maximum: 100
          minimum: 1
          title: Quantity
          default: 1
        variant:
          anyOf:
            - items:
                $ref: '#/components/schemas/ProductVariant'
              type: array
            - type: 'null'
          title: Variant
          description: Product variants to select (e.g., color, size)
      type: object
      required:
        - url
      title: OrderProduct
      description: |-
        Product item for an order.

        For example:
        ````{
            url: "https://www.amazon.com/dp/B07JGBW826",
            quantity: 1
        }```
    Address:
      properties:
        first_name:
          type: string
          title: First Name
        last_name:
          type: string
          title: Last Name
        address_line1:
          type: string
          title: Address Line1
        address_line2:
          anyOf:
            - type: string
            - type: 'null'
          title: Address Line2
        city:
          type: string
          title: City
        state:
          anyOf:
            - type: string
            - type: 'null'
          title: State
        postal_code:
          type: string
          title: Postal Code
        phone_number:
          type: string
          title: Phone Number
        country:
          type: string
          title: Country
          default: US
      type: object
      required:
        - first_name
        - last_name
        - address_line1
        - city
        - postal_code
        - phone_number
      title: Address
      description: >-
        Shipping address model.


        Supports international addresses. The `state` field is optional for
        countries

        that don't use states/provinces. The `country` field uses ISO 3166-1
        alpha-2

        country codes (e.g., "US", "CA", "GB", "DE").
    OrderStatus:
      type: string
      enum:
        - pending
        - in_progress
        - order_placed
        - order_failed
        - cancelled
      title: OrderStatus
    OrderItemResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        url:
          type: string
          title: Url
        quantity:
          type: integer
          title: Quantity
        variant:
          anyOf:
            - items:
                $ref: '#/components/schemas/ProductVariant'
              type: array
            - type: 'null'
          title: Variant
        status:
          $ref: '#/components/schemas/OrderItemStatus'
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - id
        - url
        - quantity
        - status
        - created_at
        - updated_at
      title: OrderItemResponse
      description: Response model for order item data.
    TrackingNumberResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        carrier:
          type: string
          title: Carrier
        tracking_number:
          type: string
          title: Tracking Number
        created_at:
          type: string
          format: date-time
          title: Created At
      type: object
      required:
        - id
        - carrier
        - tracking_number
        - created_at
      title: TrackingNumberResponse
      description: Response model for tracking number data.
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    ProductVariant:
      properties:
        label:
          type: string
          minLength: 1
          title: Label
          description: Variant label (e.g., 'Color', 'Size')
        value:
          type: string
          minLength: 1
          title: Value
          description: Variant value (e.g., 'Black', 'Large')
      type: object
      required:
        - label
        - value
      title: ProductVariant
      description: >-
        Product variant schema for selecting product options (color, size,
        etc.).
    OrderItemStatus:
      type: string
      enum:
        - pending
        - processing
        - ordered
        - shipped
        - delivered
        - cancelled
        - failed
      title: OrderItemStatus

````

Built with [Mintlify](https://mintlify.com).