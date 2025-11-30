# Source: https://docs.exa.ai/websets/api/webhooks/list-webhooks.md

# List webhooks

> Get a list of all webhooks in your account.
The results come in pages. Use `limit` to set how many webhooks to get per page (up to 200). Use `cursor` to get the next page of results.

## OpenAPI

````yaml get /v0/webhooks
paths:
  path: /v0/webhooks
  method: get
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
      query:
        cursor:
          schema:
            - type: string
              required: false
              description: The cursor to paginate through the results
              minLength: 1
        limit:
          schema:
            - type: number
              required: false
              description: The number of results to return
              maximum: 200
              minimum: 1
              default: 25
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

          const webhooks = await exa.websets.webhooks.list();

          console.log(`Found ${webhooks.data.length} webhooks`);
          webhooks.data.forEach(webhook => {
            console.log(`- ${webhook.id}: ${webhook.url}`);
          });
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          webhooks = exa.websets.webhooks.list()

          print(f'Found {len(webhooks.data)} webhooks')
          for webhook in webhooks.data:
              print(f'- {webhook.id}: {webhook.url}')
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/Webhook'
                    description: The list of webhooks
              hasMore:
                allOf:
                  - type:
                      - boolean
                    description: Whether there are more results to paginate through
              nextCursor:
                allOf:
                  - type: string
                    description: The cursor to paginate through the next set of results
                    nullable: true
            refIdentifier: '#/components/schemas/ListWebhooksResponse'
            requiredProperties:
              - data
              - hasMore
              - nextCursor
        examples:
          example:
            value:
              data:
                - id: <string>
                  object: webhook
                  status: active
                  events:
                    - webset.created
                  url: <string>
                  secret: <string>
                  metadata: {}
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
              hasMore: true
              nextCursor: <string>
        description: List of webhooks
  deprecated: false
  type: path
components:
  schemas:
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
            type:
              - string
            $ref: '#/components/schemas/EventType'
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

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt