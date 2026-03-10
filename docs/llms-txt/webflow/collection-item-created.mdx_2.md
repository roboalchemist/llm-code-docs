# Source: https://developers.webflow.com/data/v1.0.0/reference/cms/items/collection-item-created.mdx

# Item Created

POST 

Reference: https://developers.webflow.com/data/v1.0.0/reference/cms/items/collection-item-created

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  collection-item-created:
    post:
      operationId: collection-item-created
      summary: Item Created
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        description: The information about the collection item that was created
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CollectionItem'
components:
  schemas:
    CollectionItem:
      type: object
      properties:
        _archived:
          type: boolean
          default: false
          description: Boolean determining if the Item is set to archived
        _draft:
          type: boolean
          default: false
          description: Boolean determining if the Item is set to draft
        _id:
          type: string
          description: Unique identifier for the Item
        _cid:
          type: string
          description: Unique identifier for the Collection the Item belongs within
        name:
          type: string
          description: Name given to the Item
        slug:
          type: string
          description: >-
            URL structure of the Item in your site. Note: Updates to an item
            slug will break all links referencing the old slug.
      description: >
        The fields that define the schema for a given Item are based on the
        Collection that Item belongs to. Beyond the user defined fields, there
        are a handful of additional fields that are automatically created for
        all items
      title: CollectionItem

```