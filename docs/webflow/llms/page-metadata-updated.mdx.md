# Source: https://developers.webflow.com/data/reference/webhooks/events/page-metadata-updated.mdx

# Page Metadata Updated

POST 

Information about a page's updated metadata and/or settings

Reference: https://developers.webflow.com/data/reference/webhooks/events/page-metadata-updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  page-metadata-updated:
    post:
      operationId: page-metadata-updated
      summary: Page Metadata Updated
      description: Information about a page's updated metadata and/or settings
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
                    #/components/schemas/WebhooksPageMetadataUpdatedPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksPageMetadataUpdatedPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        siteId:
          type: string
          format: objectid
        pageId:
          type: string
          format: objectid
        pageTitle:
          type: string
        lastUpdated:
          type: string
          format: date-time
        publishedPath:
          type: string
      description: The payload of data sent from Webflow
      title: WebhooksPageMetadataUpdatedPayloadContentApplicationJsonSchemaPayload

```