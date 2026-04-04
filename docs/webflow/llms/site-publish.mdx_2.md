# Source: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/site-publish.mdx

# Site Publish

POST 

Reference: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/site-publish

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
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        description: The information about the site(s) published
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SitePublish'
components:
  schemas:
    SitePublishPublishedBy:
      type: object
      properties: {}
      description: The name andID of the user who published the site
      title: SitePublishPublishedBy
    SitePublish:
      type: object
      properties:
        site:
          type: string
          format: uuid
          description: The siteIDthat was published
        publishTime:
          type: string
          format: date-time
          description: The timestamp of the publish event
        domains:
          type: array
          items:
            type: string
          description: The domains that were published
        publishedBy:
          $ref: '#/components/schemas/SitePublishPublishedBy'
          description: The name andID of the user who published the site
      title: SitePublish

```