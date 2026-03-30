# Source: https://developers.webflow.com/data/reference/webhooks/events/collection-item-changed.mdx

# Collection Item Updated

POST 

Information about an updated collection item

Reference: https://developers.webflow.com/data/reference/webhooks/events/collection-item-changed

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  collection-item-changed:
    post:
      operationId: collection-item-changed
      summary: Collection Item Updated
      description: Information about an updated collection item
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
                    #/components/schemas/WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaTriggerType
                  description: The type of event that triggered the request
                payload:
                  $ref: >-
                    #/components/schemas/WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaPayload
              required:
                - triggerType
                - payload
components:
  schemas:
    WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaTriggerType:
      type: string
      enum:
        - collection_item_changed
      description: The type of event that triggered the request
      title: >-
        WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaTriggerType
    WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaPayloadFieldData:
      type: object
      properties:
        name:
          type: string
        slug:
          type: string
      required:
        - name
        - slug
      title: >-
        WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaPayloadFieldData
    WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the Item
        workspaceId:
          type: string
          format: uuid
          description: Unique identifier of the workspace
        siteId:
          type: string
          format: uuid
          description: Unique identifier of the site
        collectionId:
          type: string
          format: uuid
          description: Unique identifier of the collection
        cmsLocaleId:
          type:
            - string
            - 'null'
          format: uuid
          description: Unique identifier of the CMS locale for this item
        lastPublished:
          type:
            - string
            - 'null'
          format: date-time
        lastUpdated:
          type: string
          format: date-time
        createdOn:
          type: string
          format: date-time
        isArchived:
          type: boolean
        isDraft:
          type: boolean
        fieldData:
          $ref: >-
            #/components/schemas/WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaPayloadFieldData
      required:
        - id
        - workspaceId
        - siteId
        - collectionId
        - fieldData
      title: WebhooksCollectionItemChangedPayloadContentApplicationJsonSchemaPayload

```