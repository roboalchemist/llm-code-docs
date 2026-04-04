# Source: https://developers.webflow.com/data/reference/webhooks/events/collection-item-unpublished.mdx

# Collection Item Unpublished

POST 

Information about a collection item that was removed from the live site

Reference: https://developers.webflow.com/data/reference/webhooks/events/collection-item-unpublished

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
      summary: Collection Item Unpublished
      description: Information about a collection item that was removed from the live site
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
                    #/components/schemas/WebhooksCollectionItemUnpublishedPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksCollectionItemUnpublishedPayloadContentApplicationJsonSchemaPayloadFieldData:
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
        WebhooksCollectionItemUnpublishedPayloadContentApplicationJsonSchemaPayloadFieldData
    WebhooksCollectionItemUnpublishedPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: The ID of the collection item that was unpublished
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
            #/components/schemas/WebhooksCollectionItemUnpublishedPayloadContentApplicationJsonSchemaPayloadFieldData
      description: The payload of data sent from Webflow
      title: >-
        WebhooksCollectionItemUnpublishedPayloadContentApplicationJsonSchemaPayload

```