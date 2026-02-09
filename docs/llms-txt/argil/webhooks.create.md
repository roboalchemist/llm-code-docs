# Source: https://docs.argil.ai/api-reference/endpoint/webhooks.create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new webhook

> Creates a new webhook with the specified details.



## OpenAPI

````yaml post /webhooks
openapi: 3.0.1
info:
  title: Argil API
  description: API for AI clone video generation
  version: 1.0.0
  license:
    name: MIT
servers:
  - url: https://api.argil.ai/v1
security:
  - ApiKeyAuth: []
paths:
  /webhooks:
    post:
      summary: Create a new webhook
      description: Creates a new webhook with the specified details.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - callbackUrl
                - events
              properties:
                callbackUrl:
                  type: string
                  description: URL to which the webhook will send POST requests.
                events:
                  $ref: '#/components/schemas/WebhookEventSchema'
              additionalProperties: false
      responses:
        '201':
          description: Successfully created webhook
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Webhook'
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        lastTriggeredAt:
          type: string
          format: date-time
    Error:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````