# Source: https://upstash.com/docs/qstash/api-refence/messages/bulk-cancel-messages.md

# Bulk Cancel Messages

> Delete all pending messages

<Note>Cancelling a message will remove it from QStash and stop it from being delivered in the future. If a message is in flight to your API, it might be too late to cancel.</Note>
<Warning>
  If you provide a set of message IDs in the request, only those messages will be cancelled.

  If you include filter parameters in the request, only the messages that match the filters will be canceled.
  
  If no filter or messageIds are sent, QStash will cancel all of your messages. We highly recommend at least providing count parameter and cancel in batches. 
</Warning> 

This operation scans all your messages and attempts to cancel them. If an individual message cannot be cancelled, it will not continue and will return an error message. Therefore, some messages may not be cancelled at the end. In such cases, you can run the bulk cancel operation multiple times.


## OpenAPI

````yaml qstash/openapi.yaml delete /v2/messages
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
  /v2/messages:
    delete:
      tags:
        - Messages
      summary: Bulk Cancel Messages
      description: Delete all pending messages
      parameters:
        - name: messageIds
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            A list of message IDs to delete. If provided, other filters are
            ignored.
        - name: topicName
          in: query
          required: false
          schema:
            type: string
          description: Filter messages by URL Group name.
        - name: queueName
          in: query
          required: false
          schema:
            type: string
          description: Filter messages by Queue name.
        - name: url
          in: query
          required: false
          schema:
            type: string
          description: Filter messages by URL.
        - name: label
          in: query
          required: false
          schema:
            type: string
          description: Filter messages by label.
        - name: flowControlKey
          in: query
          required: false
          schema:
            type: string
          description: Filter messages by Flow Control Key.
        - name: fromDate
          in: query
          required: false
          schema:
            type: integer
          description: >-
            Filter messages created after this timestamp (Unix milli,
            inclusive).
        - name: toDate
          in: query
          required: false
          schema:
            type: integer
          description: >-
            Filter messages created before this timestamp (Unix milli,
            inclusive).
        - name: scheduleId
          in: query
          required: false
          schema:
            type: string
          description: Filter messages by Schedule ID.
        - name: callerIP
          in: query
          required: false
          schema:
            type: string
          description: Filter messages by Caller IP.
        - name: count
          in: query
          required: false
          schema:
            type: integer
          description: >-
            Maximum number of messages to delete. There is no default value, so
            if not provided, all messages matching the filters will be deleted.
      responses:
        '200':
          description: All messages deleted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  cancelled:
                    type: integer
                    description: Number of messages cancelled
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