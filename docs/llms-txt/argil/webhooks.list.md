# Source: https://docs.argil.ai/api-reference/endpoint/webhooks.list.md

# Retrieve all webhooks

> Retrieves all webhooks for the authenticated user.

## OpenAPI

````yaml get /webhooks
paths:
  path: /webhooks
  method: get
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Webhook'
        examples:
          example:
            value:
              - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                callbackUrl: <string>
                events:
                  - AVATAR_TRAINING_SUCCESS
                createAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                lastTriggeredAt: '2023-11-07T05:31:56Z'
        description: An array of webhooks
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: integer
                    format: int32
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Unexpected error
  deprecated: false
  type: path
components:
  schemas:
    Webhook:
      type: object
      properties:
        id:
          type: string
          format: uuid
        callbackUrl:
          type: string
        events:
          $ref: '#/components/schemas/WebhookEventSchema'
        createAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        lastTriggeredAt:
          type: string
          format: date-time
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