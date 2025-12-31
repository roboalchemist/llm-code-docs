# Source: https://upstash.com/docs/qstash/api-refence/dlq/retry-a-dlq-message.md

# Retry a DLQ message

> Retry delivery of a message from the DLQ

When a DLQ message is retried, a new message with the same body and headers is created and scheduled for delivery.
The original DLQ message is then removed from the DLQ.

<Note> 
  You can pass all configuration headers to override the configuration of the original message.

  For example, if the retry count of the original message is 5, you can set it to 0 for the retried message by passing `Upstash-Retries: 0 ` header to this request. 
  Check out publish documentation for complete list of configuration options you can pass.
</Note>


## OpenAPI

````yaml qstash/openapi.yaml post /v2/dlq/retry/{dlqId}
openapi: 3.1.0
info:
  title: QStash REST API
  description: |
    QStash is a message queue and scheduler built on top of Upstash Redis.
  version: 2.0.0
  contact:
    name: Upstash
    url: https://upstash.com
servers:
  - url: https://qstash.upstash.io
security:
  - bearerAuth: []
  - bearerAuthQuery: []
tags:
  - name: Messages
    description: Publish and manage messages
  - name: Queues
    description: Manage message queues
  - name: Schedules
    description: Create and manage scheduled messages
  - name: URL Groups
    description: Manage URL groups and endpoints
  - name: DLQ
    description: Dead Letter Queue operations
  - name: Logs
    description: Log operations
  - name: Signing Keys
    description: Manage signing keys
  - name: Flow Control
    description: Monitor flow control keys
paths:
  /v2/dlq/retry/{dlqId}:
    post:
      tags:
        - DLQ
      summary: Retry a DLQ message
      description: Retry delivery of a message from the DLQ
      parameters:
        - name: dlqId
          in: path
          required: true
          schema:
            type: string
          description: |
            The DLQ ID of the message you want to retry.
      responses:
        '201':
          description: Message retry initiated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublishResponse'
        '404':
          description: >
            If the message is not found in the DLQ, (either is has been removed
            by you, or automatically), the endpoint returns a 404 status code.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    PublishResponse:
      type: object
      properties:
        messageId:
          type: string
          description: >-
            Unique identifier for the published message or the old message ID if
            deduplicated
        deduplicated:
          type: boolean
          description: >-
            Whether this message is a duplicate and was not sent to the
            destination.
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: QStash authentication token
    bearerAuthQuery:
      type: apiKey
      in: query
      name: qstash_token
      description: QStash authentication token passed as a query parameter

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://upstash.com/docs/llms.txt