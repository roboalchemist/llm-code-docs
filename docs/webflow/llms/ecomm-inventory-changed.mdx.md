# Source: https://developers.webflow.com/data/reference/webhooks/events/ecomm-inventory-changed.mdx

# Updated eComm Inventory

POST 

Information about updated ecommerce inventory values

Reference: https://developers.webflow.com/data/reference/webhooks/events/ecomm-inventory-changed

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
      description: Information about updated ecommerce inventory values
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                triggerType:
                  $ref: >-
                    #/components/schemas/WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaTriggerType
                payload:
                  $ref: >-
                    #/components/schemas/WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaPayload
                  description: The availabile inventory for an item
components:
  schemas:
    WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaTriggerType:
      type: string
      enum:
        - ecomm_inventory_changed
      title: >-
        WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaTriggerType
    WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaPayloadInventoryType:
      type: string
      enum:
        - infinite
        - finite
      description: infinite or finite
      title: >-
        WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaPayloadInventoryType
    WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for a SKU item
        quantity:
          type: number
          format: double
          description: >-
            Total quantity of items remaining in inventory (if inventoryType is
            finite)
        inventoryType:
          $ref: >-
            #/components/schemas/WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaPayloadInventoryType
          description: infinite or finite
      description: The availabile inventory for an item
      title: WebhooksEcommInventoryChangedPayloadContentApplicationJsonSchemaPayload

```