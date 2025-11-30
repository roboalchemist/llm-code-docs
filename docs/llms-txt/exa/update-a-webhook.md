# Source: https://docs.exa.ai/websets/api/webhooks/update-a-webhook.md

# Update a Webhook

> Change a webhook's settings. You can update:
- Events: Add or remove which events you want to hear about - URL: Change where notifications are sent - Metadata: Update custom data linked to the webhook

Changes happen right away. If you change the events list, the webhook will start or stop getting notifications for those events immediately.

The webhook keeps its current status (`active` or `inactive`) when you update it.

## OpenAPI

````yaml patch /v0/webhooks/{id}
paths:
  path: /v0/webhooks/{id}
  method: patch
  servers:
    - url: https://api.exa.ai/websets/
      description: Production
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: Your Exa API key
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The id of the webhook
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              events:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - string
                      $ref: '#/components/schemas/EventType'
                    minItems: 1
                    maxItems: 19
                    description: The events to trigger the webhook
              url:
                allOf:
                  - type:
                      - string
                    format: uri
                    description: The URL to send the webhook to
              metadata:
                allOf:
                  - description: >-
                      Set of key-value pairs you want to associate with this
                      object.
                    type:
                      - object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
            required: true
            refIdentifier: '#/components/schemas/UpdateWebhookParameters'
        examples:
          example:
            value:
              events:
                - webset.created
              url: <string>
              metadata: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          const webhook = await exa.websets.webhooks.update('webhook_id', {
            url: 'https://api.yourapp.com/webhooks/exa-updated',
            events: ['webset.completed']
          });

          console.log(`Updated webhook: ${webhook.id}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          webhook = exa.websets.webhooks.update('webhook_id', params={
              'url': 'https://api.yourapp.com/webhooks/exa-updated',
              'events': ['webset.completed']
          })

          print(f'Updated webhook: {webhook.id}')
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type:
                      - string
                    description: The unique identifier for the webhook
              object:
                allOf:
                  - type: string
                    const: webhook
                    default: webhook
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - active
                      - inactive
                    description: The status of the webhook
                    title: WebhookStatus
              events:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - string
                      $ref: '#/components/schemas/EventType'
                    minItems: 1
                    description: The events to trigger the webhook
              url:
                allOf:
                  - type:
                      - string
                    format: uri
                    description: The URL to send the webhook to
              secret:
                allOf:
                  - type: string
                    description: >-
                      The secret to verify the webhook signature. Only returned
                      on Webhook creation.
                    nullable: true
              metadata:
                allOf:
                  - default: {}
                    description: The metadata of the webhook
                    type:
                      - object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the webhook was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the webhook was last updated
            refIdentifier: '#/components/schemas/Webhook'
            requiredProperties:
              - id
              - object
              - status
              - events
              - url
              - secret
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              object: webhook
              status: active
              events:
                - webset.created
              url: <string>
              secret: <string>
              metadata: {}
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
        description: Webhook
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Webhook not found
        examples: {}
        description: Webhook not found
  deprecated: false
  type: path
components:
  schemas:
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

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt