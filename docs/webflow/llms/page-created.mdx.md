# Source: https://developers.webflow.com/data/reference/webhooks/events/page-created.mdx

# Page Created

POST 

Information about a new pages

Reference: https://developers.webflow.com/data/reference/webhooks/events/page-created

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  page-created:
    post:
      operationId: page-created
      summary: Page Created
      description: Information about a new pages
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
                    #/components/schemas/WebhooksPageCreatedPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksPageCreatedPayloadContentApplicationJsonSchemaPayload:
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
        createdOn:
          type: string
          format: date-time
        publishedPath:
          type: string
      description: The payload of data sent from Webflow
      title: WebhooksPageCreatedPayloadContentApplicationJsonSchemaPayload

```