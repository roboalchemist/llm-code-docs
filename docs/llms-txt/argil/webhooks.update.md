# Source: https://docs.argil.ai/api-reference/endpoint/webhooks.update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a webhook

> Updates the specified details of an existing webhook.



## OpenAPI

````yaml PUT /webhooks/{id}
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
  /webhooks/{id}:
    put:
      summary: Update a webhook
      description: Updates the specified details of an existing webhook.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                callbackUrl:
                  type: string
                events:
                  $ref: '#/components/schemas/WebhookEventSchema'
              additionalProperties: false
      responses:
        '200':
          description: Successfully updated webhook
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
        '404':
          description: Webhook not found
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