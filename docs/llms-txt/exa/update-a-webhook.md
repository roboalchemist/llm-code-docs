# Source: https://exa.ai/docs/websets/api/webhooks/update-a-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Webhook

> Change a webhook's settings. You can update:
- Events: Add or remove which events you want to hear about - URL: Change where notifications are sent - Metadata: Update custom data linked to the webhook

Changes happen right away. If you change the events list, the webhook will start or stop getting notifications for those events immediately.

The webhook keeps its current status (`active` or `inactive`) when you update it.



## OpenAPI

````yaml patch /v0/webhooks/{id}
openapi: 3.1.0
info:
  title: Websets
  description: ''
  version: '0'
  contact: {}
servers:
  - url: https://api.exa.ai/websets/
    description: Production
security: []
tags: []
paths:
  /v0/webhooks/{id}:
    patch:
      tags:
        - Webhooks
      summary: Update a Webhook
      description: >-
        Change a webhook's settings. You can update:

        - Events: Add or remove which events you want to hear about - URL:
        Change where notifications are sent - Metadata: Update custom data
        linked to the webhook


        Changes happen right away. If you change the events list, the webhook
        will start or stop getting notifications for those events immediately.


        The webhook keeps its current status (`active` or `inactive`) when you
        update it.
      operationId: webhooks-update
      parameters:
        - name: id
          required: true
          in: path
          description: The id of the webhook
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateWebhookParameters'
      responses:
        '200':
          description: Webhook
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Webhook'
          headers:
            X-Request-Id:
              schema:
                type: string
              description: Unique identifier for the request.
              example: req_N6SsgoiaOQOPqsYKKiw5
              required: true
        '404':
          description: Webhook not found
          headers:
            X-Request-Id:
              schema:
                type: string
              description: Unique identifier for the request.
              example: req_N6SsgoiaOQOPqsYKKiw5
              required: true
      security:
        - api_key: []
components:
  schemas:
    UpdateWebhookParameters:
      type:
        - object
      properties:
        events:
          type:
            - array
          items:
            $ref: '#/components/schemas/EventType'
            type:
              - string
          minItems: 1
          maxItems: 19
          description: The events to trigger the webhook
        url:
          type:
            - string
          format: uri
          description: The URL to send the webhook to
        metadata:
          description: Set of key-value pairs you want to associate with this object.
          type:
            - object
          additionalProperties:
            type:
              - string
            maxLength: 1000
    Webhook:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the webhook
        object:
          type: string
          const: webhook
          default: webhook
        status:
          type:
            - string
          enum:
            - active
            - inactive
          description: The status of the webhook
          title: WebhookStatus
        events:
          type:
            - array
          items:
            $ref: '#/components/schemas/EventType'
            type:
              - string
          minItems: 1
          description: The events to trigger the webhook
        url:
          type:
            - string
          format: uri
          description: The URL to send the webhook to
        secret:
          type: string
          description: >-
            The secret to verify the webhook signature. Only returned on Webhook
            creation.
          nullable: true
        metadata:
          default: {}
          description: The metadata of the webhook
          type:
            - object
          additionalProperties:
            type:
              - string
            maxLength: 1000
        createdAt:
          type:
            - string
          format: date-time
          description: The date and time the webhook was created
        updatedAt:
          type:
            - string
          format: date-time
          description: The date and time the webhook was last updated
      required:
        - id
        - object
        - status
        - events
        - url
        - secret
        - createdAt
        - updatedAt
    EventType:
      type: string
      enum:
        - webset.created
        - webset.deleted
        - webset.paused
        - webset.idle
        - webset.search.created
        - webset.search.canceled
        - webset.search.completed
        - webset.search.updated
        - import.created
        - import.completed
        - webset.item.created
        - webset.item.enriched
        - monitor.created
        - monitor.updated
        - monitor.deleted
        - monitor.run.created
        - monitor.run.completed
        - webset.export.created
        - webset.export.completed
  securitySchemes:
    api_key:
      type: apiKey
      in: header
      name: x-api-key
      description: Your Exa API key

````