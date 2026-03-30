# Source: https://developers.webflow.com/data/reference/webhooks/events/page-deleted.mdx

# Page Deleted

POST 

Information about a page that was deleted

Reference: https://developers.webflow.com/data/reference/webhooks/events/page-deleted

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  page-deleted:
    post:
      operationId: page-deleted
      summary: Page Deleted
      description: Information about a page that was deleted
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
                    #/components/schemas/WebhooksPageDeletedPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksPageDeletedPayloadContentApplicationJsonSchemaPayload:
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
        deletedOn:
          type: string
          format: date-time
        publishedPath:
          type: string
      description: The payload of data sent from Webflow
      title: WebhooksPageDeletedPayloadContentApplicationJsonSchemaPayload

```