# Source: https://docs.exa.ai/websets/api/webhooks/attempts/list-webhook-attempts.md

# List webhook attempts

> List all attempts made by a Webhook ordered in descending order.

## OpenAPI

````yaml get /v0/webhooks/{id}/attempts
paths:
  path: /v0/webhooks/{id}/attempts
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of the webhook
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
        eventType:
          schema:
            - type: enum<string>
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
              required: false
              description: The type of event to filter by
        successful:
          schema:
            - type: boolean
              required: false
              description: Filter attempts by their success status
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: >-
          // npm install exa-js

          import Exa from 'exa-js';

          const exa = new Exa('YOUR_EXA_API_KEY');


          const attempts = await exa.websets.webhooks.listAttempts('webhook_id',
          {
            limit: 20
          });


          console.log(`Found ${attempts.data.length} webhook attempts`);

          attempts.data.forEach(attempt => {
            console.log(`- ${attempt.id}: ${attempt.status}`);
          });
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          attempts = exa.websets.webhooks.attempts.list('webhook_id')

          print(f'Found {len(attempts.data)} webhook attempts')
          for attempt in attempts.data:
              print(f'- {attempt.id}: {attempt.status}')
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
                      $ref: '#/components/schemas/WebhookAttempt'
                    description: The list of webhook attempts
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
            refIdentifier: '#/components/schemas/ListWebhookAttemptsResponse'
            requiredProperties:
              - data
              - hasMore
              - nextCursor
        examples:
          example:
            value:
              data:
                - id: <string>
                  object: webhook_attempt
                  eventId: <string>
                  eventType: webset.created
                  webhookId: <string>
                  url: <string>
                  successful: true
                  responseHeaders: {}
                  responseBody: <string>
                  responseStatusCode: 123
                  attempt: 123
                  attemptedAt: '2023-11-07T05:31:56Z'
              hasMore: true
              nextCursor: <string>
        description: List of webhook attempts
  deprecated: false
  type: path
components:
  schemas:
    WebhookAttempt:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the webhook attempt
        object:
          type: string
          const: webhook_attempt
          default: webhook_attempt
        eventId:
          type:
            - string
          description: The unique identifier for the event
        eventType:
          type:
            - string
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
          description: The type of event
        webhookId:
          type:
            - string
          description: The unique identifier for the webhook
        url:
          type:
            - string
          description: The URL that was used during the attempt
        successful:
          description: Whether the attempt was successful
          type:
            - boolean
        responseHeaders:
          type:
            - object
          additionalProperties:
            type:
              - string
          description: The headers of the response
        responseBody:
          type: string
          description: The body of the response
          nullable: true
        responseStatusCode:
          type:
            - number
          description: The status code of the response
        attempt:
          type:
            - number
          description: The attempt number of the webhook
        attemptedAt:
          type:
            - string
          format: date-time
          description: The date and time the webhook attempt was made
      required:
        - id
        - object
        - eventId
        - eventType
        - webhookId
        - url
        - successful
        - responseHeaders
        - responseBody
        - responseStatusCode
        - attempt
        - attemptedAt

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt