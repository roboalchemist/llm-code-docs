# Source: https://upstash.com/docs/qstash/api-refence/dlq/bulk-delete-dlq-messages.md

# Bulk Delete DLQ messages

> Delete multiple messages from the DLQ



## OpenAPI

````yaml qstash/openapi.yaml delete /v2/dlq
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
  /v2/dlq:
    delete:
      tags:
        - DLQ
      summary: Bulk Delete DLQ messages
      description: Delete multiple messages from the DLQ
      parameters:
        - name: dlqIds
          in: query
          schema:
            type: array
            items:
              type: string
          description: List of DLQ IDs to delete. If provided, other filters are ignored.
        - name: cursor
          in: query
          schema:
            type: string
          description: >-
            By providing a cursor you can paginate through all of the messages
            in the DLQ
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
        - name: count
          in: query
          schema:
            type: integer
            default: 100
            maximum: 100
          description: The number of messages to delete.
      responses:
        '200':
          description: DLQ messages deleted successfully
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
                  deleted:
                    type: integer
                    description: The number of messages that were deleted.
components:
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