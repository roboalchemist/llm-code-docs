# Source: https://developers.webflow.com/data/v1.0.0/reference/cms/items/collection-item-unpublished.mdx

# Item Unpublished

POST 

Reference: https://developers.webflow.com/data/v1.0.0/reference/cms/items/collection-item-unpublished

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  collection-item-unpublished:
    post:
      operationId: collection-item-unpublished
      summary: Item Unpublished
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        description: The results from unpublishing the collection item
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