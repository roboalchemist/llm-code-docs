# Source: https://developers.webflow.com/data/reference/webhooks/events/site-publish.mdx

# Site Publish

POST 

Information about a site that was published

Reference: https://developers.webflow.com/data/reference/webhooks/events/site-publish

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  site-publish:
    post:
      operationId: site-publish
      summary: Site Publish
      description: Information about a site that was published
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
                    #/components/schemas/WebhooksSitePublishPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksSitePublishPayloadContentApplicationJsonSchemaPayloadPublishedBy:
      type: object
      properties: {}
      description: The name andID of the user who published the site
      title: WebhooksSitePublishPayloadContentApplicationJsonSchemaPayloadPublishedBy
    WebhooksSitePublishPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        siteId:
          type: string
          format: objectid
          description: The ID of the site that was published
        publishedOn:
          type: string
          format: date-time
          description: The timestamp of the publish event
        domains:
          type: array
          items:
            type: string
          description: The domains that were published
        publishedBy:
          $ref: >-
            #/components/schemas/WebhooksSitePublishPayloadContentApplicationJsonSchemaPayloadPublishedBy
          description: The name andID of the user who published the site
      description: The payload of data sent from Webflow
      title: WebhooksSitePublishPayloadContentApplicationJsonSchemaPayload

```