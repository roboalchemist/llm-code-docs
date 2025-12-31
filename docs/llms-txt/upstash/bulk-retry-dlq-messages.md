# Source: https://upstash.com/docs/qstash/api-refence/dlq/bulk-retry-dlq-messages.md

# Bulk Retry DLQ messages

> Retry delivery of multiple messages from the DLQ

When DLQ messages are retried, new messages with the same body and headers are created and scheduled for delivery.
The original DLQ messages are then removed from the DLQ.

<Note> 
  You can pass all configuration headers to override the configuration of the original messages.

  For example, if the retry count of the original messages is 5, you can set it to 0 for the retried messages by passing `Upstash-Retries: 0 ` header to this request. 
  Check out publish documentation for complete list of configuration options you can pass.
</Note>


## OpenAPI

````yaml qstash/openapi.yaml post /v2/dlq/retry
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
  /v2/dlq/retry:
    post:
      tags:
        - DLQ
      summary: Bulk Retry DLQ messages
      description: Retry delivery of multiple messages from the DLQ
      parameters:
        - name: dlqIds
          in: query
          schema:
            type: array
            items:
              type: string
          description: List of DLQ IDs to retry. If provided, other filters are ignored.
        - name: messageId
          in: query
          schema:
            type: string
          description: Filter DLQ messages by message ID
        - name: url
          in: query
          schema:
            type: string
          description: Filter DLQ messages by destination URL
        - name: topicName
          in: query
          schema:
            type: string
          description: Filter DLQ messages by URL Group name
        - name: scheduleId
          in: query
          schema:
            type: string
          description: Filter DLQ messages by schedule ID
        - name: queueName
          in: query
          schema:
            type: string
          description: Filter DLQ messages by queue name
        - name: fromDate
          in: query
          schema:
            type: integer
            format: int64
          description: >-
            Filter DLQ messages by starting date, in milliseconds (Unix
            timestamp). This is inclusive.
        - name: toDate
          in: query
          schema:
            type: integer
            format: int64
          description: >-
            Filter DLQ messages by ending date, in milliseconds (Unix
            timestamp). This is inclusive.
        - name: responseStatus
          in: query
          schema:
            type: integer
          description: >-
            Filter DLQ messages by HTTP response status code of the last
            delivery attempt
        - name: callerIp
          in: query
          schema:
            type: string
          description: Filter DLQ messages by IP address of the publisher
        - name: label
          in: query
          schema:
            type: string
          description: Filter DLQ messages by the label of the message assigned by the user
        - name: flowControlKey
          in: query
          schema:
            type: string
          description: Filter DLQ messages by Flow Control Key
      responses:
        '201':
          description: Messages retry initiated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  cursor:
                    type: string
                    description: >
                      A cursor which you can use in subsequent requests to
                      paginate through all messages. 

                      If no cursor is returned, you have reached the end of the
                      messages.
                  responses:
                    type: array
                    items:
                      $ref: '#/components/schemas/PublishResponse'
        '404':
          description: Some messages were not found in the DLQ
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