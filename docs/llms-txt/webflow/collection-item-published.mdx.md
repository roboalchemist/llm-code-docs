# Source: https://developers.webflow.com/data/reference/webhooks/events/collection-item-published.mdx

# Collection Item Published

POST 

Information about a collection item that was published

Reference: https://developers.webflow.com/data/reference/webhooks/events/collection-item-published

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  collection-item-published:
    post:
      operationId: collection-item-published
      summary: Collection Item Published
      description: Information about a collection item that was published
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
                    #/components/schemas/WebhooksCollectionItemPublishedPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksCollectionItemPublishedPayloadContentApplicationJsonSchemaPayloadFieldData:
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
        WebhooksCollectionItemPublishedPayloadContentApplicationJsonSchemaPayloadFieldData
    WebhooksCollectionItemPublishedPayloadContentApplicationJsonSchemaPayload:
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
            #/components/schemas/WebhooksCollectionItemPublishedPayloadContentApplicationJsonSchemaPayloadFieldData
      description: The payload of data sent from Webflow
      title: >-
        WebhooksCollectionItemPublishedPayloadContentApplicationJsonSchemaPayload

```