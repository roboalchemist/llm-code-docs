# Source: https://developers.webflow.com/data/v1.0.0/reference/cms/items/collection-item-deleted.mdx

# Item Deleted

POST 

Reference: https://developers.webflow.com/data/v1.0.0/reference/cms/items/collection-item-deleted

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  collection-item-deleted:
    post:
      operationId: collection-item-deleted
      summary: Item Deleted
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        description: The results from deleting the collection item
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CollectionItemRemoved'
components:
  schemas:
    CollectionItemRemoved:
      type: object
      properties:
        deleted:
          type: number
          format: double
          description: The number of items deleted
        itemId:
          type: string
          format: uuid
          description: The ID of the collection item that was deleted
      title: CollectionItemRemoved

```