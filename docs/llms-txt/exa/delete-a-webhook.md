# Source: https://docs.exa.ai/websets/api/webhooks/delete-a-webhook.md

# Delete a Webhook

> Remove a webhook from your account. Once deleted, the webhook stops getting notifications right away and cannot be brought back.

Important notes: - The webhook stops working as soon as you delete it - You cannot undo this - you'll need to create a new webhook if you want it back - Any notifications currently being sent may still complete

## OpenAPI

````yaml delete /v0/webhooks/{id}
paths:
  path: /v0/webhooks/{id}
  method: delete
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
    body: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          await exa.websets.webhooks.delete('webhook_id');

          console.log('Webhook deleted successfully');
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          exa.websets.webhooks.delete('webhook_id')

          print('Webhook deleted successfully')
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