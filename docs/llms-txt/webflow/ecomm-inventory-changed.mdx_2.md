# Source: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/inventory/ecomm-inventory-changed.mdx

# Updated eComm Inventory

POST 

Reference: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/inventory/ecomm-inventory-changed

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  ecomm-inventory-changed:
    post:
      operationId: ecomm-inventory-changed
      summary: Updated eComm Inventory
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        description: The information about the inventory item that changed
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InventoryItem'
components:
  schemas:
    InventoryItemInventoryType:
      type: string
      enum:
        - infinite
        - finite
      description: infinite or finite
      title: InventoryItemInventoryType
    InventoryItem:
      type: object
      properties:
        _id:
          type: string
          format: uuid
          description: Unique identifier for a SKU item
        quantity:
          type: number
          format: double
          description: Total quantity of items remaining in inventory (if finite)
        inventoryType:
          $ref: '#/components/schemas/InventoryItemInventoryType'
          description: infinite or finite
      description: The availabile inventory for an item
      title: InventoryItem

```