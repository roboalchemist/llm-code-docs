# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/list-orders.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Orders

> Retrieve all orders for your account

Retrieve a list of all orders associated with your account. Orders are returned in reverse chronological order (most recent first).

## Response

Returns an array of order objects, each containing:

* **id** - Order UUID
* **status** - Current order status
* **items** - Products in the order
* **shipping\_address** - Delivery address
* **job\_result** - Processing results (for completed/failed orders)
* **created\_at** - Order creation timestamp
* **updated\_at** - Last update timestamp

## Order Statuses

| Status        | Description                        |
| ------------- | ---------------------------------- |
| `pending`     | Order queued, not yet processing   |
| `in_progress` | Order is being placed              |
| `ordered`     | Successfully placed with retailer  |
| `shipped`     | Order shipped (tracking available) |
| `delivered`   | Order delivered to address         |
| `cancelled`   | Order was cancelled                |
| `failed`      | Order processing failed            |

## Pagination

<Info>
  Currently, all orders are returned in a single response. Pagination will be added in a future update.
</Info>


## OpenAPI

````yaml versions/latest.json get /orders
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
    get:
      tags:
        - orders
      summary: List Orders
      description: Get a list of orders for the current user
      operationId: list_orders_orders_get
      parameters:
        - name: order_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Filter by order ID (partial match)
            title: Order Id
          description: Filter by order ID (partial match)
        - name: authorization
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Authorization
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderListResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    OrderListResponse:
      properties:
        orders:
          items:
            $ref: '#/components/schemas/OrderResponse'
          type: array
          title: Orders
      type: object
      required:
        - orders
      title: OrderListResponse
      description: List of orders for a particular user_id
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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