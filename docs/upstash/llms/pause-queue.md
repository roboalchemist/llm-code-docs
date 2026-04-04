# Source: https://upstash.com/docs/qstash/api-refence/queues/pause-queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pause Queue

> Pause a queue to stop the delivery of enqueued messages

Pausing a queue stops the delivery of enqueued messages. The queue continues to accept new messages, but they will not be delivered until the queue is resumed.

If the queue is already paused, this action has no effect.

<Warning>
  Resuming or creating a queue may take up to a minute. Therefore, it is not recommended to pause or delete a queue during critical operations.
</Warning>


## OpenAPI

````yaml qstash/openapi.yaml post /v2/queues/{queueName}/pause
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
  /v2/queues/{queueName}/pause:
    post:
      tags:
        - Queues
      summary: Pause Queue
      description: Pause a queue to stop the delivery of enqueued messages
      parameters:
        - name: queueName
          in: path
          required: true
          schema:
            type: string
          description: The name of the queue to pause.
      responses:
        '200':
          description: Queue paused successfully
        '400':
          description: >-
            Queue name is invalid. Queue names can only contain alphanumeric
            characters, hyphens, periods, and underscores.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
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