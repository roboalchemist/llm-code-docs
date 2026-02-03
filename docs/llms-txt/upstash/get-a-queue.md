# Source: https://upstash.com/docs/qstash/api-refence/queues/get-a-queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Queue

> Get details of a specific queue



## OpenAPI

````yaml qstash/openapi.yaml get /v2/queues/{queueName}
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
  /v2/queues/{queueName}:
    get:
      tags:
        - Queues
      summary: Get a Queue
      description: Get details of a specific queue
      parameters:
        - name: queueName
          in: path
          required: true
          schema:
            type: string
          description: The name of the queue to retrieve.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Queue'
        '400':
          description: >-
            Queue name is invalid. Queue names can only contain alphanumeric
            characters, hyphens, periods, and underscores.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Queue not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Queue:
      type: object
      properties:
        name:
          type: string
          description: The name of the queue.
        createdAt:
          type: integer
          format: int64
          description: The creation timestamp of the queue in Unix milliseconds
        updatedAt:
          type: integer
          format: int64
          description: The last update timestamp of the queue in Unix milliseconds
        parallelism:
          type: integer
          description: The number of parallel consumers consuming from the queue
        paused:
          type: boolean
          description: Whether the queue is paused
        lag:
          type: integer
          description: The number of unprocessed messages that exist in the queue
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