# Source: https://docs.ultravox.ai/api-reference/webhooks/webhooks-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Webhook

> Gets details for the specified webhook configuration



## OpenAPI

````yaml get /api/webhooks/{webhook_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/webhooks/{webhook_id}:
    get:
      tags:
        - webhooks
      operationId: webhooks_retrieve
      parameters:
        - in: path
          name: webhook_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Webhook'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    Webhook:
      type: object
      properties:
        webhookId:
          type: string
          format: uuid
          readOnly: true
        agentId:
          type: string
          format: uuid
          nullable: true
          description: If set, this webhook will be limited to calls with this agent.
        created:
          type: string
          format: date-time
          readOnly: true
        url:
          type: string
          format: uri
          maxLength: 200
        secrets:
          type: array
          items:
            type: string
            maxLength: 120
        events:
          type: array
          items:
            $ref: '#/components/schemas/EventsEnum'
        status:
          allOf:
            - $ref: '#/components/schemas/WebhookStatusEnum'
          readOnly: true
        lastStatusChange:
          type: string
          format: date-time
          readOnly: true
          nullable: true
        recentFailures:
          type: array
          items:
            $ref: '#/components/schemas/WebhookFailure'
          readOnly: true
          description: A list of recent failures for this webhook, if any.
      required:
        - created
        - events
        - lastStatusChange
        - recentFailures
        - status
        - url
        - webhookId
    EventsEnum:
      enum:
        - call.started
        - call.joined
        - call.ended
        - call.billed
      type: string
      description: |-
        * `call.started` - Fired when a call starts
        * `call.joined` - Fired when a call is joined
        * `call.ended` - Fired when a call ends
        * `call.billed` - Fired when a call is billed
    WebhookStatusEnum:
      enum:
        - normal
        - unhealthy
      type: string
      description: |-
        * `normal` - NORMAL
        * `unhealthy` - UNHEALTHY
    WebhookFailure:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        failure:
          type: string
      required:
        - failure
        - timestamp
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````