# Source: https://docs.argil.ai/api-reference/endpoint/webhooks.update.md

# Update a webhook

> Updates the specified details of an existing webhook.

## OpenAPI

````yaml PUT /webhooks/{id}
paths:
  path: /webhooks/{id}
  method: put
  servers:
    - url: https://api.argil.ai/v1
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: API key to be included in the x-api-key header
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              callbackUrl:
                allOf:
                  - type: string
              events:
                allOf:
                  - $ref: '#/components/schemas/WebhookEventSchema'
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              callbackUrl: <string>
              events:
                - AVATAR_TRAINING_SUCCESS
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
              callbackUrl:
                allOf:
                  - type: string
              events:
                allOf:
                  - $ref: '#/components/schemas/WebhookEventSchema'
              createAt:
                allOf:
                  - type: string
                    format: date-time
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              lastTriggeredAt:
                allOf:
                  - type: string
                    format: date-time
            refIdentifier: '#/components/schemas/Webhook'
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              callbackUrl: <string>
              events:
                - AVATAR_TRAINING_SUCCESS
              createAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
              lastTriggeredAt: '2023-11-07T05:31:56Z'
        description: Successfully updated webhook
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - &ref_0
                    type: integer
                    format: int32
              message:
                allOf:
                  - &ref_1
                    type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Validation error
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Webhook not found
  deprecated: false
  type: path
components:
  schemas:
    WebhookEventSchema:
      type: array
      description: List of events the webhook is subscribing to.
      items:
        type: string
        enum:
          - AVATAR_TRAINING_SUCCESS
          - AVATAR_TRAINING_FAILED
          - VIDEO_GENERATION_SUCCESS
          - VIDEO_GENERATION_FAILED
      minItems: 1

````