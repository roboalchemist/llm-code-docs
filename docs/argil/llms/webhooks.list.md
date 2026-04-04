# Source: https://docs.argil.ai/api-reference/endpoint/webhooks.list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve all webhooks

> Retrieves all webhooks for the authenticated user.



## OpenAPI

````yaml get /webhooks
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
    get:
      summary: Retrieve all webhooks
      description: Retrieves all webhooks for the authenticated user.
      responses:
        '200':
          description: An array of webhooks
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Webhook'
        '400':
          description: Unexpected error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````