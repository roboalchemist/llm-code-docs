# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/get-order.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Order

> Retrieve a specific order by ID

Retrieve detailed information about a specific order using its unique identifier.

## Path Parameters

* **order\_id** (required) - The UUID of the order to retrieve

## Response

Returns a complete order object with:

* **id** - Order UUID
* **status** - Current order status
* **items** - Array of order items with individual statuses
* **shipping\_address** - Delivery address
* **job\_result** - Detailed processing results (when available)
* **created\_at** - Order creation timestamp
* **updated\_at** - Last update timestamp

## Item-Level Status

Each item in the order has its own status tracking:

```json  theme={null}
{
  "id": "item-uuid",
  "url": "https://www.amazon.com/...",
  "quantity": 2,
  "status": "shipped",
  "created_at": "2025-11-24T10:00:00Z",
  "updated_at": "2025-11-24T12:30:00Z"
}
```

## Job Results

For completed or failed orders, the `job_result` field contains detailed information about the order processing, including:

* Success/failure status
* Retailer confirmation numbers
* Tracking information
* Error details (if failed)

<Tip>
  Poll this endpoint to track order progress. We recommend checking every 30-60 seconds while the order is processing.
</Tip>

## Error Responses

* **404 Not Found** - Order ID does not exist or you don't have access to it
* **401 Unauthorized** - Invalid or missing authentication


## OpenAPI

````yaml versions/latest.json get /orders/{order_id}
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
  /orders/{order_id}:
    get:
      tags:
        - orders
      summary: Get Order
      description: Retrieves an order by its ID
      operationId: get_order_orders__order_id__get
      parameters:
        - name: order_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Order Id
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
                $ref: '#/components/schemas/OrderResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
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