# Source: https://docs.exa.ai/websets/api/webhooks/create-a-webhook.md

# Create a Webhook

> Webhooks let you get notifications when things happen in your Websets. When you create a webhook, you choose which events you want to know about and where to send the notifications.

When an event happens, Exa sends an HTTP POST request to your webhook URL with:
- Event details (type, time, ID)
- Full data of what triggered the event
- A signature to verify the request came from Exa

The webhook starts as `active` and begins getting notifications right away. You'll get a secret key for checking webhook signatures - save this safely as it's only shown once when you create the webhook.

## OpenAPI

````yaml post /v0/webhooks
paths:
  path: /v0/webhooks
  method: post
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
      path: {}
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
            refIdentifier: '#/components/schemas/CreateWebhookParameters'
            requiredProperties:
              - events
              - url
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

          const webhook = await exa.websets.webhooks.create({
            url: 'https://api.yourapp.com/webhooks/exa',
            events: ['webset.completed', 'enrichment.completed']
          });

          console.log(`Created webhook: ${webhook.id}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          webhook = exa.websets.webhooks.create(params={
              'url': 'https://api.yourapp.com/webhooks/exa',
              'events': ['webset.completed', 'enrichment.completed']
          })

          print(f'Created webhook: {webhook.id}')
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