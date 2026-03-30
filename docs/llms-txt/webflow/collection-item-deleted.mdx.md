# Source: https://developers.webflow.com/data/reference/webhooks/events/collection-item-deleted.mdx

# Collection Item Deleted

POST 

Information about a deleted collection item

Reference: https://developers.webflow.com/data/reference/webhooks/events/collection-item-deleted

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
      summary: Collection Item Deleted
      description: Information about a deleted collection item
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
                  type: string
                  description: The type of event that triggered the request
                payload:
                  $ref: >-
                    #/components/schemas/WebhooksCollectionItemDeletedPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksCollectionItemDeletedPayloadContentApplicationJsonSchemaPayloadFieldData:
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
        WebhooksCollectionItemDeletedPayloadContentApplicationJsonSchemaPayloadFieldData
    WebhooksCollectionItemDeletedPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: The ID of the collection item that was deleted
        siteId:
          type: string
          format: objectid
          description: The ID of the site
        workspaceId:
          type: string
          format: objectid
          description: The ID of the workspace
        collectionId:
          type: string
          format: objectid
          description: The ID of the collection
        cmsLocaleId:
          type: string
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
            #/components/schemas/WebhooksCollectionItemDeletedPayloadContentApplicationJsonSchemaPayloadFieldData
      description: The payload of data sent from Webflow
      title: WebhooksCollectionItemDeletedPayloadContentApplicationJsonSchemaPayload

```